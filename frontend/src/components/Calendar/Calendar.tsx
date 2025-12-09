import { useState } from 'react'
import { format, startOfMonth, endOfMonth, eachDayOfInterval, isSameDay } from 'date-fns'
import { api, CalendarData } from '../../services/api'
import DateView from './DateView'
import { logger } from '../../utils/logger'
import './Calendar.css'

export default function Calendar() {
  const [currentDate, setCurrentDate] = useState(new Date())
  const [selectedDate, setSelectedDate] = useState<Date | null>(null)
  const [calendarData, setCalendarData] = useState<CalendarData | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const monthStart = startOfMonth(currentDate)
  const monthEnd = endOfMonth(currentDate)
  const days = eachDayOfInterval({ start: monthStart, end: monthEnd })

  const handleDateClick = async (date: Date) => {
    setSelectedDate(date)
    setLoading(true)
    setError(null)
    setCalendarData(null)
    
    try {
      const data = await api.getCalendar(format(date, 'yyyy-MM-dd'))
      setCalendarData(data)
      setError(null)
    } catch (error) {
      logger.error('Failed to load calendar data:', error)
      const errorMessage = error instanceof Error ? error.message : 'Не удалось загрузить данные'
      setError(errorMessage)
      setCalendarData(null)
    } finally {
      setLoading(false)
    }
  }

  const handlePrevMonth = () => {
    setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1))
    setSelectedDate(null)
    setCalendarData(null)
  }

  const handleNextMonth = () => {
    setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1))
    setSelectedDate(null)
    setCalendarData(null)
  }

  return (
    <div className="calendar-container">
      <div className="calendar-header">
        <button onClick={handlePrevMonth}>◀️</button>
        <h2>{format(currentDate, 'MMMM yyyy')}</h2>
        <button onClick={handleNextMonth}>▶️</button>
      </div>

      <div className="calendar-grid">
        {['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'].map((day) => (
          <div key={day} className="calendar-day-header">
            {day}
          </div>
        ))}

        {days.map((day) => (
          <button
            key={day.toISOString()}
            className={`calendar-day ${selectedDate && isSameDay(day, selectedDate) ? 'selected' : ''}`}
            onClick={() => handleDateClick(day)}
          >
            {format(day, 'd')}
          </button>
        ))}
      </div>

      {selectedDate && (
        <DateView 
          date={selectedDate} 
          data={calendarData} 
          loading={loading}
          error={error}
        />
      )}
    </div>
  )
}

