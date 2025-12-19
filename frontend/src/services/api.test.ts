/**
 * Тесты для API клиента.
 * 
 * Проверяют:
 * - Успешные запросы updateBirthday и deleteBirthday
 * - Обработку ошибок сети
 * - Обработку ошибок валидации
 * - Обработку 204/205 статусов
 */

import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { api } from './api'
import { Birthday } from '../types/birthday'
import { API_BASE_URL } from '../config/api'

// Используем window.fetch вместо window.fetch для совместимости с jsdom

// Мокируем глобальный fetch
window.fetch = vi.fn() as any

// Мокируем window.Telegram для getInitData
const mockTelegramWebApp = {
  initData: 'test_init_data',
}

Object.defineProperty(window, 'Telegram', {
  value: {
    WebApp: mockTelegramWebApp,
  },
  writable: true,
})

describe('API Client', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  afterEach(() => {
    vi.restoreAllMocks()
  })

  describe('updateBirthday', () => {
    it('should successfully update a birthday', async () => {
      // Arrange
      const birthdayId = 1
      const updateData: Partial<Birthday> = {
        full_name: 'Updated Name',
        company: 'Updated Company',
        position: 'Updated Position',
        birth_date: '1990-01-01',
      }
      const expectedResponse: Birthday = {
        id: birthdayId,
        full_name: 'Updated Name',
        company: 'Updated Company',
        position: 'Updated Position',
        birth_date: '1990-01-01',
        comment: 'Updated comment',
      }

      ;(window.fetch as any).mockResolvedValueOnce({
        ok: true,
        status: 200,
        statusText: 'OK',
        headers: new Headers({ 'Content-Type': 'application/json', 'Content-Length': '100' }),
        json: async () => expectedResponse,
      })

      // Act
      const result = await api.updateBirthday(birthdayId, updateData)

      // Assert
      expect(result).toEqual(expectedResponse)
      expect(window.fetch).toHaveBeenCalledWith(
        `${API_BASE_URL}/api/panel/birthdays/${birthdayId}`,
        expect.objectContaining({
          method: 'PUT',
          headers: expect.objectContaining({
            'Content-Type': 'application/json',
            'X-Init-Data': 'test_init_data',
          }),
          body: JSON.stringify(updateData),
        })
      )
    })

    it('should handle 204 No Content status', async () => {
      // Arrange
      const birthdayId = 1
      const updateData: Partial<Birthday> = {
        full_name: 'Updated Name',
      }

      ;(window.fetch as any).mockResolvedValueOnce({
        ok: true,
        status: 204,
        statusText: 'No Content',
        headers: new Headers({ 'Content-Length': '0' }),
      })

      // Act & Assert
      await expect(api.updateBirthday(birthdayId, updateData)).rejects.toThrow('Сервер вернул ответ без данных')
    })

    it('should handle 205 Reset Content status', async () => {
      // Arrange
      const birthdayId = 1
      const updateData: Partial<Birthday> = {
        full_name: 'Updated Name',
      }

      ;(window.fetch as any).mockResolvedValueOnce({
        ok: true,
        status: 205,
        statusText: 'Reset Content',
        headers: new Headers({ 'Content-Length': '0' }),
      })

      // Act & Assert
      await expect(api.updateBirthday(birthdayId, updateData)).rejects.toThrow('Сервер вернул ответ без данных')
    })

    it('should handle network errors', async () => {
      // Arrange
      const birthdayId = 1
      const updateData: Partial<Birthday> = {
        full_name: 'Updated Name',
      }

      ;(window.fetch as any).mockRejectedValueOnce(new Error('Network error'))

      // Act & Assert
      await expect(api.updateBirthday(birthdayId, updateData)).rejects.toThrow('Network error')
    })

    it('should handle validation errors (400)', async () => {
      // Arrange
      const birthdayId = 1
      const updateData: Partial<Birthday> = {
        full_name: '', // Invalid: empty
      }

      const errorResponse = {
        detail: [
          {
            loc: ['body', 'full_name'],
            msg: 'field required',
            type: 'value_error.missing',
          },
        ],
      }

      const mockResponse = {
        ok: false,
        status: 400,
        statusText: 'Bad Request',
        headers: new Headers({ 'Content-Type': 'application/json' }),
        clone: function () {
          return { ...this, json: async () => errorResponse }
        },
        json: async () => errorResponse,
      }
      ;(window.fetch as any).mockResolvedValueOnce(mockResponse)

      // Act & Assert
      await expect(api.updateBirthday(birthdayId, updateData)).rejects.toThrow()
    })

    it('should handle 401 Unauthorized', async () => {
      // Arrange
      const birthdayId = 1
      const updateData: Partial<Birthday> = {
        full_name: 'Updated Name',
      }

      const mockResponse401Update = {
        ok: false,
        status: 401,
        statusText: 'Unauthorized',
        headers: new Headers({ 'Content-Type': 'application/json' }),
        clone: function () {
          return { ...this, json: async () => ({ detail: 'Unauthorized' }) }
        },
        json: async () => ({ detail: 'Unauthorized' }),
      }
      ;(window.fetch as any).mockResolvedValueOnce(mockResponse401Update)

      // Act & Assert
      await expect(api.updateBirthday(birthdayId, updateData)).rejects.toThrow()
    })

    it('should handle 404 Not Found', async () => {
      // Arrange
      const birthdayId = 999
      const updateData: Partial<Birthday> = {
        full_name: 'Updated Name',
      }

      const mockResponse404Update = {
        ok: false,
        status: 404,
        statusText: 'Not Found',
        headers: new Headers({ 'Content-Type': 'application/json' }),
        clone: function () {
          return { ...this, json: async () => ({ detail: 'Birthday not found' }) }
        },
        json: async () => ({ detail: 'Birthday not found' }),
      }
      ;(window.fetch as any).mockResolvedValueOnce(mockResponse404Update)

      // Act & Assert
      await expect(api.updateBirthday(birthdayId, updateData)).rejects.toThrow()
    })

    it('should handle empty response body', async () => {
      // Arrange
      const birthdayId = 1
      const updateData: Partial<Birthday> = {
        full_name: 'Updated Name',
      }

      ;(window.fetch as any).mockResolvedValueOnce({
        ok: true,
        status: 200,
        statusText: 'OK',
        headers: new Headers({ 'Content-Length': '0' }),
      })

      // Act & Assert
      await expect(api.updateBirthday(birthdayId, updateData)).rejects.toThrow('Сервер вернул пустой ответ')
    })

    it('should handle invalid response data', async () => {
      // Arrange
      const birthdayId = 1
      const updateData: Partial<Birthday> = {
        full_name: 'Updated Name',
      }

      ;(window.fetch as any).mockResolvedValueOnce({
        ok: true,
        status: 200,
        statusText: 'OK',
        headers: new Headers({ 'Content-Type': 'application/json', 'Content-Length': '10' }),
        json: async () => null,
      })

      // Act & Assert
      await expect(api.updateBirthday(birthdayId, updateData)).rejects.toThrow('Сервер вернул невалидные данные')
    })

    it('should handle incomplete response data', async () => {
      // Arrange
      const birthdayId = 1
      const updateData: Partial<Birthday> = {
        full_name: 'Updated Name',
      }

      ;(window.fetch as any).mockResolvedValueOnce({
        ok: true,
        status: 200,
        statusText: 'OK',
        headers: new Headers({ 'Content-Type': 'application/json', 'Content-Length': '10' }),
        json: async () => ({ company: 'Company' }), // Missing id and full_name
      })

      // Act & Assert
      await expect(api.updateBirthday(birthdayId, updateData)).rejects.toThrow('Сервер вернул неполные данные')
    })
  })

  describe('deleteBirthday', () => {
    it('should successfully delete a birthday with 200 status', async () => {
      // Arrange
      const birthdayId = 1

      ;(window.fetch as any).mockResolvedValueOnce({
        ok: true,
        status: 200,
        statusText: 'OK',
        headers: new Headers({ 'Content-Type': 'application/json' }),
        json: async () => ({ status: 'deleted' }),
      })

      // Act
      await api.deleteBirthday(birthdayId)

      // Assert
      expect(window.fetch).toHaveBeenCalledWith(
        `${API_BASE_URL}/api/panel/birthdays/${birthdayId}`,
        expect.objectContaining({
          method: 'DELETE',
          headers: expect.objectContaining({
            'Content-Type': 'application/json',
            'X-Init-Data': 'test_init_data',
          }),
        })
      )
    })

    it('should handle 204 No Content status', async () => {
      // Arrange
      const birthdayId = 1

      ;(window.fetch as any).mockResolvedValueOnce({
        ok: true,
        status: 204,
        statusText: 'No Content',
        headers: new Headers({ 'Content-Length': '0' }),
      })

      // Act
      await api.deleteBirthday(birthdayId)

      // Assert
      expect(window.fetch).toHaveBeenCalled()
      // Should not throw for 204
    })

    it('should handle 205 Reset Content status', async () => {
      // Arrange
      const birthdayId = 1

      ;(window.fetch as any).mockResolvedValueOnce({
        ok: true,
        status: 205,
        statusText: 'Reset Content',
        headers: new Headers({ 'Content-Length': '0' }),
      })

      // Act
      await api.deleteBirthday(birthdayId)

      // Assert
      expect(window.fetch).toHaveBeenCalled()
      // Should not throw for 205
    })

    it('should handle network errors', async () => {
      // Arrange
      const birthdayId = 1

      ;(window.fetch as any).mockRejectedValueOnce(new Error('Network error'))

      // Act & Assert
      await expect(api.deleteBirthday(birthdayId)).rejects.toThrow('Network error')
    })

    it('should handle 401 Unauthorized', async () => {
      // Arrange
      const birthdayId = 1

      const mockResponse401Update = {
        ok: false,
        status: 401,
        statusText: 'Unauthorized',
        headers: new Headers({ 'Content-Type': 'application/json' }),
        clone: function () {
          return { ...this, json: async () => ({ detail: 'Unauthorized' }) }
        },
        json: async () => ({ detail: 'Unauthorized' }),
      }
      ;(window.fetch as any).mockResolvedValueOnce(mockResponse401Update)

      // Act & Assert
      await expect(api.deleteBirthday(birthdayId)).rejects.toThrow()
    })

    it('should handle 404 Not Found', async () => {
      // Arrange
      const birthdayId = 999

      const mockResponse404Update = {
        ok: false,
        status: 404,
        statusText: 'Not Found',
        headers: new Headers({ 'Content-Type': 'application/json' }),
        clone: function () {
          return { ...this, json: async () => ({ detail: 'Birthday not found' }) }
        },
        json: async () => ({ detail: 'Birthday not found' }),
      }
      ;(window.fetch as any).mockResolvedValueOnce(mockResponse404Update)

      // Act & Assert
      await expect(api.deleteBirthday(birthdayId)).rejects.toThrow()
    })

    it('should handle 403 Forbidden', async () => {
      // Arrange
      const birthdayId = 1

      const mockResponse403 = {
        ok: false,
        status: 403,
        statusText: 'Forbidden',
        headers: new Headers({ 'Content-Type': 'application/json' }),
        clone: function () {
          return { ...this, json: async () => ({ detail: 'Access denied' }) }
        },
        json: async () => ({ detail: 'Access denied' }),
      }
      ;(window.fetch as any).mockResolvedValueOnce(mockResponse403)

      // Act & Assert
      await expect(api.deleteBirthday(birthdayId)).rejects.toThrow()
    })

    it('should handle empty response with Content-Length: 0', async () => {
      // Arrange
      const birthdayId = 1

      ;(window.fetch as any).mockResolvedValueOnce({
        ok: true,
        status: 200,
        statusText: 'OK',
        headers: new Headers({ 'Content-Length': '0' }),
      })

      // Act
      await api.deleteBirthday(birthdayId)

      // Assert
      expect(window.fetch).toHaveBeenCalled()
      // Should not throw for empty response
    })
  })
})

