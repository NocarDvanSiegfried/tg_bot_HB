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
  
  // ЛОГИРОВАНИЕ ПЕРЕД ОТПРАВКОЙ
  logger.info(`[API] ===== Starting ${method} ${url} =====`)
  logger.info(`[API] Request options:`, {
    method,
    headers: options.headers,
    body: options.body ? (typeof options.body === 'string' ? options.body.substring(0, 200) + '...' : '[...]') : undefined
  })
  
  try {
    const controller = new AbortController()
    const timeoutId = setTimeout(() => controller.abort(), API_TIMEOUT_MS)
    
    logger.info(`[API] Sending ${method} request to ${url}...`)
    const response = await fetch(url, {
      ...options,
      signal: controller.signal,
    })
    
    clearTimeout(timeoutId)
    logger.info(`[API] Response received: ${response.status} ${response.statusText}`)
    
    if (!response.ok) {
      // Детальная обработка ошибок
      if (response.status === 0) {
        throw new Error('CORS error: запрос заблокирован браузером')
      }
      
      // Клонируем response перед чтением, чтобы не повредить оригинальный объект
      const responseClone = response.clone()
      
      // Пытаемся получить детали ошибки из ответа
      let errorMessage = `HTTP ${response.status}: ${response.statusText}`
      let errorData: any = null
      try {
        errorData = await responseClone.json()
        if (errorData.detail) {
          // Если detail - строка, используем её
          if (typeof errorData.detail === 'string') {
            errorMessage = errorData.detail
          } else if (Array.isArray(errorData.detail)) {
            // Если detail - массив (ошибки валидации FastAPI)
            const validationErrors = errorData.detail.map((e: any) => {
              const field = e.loc ? e.loc.join('.') : 'unknown'
              return `${field}: ${e.msg || e.message || 'validation error'}`
            }).join(', ')
            errorMessage = `Ошибка валидации: ${validationErrors}`
          }
        } else if (errorData.errors) {
          // Обработка ошибок валидации Pydantic (формат с errors)
          const validationErrors = errorData.errors.map((e: any) => {
            const field = e.loc ? e.loc.join('.') : 'unknown'
            return `${field}: ${e.msg || e.message || 'validation error'}`
          }).join(', ')
          errorMessage = `Ошибка валидации: ${validationErrors}`
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
    logger.error(`[API] ===== Fetch ERROR for ${method} ${url} =====`)
    logger.error(`[API] Error type: ${error instanceof Error ? error.constructor.name : typeof error}`)
    logger.error(`[API] Error message: ${error instanceof Error ? error.message : String(error)}`)
    logger.error(`[API] Error stack: ${error instanceof Error ? error.stack : 'N/A'}`)
    if (error instanceof Error) {
      if (error.name === 'AbortError') {
        throw new Error('Request timeout: сервер не отвечает')
      }
      if (error.message.includes('Failed to fetch') || error.message.includes('NetworkError')) {
        logger.error(`[API] Network error - возможно CORS или сеть: ${error.message}`)
        throw new Error('Network error: не удалось подключиться к серверу. Проверьте подключение к интернету и URL API.')
      }
      // Обработка ошибок CORS
      if (error.message.includes('CORS') || error.message.includes('Cross-Origin')) {
        throw new Error('Ошибка CORS: проверьте настройки сервера')
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
    logger.info(`[API] updateBirthday called with id=${id}, data:`, data)
    const headers = getHeaders()
    headers['Content-Type'] = 'application/json'
    logger.info(`[API] updateBirthday headers:`, { 
      'Content-Type': headers['Content-Type'],
      'X-Init-Data': headers['X-Init-Data'] ? `${headers['X-Init-Data'].substring(0, 20)}...` : 'missing'
    })
    
    try {
      const response = await fetchWithErrorHandling(`${API_BASE_URL}/api/panel/birthdays/${id}`, {
        method: 'PUT',
        headers: headers,
        body: JSON.stringify(data),
      })
      logger.info(`[API] updateBirthday response received, status: ${response.status}`)
      logger.info(`[API] updateBirthday response headers:`, Object.fromEntries(response.headers.entries()))
      
      // Проверка статуса ответа
      if (!response.ok) {
        logger.error(`[API] updateBirthday received non-ok status: ${response.status} ${response.statusText}`)
        throw new Error(`HTTP ${response.status}: ${response.statusText}`)
      }
      
      // Проверка на наличие тела ответа перед чтением
      // Статусы 204 No Content и 205 Reset Content не имеют тела
      if (response.status === 204 || response.status === 205) {
        logger.warn(`[API] updateBirthday received ${response.status} status with no body`)
        throw new Error('Сервер вернул ответ без данных')
      }
      
      // Проверка Content-Length header
      const contentLength = response.headers.get('Content-Length')
      if (contentLength === '0') {
        logger.warn(`[API] updateBirthday received response with Content-Length: 0`)
        throw new Error('Сервер вернул пустой ответ')
      }
      
      logger.info(`[API] updateBirthday reading response body`)
      const result = await response.json()
      logger.info(`[API] updateBirthday response data:`, result)
      
      // Проверка, что ответ содержит ожидаемые данные
      if (!result || typeof result !== 'object') {
        logger.error(`[API] updateBirthday received invalid response data:`, result)
        throw new Error('Сервер вернул невалидные данные')
      }
      
      if (!result.id || !result.full_name) {
        logger.error(`[API] updateBirthday response missing required fields:`, result)
        throw new Error('Сервер вернул неполные данные')
      }
      
      logger.info(`[API] updateBirthday success: id=${result.id}, full_name=${result.full_name}`)
      return result
    } catch (error) {
      logger.error(`[API] updateBirthday error:`, error)
      throw error
    }
  },

  async deleteBirthday(id: number): Promise<void> {
    logger.info(`[API] deleteBirthday called with id=${id}`)
    const headers = getHeaders()
    logger.info(`[API] deleteBirthday headers:`, { 
      'Content-Type': headers['Content-Type'],
      'X-Init-Data': headers['X-Init-Data'] ? `${headers['X-Init-Data'].substring(0, 20)}...` : 'missing'
    })
    
    try {
      const response = await fetchWithErrorHandling(`${API_BASE_URL}/api/panel/birthdays/${id}`, {
        method: 'DELETE',
        headers: headers,
      })
      logger.info(`[API] deleteBirthday response received, status: ${response.status}`)
      logger.info(`[API] deleteBirthday response headers:`, Object.fromEntries(response.headers.entries()))
      
      // Проверка статуса ответа
      if (!response.ok) {
        logger.error(`[API] deleteBirthday received non-ok status: ${response.status} ${response.statusText}`)
        throw new Error(`HTTP ${response.status}: ${response.statusText}`)
      }
      
      // DELETE запросы могут возвращать 204 No Content или 205 Reset Content без тела
      // Не пытаемся читать тело ответа для этих статусов
      if (response.status === 204 || response.status === 205) {
        logger.info(`[API] deleteBirthday received ${response.status} status (no body expected)`)
        logger.info(`[API] deleteBirthday success: birthday ${id} deleted`)
        return
      }
      
      // Если статус не 204/205, проверяем наличие тела ответа
      const contentLength = response.headers.get('Content-Length')
      if (contentLength && contentLength !== '0') {
        logger.info(`[API] deleteBirthday reading response body`)
        const result = await response.json()
        logger.info(`[API] deleteBirthday response data:`, result)
      }
      
      logger.info(`[API] deleteBirthday success: birthday ${id} deleted`)
      
      // Если статус не 204/205, но тело может быть пустым, проверяем Content-Length
      const contentLength = response.headers.get('Content-Length')
      if (contentLength === '0') {
        logger.info(`[API] deleteBirthday received response with Content-Length: 0`)
        return
      }
      
      // Если есть тело ответа, пытаемся его прочитать (опционально, для логирования)
      // Но для DELETE обычно не требуется читать тело
      logger.info(`[API] deleteBirthday completed successfully`)
    } catch (error) {
      logger.error(`[API] deleteBirthday error:`, error)
      throw error
    }
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

