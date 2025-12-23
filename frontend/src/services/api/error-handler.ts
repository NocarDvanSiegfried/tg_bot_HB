/**
 * Error Handler - обработка ошибок API запросов
 * 
 * Централизованная обработка всех типов ошибок API:
 * - CORS ошибки
 * - HTTP ошибки (401, 403, 404, 422, 500+)
 * - Network ошибки
 * - Timeout ошибки
 * - Ошибки валидации (FastAPI format)
 */

import { logger } from '../../utils/logger'

export interface ApiError {
  message: string
  status?: number
  statusText?: string
  data?: any
}

/**
 * Обработка ошибок валидации FastAPI
 * Преобразует массив ошибок валидации в читаемое сообщение
 */
function formatValidationErrors(errorData: any): string {
  if (errorData.detail) {
    // Если detail - строка, используем её
    if (typeof errorData.detail === 'string') {
      return errorData.detail
    }
    
    // Если detail - массив (ошибки валидации FastAPI)
    if (Array.isArray(errorData.detail)) {
      const validationErrors = errorData.detail.map((e: any) => {
        const field = e.loc ? e.loc.slice(1).join('.') : 'unknown' // Убираем 'body' из пути
        const fieldName = field === 'full_name' ? 'ФИО' :
                         field === 'company' ? 'Компания' :
                         field === 'position' ? 'Должность' :
                         field === 'birth_date' ? 'Дата рождения' :
                         field === 'comment' ? 'Комментарий' : field
        const message = e.msg || e.message || 'Ошибка валидации'
        return `${fieldName}: ${message}`
      }).join('; ')
      return `Ошибка валидации: ${validationErrors}`
    }
  }
  
  // Обработка ошибок валидации Pydantic (формат с errors)
  if (errorData.errors && Array.isArray(errorData.errors)) {
    const validationErrors = errorData.errors.map((e: any) => {
      const field = e.loc ? e.loc.slice(1).join('.') : 'unknown'
      const fieldName = field === 'full_name' ? 'ФИО' :
                       field === 'company' ? 'Компания' :
                       field === 'position' ? 'Должность' :
                       field === 'birth_date' ? 'Дата рождения' :
                       field === 'comment' ? 'Комментарий' : field
      const message = e.msg || e.message || 'Ошибка валидации'
      return `${fieldName}: ${message}`
    }).join('; ')
    return `Ошибка валидации: ${validationErrors}`
  }
  
  return ''
}

/**
 * Обработка HTTP ошибок ответа
 * Преобразует Response в понятное сообщение об ошибке
 */
export async function handleHttpError(response: Response, url: string, method: string): Promise<ApiError> {
  // CORS ошибка
  if (response.status === 0) {
    return {
      message: 'CORS error: запрос заблокирован браузером',
      status: 0,
    }
  }
  
  // Клонируем response перед чтением, чтобы не повредить оригинальный объект
  const responseClone = response.clone()
  
  // Пытаемся получить детали ошибки из ответа
  let errorMessage = `HTTP ${response.status}: ${response.statusText}`
  let errorData: any = null
  
  try {
    errorData = await responseClone.json()
    const validationMessage = formatValidationErrors(errorData)
    if (validationMessage) {
      errorMessage = validationMessage
    }
    
    // Улучшенные сообщения для различных статусов
    if (response.status === 401) {
      errorMessage = errorMessage || 'Ошибка авторизации. Пожалуйста, обновите страницу.'
    } else if (response.status === 403) {
      errorMessage = errorMessage || 'Доступ запрещен. У вас нет прав для выполнения этого действия.'
    } else if (response.status === 404) {
      errorMessage = errorMessage || 'Ресурс не найден. Возможно, он был удален.'
    } else if (response.status === 422) {
      errorMessage = errorMessage || 'Ошибка валидации данных. Проверьте введенные данные.'
    } else if (response.status >= 500) {
      errorMessage = 'Ошибка сервера. Пожалуйста, попробуйте позже.'
    }
    
    logger.error(`[API] Error response for ${method} ${url}:`, errorData)
  } catch {
    // Игнорируем ошибку парсинга JSON
    logger.error(`[API] Error response for ${method} ${url}: ${response.status} ${response.statusText}`)
  }
  
  return {
    message: errorMessage,
    status: response.status,
    statusText: response.statusText,
    data: errorData,
  }
}

/**
 * Обработка ошибок сети и других исключений
 * Преобразует различные типы ошибок в понятное сообщение
 */
export function handleNetworkError(error: unknown, url: string, method: string): ApiError {
  logger.error(`[API] ===== Fetch ERROR for ${method} ${url} =====`)
  logger.error(`[API] Error type: ${error instanceof Error ? error.constructor.name : typeof error}`)
  logger.error(`[API] Error message: ${error instanceof Error ? error.message : String(error)}`)
  logger.error(`[API] Error stack: ${error instanceof Error ? error.stack : 'N/A'}`)
  
  if (error instanceof Error) {
    // Timeout ошибка
    if (error.name === 'AbortError') {
      return {
        message: 'Request timeout: сервер не отвечает',
      }
    }
    
    // Network ошибка
    if (error.message.includes('Failed to fetch') || error.message.includes('NetworkError')) {
      logger.error(`[API] Network error - возможно CORS или сеть: ${error.message}`)
      return {
        message: 'Network error: не удалось подключиться к серверу. Проверьте подключение к интернету и URL API.',
      }
    }
    
    // CORS ошибка
    if (error.message.includes('CORS') || error.message.includes('Cross-Origin')) {
      return {
        message: 'Ошибка CORS: проверьте настройки сервера',
      }
    }
    
    // Возвращаем оригинальную ошибку
    return {
      message: error.message,
    }
  }
  
  return {
    message: 'Unknown error occurred',
  }
}

/**
 * Главная функция обработки ошибок API
 * Объединяет обработку HTTP и Network ошибок
 * 
 * Примечание: Эта функция используется для синхронной обработки ошибок.
 * Для асинхронной обработки HTTP ошибок используйте handleHttpError напрямую.
 */
export function handleApiError(error: unknown, url?: string, method?: string): never {
  const apiError = handleNetworkError(error, url || '', method || 'GET')
  throw new Error(apiError.message)
}

