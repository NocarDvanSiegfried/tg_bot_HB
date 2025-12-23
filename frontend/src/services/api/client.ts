/**
 * API Client - базовый HTTP клиент для API запросов
 * 
 * Содержит базовые функции для работы с API:
 * - getInitData() - получение initData из Telegram WebApp
 * - getHeaders() - создание headers с авторизацией
 * - fetchWithErrorHandling() - выполнение запросов с обработкой ошибок
 */

import { API_BASE_URL, API_TIMEOUT_MS } from '../../config/api'
import { logger } from '../../utils/logger'
import { maskSensitiveHeaders } from '../../utils/mask-sensitive-data'
import { handleHttpError, handleNetworkError } from './error-handler'

/**
 * Получить initData из Telegram WebApp
 */
export function getInitData(): string | null {
  if (typeof window !== 'undefined' && window.Telegram?.WebApp) {
    return window.Telegram.WebApp.initData || null
  }
  return null
}

/**
 * Создать headers с initData для авторизации
 */
export function getHeaders(additionalHeaders: Record<string, string> = {}): Record<string, string> {
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

/**
 * Выполнить fetch запрос с обработкой ошибок и таймаутом
 * 
 * @param url - полный URL запроса (включая API_BASE_URL)
 * @param options - опции для fetch запроса
 * @returns Promise<Response> - ответ сервера
 * @throws Error - ошибка с понятным сообщением
 */
export async function fetchWithErrorHandling(
  url: string,
  options: RequestInit = {}
): Promise<Response> {
  const method = options.method || 'GET'
  
  // ЛОГИРОВАНИЕ ПЕРЕД ОТПРАВКОЙ (с маскировкой чувствительных данных)
  const headersToLog = options.headers && typeof options.headers === 'object' && !(options.headers instanceof Headers)
    ? maskSensitiveHeaders(options.headers as Record<string, string>)
    : options.headers
  
  logger.info(`[API] ===== Starting ${method} ${url} =====`)
  logger.info(`[API] Request options:`, {
    method,
    headers: headersToLog,
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
      // Обработка HTTP ошибок
      const apiError = await handleHttpError(response, url, method)
      throw new Error(apiError.message)
    }
    
    return response
  } catch (error) {
    // Обработка Network и других ошибок
    const apiError = handleNetworkError(error, url, method)
    throw new Error(apiError.message)
  }
}

/**
 * Создать полный URL для API запроса
 * 
 * @param endpoint - endpoint путь (например, '/api/calendar')
 * @returns полный URL с API_BASE_URL
 */
export function buildApiUrl(endpoint: string): string {
  return `${API_BASE_URL}${endpoint}`
}

