import { useEffect, useState } from 'react'
import { useTelegram } from '../../hooks/useTelegram'
import { API_BASE_URL } from '../../config/api'
import './Diagnostics.css'

const STORAGE_KEY_COLLAPSED = 'diagnostics_collapsed'
const STORAGE_KEY_HIDDEN = 'diagnostics_hidden'

// Функция для нормализации сообщений об ошибках API
function normalizeApiError(error: unknown): string {
  if (!(error instanceof Error)) {
    return 'Неизвестная ошибка'
  }

  const message = error.message.toLowerCase()

  if (message.includes('failed to fetch') || message.includes('networkerror')) {
    return 'Не удалось подключиться к API. Проверьте URL и доступность сервера.'
  }

  if (error.name === 'AbortError' || message.includes('timeout')) {
    return 'Превышено время ожидания ответа от API.'
  }

  if (message.includes('cors') || message.includes('cross-origin')) {
    return 'Ошибка CORS. Проверьте настройки сервера.'
  }

  if (message.includes('network request failed')) {
    return 'Ошибка сети. Проверьте подключение к интернету.'
  }

  return error.message || 'Неизвестная ошибка'
}

export default function Diagnostics() {
  const { webApp, initData, isReady } = useTelegram()
  const [apiStatus, setApiStatus] = useState<'checking' | 'online' | 'offline'>('checking')
  const [apiError, setApiError] = useState<string | null>(null)
  const [isCollapsed, setIsCollapsed] = useState(() => {
    // Проверяем параметр URL
    const urlParams = new URLSearchParams(window.location.search)
    if (urlParams.get('diagnostics') === 'false') {
      return true
    }
    // Проверяем localStorage
    const saved = localStorage.getItem(STORAGE_KEY_COLLAPSED)
    return saved ? saved === 'true' : true // По умолчанию свернута
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

  useEffect(() => {
    // Проверяем доступность API
    const checkApi = async () => {
      try {
        const controller = new AbortController()
        const timeoutId = setTimeout(() => controller.abort(), 5000) // 5 секунд таймаут

        const response = await fetch(`${API_BASE_URL}/`, {
          method: 'GET',
          headers: { 'Content-Type': 'application/json' },
          signal: controller.signal,
        })

        clearTimeout(timeoutId)

        if (response.ok) {
          setApiStatus('online')
          setApiError(null)
        } else {
          setApiStatus('offline')
          setApiError(`HTTP ${response.status}: ${response.statusText}`)
        }
      } catch (error) {
        setApiStatus('offline')
        setApiError(normalizeApiError(error))
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
                <li>
                  <strong>Ошибка:</strong> <span className="status-error">{apiError}</span>
                </li>
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
                  ❌ API недоступен. Проверьте:
                  <ul>
                    <li>Запущен ли backend сервер</li>
                    <li>Правильно ли настроен VITE_API_URL</li>
                    <li>
                      Доступен ли API из браузера (для Mini App нужен внешний URL, не localhost)
                    </li>
                    <li>Для разработки используйте ngrok или другой tunnel</li>
                  </ul>
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

