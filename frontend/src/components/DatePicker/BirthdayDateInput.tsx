import { useState, useEffect, useMemo } from 'react'
import './BirthdayDateInput.css'

interface BirthdayDateInputProps {
  value: string // YYYY-MM-DD или пустая строка
  onChange: (date: string) => void
  disabled?: boolean
  error?: string
}

export default function BirthdayDateInput({ 
  value, 
  onChange, 
  disabled = false,
  error 
}: BirthdayDateInputProps) {
  // Парсим значение в отдельные поля
  const parseValue = (dateStr: string): { day: string; month: string; year: string } => {
    if (!dateStr || !/^\d{4}-\d{2}-\d{2}$/.test(dateStr)) {
      return { day: '', month: '', year: '' }
    }
    
    const [year, month, day] = dateStr.split('-')
    return { day, month, year }
  }

  const initialValues = useMemo(() => parseValue(value), [])
  const [day, setDay] = useState(initialValues.day)
  const [month, setMonth] = useState(initialValues.month)
  const [year, setYear] = useState(initialValues.year)

  // Синхронизация с внешним value
  useEffect(() => {
    const parsed = parseValue(value)
    if (parsed.day !== day || parsed.month !== month || parsed.year !== year) {
      setDay(parsed.day)
      setMonth(parsed.month)
      setYear(parsed.year)
    }
  }, [value])

  // Формируем дату и вызываем onChange
  const updateDate = (newDay: string, newMonth: string, newYear: string) => {
    // Валидация: все поля должны быть заполнены
    if (newDay && newMonth && newYear) {
      const dayNum = parseInt(newDay, 10)
      const monthNum = parseInt(newMonth, 10)
      const yearNum = parseInt(newYear, 10)

      // Проверка валидности даты
      const date = new Date(yearNum, monthNum - 1, dayNum)
      if (
        date.getFullYear() === yearNum &&
        date.getMonth() === monthNum - 1 &&
        date.getDate() === dayNum
      ) {
        const formattedDate = `${yearNum}-${monthNum.toString().padStart(2, '0')}-${dayNum.toString().padStart(2, '0')}`
        onChange(formattedDate)
      } else {
        // Невалидная дата - не вызываем onChange
        return
      }
    } else {
      // Если не все поля заполнены, отправляем пустую строку
      onChange('')
    }
  }

  const handleDayChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newDay = e.target.value.replace(/\D/g, '').slice(0, 2)
    setDay(newDay)
    updateDate(newDay, month, year)
  }

  const handleMonthChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const newMonth = e.target.value
    setMonth(newMonth)
    updateDate(day, newMonth, year)
  }

  const handleYearChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newYear = e.target.value.replace(/\D/g, '').slice(0, 4)
    setYear(newYear)
    updateDate(day, month, newYear)
  }

  // Вычисляем возраст, если все поля заполнены
  const age = useMemo(() => {
    if (day && month && year) {
      const dayNum = parseInt(day, 10)
      const monthNum = parseInt(month, 10)
      const yearNum = parseInt(year, 10)
      
      const birthDate = new Date(yearNum, monthNum - 1, dayNum)
      const today = new Date()
      
      if (!isNaN(birthDate.getTime()) && birthDate <= today) {
        let calculatedAge = today.getFullYear() - birthDate.getFullYear()
        const monthDiff = today.getMonth() - birthDate.getMonth()
        
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
          calculatedAge--
        }
        
        return calculatedAge >= 0 ? calculatedAge : null
      }
    }
    return null
  }, [day, month, year])

  const monthNames = [
    'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
    'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
  ]

  return (
    <div className="birthday-date-input">
      <label className="birthday-date-input-label">
        Дата рождения <span className="required">*</span>
      </label>
      <div className="birthday-date-input-fields">
        <div className="birthday-date-field">
          <label htmlFor="birthday-day">День</label>
          <input
            id="birthday-day"
            type="text"
            inputMode="numeric"
            placeholder="ДД"
            value={day}
            onChange={handleDayChange}
            disabled={disabled}
            maxLength={2}
            className={error ? 'error' : ''}
          />
        </div>
        <div className="birthday-date-field">
          <label htmlFor="birthday-month">Месяц</label>
          <select
            id="birthday-month"
            value={month}
            onChange={handleMonthChange}
            disabled={disabled}
            className={error ? 'error' : ''}
          >
            <option value="">Месяц</option>
            {monthNames.map((name, index) => (
              <option key={index + 1} value={(index + 1).toString().padStart(2, '0')}>
                {name}
              </option>
            ))}
          </select>
        </div>
        <div className="birthday-date-field">
          <label htmlFor="birthday-year">Год <span className="required">*</span></label>
          <input
            id="birthday-year"
            type="text"
            inputMode="numeric"
            placeholder="ГГГГ"
            value={year}
            onChange={handleYearChange}
            disabled={disabled}
            maxLength={4}
            className={error ? 'error' : ''}
            required
          />
        </div>
      </div>
      {age !== null && age >= 0 ? (
        <div className="birthday-date-age">
          Возраст: <strong>{age} {age === 1 ? 'год' : age < 5 ? 'года' : 'лет'}</strong>
        </div>
      ) : (
        <div className="birthday-date-hint">
          Используется для расчёта возраста
        </div>
      )}
      {error && (
        <div className="birthday-date-error">{error}</div>
      )}
    </div>
  )
}


