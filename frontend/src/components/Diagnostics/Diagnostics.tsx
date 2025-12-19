import { useEffect, useState } from 'react'
import { useTelegram } from '../../hooks/useTelegram'
import { API_BASE_URL } from '../../config/api'
import './Diagnostics.css'

const STORAGE_KEY_COLLAPSED = 'diagnostics_collapsed'
const STORAGE_KEY_HIDDEN = 'diagnostics_hidden'

// Типы ошибок API
type ApiErrorType = 'CORS' | 'SSL' | 'Network' | 'Timeout' | 'HTTP' | 'Unknown'

interface ApiErrorInfo {
  type: ApiErrorType
  message: string
  details?: string
  httpStatus?: number
  httpStatusText?: string
}

// Функция для нормализации сообщений об ошибках API с детальной информацией
function normalizeApiError(error: unknown, response?: Response): ApiErrorInfo {
  // Если есть HTTP ответ, но статус не OK
  if (response && !response.ok) {
    return {
      type: 'HTTP',
      message: `HTTP ${response.status}: ${response.statusText}`,
      httpStatus: response.status,
      httpStatusText: response.statusText,
      details: `Сервер ответил с ошибкой ${response.status}. Проверьте логи сервера.`,
    }
  }

  // Обрабатываем разные типы ошибок
  if (error instanceof TypeError) {
    const message = error.message.toLowerCase()

    // CORS ошибки обычно проявляются как TypeError с "Failed to fetch"
    // но мы не можем точно определить CORS без дополнительной информации
    if (message.includes('failed to fetch') || message.includes('networkerror')) {
      // Проверяем, может ли это быть CORS ошибка
      // CORS ошибки обычно не дают детальной информации в браузере
      return {
        type: 'Network',
        message: 'Не удалось подключиться к API. Проверьте URL и доступность сервера.',
        details:
          'Возможные причины: сервер недоступен, проблема с сетью, или CORS блокирует запрос. Проверьте настройки ALLOWED_ORIGINS на сервере.',
      }
    }
  }

  if (error instanceof Error) {
    const message = error.message.toLowerCase()
    const name = error.name.toLowerCase()

    // Проверяем имя ошибки
    if (name === 'aborterror' || message.includes('timeout') || message.includes('aborted')) {
      return {
        type: 'Timeout',
        message: 'Превышено время ожидания ответа от API.',
        details: 'Сервер не отвечает в течение 5 секунд. Проверьте, что backend запущен и доступен.',
      }
    }

    // Проверяем сообщение об ошибке
    if (message.includes('failed to fetch') || message.includes('networkerror')) {
      return {
        type: 'Network',
        message: 'Не удалось подключиться к API. Проверьте URL и доступность сервера.',
        details:
          'Возможные причины: сервер недоступен, проблема с сетью, или CORS блокирует запрос. Проверьте настройки ALLOWED_ORIGINS на сервере.',
      }
    }

    if (message.includes('cors') || message.includes('cross-origin')) {
      return {
        type: 'CORS',
        message: 'Ошибка CORS: запрос заблокирован политикой CORS.',
        details:
          'Проверьте настройки ALLOWED_ORIGINS на сервере. Убедитесь, что origin фронтенда добавлен в разрешенные origins.',
      }
    }

    if (message.includes('ssl') || message.includes('certificate') || message.includes('tls')) {
      return {
        type: 'SSL',
        message: 'Ошибка SSL: проблема с сертификатом или безопасным соединением.',
        details: 'Проверьте SSL сертификат на сервере. Убедитесь, что сертификат валиден и не истек.',
      }
    }

    if (message.includes('network request failed')) {
      return {
        type: 'Network',
        message: 'Ошибка сети. Проверьте подключение к интернету.',
        details: 'Проверьте подключение к интернету и доступность сервера.',
      }
    }

    // Возвращаем оригинальное сообщение, если не удалось нормализовать
    return {
      type: 'Unknown',
      message: error.message || 'Неизвестная ошибка',
      details: 'Не удалось определить тип ошибки. Проверьте консоль браузера для деталей.',
    }
  }

  // Если это строка
  if (typeof error === 'string') {
    const message = error.toLowerCase()
    if (message.includes('failed to fetch') || message.includes('networkerror')) {
      return {
        type: 'Network',
        message: 'Не удалось подключиться к API. Проверьте URL и доступность сервера.',
        details:
          'Возможные причины: сервер недоступен, проблема с сетью, или CORS блокирует запрос.',
      }
    }
    return {
      type: 'Unknown',
      message: error,
      details: 'Ошибка в строковом формате.',
    }
  }

  return {
    type: 'Unknown',
    message: 'Неизвестная ошибка',
    details: 'Не удалось определить тип ошибки.',
  }
}

export default function Diagnostics() {
  const { webApp, initData, isReady } = useTelegram()
  const [apiStatus, setApiStatus] = useState<'checking' | 'online' | 'offline'>('checking')
  const [apiError, setApiError] = useState<string | null>(null)
  const [apiErrorInfo, setApiErrorInfo] = useState<ApiErrorInfo | null>(null)
  const [currentOrigin] = useState<string>(() => {
    if (typeof window !== 'undefined') {
      return window.location.origin
    }
    return 'unknown'
  })
  const [corsBlocked, setCorsBlocked] = useState<boolean | null>(null)
  const [isCollapsed, setIsCollapsed] = useState(() => {
    // Проверяем параметр URL
    const urlParams = new URLSearchParams(window.location.search)
    if (urlParams.get('diagnostics') === 'false') {
      return true
    }
    // Проверяем localStorage, но по умолчанию всегда свернута
    // Это позволяет сбросить состояние при обновлении кода
    try {
      const saved = localStorage.getItem(STORAGE_KEY_COLLAPSED)
      // Если значение явно установлено, используем его
      // Иначе по умолчанию свернута
      return saved !== null ? saved === 'true' : true
    } catch {
      // Если localStorage недоступен, по умолчанию свернута
      return true
    }
  })
  const [isHidden, setIsHidden] = useState(() => {
    // Проверяем параметр URL
    const urlParams = new URLSearchParams(window.location.search)
    if (urlParams.get('diagnostics') === 'false') {
      return true
    }
    // Проверяем localStorage
    const saved = localStorage.getItem(STORAGE_KEY_HIDDEN)
    return saved ? saved === 'true' : false
  })

  // Функция для проверки CORS через OPTIONS запрос
  const checkCors = async (): Promise<boolean> => {
    try {
      const controller = new AbortController()
      const timeoutId = setTimeout(() => controller.abort(), 3000) // 3 секунды для CORS проверки

      try {
        const response = await fetch(`${API_BASE_URL}/`, {
          method: 'OPTIONS',
          headers: {
            'Origin': currentOrigin,
            'Access-Control-Request-Method': 'GET',
            'Access-Control-Request-Headers': 'Content-Type',
          },
          signal: controller.signal,
        })

        clearTimeout(timeoutId)
        
        // Если OPTIONS запрос прошел, проверяем CORS заголовки
        const allowOrigin = response.headers.get('Access-Control-Allow-Origin')
        const allowMethods = response.headers.get('Access-Control-Allow-Methods')
        
        // CORS настроен правильно, если:
        // 1. Есть заголовок Access-Control-Allow-Origin со значением "*" или наш origin
        // 2. Или есть заголовок Access-Control-Allow-Methods (значит сервер обрабатывает preflight)
        const hasCorsHeaders = 
          (allowOrigin !== null && (allowOrigin === '*' || allowOrigin === currentOrigin)) ||
          allowMethods !== null

        return hasCorsHeaders
      } catch (error) {
        clearTimeout(timeoutId)
        
        // Если OPTIONS запрос блокируется с "Failed to fetch", это CORS ошибка
        if (error instanceof TypeError || (error instanceof Error && error.message.includes('Failed to fetch'))) {
          return false // CORS блокирует
        }
        // Другие ошибки - не можем определить
        return true // Предполагаем, что CORS настроен
      }
    } catch (error) {
      // Если не удалось проверить, предполагаем что это может быть CORS
      return false
    }
  }

  useEffect(() => {
    // Проверяем доступность API с детальной диагностикой
    const checkApi = async () => {
      setApiStatus('checking')
      setApiError(null)
      setApiErrorInfo(null)
      setCorsBlocked(null)

      // Сначала проверяем CORS
      const corsCheck = await checkCors()
      setCorsBlocked(!corsCheck)

      // Если CORS блокирует, сразу помечаем как CORS ошибку
      if (!corsCheck) {
        const corsErrorInfo: ApiErrorInfo = {
          type: 'CORS',
          message: 'Ошибка CORS: запрос заблокирован политикой CORS.',
          details: `Origin "${currentOrigin}" не разрешен сервером. Добавьте этот origin в ALLOWED_ORIGINS на сервере.`,
        }
        setApiStatus('offline')
        setApiError(corsErrorInfo.message)
        setApiErrorInfo(corsErrorInfo)
        return
      }

      // Пробуем несколько endpoints для проверки
      const endpoints = ['/health', '/']
      let lastError: unknown = null
      let lastResponse: Response | undefined = undefined

      for (const endpoint of endpoints) {
        try {
          const controller = new AbortController()
          const timeoutId = setTimeout(() => controller.abort(), 5000) // 5 секунд таймаут

          let response: Response | undefined

          try {
            response = await fetch(`${API_BASE_URL}${endpoint}`, {
              method: 'GET',
              headers: { 'Content-Type': 'application/json' },
              signal: controller.signal,
            })

            clearTimeout(timeoutId)
          } catch (fetchError) {
            clearTimeout(timeoutId)
            // Если это AbortError, значит таймаут
            if (fetchError instanceof Error && fetchError.name === 'AbortError') {
              const errorInfo = normalizeApiError(fetchError)
              setApiStatus('offline')
              setApiError(errorInfo.message)
              setApiErrorInfo(errorInfo)
              return
            }
            // Сохраняем ошибку и пробуем следующий endpoint
            lastError = fetchError
            continue
          }

          if (response.ok) {
            setApiStatus('online')
            setApiError(null)
            setApiErrorInfo(null)
            return // Успешно подключились
          } else {
            // Сервер ответил, но с ошибкой
            lastResponse = response
            // Пробуем следующий endpoint
            continue
          }
        } catch (error) {
          // Сохраняем ошибку и пробуем следующий endpoint
          lastError = error
          continue
        }
      }

      // Если все endpoints не сработали, показываем последнюю ошибку
      if (lastResponse) {
        // Сервер ответил, но с ошибкой
        const errorInfo = normalizeApiError(null, lastResponse)
        setApiStatus('offline')
        setApiError(errorInfo.message)
        setApiErrorInfo(errorInfo)
      } else if (lastError) {
        // Обрабатываем ошибку с детальной информацией
        // Если CORS проверка прошла, но GET не проходит, это не CORS
        let errorInfo = normalizeApiError(lastError)
        
        // Если CORS проверка показала, что CORS настроен, но все равно ошибка "Failed to fetch",
        // это может быть реальная сетевая проблема, а не CORS
        // corsCheck доступен из замыкания функции checkApi
        if (corsCheck && errorInfo.type === 'Network') {
          // Оставляем как Network ошибку, но добавляем информацию о том, что CORS настроен
          errorInfo = {
            ...errorInfo,
            details: `${errorInfo.details || ''} CORS настроен правильно, проблема в другом.`,
          }
        }
        
        setApiStatus('offline')
        setApiError(errorInfo.message)
        setApiErrorInfo(errorInfo)

        // Логируем детали в консоль для отладки
        if (import.meta.env.DEV) {
          console.error('[Diagnostics] API Error Details:', {
            type: errorInfo.type,
            message: errorInfo.message,
            details: errorInfo.details,
            originalError: lastError,
            url: API_BASE_URL,
          })
        }
      } else {
        // Неожиданная ситуация
        const errorInfo: ApiErrorInfo = {
          type: 'Unknown',
          message: 'Не удалось проверить доступность API',
          details: 'Все попытки подключения не удались.',
        }
        setApiStatus('offline')
        setApiError(errorInfo.message)
        setApiErrorInfo(errorInfo)
      }
    }

    checkApi()
  }, [])

  // Сохраняем состояние collapsed в localStorage
  useEffect(() => {
    localStorage.setItem(STORAGE_KEY_COLLAPSED, String(isCollapsed))
  }, [isCollapsed])

  // Сохраняем состояние hidden в localStorage
  useEffect(() => {
    localStorage.setItem(STORAGE_KEY_HIDDEN, String(isHidden))
  }, [isHidden])

  // Показываем диагностику только в dev режиме
  if (!import.meta.env.DEV) {
    return null
  }

  // Если диагностика скрыта, не рендерим компонент
  if (isHidden) {
    return null
  }

  const toggleCollapsed = () => {
    setIsCollapsed(!isCollapsed)
  }

  const handleHide = () => {
    setIsHidden(true)
  }

  return (
    <div className={`diagnostics ${isCollapsed ? 'diagnostics-collapsed' : ''}`}>
      <div className="diagnostics-header" onClick={toggleCollapsed}>
        <h3>🔍 Диагностика Mini App</h3>
        <div className="diagnostics-controls">
          <button
            className="diagnostics-toggle"
            onClick={(e) => {
              e.stopPropagation()
              toggleCollapsed()
            }}
            aria-label={isCollapsed ? 'Развернуть диагностику' : 'Свернуть диагностику'}
            title={isCollapsed ? 'Развернуть диагностику' : 'Свернуть диагностику'}
          >
            {isCollapsed ? '▶' : '▼'}
          </button>
          <button
            className="diagnostics-close"
            onClick={(e) => {
              e.stopPropagation()
              handleHide()
            }}
            aria-label="Скрыть диагностику"
            title="Скрыть диагностику"
          >
            ×
          </button>
        </div>
      </div>

      {!isCollapsed && (
        <div className="diagnostics-content">
          <div className="diagnostics-section">
            <h4>Telegram WebApp</h4>
            <ul>
              <li>
                <strong>Инициализирован:</strong>{' '}
                <span className={isReady ? 'status-ok' : 'status-error'}>
                  {isReady ? '✅ Да' : '❌ Нет'}
                </span>
              </li>
              <li>
                <strong>WebApp объект:</strong>{' '}
                <span className={webApp ? 'status-ok' : 'status-warning'}>
                  {webApp ? '✅ Доступен' : '⚠️ Недоступен'}
                </span>
              </li>
              <li>
                <strong>initData:</strong>{' '}
                <span className={initData ? 'status-ok' : 'status-warning'}>
                  {initData ? `✅ Есть (${initData.length} символов)` : '⚠️ Отсутствует'}
                </span>
              </li>
            </ul>
          </div>

          <div className="diagnostics-section">
            <h4>API Backend</h4>
            <ul>
              <li>
                <strong>URL:</strong> <code>{API_BASE_URL}</code>
              </li>
              <li>
                <strong>Текущий Origin:</strong> <code>{currentOrigin}</code>
              </li>
              {corsBlocked !== null && (
                <li>
                  <strong>CORS:</strong>{' '}
                  <span className={corsBlocked ? 'status-error' : 'status-ok'}>
                    {corsBlocked ? '❌ Заблокирован' : '✅ Разрешен'}
                  </span>
                </li>
              )}
              <li>
                <strong>Статус:</strong>{' '}
                <span
                  className={
                    apiStatus === 'online'
                      ? 'status-ok'
                      : apiStatus === 'offline'
                        ? 'status-error'
                        : 'status-warning'
                  }
                >
                  {apiStatus === 'online' && '✅ Онлайн'}
                  {apiStatus === 'offline' && '❌ Офлайн'}
                  {apiStatus === 'checking' && '⏳ Проверка...'}
                </span>
              </li>
              {apiError && (
                <>
                  <li>
                    <strong>Ошибка:</strong> <span className="status-error">{apiError}</span>
                  </li>
                  {apiErrorInfo && (
                    <>
                      {apiErrorInfo.type && (
                        <li>
                          <strong>Тип ошибки:</strong>{' '}
                          <span className="status-error">{apiErrorInfo.type}</span>
                        </li>
                      )}
                      {apiErrorInfo.httpStatus && (
                        <li>
                          <strong>HTTP статус:</strong>{' '}
                          <span className="status-error">
                            {apiErrorInfo.httpStatus} {apiErrorInfo.httpStatusText || ''}
                          </span>
                        </li>
                      )}
                      {apiErrorInfo.details && (
                        <li>
                          <strong>Детали:</strong> <span className="status-warning">{apiErrorInfo.details}</span>
                        </li>
                      )}
                    </>
                  )}
                </>
              )}
            </ul>
          </div>

          <div className="diagnostics-section">
            <h4>Рекомендации</h4>
            <ul className="recommendations">
              {!isReady && (
                <li>
                  ⚠️ Telegram WebApp не инициализирован. Убедитесь, что приложение открыто через
                  Telegram.
                </li>
              )}
              {!initData && (
                <li>
                  ⚠️ initData отсутствует. Это нормально, если приложение открыто не через
                  Telegram Mini App.
                </li>
              )}
              {apiStatus === 'offline' && (
                <li>
                  ❌ API недоступен.
                  {apiErrorInfo && (
                    <ul>
                      {apiErrorInfo.type === 'CORS' && (
                        <>
                          <li>
                            <strong>Проблема CORS:</strong> Запрос заблокирован политикой CORS.
                          </li>
                          <li>
                            <strong>Текущий Origin:</strong> <code>{currentOrigin}</code>
                          </li>
                          <li>
                            <strong>Решение:</strong> Добавьте следующий origin в переменную окружения ALLOWED_ORIGINS на
                            сервере:
                            <ul>
                              <li>
                                <code>ALLOWED_ORIGINS={currentOrigin}</code>
                              </li>
                              <li>
                                Или если уже есть другие origins:{' '}
                                <code>ALLOWED_ORIGINS=origin1,{currentOrigin},origin2</code>
                              </li>
                            </ul>
                          </li>
                          <li>
                            <strong>Где настроить:</strong>
                            <ul>
                              <li>В файле <code>.env</code> на сервере добавьте или обновите: <code>ALLOWED_ORIGINS={currentOrigin}</code></li>
                              <li>Перезапустите backend: <code>docker compose restart backend</code></li>
                            </ul>
                          </li>
                          <li>
                            <strong>Проверка:</strong> Откройте консоль браузера (F12) и проверьте ошибки CORS в
                            Network tab. Должна быть ошибка типа "CORS policy" или "Access-Control-Allow-Origin".
                          </li>
                        </>
                      )}
                      {apiErrorInfo.type === 'SSL' && (
                        <>
                          <li>
                            <strong>Проблема SSL:</strong> Ошибка с сертификатом или безопасным соединением.
                          </li>
                          <li>
                            <strong>Решение:</strong> Проверьте SSL сертификат на сервере. Убедитесь, что сертификат
                            валиден и не истек.
                          </li>
                          <li>
                            <strong>Проверка:</strong> Откройте https://api.micro-tab.ru:9443 в браузере и проверьте
                            сертификат.
                          </li>
                        </>
                      )}
                      {apiErrorInfo.type === 'Network' && (
                        <>
                          <li>
                            <strong>Проблема сети:</strong> Не удалось подключиться к серверу.
                          </li>
                          <li>
                            <strong>Проверьте:</strong>
                            <ul>
                              <li>Запущен ли backend сервер (docker compose ps)</li>
                              <li>Правильно ли настроен VITE_API_URL</li>
                              <li>Доступен ли API из браузера (откройте URL в новой вкладке)</li>
                              <li>Работает ли Nginx (sudo systemctl status nginx)</li>
                            </ul>
                          </li>
                          <li>
                            <strong>Возможная причина CORS:</strong> Если сервер доступен через браузер, но запрос
                            не проходит, это может быть проблема CORS. Проверьте ALLOWED_ORIGINS.
                          </li>
                        </>
                      )}
                      {apiErrorInfo.type === 'Timeout' && (
                        <>
                          <li>
                            <strong>Проблема таймаута:</strong> Сервер не отвечает в течение 5 секунд.
                          </li>
                          <li>
                            <strong>Проверьте:</strong>
                            <ul>
                              <li>Запущен ли backend сервер</li>
                              <li>Не перегружен ли сервер</li>
                              <li>Работает ли Nginx и проксирует ли запросы</li>
                            </ul>
                          </li>
                        </>
                      )}
                      {apiErrorInfo.type === 'HTTP' && apiErrorInfo.httpStatus && (
                        <>
                          <li>
                            <strong>HTTP ошибка:</strong> Сервер ответил с кодом {apiErrorInfo.httpStatus}
                            {apiErrorInfo.httpStatusText && ` (${apiErrorInfo.httpStatusText})`}
                          </li>
                          <li>
                            <strong>Проверьте:</strong>
                            <ul>
                              <li>Логи backend сервера (docker compose logs backend)</li>
                              <li>Логи Nginx (sudo tail -f /var/log/nginx/backend_error.log)</li>
                              <li>Конфигурацию Nginx</li>
                            </ul>
                          </li>
                        </>
                      )}
                      {apiErrorInfo.type === 'Unknown' && (
                        <>
                          <li>
                            <strong>Неизвестная ошибка:</strong> Не удалось определить тип ошибки.
                          </li>
                          <li>
                            <strong>Проверьте:</strong>
                            <ul>
                              <li>Консоль браузера (F12) для деталей ошибки</li>
                              <li>Запущен ли backend сервер</li>
                              <li>Правильно ли настроен VITE_API_URL</li>
                            </ul>
                          </li>
                        </>
                      )}
                      {!apiErrorInfo.type && (
                        <>
                          <li>Запущен ли backend сервер</li>
                          <li>Правильно ли настроен VITE_API_URL</li>
                          <li>
                            Доступен ли API из браузера (для Mini App нужен внешний URL, не localhost)
                          </li>
                          <li>Для разработки используйте ngrok или другой tunnel</li>
                        </>
                      )}
                    </ul>
                  )}
                  {!apiErrorInfo && (
                    <ul>
                      <li>Запущен ли backend сервер</li>
                      <li>Правильно ли настроен VITE_API_URL</li>
                      <li>
                        Доступен ли API из браузера (для Mini App нужен внешний URL, не localhost)
                      </li>
                      <li>Для разработки используйте ngrok или другой tunnel</li>
                    </ul>
                  )}
                </li>
              )}
              {API_BASE_URL.includes('localhost') && (
                <li>
                  ⚠️ VITE_API_URL указывает на localhost. Для Mini App нужен внешний HTTPS URL.
                  Используйте ngrok для разработки.
                </li>
              )}
            </ul>
          </div>
        </div>
      )}
    </div>
  )
}

