import { Birthday } from '../types/birthday'
import { Responsible } from '../types/responsible'
import { API_BASE_URL } from '../config/api'

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

export const api = {
  async getCalendar(date: string): Promise<CalendarData> {
    const response = await fetch(`${API_BASE_URL}/api/calendar/${date}`, {
      headers: getHeaders(),
    })
    if (!response.ok) throw new Error('Failed to fetch calendar')
    return response.json()
  },

  async getBirthdays(): Promise<Birthday[]> {
    const response = await fetch(`${API_BASE_URL}/api/panel/birthdays`, {
      headers: getHeaders(),
    })
    if (!response.ok) throw new Error('Failed to fetch birthdays')
    return response.json()
  },

  async createBirthday(data: Omit<Birthday, 'id'>): Promise<Birthday> {
    const response = await fetch(`${API_BASE_URL}/api/panel/birthdays`, {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify(data),
    })
    if (!response.ok) throw new Error('Failed to create birthday')
    return response.json()
  },

  async updateBirthday(id: number, data: Partial<Birthday>): Promise<Birthday> {
    const response = await fetch(`${API_BASE_URL}/api/panel/birthdays/${id}`, {
      method: 'PUT',
      headers: getHeaders(),
      body: JSON.stringify(data),
    })
    if (!response.ok) throw new Error('Failed to update birthday')
    return response.json()
  },

  async deleteBirthday(id: number): Promise<void> {
    const response = await fetch(`${API_BASE_URL}/api/panel/birthdays/${id}`, {
      method: 'DELETE',
      headers: getHeaders(),
    })
    if (!response.ok) throw new Error('Failed to delete birthday')
  },

  async getResponsible(): Promise<Responsible[]> {
    const response = await fetch(`${API_BASE_URL}/api/panel/responsible`, {
      headers: getHeaders(),
    })
    if (!response.ok) throw new Error('Failed to fetch responsible')
    return response.json()
  },

  async createResponsible(data: Omit<Responsible, 'id'>): Promise<Responsible> {
    const response = await fetch(`${API_BASE_URL}/api/panel/responsible`, {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify(data),
    })
    if (!response.ok) throw new Error('Failed to create responsible')
    return response.json()
  },

  async updateResponsible(id: number, data: Partial<Responsible>): Promise<Responsible> {
    const response = await fetch(`${API_BASE_URL}/api/panel/responsible/${id}`, {
      method: 'PUT',
      headers: getHeaders(),
      body: JSON.stringify(data),
    })
    if (!response.ok) throw new Error('Failed to update responsible')
    return response.json()
  },

  async deleteResponsible(id: number): Promise<void> {
    const response = await fetch(`${API_BASE_URL}/api/panel/responsible/${id}`, {
      method: 'DELETE',
      headers: getHeaders(),
    })
    if (!response.ok) throw new Error('Failed to delete responsible')
  },

  async assignResponsible(responsibleId: number, date: string): Promise<void> {
    const response = await fetch(`${API_BASE_URL}/api/panel/assign-responsible`, {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify({ responsible_id: responsibleId, date }),
    })
    if (!response.ok) throw new Error('Failed to assign responsible')
  },

  async searchPeople(query: string): Promise<Array<{ type: string; id: number; full_name: string; company: string; position: string }>> {
    const response = await fetch(`${API_BASE_URL}/api/panel/search?q=${encodeURIComponent(query)}`, {
      headers: getHeaders(),
    })
    if (!response.ok) throw new Error('Failed to search')
    return response.json()
  },

  async generateGreeting(birthdayId: number, style: string, length: string, theme?: string): Promise<{ greeting: string }> {
    const response = await fetch(`${API_BASE_URL}/api/panel/generate-greeting`, {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify({ birthday_id: birthdayId, style, length, theme }),
    })
    if (!response.ok) throw new Error('Failed to generate greeting')
    return response.json()
  },

  async createCard(birthdayId: number, greetingText: string, qrUrl?: string): Promise<Blob> {
    const response = await fetch(`${API_BASE_URL}/api/panel/create-card`, {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify({ birthday_id: birthdayId, greeting_text: greetingText, qr_url: qrUrl }),
    })
    if (!response.ok) throw new Error('Failed to create card')
    return response.blob()
  },

  async checkPanelAccess(): Promise<{ has_access: boolean }> {
    const response = await fetch(`${API_BASE_URL}/api/panel/check-access`, {
      headers: getHeaders(),
    })
    if (!response.ok) throw new Error('Failed to check panel access')
    return response.json()
  },
}

