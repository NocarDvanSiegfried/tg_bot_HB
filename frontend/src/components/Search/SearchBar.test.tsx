import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import SearchBar from './SearchBar'
import * as apiModule from '../../services/api'

// Мокируем API модуль
vi.mock('../../services/api', () => ({
  api: {
    searchPeople: vi.fn(),
  },
}))

describe('SearchBar', () => {
  const mockOnSelect = vi.fn()

  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('should render search input and button', () => {
    render(<SearchBar onSelect={mockOnSelect} />)
    
    expect(screen.getByPlaceholderText('Поиск по ФИО, компании, должности...')).toBeInTheDocument()
    expect(screen.getByText('Поиск')).toBeInTheDocument()
  })

  it('should update input value when typing', async () => {
    const user = userEvent.setup()
    render(<SearchBar onSelect={mockOnSelect} />)
    
    const input = screen.getByPlaceholderText('Поиск по ФИО, компании, должности...') as HTMLInputElement
    await user.type(input, 'Иван')
    
    expect(input.value).toBe('Иван')
  })

  it('should call search API when search button is clicked', async () => {
    const mockResults = [
      {
        type: 'birthday',
        id: 1,
        full_name: 'Иван Иванов',
        company: 'ООО Тест',
        position: 'Разработчик',
      },
    ]

    vi.mocked(apiModule.api.searchPeople).mockResolvedValue(mockResults)

    render(<SearchBar onSelect={mockOnSelect} />)
    
    const input = screen.getByPlaceholderText('Поиск по ФИО, компании, должности...')
    const searchButton = screen.getByText('Поиск')
    
    fireEvent.change(input, { target: { value: 'Иван' } })
    fireEvent.click(searchButton)
    
    await waitFor(() => {
      expect(apiModule.api.searchPeople).toHaveBeenCalledWith('Иван')
    })
  })

  it('should call search API when Enter key is pressed', async () => {
    const mockResults = [
      {
        type: 'birthday',
        id: 1,
        full_name: 'Иван Иванов',
        company: 'ООО Тест',
        position: 'Разработчик',
      },
    ]

    vi.mocked(apiModule.api.searchPeople).mockResolvedValue(mockResults)

    render(<SearchBar onSelect={mockOnSelect} />)
    
    const input = screen.getByPlaceholderText('Поиск по ФИО, компании, должности...')
    
    fireEvent.change(input, { target: { value: 'Иван' } })
    fireEvent.keyPress(input, { key: 'Enter', code: 'Enter', charCode: 13 })
    
    await waitFor(() => {
      expect(apiModule.api.searchPeople).toHaveBeenCalledWith('Иван')
    })
  })

  it('should not call search API when query is empty', async () => {
    render(<SearchBar onSelect={mockOnSelect} />)
    
    const searchButton = screen.getByText('Поиск')
    fireEvent.click(searchButton)
    
    await waitFor(() => {
      expect(apiModule.api.searchPeople).not.toHaveBeenCalled()
    })
  })

  it('should display search results', async () => {
    const mockResults = [
      {
        type: 'birthday',
        id: 1,
        full_name: 'Иван Иванов',
        company: 'ООО Тест',
        position: 'Разработчик',
      },
      {
        type: 'responsible',
        id: 2,
        full_name: 'Петр Петров',
        company: 'ООО Другой',
        position: 'Менеджер',
      },
    ]

    vi.mocked(apiModule.api.searchPeople).mockResolvedValue(mockResults)

    render(<SearchBar onSelect={mockOnSelect} />)
    
    const input = screen.getByPlaceholderText('Поиск по ФИО, компании, должности...')
    const searchButton = screen.getByText('Поиск')
    
    fireEvent.change(input, { target: { value: 'Иван' } })
    fireEvent.click(searchButton)
    
    await waitFor(() => {
      expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
      expect(screen.getByText('Петр Петров')).toBeInTheDocument()
    })
    
    expect(screen.getByText(/ООО Тест/)).toBeInTheDocument()
    expect(screen.getByText(/ООО Другой/)).toBeInTheDocument()
  })

  it('should call onSelect when result is clicked', async () => {
    const mockResults = [
      {
        type: 'birthday',
        id: 1,
        full_name: 'Иван Иванов',
        company: 'ООО Тест',
        position: 'Разработчик',
      },
    ]

    vi.mocked(apiModule.api.searchPeople).mockResolvedValue(mockResults)

    render(<SearchBar onSelect={mockOnSelect} />)
    
    const input = screen.getByPlaceholderText('Поиск по ФИО, компании, должности...')
    const searchButton = screen.getByText('Поиск')
    
    fireEvent.change(input, { target: { value: 'Иван' } })
    fireEvent.click(searchButton)
    
    await waitFor(() => {
      expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
    })
    
    const resultItem = screen.getByText('Иван Иванов').closest('li')
    if (resultItem) {
      fireEvent.click(resultItem)
      expect(mockOnSelect).toHaveBeenCalledWith(1, 'birthday')
    }
  })

  it('should show loading state during search', async () => {
    // Задержка для проверки loading состояния
    vi.mocked(apiModule.api.searchPeople).mockImplementation(
      () => new Promise(resolve => setTimeout(() => resolve([]), 100))
    )

    render(<SearchBar onSelect={mockOnSelect} />)
    
    const input = screen.getByPlaceholderText('Поиск по ФИО, компании, должности...')
    const searchButton = screen.getByText('Поиск')
    
    fireEvent.change(input, { target: { value: 'Иван' } })
    fireEvent.click(searchButton)
    
    await waitFor(() => {
      expect(screen.getByText('Поиск...')).toBeInTheDocument()
    })
  })

  it('should handle search error gracefully', async () => {
    const consoleErrorSpy = vi.spyOn(console, 'error').mockImplementation(() => {})
    
    vi.mocked(apiModule.api.searchPeople).mockRejectedValue(new Error('Search failed'))

    render(<SearchBar onSelect={mockOnSelect} />)
    
    const input = screen.getByPlaceholderText('Поиск по ФИО, компании, должности...')
    const searchButton = screen.getByText('Поиск')
    
    fireEvent.change(input, { target: { value: 'Иван' } })
    fireEvent.click(searchButton)
    
    await waitFor(() => {
      expect(consoleErrorSpy).toHaveBeenCalledWith('Search failed:', expect.any(Error))
    })
    
    consoleErrorSpy.mockRestore()
  })

  it('should clear results when new search is performed', async () => {
    const mockResults1 = [
      {
        type: 'birthday',
        id: 1,
        full_name: 'Иван Иванов',
        company: 'ООО Тест',
        position: 'Разработчик',
      },
    ]

    const mockResults2 = [
      {
        type: 'birthday',
        id: 2,
        full_name: 'Петр Петров',
        company: 'ООО Другой',
        position: 'Менеджер',
      },
    ]

    vi.mocked(apiModule.api.searchPeople)
      .mockResolvedValueOnce(mockResults1)
      .mockResolvedValueOnce(mockResults2)

    render(<SearchBar onSelect={mockOnSelect} />)
    
    const input = screen.getByPlaceholderText('Поиск по ФИО, компании, должности...')
    const searchButton = screen.getByText('Поиск')
    
    // Первый поиск
    fireEvent.change(input, { target: { value: 'Иван' } })
    fireEvent.click(searchButton)
    
    await waitFor(() => {
      expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
    })
    
    // Второй поиск
    fireEvent.change(input, { target: { value: 'Петр' } })
    fireEvent.click(searchButton)
    
    await waitFor(() => {
      expect(screen.queryByText('Иван Иванов')).not.toBeInTheDocument()
      expect(screen.getByText('Петр Петров')).toBeInTheDocument()
    })
  })
})

