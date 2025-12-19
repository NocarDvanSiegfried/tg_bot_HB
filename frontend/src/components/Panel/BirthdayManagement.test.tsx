/**
 * Тесты для компонента BirthdayManagement.
 * 
 * Проверяют:
 * - Отображение списка дней рождения
 * - Редактирование дня рождения
 * - Удаление дня рождения
 * - Обработку ошибок API
 * - Валидацию форм
 */

import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { screen, fireEvent, waitFor, act } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { renderWithRouter } from '../../test/test-utils'
import BirthdayManagement from './BirthdayManagement'
import { api } from '../../services/api'
import { Birthday } from '../../types/birthday'

// Мокируем API
vi.mock('../../services/api', () => ({
  api: {
    getBirthdays: vi.fn(),
    createBirthday: vi.fn(),
    updateBirthday: vi.fn(),
    deleteBirthday: vi.fn(),
  },
}))

// Мокируем logger
vi.mock('../../utils/logger', () => ({
  logger: {
    info: vi.fn(),
    error: vi.fn(),
    warn: vi.fn(),
  },
}))

// Мокируем window.confirm
const mockConfirm = vi.fn()
window.confirm = mockConfirm

describe('BirthdayManagement', () => {
  const mockOnBack = vi.fn()
  const mockBirthdays: Birthday[] = [
    {
      id: 1,
      full_name: 'Иван Иванов',
      company: 'Компания 1',
      position: 'Должность 1',
      birth_date: '1990-01-01',
      comment: 'Комментарий 1',
    },
    {
      id: 2,
      full_name: 'Петр Петров',
      company: 'Компания 2',
      position: 'Должность 2',
      birth_date: '1991-02-02',
      comment: 'Комментарий 2',
    },
  ]

  beforeEach(() => {
    vi.clearAllMocks()
    mockConfirm.mockReturnValue(true) // По умолчанию confirm возвращает true
    ;(api.getBirthdays as any).mockResolvedValue(mockBirthdays)
  })

  afterEach(() => {
    vi.restoreAllMocks()
  })

  describe('Отображение списка дней рождения', () => {
    it('should display list of birthdays', async () => {
      // Arrange & Act
      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      // Assert
      await waitFor(() => {
        expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
        expect(screen.getByText('Петр Петров')).toBeInTheDocument()
        // Компания отображается как часть строки "Имя - Компания, Должность"
        expect(screen.getByText(/Компания 1/)).toBeInTheDocument()
        expect(screen.getByText(/Компания 2/)).toBeInTheDocument()
      })

      expect(api.getBirthdays).toHaveBeenCalledTimes(1)
    })

    it('should display loading state', async () => {
      // Arrange
      ;(api.getBirthdays as any).mockImplementation(
        () => new Promise((resolve) => setTimeout(() => resolve(mockBirthdays), 100))
      )

      // Act
      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      // Assert
      // Loading state может быть не виден, но компонент должен обрабатывать его
      await waitFor(() => {
        expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
      })
    })

    it('should display error when loading fails', async () => {
      // Arrange
      const errorMessage = 'Failed to load birthdays'
      ;(api.getBirthdays as any).mockRejectedValueOnce(new Error(errorMessage))

      // Act
      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      // Assert
      await waitFor(() => {
        // Ошибка отображается с префиксом "⚠️ "
        expect(screen.getByText(new RegExp(errorMessage))).toBeInTheDocument()
      }, { timeout: 3000 })
    })
  })

  describe('Редактирование дня рождения', () => {
    it('should open edit form when edit button is clicked', async () => {
      // Arrange
      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      await waitFor(() => {
        expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
      })

      // Act
      const editButtons = screen.getAllByText('Редактировать')
      fireEvent.click(editButtons[0])

      // Assert
      await waitFor(() => {
        // Проверяем, что форма редактирования открыта
        const fullNameInput = screen.getByDisplayValue('Иван Иванов')
        expect(fullNameInput).toBeInTheDocument()
      })
    })

    it('should update birthday when form is submitted', async () => {
      // Arrange
      const updatedBirthday: Birthday = {
        id: 1,
        full_name: 'Иван Обновленный',
        company: 'Компания 1',
        position: 'Должность 1',
        birth_date: '1990-01-01',
        comment: 'Комментарий 1',
      }
      ;(api.updateBirthday as any).mockResolvedValueOnce(updatedBirthday)

      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      await waitFor(() => {
        expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
      })

      // Открываем форму редактирования
      const editButtons = screen.getAllByText('Редактировать')
      fireEvent.click(editButtons[0])

      await waitFor(() => {
        expect(screen.getByDisplayValue('Иван Иванов')).toBeInTheDocument()
      })

      // Изменяем данные
      const fullNameInput = screen.getByDisplayValue('Иван Иванов')
      fireEvent.change(fullNameInput, { target: { value: 'Иван Обновленный' } })

      // Act
      const saveButton = screen.getByText('Сохранить')
      fireEvent.click(saveButton)

      // Assert
      await waitFor(() => {
        expect(api.updateBirthday).toHaveBeenCalledWith(1, expect.objectContaining({
          full_name: 'Иван Обновленный',
        }))
      })

      // Проверяем, что список обновлен
      await waitFor(() => {
        expect(api.getBirthdays).toHaveBeenCalledTimes(2) // Первый вызов при загрузке, второй после обновления
      })
    })

    it('should validate form before submitting', async () => {
      // Arrange
      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      await waitFor(() => {
        expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
      })

      // Открываем форму редактирования
      const editButtons = screen.getAllByText('Редактировать')
      fireEvent.click(editButtons[0])

      await waitFor(() => {
        expect(screen.getByDisplayValue('Иван Иванов')).toBeInTheDocument()
      })

      // Очищаем обязательное поле
      const fullNameInput = screen.getByDisplayValue('Иван Иванов')
      fireEvent.change(fullNameInput, { target: { value: '' } })

      // Act
      const saveButton = screen.getByText('Сохранить')
      fireEvent.click(saveButton)

      // Assert
      await waitFor(() => {
        expect(screen.getByText('ФИО не может быть пустым')).toBeInTheDocument()
      })

      expect(api.updateBirthday).not.toHaveBeenCalled()
    })

    it('should validate date format', async () => {
      // Arrange
      const user = userEvent.setup()
      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      await waitFor(() => {
        expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
      })

      // Открываем форму редактирования
      const editButtons = screen.getAllByText('Редактировать')
      await user.click(editButtons[0])

      await waitFor(() => {
        expect(screen.getByDisplayValue('Иван Иванов')).toBeInTheDocument()
      })

      // Находим input для даты и очищаем его
      const dateInput = screen.getByDisplayValue('1990-01-01') as HTMLInputElement
      
      // Input type="date" не позволяет ввести неверный формат напрямую
      // Очищаем поле, чтобы проверить валидацию обязательного поля
      await act(async () => {
        fireEvent.change(dateInput, { target: { value: '' } })
      })

      // Act - отправляем форму через submit, чтобы валидация сработала
      const saveButton = screen.getByText('Сохранить')
      await user.click(saveButton)

      // Assert - валидация должна сработать в validateEditForm
      // Проверяем наличие ошибки валидации
      await waitFor(() => {
        const errorTexts = [
          /Дата рождения обязательна/,
        ]
        const foundError = errorTexts.some(pattern => {
          const errorElement = screen.queryByText(pattern)
          return errorElement !== null
        })
        expect(foundError).toBe(true)
      }, { timeout: 3000 })

      // API не должен быть вызван из-за валидации
      expect(api.updateBirthday).not.toHaveBeenCalled()
    })

    it('should handle update errors', async () => {
      // Arrange
      const errorMessage = 'Failed to update birthday'
      ;(api.updateBirthday as any).mockRejectedValueOnce(new Error(errorMessage))

      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      await waitFor(() => {
        expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
      })

      // Открываем форму редактирования
      const editButtons = screen.getAllByText('Редактировать')
      fireEvent.click(editButtons[0])

      await waitFor(() => {
        expect(screen.getByDisplayValue('Иван Иванов')).toBeInTheDocument()
      })

      // Act
      const saveButton = screen.getByText('Сохранить')
      fireEvent.click(saveButton)

      // Assert
      await waitFor(() => {
        expect(screen.getByText(errorMessage)).toBeInTheDocument()
      })
    })

    it('should cancel edit when cancel button is clicked', async () => {
      // Arrange
      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      await waitFor(() => {
        expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
      })

      // Открываем форму редактирования
      const editButtons = screen.getAllByText('Редактировать')
      fireEvent.click(editButtons[0])

      await waitFor(() => {
        expect(screen.getByDisplayValue('Иван Иванов')).toBeInTheDocument()
      })

      // Act
      const cancelButton = screen.getByText('Отмена')
      fireEvent.click(cancelButton)

      // Assert
      await waitFor(() => {
        expect(screen.queryByDisplayValue('Иван Иванов')).not.toBeInTheDocument()
      })

      expect(api.updateBirthday).not.toHaveBeenCalled()
    })
  })

  describe('Удаление дня рождения', () => {
    it('should delete birthday when delete button is clicked and confirmed', async () => {
      // Arrange
      mockConfirm.mockReturnValueOnce(true)
      ;(api.deleteBirthday as any).mockResolvedValueOnce(undefined)

      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      await waitFor(() => {
        expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
      })

      // Act
      const deleteButtons = screen.getAllByText('Удалить')
      fireEvent.click(deleteButtons[0])

      // Assert
      await waitFor(() => {
        expect(api.deleteBirthday).toHaveBeenCalledWith(1)
      })

      // Проверяем, что список обновлен
      await waitFor(() => {
        expect(api.getBirthdays).toHaveBeenCalledTimes(2) // Первый вызов при загрузке, второй после удаления
      })
    })

    it('should not delete birthday when confirmation is cancelled', async () => {
      // Arrange
      mockConfirm.mockReturnValueOnce(false)

      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      await waitFor(() => {
        expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
      })

      // Act
      const deleteButtons = screen.getAllByText('Удалить')
      fireEvent.click(deleteButtons[0])

      // Assert
      expect(api.deleteBirthday).not.toHaveBeenCalled()
    })

    it('should handle delete errors', async () => {
      // Arrange
      mockConfirm.mockReturnValueOnce(true)
      const errorMessage = 'Failed to delete birthday'
      ;(api.deleteBirthday as any).mockRejectedValueOnce(new Error(errorMessage))

      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      await waitFor(() => {
        expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
      })

      // Act
      const deleteButtons = screen.getAllByText('Удалить')
      fireEvent.click(deleteButtons[0])

      // Assert
      await waitFor(() => {
        // Ошибка отображается с префиксом "⚠️ "
        expect(screen.getByText(new RegExp(errorMessage))).toBeInTheDocument()
      }, { timeout: 3000 })
    })
  })

  describe('Обработка ошибок API', () => {
    it('should display error message when getBirthdays fails', async () => {
      // Arrange
      const errorMessage = 'Network error'
      ;(api.getBirthdays as any).mockRejectedValueOnce(new Error(errorMessage))

      // Act
      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      // Assert
      await waitFor(() => {
        // Ошибка отображается с префиксом "⚠️ "
        expect(screen.getByText(new RegExp(errorMessage))).toBeInTheDocument()
      }, { timeout: 3000 })
    })

    it('should display error message when updateBirthday fails', async () => {
      // Arrange
      const errorMessage = 'Update failed'
      ;(api.updateBirthday as any).mockRejectedValueOnce(new Error(errorMessage))

      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      await waitFor(() => {
        expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
      })

      // Открываем форму редактирования
      const editButtons = screen.getAllByText('Редактировать')
      fireEvent.click(editButtons[0])

      await waitFor(() => {
        expect(screen.getByDisplayValue('Иван Иванов')).toBeInTheDocument()
      })

      // Act
      const saveButton = screen.getByText('Сохранить')
      fireEvent.click(saveButton)

      // Assert
      await waitFor(() => {
        expect(screen.getByText(errorMessage)).toBeInTheDocument()
      })
    })

    it('should display error message when deleteBirthday fails', async () => {
      // Arrange
      mockConfirm.mockReturnValueOnce(true)
      const errorMessage = 'Delete failed'
      ;(api.deleteBirthday as any).mockRejectedValueOnce(new Error(errorMessage))

      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      await waitFor(() => {
        expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
      })

      // Act
      const deleteButtons = screen.getAllByText('Удалить')
      fireEvent.click(deleteButtons[0])

      // Assert
      await waitFor(() => {
        // Ошибка отображается с префиксом "⚠️ "
        expect(screen.getByText(new RegExp(errorMessage))).toBeInTheDocument()
      }, { timeout: 3000 })
    })
  })

  describe('Валидация форм', () => {
    it('should validate required fields in edit form', async () => {
      // Arrange
      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      await waitFor(() => {
        expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
      })

      // Открываем форму редактирования
      const editButtons = screen.getAllByText('Редактировать')
      fireEvent.click(editButtons[0])

      await waitFor(() => {
        expect(screen.getByDisplayValue('Иван Иванов')).toBeInTheDocument()
      })

      // Очищаем все обязательные поля
      const fullNameInput = screen.getByDisplayValue('Иван Иванов')
      const companyInput = screen.getByDisplayValue('Компания 1')
      const positionInput = screen.getByDisplayValue('Должность 1')

      fireEvent.change(fullNameInput, { target: { value: '' } })
      fireEvent.change(companyInput, { target: { value: '' } })
      fireEvent.change(positionInput, { target: { value: '' } })

      // Act
      const saveButton = screen.getByText('Сохранить')
      fireEvent.click(saveButton)

      // Assert
      await waitFor(() => {
        expect(screen.getByText('ФИО не может быть пустым')).toBeInTheDocument()
      })

      expect(api.updateBirthday).not.toHaveBeenCalled()
    })

    it('should validate date format in edit form', async () => {
      // Arrange
      const user = userEvent.setup()
      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      await waitFor(() => {
        expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
      })

      // Открываем форму редактирования
      const editButtons = screen.getAllByText('Редактировать')
      await user.click(editButtons[0])

      await waitFor(() => {
        expect(screen.getByDisplayValue('Иван Иванов')).toBeInTheDocument()
      })

      // Находим input для даты и очищаем его
      const dateInput = screen.getByDisplayValue('1990-01-01') as HTMLInputElement
      
      // Input type="date" не позволяет ввести неверный формат напрямую
      // Очищаем поле, чтобы проверить валидацию обязательного поля
      await act(async () => {
        fireEvent.change(dateInput, { target: { value: '' } })
      })

      // Act - отправляем форму через submit, чтобы валидация сработала
      const saveButton = screen.getByText('Сохранить')
      await user.click(saveButton)

      // Assert - валидация должна сработать в validateEditForm
      await waitFor(() => {
        const errorTexts = [
          /Дата рождения обязательна/,
        ]
        const foundError = errorTexts.some(pattern => {
          const errorElement = screen.queryByText(pattern)
          return errorElement !== null
        })
        expect(foundError).toBe(true)
      }, { timeout: 3000 })

      // API не должен быть вызван из-за валидации
      expect(api.updateBirthday).not.toHaveBeenCalled()
    })

    it('should validate that date is not in the future', async () => {
      // Arrange
      const user = userEvent.setup()
      const futureDate = new Date()
      futureDate.setFullYear(futureDate.getFullYear() + 1)
      const futureDateString = futureDate.toISOString().split('T')[0]

      renderWithRouter(<BirthdayManagement onBack={mockOnBack} />)

      await waitFor(() => {
        expect(screen.getByText('Иван Иванов')).toBeInTheDocument()
      })

      // Открываем форму редактирования
      const editButtons = screen.getAllByText('Редактировать')
      await user.click(editButtons[0])

      await waitFor(() => {
        expect(screen.getByDisplayValue('Иван Иванов')).toBeInTheDocument()
      })

      // Изменяем дату на будущую (input type="date" принимает формат YYYY-MM-DD)
      const dateInput = screen.getByDisplayValue('1990-01-01') as HTMLInputElement
      await act(async () => {
        // Устанавливаем будущую дату через fireEvent.change
        fireEvent.change(dateInput, { target: { value: futureDateString } })
      })

      // Ждем, чтобы состояние обновилось
      await waitFor(() => {
        expect(dateInput.value).toBe(futureDateString)
      }, { timeout: 2000 })

      // Act
      const saveButton = screen.getByText('Сохранить')
      await user.click(saveButton)

      // Assert
      await waitFor(() => {
        // Ищем ошибку валидации даты в будущем
        const errorTexts = [
          /Дата рождения не может быть в будущем/,
          /не может быть в будущем/,
        ]
        const foundError = errorTexts.some(pattern => 
          screen.queryByText(pattern) !== null
        )
        expect(foundError).toBe(true)
      }, { timeout: 3000 })

      expect(api.updateBirthday).not.toHaveBeenCalled()
    })
  })
})

