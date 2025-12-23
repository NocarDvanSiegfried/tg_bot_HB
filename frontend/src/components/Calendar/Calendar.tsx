import { useState, useEffect } from 'react'
// Оптимизированные импорты из date-fns для tree-shaking
import format from 'date-fns/format'
import startOfMonth from 'date-fns/startOfMonth'
import endOfMonth from 'date-fns/endOfMonth'
import eachDayOfInterval from 'date-fns/eachDayOfInterval'
import isToday from 'date-fns/isToday'
import { api, CalendarData, MonthBirthdays } from '../../services/api'
import DateView from './DateView'
import { logger } from '../../utils/logger'
import BirthdayManagement from '../Panel/BirthdayManagement'
import './Calendar.css'
import '../Panel/Panel.css'

/**
 * Calendar - компонент для просмотра календаря дней рождения
 * 
 * КРИТИЧНО: Это "тупой" компонент только для user-режима
 * - Не знает про panel режим
 * - Не делает redirect
 * - Не вызывает navigate
 * - Не проверяет startParam
 * - Не использует useAppMode
 * 
 * Режим определяется только в App.tsx, который рендерит нужное дерево компонентов
 */
export default function Calendar() {
  // Все хуки вызываются всегда, без условий
  const [currentDate, setCurrentDate] = useState(new Date())
  const [selectedDate, setSelectedDate] = useState<Date | null>(null)
  const [calendarData, setCalendarData] = useState<CalendarData | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [renderError, setRenderError] = useState<string | null>(null)
  const [monthBirthdays, setMonthBirthdays] = useState<MonthBirthdays | null>(null)
  const [, setLoadingMonth] = useState(false) // Используется для управления состоянием загрузки месяца
  const [showManagement, setShowManagement] = useState(false) // Состояние для переключения между календарем и управлением

  // Логирование для отладки
  useEffect(() => {
    if (import.meta.env.DEV) {
      logger.info('[Calendar] Component mounted')
    }
  }, [])

  // Загрузка дней рождения за месяц
  useEffect(() => {
    const loadMonthBirthdays = async () => {
      const year = currentDate.getFullYear()
      const month = currentDate.getMonth() + 1 // date-fns использует 0-11, API ожидает 1-12
      
      setLoadingMonth(true)
      try {
        if (import.meta.env.DEV) {
          logger.info('[Calendar] Loading birthdays for month:', { year, month })
        }
        const data = await api.getCalendarMonth(year, month)
        if (import.meta.env.DEV) {
          logger.info('[Calendar] Month birthdays loaded:', {
            year: data.year,
            month: data.month,
            datesCount: Object.keys(data.birthdays_by_date).length,
            totalBirthdays: Object.values(data.birthdays_by_date).reduce((sum, arr) => sum + arr.length, 0),
            dates: Object.keys(data.birthdays_by_date),
          })
        }
        setMonthBirthdays(data)
      } catch (error) {
        logger.error('[Calendar] Failed to load month birthdays:', error)
        // Не показываем ошибку пользователю, просто не загружаем индикаторы
        setMonthBirthdays(null)
      } finally {
        setLoadingMonth(false)
      }
    }

    loadMonthBirthdays()
  }, [currentDate])

  // Безопасное вычисление дней месяца с обработкой ошибок
  const getDays = (): Date[] => {
    try {
      const monthStart = startOfMonth(currentDate)
      const monthEnd = endOfMonth(currentDate)
      return eachDayOfInterval({ start: monthStart, end: monthEnd })
    } catch (err) {
      logger.error('[Calendar] Error calculating month days:', err)
      setRenderError('Ошибка при отображении календаря. Попробуйте обновить страницу.')
      // Используем текущую дату как fallback
      return [new Date()]
    }
  }

  const days = getDays()

  // Проверка, есть ли ДР в определенный день
  const hasBirthday = (day: Date): boolean => {
    if (!monthBirthdays) return false
    const dateKey = format(day, 'yyyy-MM-dd')
    const hasBD = dateKey in monthBirthdays.birthdays_by_date && 
                  monthBirthdays.birthdays_by_date[dateKey].length > 0
    if (import.meta.env.DEV && hasBD) {
      logger.info('[Calendar] Day has birthday:', {
        date: dateKey,
        count: monthBirthdays.birthdays_by_date[dateKey].length,
        names: monthBirthdays.birthdays_by_date[dateKey].map(b => b.full_name),
      })
    }
    return hasBD
  }

  // Улучшенное сравнение дат для выделения (без учета времени)
  const isSelected = (day: Date): boolean => {
    if (!selectedDate) return false
    // Используем сравнение только по дате, без времени
    return format(day, 'yyyy-MM-dd') === format(selectedDate, 'yyyy-MM-dd')
  }

  // Проверка является ли день сегодняшним
  const isTodayDay = (day: Date): boolean => {
    return isToday(day)
  }

  const handleDateClick = async (date: Date) => {
    try {
      setSelectedDate(date)
      setLoading(true)
      setError(null)
      setCalendarData(null)
      
      const dateString = format(date, 'yyyy-MM-dd')
      if (import.meta.env.DEV) {
        logger.info('[Calendar] Loading data for date:', dateString)
      }
      
      const data = await api.getCalendar(dateString)
      setCalendarData(data)
      setError(null)
    } catch (error) {
      logger.error('[Calendar] Failed to load calendar data:', error)
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

  // Обработчик возврата из управления днями рождения
  const handleBackFromManagement = () => {
    setShowManagement(false)
    // Обновить календарь для отображения изменений (новые/измененные/удаленные дни рождения)
    // Изменение currentDate заставит useEffect перезапуститься и загрузить актуальные данные
    setCurrentDate(new Date(currentDate.getTime()))
  }

  // Если открыто управление, показываем компонент управления
  if (showManagement) {
    return <BirthdayManagement onBack={handleBackFromManagement} />
  }

  // Если есть ошибка рендеринга, показываем сообщение
  if (renderError) {
    return (
      <div className="calendar-container">
        <div className="error-message" style={{ padding: '20px', textAlign: 'center' }}>
          <p>⚠️ {renderError}</p>
          <button
            onClick={() => {
              setRenderError(null)
              setCurrentDate(new Date())
            }}
            style={{
              marginTop: '10px',
              padding: '10px 20px',
              background: 'var(--color-primary)',
              color: 'white',
              border: 'none',
              borderRadius: '4px',
              cursor: 'pointer',
            }}
          >
            Обновить календарь
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="calendar-container">
      <div className="calendar-header">
        <button onClick={handlePrevMonth}>◀️</button>
        <h2>{format(currentDate, 'MMMM yyyy')}</h2>
        <button onClick={handleNextMonth}>▶️</button>
        <button
          onClick={() => setShowManagement(true)}
          className="management-button"
          title="Управление днями рождения"
        >
          ➕ Управление
        </button>
      </div>

      <div className="calendar-grid">
        {['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'].map((day) => (
          <div key={day} className="calendar-day-header">
            {day}
          </div>
        ))}

        {days.length > 0 ? (
          days.map((day) => {
            const dayHasBirthday = hasBirthday(day)
            const dayIsSelected = isSelected(day)
            const dayIsToday = isTodayDay(day)
            const dayClasses = [
              'calendar-day',
              dayIsSelected ? 'selected' : '',
              dayIsToday ? 'today' : '',
              dayHasBirthday ? 'has-birthday' : '',
            ].filter(Boolean).join(' ')

            return (
              <button
                key={day.toISOString()}
                className={dayClasses}
                onClick={() => handleDateClick(day)}
                title={dayHasBirthday ? 'Есть дни рождения' : dayIsToday ? 'Сегодня' : ''}
              >
                <span className="day-number">{format(day, 'd')}</span>
                {dayHasBirthday && <span className="birthday-indicator">🎂</span>}
              </button>
            )
          })
        ) : (
          <div style={{ gridColumn: '1 / -1', textAlign: 'center', padding: '20px' }}>
            <p>Не удалось загрузить календарь</p>
          </div>
        )}
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

