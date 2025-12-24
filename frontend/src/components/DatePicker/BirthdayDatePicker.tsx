import { useState, useMemo, useEffect } from 'react'
import { startOfMonth, endOfMonth, eachDayOfInterval, getDay, isSameDay, addMonths, subMonths } from 'date-fns'
import './BirthdayDatePicker.css'

interface BirthdayDatePickerProps {
  value: string // YYYY-MM-DD или пустая строка
  onChange: (date: string) => void
  disabled?: boolean
}

export default function BirthdayDatePicker({ value, onChange, disabled = false }: BirthdayDatePickerProps) {
  const [showYearInput, setShowYearInput] = useState(() => {
    if (value) {
      const date = new Date(value + 'T00:00:00')
      return !isNaN(date.getTime()) && date.getFullYear() > 1900
    }
    return false
  })
  const [selectedMonth, setSelectedMonth] = useState(() => {
    if (value) {
      const date = new Date(value + 'T00:00:00')
      return new Date(date.getFullYear(), date.getMonth(), 1)
    }
    return new Date(new Date().getFullYear(), new Date().getMonth(), 1)
  })
  const [selectedDay, setSelectedDay] = useState<number | null>(() => {
    if (value) {
      const date = new Date(value + 'T00:00:00')
      return date.getDate()
    }
    return null
  })
  const [selectedMonthNum, setSelectedMonthNum] = useState<number | null>(() => {
    if (value) {
      const date = new Date(value + 'T00:00:00')
      return date.getMonth() + 1
    }
    return null
  })
  const [year, setYear] = useState<string>(() => {
    if (value) {
      const date = new Date(value + 'T00:00:00')
      return String(date.getFullYear())
    }
    return ''
  })

  // Синхронизация состояния при изменении value извне
  useEffect(() => {
    if (value) {
      const date = new Date(value + 'T00:00:00')
      if (!isNaN(date.getTime())) {
        const day = date.getDate()
        const month = date.getMonth() + 1
        const yearValue = date.getFullYear()
        
        // Обновляем выбранный день и месяц
        setSelectedDay(prev => prev !== day ? day : prev)
        setSelectedMonthNum(prev => prev !== month ? month : prev)
        
        // Обновляем месяц календаря
        const monthStart = new Date(yearValue, month - 1, 1)
        setSelectedMonth(prev => {
          if (prev.getTime() !== monthStart.getTime()) {
            return monthStart
          }
          return prev
        })
        
        // Обновляем год и переключатель
        const hasYear = yearValue > 1900
        if (hasYear) {
          setShowYearInput(prev => !prev ? true : prev)
          setYear(prev => prev !== String(yearValue) ? String(yearValue) : prev)
        }
      }
    } else {
      // Если value пустое, сбрасываем выбор (но не месяц календаря)
      setSelectedDay(null)
      setSelectedMonthNum(null)
    }
  }, [value])

  const monthNames = [
    'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
    'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
  ]

  const weekDays = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

  // Получаем дни месяца для отображения
  const daysInMonth = useMemo(() => {
    const start = startOfMonth(selectedMonth)
    const end = endOfMonth(selectedMonth)
    const days = eachDayOfInterval({ start, end })
    
    // Добавляем пустые ячейки для выравнивания (начало недели)
    const firstDayOfWeek = getDay(start)
    const offset = firstDayOfWeek === 0 ? 6 : firstDayOfWeek - 1 // Понедельник = 0
    
    return {
      offset,
      days: days.map(day => ({
        date: day,
        day: day.getDate(),
        month: day.getMonth() + 1,
        isSelected: selectedDay === day.getDate() && selectedMonthNum === day.getMonth() + 1,
        isToday: isSameDay(day, new Date()),
      }))
    }
  }, [selectedMonth, selectedDay, selectedMonthNum])

  const handleDayClick = (day: number, month: number) => {
    setSelectedDay(day)
    setSelectedMonthNum(month)
    
    // Формируем дату: если год указан - используем его, иначе - текущий год
    const yearToUse = showYearInput && year ? parseInt(year, 10) : new Date().getFullYear()
    const dateStr = `${yearToUse}-${String(month).padStart(2, '0')}-${String(day).padStart(2, '0')}`
    onChange(dateStr)
  }

  const handleYearToggle = (checked: boolean) => {
    setShowYearInput(checked)
    
    if (checked) {
      // Если год не был указан, используем текущий год
      if (!year) {
        const currentYear = new Date().getFullYear()
        setYear(String(currentYear))
      }
    } else {
      // При отключении года используем текущий год для формирования даты
      if (selectedDay && selectedMonthNum) {
        const currentYear = new Date().getFullYear()
        const dateStr = `${currentYear}-${String(selectedMonthNum).padStart(2, '0')}-${String(selectedDay).padStart(2, '0')}`
        onChange(dateStr)
      }
    }
  }

  const handleYearChange = (newYear: string) => {
    setYear(newYear)
    
    // Обновляем дату с новым годом
    if (selectedDay && selectedMonthNum && newYear) {
      const yearNum = parseInt(newYear, 10)
      if (!isNaN(yearNum) && yearNum >= 1900 && yearNum <= new Date().getFullYear()) {
        const dateStr = `${yearNum}-${String(selectedMonthNum).padStart(2, '0')}-${String(selectedDay).padStart(2, '0')}`
        onChange(dateStr)
      }
    }
  }

  const handlePrevMonth = () => {
    setSelectedMonth(subMonths(selectedMonth, 1))
  }

  const handleNextMonth = () => {
    setSelectedMonth(addMonths(selectedMonth, 1))
  }

  // Вычисляем возраст, если год указан
  const calculatedAge = useMemo(() => {
    if (showYearInput && year && selectedDay && selectedMonthNum) {
      const yearNum = parseInt(year, 10)
      if (!isNaN(yearNum) && yearNum >= 1900 && yearNum <= new Date().getFullYear()) {
        const today = new Date()
        const birthDate = new Date(yearNum, selectedMonthNum - 1, selectedDay)
        let age = today.getFullYear() - birthDate.getFullYear()
        const monthDiff = today.getMonth() - birthDate.getMonth()
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
          age--
        }
        return age >= 0 ? age : null
      }
    }
    return null
  }, [showYearInput, year, selectedDay, selectedMonthNum])

  return (
    <div className="birthday-date-picker">
      <label className="birthday-date-picker-label">
        Дата рождения <span className="required-mark">*</span>
      </label>
      
      {/* Календарь для выбора дня и месяца */}
      <div className="birthday-calendar-container">
        <div className="birthday-calendar-header">
          <button
            type="button"
            className="birthday-calendar-nav-button"
            onClick={handlePrevMonth}
            disabled={disabled}
            aria-label="Предыдущий месяц"
          >
            ◀️
          </button>
          <h3 className="birthday-calendar-month-title">
            {monthNames[selectedMonth.getMonth()]} {selectedMonth.getFullYear()}
          </h3>
          <button
            type="button"
            className="birthday-calendar-nav-button"
            onClick={handleNextMonth}
            disabled={disabled}
            aria-label="Следующий месяц"
          >
            ▶️
          </button>
        </div>

        <div className="birthday-calendar-grid">
          {/* Заголовки дней недели */}
          {weekDays.map(day => (
            <div key={day} className="birthday-calendar-weekday">
              {day}
            </div>
          ))}
          
          {/* Пустые ячейки для выравнивания */}
          {Array.from({ length: daysInMonth.offset }).map((_, i) => (
            <div key={`empty-${i}`} className="birthday-calendar-day-empty" />
          ))}
          
          {/* Дни месяца */}
          {daysInMonth.days.map(({ day, month, isSelected, isToday }) => (
            <button
              key={`${month}-${day}`}
              type="button"
              className={`birthday-calendar-day ${isSelected ? 'selected' : ''} ${isToday ? 'today' : ''}`}
              onClick={() => handleDayClick(day, month)}
              disabled={disabled}
              aria-label={`${day} ${monthNames[month - 1]}`}
            >
              {day}
            </button>
          ))}
        </div>
      </div>

      {/* Выбранная дата */}
      {selectedDay && selectedMonthNum && (
        <div className="birthday-selected-date">
          <span className="birthday-selected-date-label">Выбрано:</span>
          <span className="birthday-selected-date-value">
            {String(selectedDay).padStart(2, '0')} {monthNames[selectedMonthNum - 1]}
            {showYearInput && year ? ` ${year}` : ''}
          </span>
        </div>
      )}

      {/* Переключатель года */}
      <div className="birthday-year-toggle">
        <label className="birthday-year-toggle-label">
          <input
            type="checkbox"
            checked={showYearInput}
            onChange={(e) => handleYearToggle(e.target.checked)}
            disabled={disabled}
            className="birthday-year-toggle-checkbox"
          />
          <span className="birthday-year-toggle-text">
            Указать год рождения
          </span>
        </label>
        <small className="birthday-year-hint">
          Год нужен только для расчёта возраста
        </small>
      </div>

      {/* Поле ввода года (появляется при включении переключателя) */}
      {showYearInput && (
        <div className="birthday-year-input-container">
          <label className="birthday-year-input-label">Год рождения:</label>
          <input
            type="number"
            min="1900"
            max={new Date().getFullYear()}
            value={year}
            onChange={(e) => handleYearChange(e.target.value)}
            disabled={disabled}
            placeholder="Например, 1990"
            className="birthday-year-input"
          />
          {calculatedAge !== null && (
            <div className="birthday-age-preview">
              Возраст: {calculatedAge} {calculatedAge === 1 ? 'год' : calculatedAge < 5 ? 'года' : 'лет'}
            </div>
          )}
        </div>
      )}
    </div>
  )
}

