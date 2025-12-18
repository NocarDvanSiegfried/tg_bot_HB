import { Birthday } from '../types/birthday'
import { Responsible } from '../types/responsible'
import { API_BASE_URL, API_TIMEOUT_MS } from '../config/api'
import { logger } from '../utils/logger'

// Получить initData из Telegram WebApp
function getInitData(): string | null {
  if (typeof window !== 'undefined' && window.Telegram?.WebApp) {
    return window.Telegram.WebApp.initData || null
  }
  return null
}

// Создать headers с initData
function getHeaders(additionalHeaders: Record<string, string> = {}): Record<string, string> {
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
    ...additionalHeaders,
  }
  
  const initData = getInitData()
  if (initData) {
    headers['X-Init-Data'] = initData
  }
  
  return headers
}

// Улучшенная обработка ошибок fetch
async function fetchWithErrorHandling(
  url: string,
  options: RequestInit = {}
): Promise<Response> {
  const method = options.method || 'GET'
  logger.info(`[API] ${method} ${url}`, options.body ? { body: options.body } : {})
  
  try {
    const controller = new AbortController()
    const timeoutId = setTimeout(() => controller.abort(), API_TIMEOUT_MS)
    
    const response = await fetch(url, {
      ...options,
      signal: controller.signal,
    })
    
    clearTimeout(timeoutId)
    
    logger.info(`[API] Response ${response.status} for ${method} ${url}`)
    
    if (!response.ok) {
      // Пытаемся получить детали ошибки из ответа
      let errorMessage = `HTTP ${response.status}: ${response.statusText}`
      let errorData: any = null
      try {
        errorData = await response.json()
        if (errorData.detail) {
          errorMessage = errorData.detail
        } else if (errorData.errors) {
          // Обработка ошибок валидации Pydantic
          const validationErrors = errorData.errors.map((e: any) => 
            `${e.loc.join('.')}: ${e.msg}`
          ).join(', ')
          errorMessage = `Validation error: ${validationErrors}`
        }
        logger.error(`[API] Error response for ${method} ${url}:`, errorData)
      } catch {
        // Игнорируем ошибку парсинга JSON
        logger.error(`[API] Error response for ${method} ${url}: ${response.status} ${response.statusText}`)
      }
      throw new Error(errorMessage)
    }
    
    return response
  } catch (error) {
    logger.error(`[API] Error in ${method} ${url}:`, error)
    if (error instanceof Error) {
      if (error.name === 'AbortError') {
        throw new Error('Request timeout: сервер не отвечает')
      }
      if (error.message.includes('Failed to fetch') || error.message.includes('NetworkError')) {
        throw new Error('Network error: не удалось подключиться к серверу. Проверьте подключение к интернету и URL API.')
      }
      throw error
    }
    throw new Error('Unknown error occurred')
  }
}

export interface CalendarData {
  date: string
  birthdays: Array<{
    id: number
    full_name: string
    company: string
    position: string
    age: number
    comment?: string
  }>
  holidays: Array<{
    id: number
    name: string
    description?: string
  }>
  responsible: {
    id: number
    full_name: string
    company: string
    position: string
  } | null
}

export interface MonthBirthdays {
  year: number
  month: number
  birthdays_by_date: Record<string, Array<{
    id: number
    full_name: string
    company: string
    position: string
  }>>
}

export const api = {
  async getCalendar(date: string): Promise<CalendarData> {
    const response = await fetchWithErrorHandling(`${API_BASE_URL}/api/calendar/${date}`, {
      headers: getHeaders(),
    })
    return response.json()
  },

  async getCalendarMonth(year: number, month: number): Promise<MonthBirthdays> {
    const response = await fetchWithErrorHandling(`${API_BASE_URL}/api/calendar/month/${year}/${month}`, {
      headers: getHeaders(),
    })
    return response.json()
  },

  async getBirthdays(): Promise<Birthday[]> {
    const response = await fetchWithErrorHandling(`${API_BASE_URL}/api/panel/birthdays`, {
      headers: getHeaders(),
    })
    return response.json()
  },

  async createBirthday(data: Omit<Birthday, 'id'>): Promise<Birthday> {
    const response = await fetchWithErrorHandling(`${API_BASE_URL}/api/panel/birthdays`, {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify(data),
    })
    return response.json()
  },

  async updateBirthday(id: number, data: Partial<Birthday>): Promise<Birthday> {
    const response = await fetchWithErrorHandling(`${API_BASE_URL}/api/panel/birthdays/${id}`, {
      method: 'PUT',
      headers: getHeaders(),
      body: JSON.stringify(data),
    })
    return response.json()
  },

  async deleteBirthday(id: number): Promise<void> {
    await fetchWithErrorHandling(`${API_BASE_URL}/api/panel/birthdays/${id}`, {
      method: 'DELETE',
      headers: getHeaders(),
    })
  },

  async getResponsible(): Promise<Responsible[]> {
    const response = await fetchWithErrorHandling(`${API_BASE_URL}/api/panel/responsible`, {
      headers: getHeaders(),
    })
    return response.json()
  },

  async createResponsible(data: Omit<Responsible, 'id'>): Promise<Responsible> {
    const response = await fetchWithErrorHandling(`${API_BASE_URL}/api/panel/responsible`, {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify(data),
    })
    return response.json()
  },

  async updateResponsible(id: number, data: Partial<Responsible>): Promise<Responsible> {
    const response = await fetchWithErrorHandling(`${API_BASE_URL}/api/panel/responsible/${id}`, {
      method: 'PUT',
      headers: getHeaders(),
      body: JSON.stringify(data),
    })
    return response.json()
  },

  async deleteResponsible(id: number): Promise<void> {
    await fetchWithErrorHandling(`${API_BASE_URL}/api/panel/responsible/${id}`, {
      method: 'DELETE',
      headers: getHeaders(),
    })
  },

  async assignResponsible(responsibleId: number, date: string): Promise<void> {
    await fetchWithErrorHandling(`${API_BASE_URL}/api/panel/assign-responsible`, {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify({ responsible_id: responsibleId, date }),
    })
  },

  async searchPeople(query: string): Promise<Array<{ type: string; id: number; full_name: string; company: string; position: string }>> {
    const response = await fetchWithErrorHandling(`${API_BASE_URL}/api/panel/search?q=${encodeURIComponent(query)}`, {
      headers: getHeaders(),
    })
    return response.json()
  },

  async generateGreeting(birthdayId: number, style: string, length: string, theme?: string): Promise<{ greeting: string }> {
    const response = await fetchWithErrorHandling(`${API_BASE_URL}/api/panel/generate-greeting`, {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify({ birthday_id: birthdayId, style, length, theme }),
    })
    return response.json()
  },

  async createCard(birthdayId: number, greetingText: string, qrUrl?: string): Promise<Blob> {
    const response = await fetchWithErrorHandling(`${API_BASE_URL}/api/panel/create-card`, {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify({ birthday_id: birthdayId, greeting_text: greetingText, qr_url: qrUrl }),
    })
    return response.blob()
  },

  async checkPanelAccess(): Promise<{ has_access: boolean }> {
    const response = await fetchWithErrorHandling(`${API_BASE_URL}/api/panel/check-access`, {
      headers: getHeaders(),
    })
    return response.json()
  },
}

