const fallbackUrl = 'http://localhost:8000'
const apiUrl = import.meta.env.VITE_API_URL || fallbackUrl

// Предупреждение в dev режиме, если используется fallback URL
if (import.meta.env.DEV && apiUrl === fallbackUrl) {
  console.warn(
    '[Config] VITE_API_URL не установлен, используется fallback URL:',
    fallbackUrl,
    '\nВ production обязательно установите VITE_API_URL в переменных окружения.'
  )
}

export const API_BASE_URL = apiUrl

