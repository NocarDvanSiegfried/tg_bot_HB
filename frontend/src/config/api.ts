const fallbackUrl = 'http://localhost:8000'
const apiUrl = import.meta.env.VITE_API_URL || fallbackUrl

// Таймаут для API запросов (в миллисекундах)
// Можно переопределить через переменную окружения VITE_API_TIMEOUT_MS
export const API_TIMEOUT_MS = Number(import.meta.env.VITE_API_TIMEOUT_MS) || 30000

// Проверка на localhost (не работает для Telegram Mini App)
const isLocalhost = apiUrl.includes('localhost') || apiUrl.includes('127.0.0.1') || apiUrl.startsWith('http://localhost') || apiUrl.startsWith('http://127.0.0.1')

// Предупреждение в dev режиме, если используется fallback URL
// Используем прямой console.warn, так как logger может быть еще не инициализирован
if (import.meta.env.DEV && apiUrl === fallbackUrl) {
  console.warn(
    '[Config] VITE_API_URL не установлен, используется fallback URL:',
    fallbackUrl,
    '\nВ production обязательно установите VITE_API_URL в переменных окружения.',
    '\nДля Telegram Mini App нужен внешний URL (не localhost).',
    '\nДля разработки используйте ngrok или другой tunnel.'
  )
}

// Предупреждение, если используется localhost (не работает для Mini App)
// Проверяем только если приложение запущено в Telegram (есть window.Telegram)
if (typeof window !== 'undefined' && window.Telegram?.WebApp && isLocalhost) {
  console.error(
    '[Config] КРИТИЧЕСКАЯ ОШИБКА: VITE_API_URL указывает на localhost!',
    '\nTelegram Mini App не может обращаться к localhost.',
    '\nТекущий URL:', apiUrl,
    '\n\nРешение:',
    '\n1. Для разработки: используйте ngrok (ngrok http 8000)',
    '\n2. Для production: установите VITE_API_URL на внешний HTTPS URL',
    '\n   Пример: VITE_API_URL=https://your-domain.com:8001',
    '\n\nПодробные инструкции: см. MINI_APP_SETUP.md'
  )
}

export const API_BASE_URL = apiUrl

// Проверка конфигурации API_BASE_URL
if (!API_BASE_URL) {
  console.error('[API] API_BASE_URL is not defined!')
  throw new Error('API_BASE_URL is not configured')
}

console.log(`[API] Using API_BASE_URL: ${API_BASE_URL}`)

