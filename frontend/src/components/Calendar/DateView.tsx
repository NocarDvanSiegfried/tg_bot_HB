// Оптимизированные импорты из date-fns для tree-shaking
import { memo, useEffect } from 'react'
import format from 'date-fns/format'
import ru from 'date-fns/locale/ru'
import { CalendarData } from '../../services/api'
import { logger } from '../../utils/logger'
import './Calendar.css'

interface DateViewProps {
  date: Date
  data: CalendarData | null
  loading: boolean
  error?: string | null
  onHolidaysClick?: () => void
  onGenerateGreeting?: (birthdayId: number, birthdayName: string, company: string, position: string) => void
}

function DateView({ date, data, loading, error, onHolidaysClick, onGenerateGreeting }: DateViewProps) {
  // Диагностика: проверяем, передан ли обработчик
  useEffect(() => {
    if (import.meta.env.DEV) {
      console.log('[DateView] onGenerateGreeting provided:', !!onGenerateGreeting)
    }
  }, [onGenerateGreeting])
  if (loading) {
    return <div className="date-view">Загрузка...</div>
  }

  // Форматирование даты с днем недели
  const formatDateWithWeekday = (date: Date): string => {
    const dateStr = format(date, 'd MMMM yyyy', { locale: ru })
    const weekday = format(date, 'EEEE', { locale: ru })
    return `${dateStr}, ${weekday}`
  }

  if (error) {
    return (
      <div className="date-view">
        <h3>{formatDateWithWeekday(date)}</h3>
        <div className="error-message">
          <p>⚠️ Ошибка загрузки данных</p>
          <p>{error}</p>
          <p className="error-hint">
            Проверьте подключение к интернету и настройки API.
          </p>
        </div>
      </div>
    )
  }

  if (!data) {
    if (import.meta.env.DEV) {
      logger.info('[DateView] No data for date:', format(date, 'yyyy-MM-dd'))
    }
    return (
      <div className="date-view">
        <h3>{formatDateWithWeekday(date)}</h3>
        <p>Нет данных для этой даты</p>
      </div>
    )
  }

  // Логирование для отладки
  if (import.meta.env.DEV) {
    logger.info('[DateView] Data loaded:', {
      date: format(date, 'yyyy-MM-dd'),
      birthdaysCount: data.birthdays.length,
      holidaysCount: data.holidays.length,
      birthdays: data.birthdays.map(b => ({
        id: b.id,
        name: b.full_name,
        company: b.company,
      })),
    })
  }

  return (
    <div className="date-view">
      <h3>{formatDateWithWeekday(date)}</h3>

      {/* Секция дней рождения - показываем всегда */}
      <div className="date-section">
        <h4>🎂 Дни рождения</h4>
        {data.birthdays.length > 0 ? (
          data.birthdays.map((bd) => (
            <div key={bd.id} className="birthday-card">
              <div className="birthday-card-header">
                <strong className="birthday-name">{bd.full_name}</strong>
                {onGenerateGreeting ? (
                  <button 
                    className="greeting-button"
                    onClick={() => {
                      console.log('[DateView] Greeting button clicked:', { 
                        id: bd.id, 
                        name: bd.full_name,
                        company: bd.company,
                        position: bd.position
                      })
                      onGenerateGreeting(bd.id, bd.full_name, bd.company, bd.position)
                    }}
                    title="Сгенерировать поздравление"
                  >
                    🤖 Поздравить
                  </button>
                ) : (
                  // Диагностика в dev режиме
                  import.meta.env.DEV && console.log('[DateView] onGenerateGreeting is not provided for:', bd.full_name)
                )}
              </div>
              <div className="birthday-card-body">
                <p className="birthday-company-position">{bd.company}, {bd.position}</p>
                <p className="birthday-age">Исполняется {bd.age} лет</p>
                {bd.comment && <p className="birthday-comment">{bd.comment}</p>}
                {bd.responsible && (
                  <p className="birthday-responsible">
                    👤 <strong>Ответственный:</strong> {bd.responsible}
                  </p>
                )}
              </div>
            </div>
          ))
        ) : (
          <p className="empty-state">Нет дней рождения на эту дату</p>
        )}
      </div>

      {/* Секция профессиональных праздников - показываем всегда */}
      <div className="date-section">
        <h4
          onClick={onHolidaysClick}
          className={onHolidaysClick ? 'holidays-header-clickable' : ''}
        >
          🎉 Профессиональные праздники
        </h4>
        {data.holidays.length > 0 ? (
          data.holidays.map((holiday) => (
            <div key={holiday.id} className="holiday-card">
              <p className="holiday-name"><strong>{holiday.name}</strong></p>
              {holiday.description && <p className="holiday-description">{holiday.description}</p>}
            </div>
          ))
        ) : (
          <p className="empty-state">Нет профессиональных праздников</p>
        )}
      </div>

    </div>
  )
}

// Мемоизация компонента для оптимизации рендеринга
export default memo(DateView)

