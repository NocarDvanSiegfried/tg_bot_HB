// VITE_API_URL обязателен для работы приложения
// Проект работает на сервере, localhost не поддерживается
const apiUrl = import.meta.env.VITE_API_URL

if (!apiUrl) {
  const errorMessage = 'VITE_API_URL is required and must be set in environment variables. ' +
    'The application runs on a server and requires a production URL (HTTPS). ' +
    'Please set VITE_API_URL in your environment configuration.'
  // В production ошибки конфигурации должны быть видны
  // Используем console.error только для критических ошибок
  if (typeof console !== 'undefined' && console.error) {
    console.error('[Config]', errorMessage)
  }
  throw new Error(errorMessage)
}

// Таймаут для API запросов (в миллисекундах)
// Можно переопределить через переменную окружения VITE_API_TIMEOUT_MS
export const API_TIMEOUT_MS = Number(import.meta.env.VITE_API_TIMEOUT_MS) || 30000

// Проверка на использование HTTP (для production рекомендуется HTTPS)
// Предупреждение только в development
if (import.meta.env.DEV && apiUrl.startsWith('http://')) {
  if (typeof console !== 'undefined' && console.warn) {
    console.warn(
      '[Config] VITE_API_URL использует HTTP вместо HTTPS.',
      '\nДля production рекомендуется использовать HTTPS для безопасности.',
      '\nТекущий URL:', apiUrl
    )
  }
}

export const API_BASE_URL = apiUrl

// Проверка конфигурации API_BASE_URL
if (!API_BASE_URL) {
  // Критическая ошибка - должна быть видна в production
  if (typeof console !== 'undefined' && console.error) {
    console.error('[API] API_BASE_URL is not defined!')
  }
  throw new Error('API_BASE_URL is not configured')
}

// Логирование только в development режиме
if (import.meta.env.DEV && typeof console !== 'undefined' && console.log) {
  console.log(`[API] Using API_BASE_URL: ${API_BASE_URL}`)
}

