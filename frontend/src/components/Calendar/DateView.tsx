import { format } from 'date-fns'
import { ru } from 'date-fns/locale'
import { CalendarData } from '../../services/api'
import { logger } from '../../utils/logger'
import './Calendar.css'

interface DateViewProps {
  date: Date
  data: CalendarData | null
  loading: boolean
  error?: string | null
}

export default function DateView({ date, data, loading, error }: DateViewProps) {
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
    return (
      <div className="date-view">
        <h3>{formatDateWithWeekday(date)}</h3>
        <p>Нет данных для этой даты</p>
      </div>
    )
  }

  // Логирование для отладки праздников
  if (import.meta.env.DEV) {
    logger.info('[DateView] Data loaded:', {
      date: format(date, 'yyyy-MM-dd'),
      birthdaysCount: data.birthdays.length,
      holidaysCount: data.holidays.length,
      hasResponsible: !!data.responsible,
    })
  }

  return (
    <div className="date-view">
      <h3>{formatDateWithWeekday(date)}</h3>

      {/* Секция дней рождения - показываем только если есть */}
      {data.birthdays.length > 0 && (
        <div className="date-section">
          <h4>🎂 Дни рождения</h4>
          {data.birthdays.map((bd) => (
            <div key={bd.id} className="birthday-item">
              <p><strong>{bd.full_name}</strong></p>
              <p>{bd.company}, {bd.position}</p>
              <p>Исполняется {bd.age} лет</p>
              {bd.comment && <p className="comment">Комментарий: {bd.comment}</p>}
            </div>
          ))}
        </div>
      )}

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

      {/* Секция ответственного лица - показываем всегда */}
      <div className="date-section">
        <h4>👤 Ответственное лицо</h4>
        {data.responsible ? (
          <div className="responsible-item">
            <p><strong>{data.responsible.full_name}</strong></p>
            <p>{data.responsible.company}, {data.responsible.position}</p>
          </div>
        ) : (
          <p style={{ color: '#666', fontStyle: 'italic' }}>Ответственный не назначен</p>
        )}
      </div>
    </div>
  )
}

