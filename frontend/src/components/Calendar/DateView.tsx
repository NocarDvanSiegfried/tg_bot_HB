import { format } from 'date-fns'
import { CalendarData } from '../../services/api'
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

  if (error) {
    return (
      <div className="date-view">
        <h3>{format(date, 'dd.MM.yyyy')}</h3>
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
        <h3>{format(date, 'dd.MM.yyyy')}</h3>
        <p>Нет данных для этой даты</p>
      </div>
    )
  }

  return (
    <div className="date-view">
      <h3>{format(date, 'dd.MM.yyyy')}</h3>

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

      {data.holidays.length > 0 && (
        <div className="date-section">
          <h4>🎉 Профессиональные праздники</h4>
          {data.holidays.map((holiday) => (
            <div key={holiday.id} className="holiday-item">
              <p><strong>{holiday.name}</strong></p>
              {holiday.description && <p>{holiday.description}</p>}
            </div>
          ))}
        </div>
      )}

      <div className="date-section">
        <h4>👤 Ответственное лицо</h4>
        {data.responsible ? (
          <div className="responsible-item">
            <p><strong>{data.responsible.full_name}</strong></p>
            <p>{data.responsible.company}, {data.responsible.position}</p>
          </div>
        ) : (
          <p>Ответственный не назначен</p>
        )}
      </div>
    </div>
  )
}

