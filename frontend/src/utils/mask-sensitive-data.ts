/**
 * Mask Sensitive Data - утилиты для маскировки чувствительных данных в логах
 * 
 * Предотвращает утечку чувствительных данных (токены, пароли, API ключи)
 * в логи приложения.
 */

/**
 * Список полей, которые содержат чувствительные данные
 */
const SENSITIVE_FIELDS = [
  'X-Init-Data',
  'Authorization',
  'X-Api-Key',
  'X-Auth-Token',
  'password',
  'token',
  'secret',
  'api_key',
  'apiKey',
] as const

/**
 * Маскировать значение чувствительного поля
 * 
 * @param value - исходное значение
 * @param visibleChars - количество видимых символов в начале (по умолчанию 20)
 * @returns замаскированное значение (первые N символов + "...")
 */
function maskValue(value: string, visibleChars: number = 20): string {
  if (!value || value.length <= visibleChars) {
    return '***'
  }
  return `${value.substring(0, visibleChars)}...`
}

/**
 * Проверить, является ли поле чувствительным
 * 
 * @param fieldName - имя поля
 * @returns true, если поле содержит чувствительные данные
 */
function isSensitiveField(fieldName: string): boolean {
  const lowerFieldName = fieldName.toLowerCase()
  return SENSITIVE_FIELDS.some(field => lowerFieldName.includes(field.toLowerCase()))
}

/**
 * Маскировать чувствительные данные в headers
 * 
 * @param headers - объект с headers
 * @returns новый объект с замаскированными чувствительными полями
 */
export function maskSensitiveHeaders(headers: Record<string, string>): Record<string, string> {
  const masked: Record<string, string> = {}
  
  for (const [key, value] of Object.entries(headers)) {
    if (isSensitiveField(key)) {
      masked[key] = maskValue(value)
    } else {
      masked[key] = value
    }
  }
  
  return masked
}

/**
 * Маскировать чувствительные данные в объекте
 * 
 * @param data - объект с данными
 * @returns новый объект с замаскированными чувствительными полями
 */
export function maskSensitiveData(data: Record<string, any>): Record<string, any> {
  const masked: Record<string, any> = {}
  
  for (const [key, value] of Object.entries(data)) {
    if (isSensitiveField(key)) {
      if (typeof value === 'string') {
        masked[key] = maskValue(value)
      } else {
        masked[key] = '***'
      }
    } else if (typeof value === 'object' && value !== null && !Array.isArray(value)) {
      // Рекурсивно маскируем вложенные объекты
      masked[key] = maskSensitiveData(value as Record<string, any>)
    } else {
      masked[key] = value
    }
  }
  
  return masked
}

