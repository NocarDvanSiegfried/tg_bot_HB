// Оптимизированные импорты из date-fns для tree-shaking
import { memo } from 'react'
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
}

function DateView({ date, data, loading, error }: DateViewProps) {
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
            <div key={bd.id} className="birthday-item">
              <p><strong>{bd.full_name}</strong></p>
              <p>{bd.company}, {bd.position}</p>
              <p>Исполняется {bd.age} лет</p>
              {bd.comment && <p className="comment">Комментарий: {bd.comment}</p>}
              {bd.responsible && (
                <p className="responsible-person">
                  👤 <strong>Ответственный:</strong> {bd.responsible}
                </p>
              )}
            </div>
          ))
        ) : (
          <p style={{ color: '#666', fontStyle: 'italic' }}>Нет дней рождения на эту дату</p>
        )}
      </div>

      {/* Секция профессиональных праздников - показываем всегда */}
      <div className="date-section">
        <h4>🎉 Профессиональные праздники</h4>
        {data.holidays.length > 0 ? (
          data.holidays.map((holiday) => (
            <div key={holiday.id} className="holiday-item">
              <p><strong>{holiday.name}</strong></p>
              {holiday.description && <p>{holiday.description}</p>}
            </div>
          ))
        ) : (
          <p style={{ color: '#666', fontStyle: 'italic' }}>Нет профессиональных праздников</p>
        )}
      </div>

    </div>
  )
}

// Мемоизация компонента для оптимизации рендеринга
export default memo(DateView)

