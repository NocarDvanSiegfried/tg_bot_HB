import { Birthday } from '../types/birthday'
import { Responsible } from '../types/responsible'
import { Holiday } from '../types/holiday'
import { logger } from '../utils/logger'
import { cache, CacheKeys, CacheTTL } from '../utils/cache'
import { API_ENDPOINTS } from './api/endpoints'
import { buildApiUrl, fetchWithErrorHandling, getHeaders } from './api/client'

export interface CalendarData {
  date: string
  birthdays: Array<{
    id: number
    full_name: string
    company: string
    position: string
    age: number
    comment?: string
    responsible?: string
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
    const response = await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.CALENDAR(date)), {
      headers: getHeaders(),
    })
    return response.json()
  },

  async getCalendarMonth(year: number, month: number): Promise<MonthBirthdays> {
    const cacheKey = CacheKeys.calendarMonth(year, month)
    
    // Проверяем кэш
    const cached = cache.get<MonthBirthdays>(cacheKey)
    if (cached) {
      logger.info(`[API] Cache hit for calendar month ${year}/${month}`)
      return cached
    }
    
    // Загружаем данные
    const response = await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.CALENDAR_MONTH(year, month)), {
      headers: getHeaders(),
    })
    const data = await response.json()
    
    // Сохраняем в кэш
    cache.set(cacheKey, data, CacheTTL.calendarMonth)
    
    return data
  },

  async getBirthdays(): Promise<Birthday[]> {
    const cacheKey = CacheKeys.birthdays
    
    // Проверяем кэш
    const cached = cache.get<Birthday[]>(cacheKey)
    if (cached) {
      logger.info('[API] Cache hit for birthdays')
      return cached
    }
    
    // Загружаем данные
    const response = await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.BIRTHDAYS.LIST), {
      headers: getHeaders(),
    })
    const data = await response.json()
    
    // Сохраняем в кэш
    cache.set(cacheKey, data, CacheTTL.birthdays)
    
    return data
  },

  async createBirthday(data: Omit<Birthday, 'id'>): Promise<Birthday> {
    const response = await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.BIRTHDAYS.LIST), {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify(data),
    })
    const result = await response.json()
    
    // Инвалидируем кэш дней рождения
    cache.delete(CacheKeys.birthdays)
    cache.invalidatePattern('^calendar:') // Инвалидируем все месяцы календаря
    
    return result
  },

  async updateBirthday(id: number, data: Partial<Birthday>): Promise<Birthday> {
    const response = await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.BIRTHDAYS.BY_ID(id)), {
      method: 'PUT',
      headers: getHeaders(),
      body: JSON.stringify(data),
    })
    
    // Проверка на наличие тела ответа перед чтением
    // Статусы 204 No Content и 205 Reset Content не имеют тела
    if (response.status === 204 || response.status === 205) {
      throw new Error('Сервер вернул ответ без данных')
    }
    
    // Проверка Content-Length header
    const contentLength = response.headers.get('Content-Length')
    if (contentLength === '0') {
      throw new Error('Сервер вернул пустой ответ')
    }
    
    const result = await response.json()
    
    // Проверка, что ответ содержит ожидаемые данные
    if (!result || typeof result !== 'object' || !result.id || !result.full_name) {
      throw new Error('Сервер вернул невалидные данные')
    }
    
    // Инвалидируем кэш дней рождения
    cache.delete(CacheKeys.birthdays)
    cache.delete(CacheKeys.birthday(id))
    cache.invalidatePattern('^calendar:') // Инвалидируем все месяцы календаря
    
    return result
  },

  async deleteBirthday(id: number): Promise<void> {
    const response = await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.BIRTHDAYS.BY_ID(id)), {
      method: 'DELETE',
      headers: getHeaders(),
    })
    
    // DELETE запросы могут возвращать 204 No Content или 205 Reset Content без тела
    // Не пытаемся читать тело ответа для этих статусов
    if (response.status === 204 || response.status === 205) {
      // Инвалидируем кэш дней рождения
      cache.delete(CacheKeys.birthdays)
      cache.delete(CacheKeys.birthday(id))
      cache.invalidatePattern('^calendar:') // Инвалидируем все месяцы календаря
      return
    }
    
    // Если статус не 204/205, проверяем наличие тела ответа
    const contentLength = response.headers.get('Content-Length')
    if (contentLength && contentLength !== '0') {
      await response.json()
    }
    
    // Инвалидируем кэш дней рождения
    cache.delete(CacheKeys.birthdays)
    cache.delete(CacheKeys.birthday(id))
    cache.invalidatePattern('^calendar:') // Инвалидируем все месяцы календаря
  },

  async getResponsible(): Promise<Responsible[]> {
    const response = await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.RESPONSIBLE.LIST), {
      headers: getHeaders(),
    })
    return response.json()
  },

  async createResponsible(data: Omit<Responsible, 'id'>): Promise<Responsible> {
    const response = await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.RESPONSIBLE.LIST), {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify(data),
    })
    return response.json()
  },

  async updateResponsible(id: number, data: Partial<Responsible>): Promise<Responsible> {
    const response = await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.RESPONSIBLE.BY_ID(id)), {
      method: 'PUT',
      headers: getHeaders(),
      body: JSON.stringify(data),
    })
    return response.json()
  },

  async deleteResponsible(id: number): Promise<void> {
    await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.RESPONSIBLE.BY_ID(id)), {
      method: 'DELETE',
      headers: getHeaders(),
    })
  },

  async assignResponsible(responsibleId: number, date: string): Promise<void> {
    await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.RESPONSIBLE.ASSIGN), {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify({ responsible_id: responsibleId, date }),
    })
  },

  async searchPeople(query: string): Promise<Array<{ type: string; id: number; full_name: string; company: string; position: string }>> {
    const response = await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.SEARCH.PEOPLE(query)), {
      headers: getHeaders(),
    })
    return response.json()
  },

  async generateGreeting(birthdayId: number, style: string, length: string, theme?: string): Promise<{ greeting: string }> {
    const response = await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.GREETING.GENERATE), {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify({ birthday_id: birthdayId, style, length, theme }),
    })
    return response.json()
  },

  async createCard(birthdayId: number, greetingText: string, qrUrl?: string): Promise<Blob> {
    const response = await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.GREETING.CREATE_CARD), {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify({ birthday_id: birthdayId, greeting_text: greetingText, qr_url: qrUrl }),
    })
    return response.blob()
  },

  async checkPanelAccess(): Promise<{ has_access: boolean }> {
    const response = await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.PANEL.CHECK_ACCESS), {
      headers: getHeaders(),
    })
    return response.json()
  },

  async getHolidays(): Promise<Holiday[]> {
    const cacheKey = CacheKeys.holidays
    
    // Проверяем кэш
    const cached = cache.get<Holiday[]>(cacheKey)
    if (cached) {
      logger.info('[API] Cache hit for holidays')
      return cached
    }
    
    // Загружаем данные
    const response = await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.HOLIDAYS.LIST), {
      headers: getHeaders(),
    })
    const data = await response.json()
    
    // Сохраняем в кэш
    cache.set(cacheKey, data, CacheTTL.holidays)
    
    return data
  },

  async createHoliday(data: Omit<Holiday, 'id'>): Promise<Holiday> {
    const response = await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.HOLIDAYS.LIST), {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify(data),
    })
    const result = await response.json()
    
    // Инвалидируем кэш праздников
    cache.delete(CacheKeys.holidays)
    cache.invalidatePattern('^calendar:') // Инвалидируем все месяцы календаря
    
    return result
  },

  async updateHoliday(id: number, data: Partial<Holiday>): Promise<Holiday> {
    const response = await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.HOLIDAYS.BY_ID(id)), {
      method: 'PUT',
      headers: getHeaders(),
      body: JSON.stringify(data),
    })
    
    // Проверка на наличие тела ответа перед чтением
    if (response.status === 204 || response.status === 205) {
      throw new Error('Сервер вернул ответ без данных')
    }
    
    const contentLength = response.headers.get('Content-Length')
    if (contentLength === '0') {
      throw new Error('Сервер вернул пустой ответ')
    }
    
    const result = await response.json()
    
    // Проверка, что ответ содержит ожидаемые данные
    if (!result || typeof result !== 'object' || !result.id || !result.name) {
      throw new Error('Сервер вернул невалидные данные')
    }
    
    // Инвалидируем кэш праздников
    cache.delete(CacheKeys.holidays)
    cache.delete(CacheKeys.holiday(id))
    cache.invalidatePattern('^calendar:') // Инвалидируем все месяцы календаря
    
    return result
  },

  async deleteHoliday(id: number): Promise<void> {
    const response = await fetchWithErrorHandling(buildApiUrl(API_ENDPOINTS.HOLIDAYS.BY_ID(id)), {
      method: 'DELETE',
      headers: getHeaders(),
    })
    
    if (!response.ok) {
      const errorText = await response.text()
      throw new Error(`Failed to delete holiday: ${errorText}`)
    }
    
    // Инвалидируем кэш праздников
    cache.delete(CacheKeys.holidays)
    cache.delete(CacheKeys.holiday(id))
    cache.invalidatePattern('^calendar:') // Инвалидируем все месяцы календаря
  },
}

