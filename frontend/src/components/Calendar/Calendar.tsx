import { useState, useEffect, useCallback } from 'react'
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
import HolidayManagement from '../Panel/HolidayManagement'
import NavigationBar from '../Navigation/NavigationBar'
import GreetingModal from './GreetingModal'
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
  const [allHolidays, setAllHolidays] = useState<Array<{ day: number; month: number }>>([]) // Праздники для подсветки в календаре
  const [activeSection, setActiveSection] = useState<'calendar' | 'birthdays' | 'holidays'>('calendar') // Активный раздел навигации
  const [greetingModal, setGreetingModal] = useState<{
    isOpen: boolean
    birthdayId: number
    name: string
    company: string
    position: string
  } | null>(null)
  const [hasPanelAccess, setHasPanelAccess] = useState(false)
  const [checkingAccess, setCheckingAccess] = useState(true) // Флаг проверки доступа

  // Логирование для отладки
  useEffect(() => {
    if (import.meta.env.DEV) {
      logger.info('[Calendar] Component mounted')
    }
  }, [])

  // Проверка доступа к панели
  useEffect(() => {
    const checkAccess = async () => {
      setCheckingAccess(true)
      try {
        const result = await api.checkPanelAccess()
        setHasPanelAccess(result.has_access)
        // Диагностика
        console.log('[Calendar] Panel access check result:', result.has_access)
        if (import.meta.env.DEV) {
          logger.info('[Calendar] Panel access check:', result.has_access)
        }
      } catch (error) {
        logger.error('[Calendar] Failed to check panel access:', error)
        setHasPanelAccess(false)
        console.error('[Calendar] Failed to check panel access:', error)
      } finally {
        setCheckingAccess(false)
      }
    }
    checkAccess()
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

  // Загрузка всех праздников для подсветки в календаре
  useEffect(() => {
    const loadHolidays = async () => {
      try {
        const holidays = await api.getHolidays()
        // Преобразуем в формат для быстрой проверки (день + месяц)
        const holidaysMap = holidays.map(h => ({
          day: h.day || (h.date ? new Date(h.date).getDate() : 0),
          month: h.month || (h.date ? new Date(h.date).getMonth() + 1 : 0)
        })).filter(h => h.day > 0 && h.month > 0)
        setAllHolidays(holidaysMap)
      } catch (error) {
        logger.error('[Calendar] Failed to load holidays:', error)
        setAllHolidays([])
      }
    }
    
    loadHolidays()
  }, [currentDate, activeSection]) // Перезагружаем при изменении месяца или возврате из управления праздниками

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

  // Проверка, есть ли праздник в определенный день (по дню и месяцу)
  const hasHoliday = (day: Date): boolean => {
    const dayNum = day.getDate()
    const monthNum = day.getMonth() + 1
    
    // Проверяем загруженные праздники
    const hasHolidayInList = allHolidays.some(h => h.day === dayNum && h.month === monthNum)
    
    // Также проверяем данные календаря для выбранного дня
    if (calendarData) {
      const dayStr = format(day, 'yyyy-MM-dd')
      const hasHolidayInCalendar = calendarData.date === dayStr && calendarData.holidays.length > 0
      return hasHolidayInList || hasHolidayInCalendar
    }
    
    return hasHolidayInList
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

  // Обработчик изменения раздела навигации
  const handleSectionChange = (section: 'calendar' | 'birthdays' | 'holidays') => {
    setActiveSection(section)
    // При переходе в календарь не сбрасываем выбранную дату
    if (section === 'calendar') {
      // Оставляем selectedDate как есть
    } else {
      // При переходе в другие разделы закрываем DateView
      setSelectedDate(null)
    }
  }

  // Обработчик возврата из управления днями рождения
  const handleBackFromManagement = () => {
    setActiveSection('calendar')
    // Обновить календарь для отображения изменений (новые/измененные/удаленные дни рождения)
    // Изменение currentDate заставит useEffect перезапуститься и загрузить актуальные данные
    setCurrentDate(new Date(currentDate.getTime()))
  }

  // Обработчик возврата из управления праздниками
  const handleBackFromHolidayManagement = () => {
    setActiveSection('calendar')
    // Обновляем календарь для отображения изменений в праздниках
    setCurrentDate(new Date(currentDate.getTime()))
  }

  // Обработчик генерации поздравления (мемоизирован для стабильности ссылки)
  const handleGenerateGreeting = useCallback(async (id: number, name: string, company: string, position: string) => {
    // Диагностика
    console.log('[Calendar] handleGenerateGreeting called:', { id, name, hasPanelAccess, checkingAccess })
    
    // Если проверка ещё не завершена, ждём
    if (checkingAccess) {
      console.log('[Calendar] Still checking access, waiting...')
      // Можно показать индикатор загрузки
      return
    }
    
    // Если доступа нет, проверяем ещё раз (на случай, если доступ появился)
    if (!hasPanelAccess) {
      console.log('[Calendar] No access, re-checking...')
      try {
        const result = await api.checkPanelAccess()
        setHasPanelAccess(result.has_access)
        console.log('[Calendar] Re-check result:', result.has_access)
        
        if (!result.has_access) {
          logger.warn('[Calendar] Attempt to generate greeting without panel access')
          console.warn('[Calendar] No panel access, cannot generate greeting')
          // Можно показать сообщение пользователю
          alert('У вас нет доступа к функции генерации поздравлений. Обратитесь к администратору.')
          return
        }
      } catch (error) {
        logger.error('[Calendar] Failed to re-check panel access:', error)
        console.error('[Calendar] Failed to re-check panel access:', error)
        alert('Ошибка при проверке доступа. Попробуйте позже.')
        return
      }
    }
    
    // Если доступ есть, открываем модальное окно
    console.log('[Calendar] Opening greeting modal')
    setGreetingModal({ isOpen: true, birthdayId: id, name, company, position })
  }, [hasPanelAccess, checkingAccess]) // setGreetingModal стабильна, не нужна в зависимостях

  // Закрытие модального окна
  const handleCloseGreetingModal = () => {
    setGreetingModal(null)
  }

  // Если открыто управление днями рождения, показываем компонент управления
  if (activeSection === 'birthdays') {
    return (
      <>
        <NavigationBar activeSection={activeSection} onSectionChange={handleSectionChange} />
        <BirthdayManagement onBack={handleBackFromManagement} />
      </>
    )
  }

  // Если открыто управление праздниками, показываем компонент управления праздниками
  if (activeSection === 'holidays') {
    return (
      <>
        <NavigationBar activeSection={activeSection} onSectionChange={handleSectionChange} />
        <HolidayManagement onBack={handleBackFromHolidayManagement} />
      </>
    )
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
      <NavigationBar activeSection={activeSection} onSectionChange={handleSectionChange} />
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

        {days.length > 0 ? (
          days.map((day) => {
            const dayHasBirthday = hasBirthday(day)
            const dayHasHoliday = hasHoliday(day)
            const dayIsSelected = isSelected(day)
            const dayIsToday = isTodayDay(day)
            const dayClasses = [
              'calendar-day',
              dayIsSelected ? 'selected' : '',
              dayIsToday ? 'today' : '',
              dayHasBirthday ? 'has-birthday' : '',
              dayHasHoliday ? 'has-holiday' : '',
            ].filter(Boolean).join(' ')

            // Определяем индикаторы
            const indicators = []
            if (dayHasBirthday && dayHasHoliday) {
              indicators.push('both')
            } else if (dayHasBirthday) {
              indicators.push('birthday')
            } else if (dayHasHoliday) {
              indicators.push('holiday')
            }

            const title = dayHasBirthday && dayHasHoliday 
              ? 'Есть дни рождения и праздники'
              : dayHasBirthday 
              ? 'Есть дни рождения'
              : dayHasHoliday
              ? 'Есть праздники'
              : dayIsToday 
              ? 'Сегодня'
              : ''

            return (
              <button
                key={day.toISOString()}
                className={dayClasses}
                onClick={() => handleDateClick(day)}
                title={title}
              >
                <span className="day-number">{format(day, 'd')}</span>
                {indicators.length > 0 && (
                  <span className={`day-indicators ${indicators.join(' ')}`}>
                    {indicators.includes('both') ? (
                      <span className="indicator-badge combined">🎂🎉</span>
                    ) : (
                      <>
                        {indicators.includes('birthday') && <span className="indicator-badge birthday">🎂</span>}
                        {indicators.includes('holiday') && <span className="indicator-badge holiday">🎉</span>}
                      </>
                    )}
                  </span>
                )}
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
          onHolidaysClick={() => {
            setActiveSection('holidays')
            setSelectedDate(null) // Закрываем DateView при переходе
          }}
          onGenerateGreeting={handleGenerateGreeting}
        />
      )}

      {/* Модальное окно генерации поздравлений */}
      {greetingModal && (
        <GreetingModal
          isOpen={greetingModal.isOpen}
          birthdayId={greetingModal.birthdayId}
          birthdayName={greetingModal.name}
          birthdayCompany={greetingModal.company}
          birthdayPosition={greetingModal.position}
          onClose={handleCloseGreetingModal}
        />
      )}
    </div>
  )
}

