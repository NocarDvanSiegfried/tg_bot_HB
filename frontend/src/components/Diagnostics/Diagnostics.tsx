import { useEffect, useState } from 'react'
import { useTelegram } from '../../hooks/useTelegram'
import { API_BASE_URL } from '../../config/api'
import './Diagnostics.css'

export default function Diagnostics() {
  const { webApp, initData, isReady } = useTelegram()
  const [apiStatus, setApiStatus] = useState<'checking' | 'online' | 'offline'>('checking')
  const [apiError, setApiError] = useState<string | null>(null)

  useEffect(() => {
    // Проверяем доступность API
    const checkApi = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/`, {
          method: 'GET',
          headers: { 'Content-Type': 'application/json' },
        })
        if (response.ok) {
          setApiStatus('online')
          setApiError(null)
        } else {
          setApiStatus('offline')
          setApiError(`HTTP ${response.status}: ${response.statusText}`)
        }
      } catch (error) {
        setApiStatus('offline')
        setApiError(error instanceof Error ? error.message : 'Unknown error')
      }
    }

    checkApi()
  }, [])

  // Показываем диагностику только в dev режиме
  if (!import.meta.env.DEV) {
    return null
  }

  return (
    <div className="diagnostics">
      <h3>🔍 Диагностика Mini App (только в dev режиме)</h3>
      
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
              ⚠️ initData отсутствует. Это нормально, если приложение открыто не через Telegram
              Mini App.
            </li>
          )}
          {apiStatus === 'offline' && (
            <li>
              ❌ API недоступен. Проверьте:
              <ul>
                <li>Запущен ли backend сервер</li>
                <li>Правильно ли настроен VITE_API_URL</li>
                <li>Доступен ли API из браузера (для Mini App нужен внешний URL, не localhost)</li>
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
  )
}

