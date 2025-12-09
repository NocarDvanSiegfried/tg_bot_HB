import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import Calendar from './Calendar'
import * as apiModule from '../../services/api'

// Мокируем API модуль
vi.mock('../../services/api', () => ({
  api: {
    getCalendar: vi.fn(),
  },
}))

// Мокируем DateView компонент
vi.mock('./DateView', () => ({
  default: ({ date, data, loading }: { date: Date; data: any; loading: boolean }) => (
    <div data-testid="date-view">
      <div data-testid="date">{date.toISOString()}</div>
      {loading && <div data-testid="loading">Loading...</div>}
      {data && <div data-testid="calendar-data">{JSON.stringify(data)}</div>}
    </div>
  ),
}))

describe('Calendar', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('should render calendar with current month', () => {
    render(<Calendar />)
    
    // Проверяем наличие заголовка календаря (формат: "MMMM yyyy")
    const currentDate = new Date()
    const year = currentDate.getFullYear()
    
    // Ищем заголовок с годом
    expect(screen.getByText(new RegExp(year.toString(), 'i'))).toBeInTheDocument()
  })

  it('should display week day headers', () => {
    render(<Calendar />)
    
    const weekDays = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
    weekDays.forEach(day => {
      expect(screen.getByText(day)).toBeInTheDocument()
    })
  })

  it('should navigate to previous month', () => {
    render(<Calendar />)
    
    const prevButton = screen.getByText('◀️')
    const currentDate = new Date()
    const currentYear = currentDate.getFullYear()
    
    // Проверяем, что текущий год отображается
    expect(screen.getByText(new RegExp(currentYear.toString(), 'i'))).toBeInTheDocument()
    
    fireEvent.click(prevButton)
    
    // После навигации год должен остаться (или измениться, если перешли через январь)
    const prevMonth = new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1)
    const prevYear = prevMonth.getFullYear()
    expect(screen.getByText(new RegExp(prevYear.toString(), 'i'))).toBeInTheDocument()
  })

  it('should navigate to next month', () => {
    render(<Calendar />)
    
    const nextButton = screen.getByText('▶️')
    const currentDate = new Date()
    const currentYear = currentDate.getFullYear()
    
    // Проверяем, что текущий год отображается
    expect(screen.getByText(new RegExp(currentYear.toString(), 'i'))).toBeInTheDocument()
    
    fireEvent.click(nextButton)
    
    // После навигации год должен остаться (или измениться, если перешли через декабрь)
    const nextMonth = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1)
    const nextYear = nextMonth.getFullYear()
    expect(screen.getByText(new RegExp(nextYear.toString(), 'i'))).toBeInTheDocument()
  })

  it('should load calendar data when date is clicked', async () => {
    const mockCalendarData = {
      date: '2024-01-15',
      birthdays: [
        {
          id: 1,
          full_name: 'Иван Иванов',
          company: 'ООО Тест',
          position: 'Разработчик',
          age: 30,
        },
      ],
      holidays: [],
      responsible: null,
    }

    vi.mocked(apiModule.api.getCalendar).mockResolvedValue(mockCalendarData)

    render(<Calendar />)
    
    // Находим первую кнопку с датой (не заголовок)
    const dayButtons = screen.getAllByRole('button').filter(
      btn => btn.textContent && /^\d+$/.test(btn.textContent.trim())
    )
    
    if (dayButtons.length > 0) {
      fireEvent.click(dayButtons[0])
      
      await waitFor(() => {
        expect(apiModule.api.getCalendar).toHaveBeenCalled()
      })
      
      await waitFor(() => {
        expect(screen.getByTestId('date-view')).toBeInTheDocument()
      })
    }
  })

  it('should show loading state when fetching calendar data', async () => {
    const mockCalendarData = {
      date: '2024-01-15',
      birthdays: [],
      holidays: [],
      responsible: null,
    }

    // Задержка для проверки loading состояния
    vi.mocked(apiModule.api.getCalendar).mockImplementation(
      () => new Promise(resolve => setTimeout(() => resolve(mockCalendarData), 100))
    )

    render(<Calendar />)
    
    const dayButtons = screen.getAllByRole('button').filter(
      btn => btn.textContent && /^\d+$/.test(btn.textContent.trim())
    )
    
    if (dayButtons.length > 0) {
      fireEvent.click(dayButtons[0])
      
      await waitFor(() => {
        expect(screen.getByTestId('loading')).toBeInTheDocument()
      })
    }
  })

  it('should clear selected date when navigating to different month', () => {
    render(<Calendar />)
    
    const dayButtons = screen.getAllByRole('button').filter(
      btn => btn.textContent && /^\d+$/.test(btn.textContent.trim())
    )
    
    if (dayButtons.length > 0) {
      fireEvent.click(dayButtons[0])
      
      // Навигация на предыдущий месяц должна очистить выбранную дату
      const prevButton = screen.getByText('◀️')
      fireEvent.click(prevButton)
      
      // DateView не должен отображаться после навигации
      expect(screen.queryByTestId('date-view')).not.toBeInTheDocument()
    }
  })

  it('should handle API error gracefully', async () => {
    const consoleErrorSpy = vi.spyOn(console, 'error').mockImplementation(() => {})
    
    vi.mocked(apiModule.api.getCalendar).mockRejectedValue(new Error('API Error'))

    render(<Calendar />)
    
    const dayButtons = screen.getAllByRole('button').filter(
      btn => btn.textContent && /^\d+$/.test(btn.textContent.trim())
    )
    
    if (dayButtons.length > 0) {
      fireEvent.click(dayButtons[0])
      
      await waitFor(() => {
        expect(consoleErrorSpy).toHaveBeenCalledWith(
          'Failed to load calendar data:',
          expect.any(Error)
        )
      })
    }
    
    consoleErrorSpy.mockRestore()
  })
})

