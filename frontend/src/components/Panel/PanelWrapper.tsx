import { useEffect, useState } from 'react'
import { useTelegram } from '../../hooks/useTelegram'
import { api } from '../../services/api'
import { logger } from '../../utils/logger'
import Panel from './Panel'

/**
 * PanelWrapper - обертка для панели управления
 * 
 * КРИТИЧНО: Это компонент только для panel-режима
 * - Не знает про user режим
 * - Не делает redirect
 * - Не вызывает navigate
 * - Не проверяет startParam
 * - Не использует useAppMode
 * 
 * Режим определяется только в App.tsx, который рендерит нужное дерево компонентов
 */
export default function PanelWrapper() {
  // Все хуки вызываются всегда, без условий
  const { initData, isReady, webApp } = useTelegram()
  const [isCheckingAccess, setIsCheckingAccess] = useState(true)
  const [hasAccess, setHasAccess] = useState(false)
  const [accessError, setAccessError] = useState<string | null>(null)
  const [waitingForInitData, setWaitingForInitData] = useState(true)

  useEffect(() => {

    // Если initData появился, прекращаем ожидание
    if (initData && waitingForInitData) {
      setWaitingForInitData(false)
      return
    }

    // Ждем появления initData до 5 секунд
    if (!initData && waitingForInitData) {
      const timeoutId = setTimeout(() => {
        // Проверяем еще раз, может initData появился за это время
        if (!initData) {
          if (import.meta.env.DEV) {
            logger.info('[PanelWrapper] initData не появился через 5 секунд, редирект на календарь')
          }
          setWaitingForInitData(false)
          setIsCheckingAccess(false)
          setAccessError(
            'Не удалось получить данные авторизации. Убедитесь, что приложение открыто через Telegram Mini App.'
          )
        }
      }, 5000)

      return () => clearTimeout(timeoutId)
    }

    // Ждем пока isReady станет true
    if (!isReady) {
      setIsCheckingAccess(true)
      return
    }

    // Если WebApp готов и есть initData, проверяем доступ
    if (isReady && initData) {
      if (import.meta.env.DEV) {
        logger.info('[PanelWrapper] Проверка доступа к панели...', { initDataLength: initData.length })
      }
      setIsCheckingAccess(true)
      setAccessError(null)

      api.checkPanelAccess()
        .then((result) => {
          if (import.meta.env.DEV) {
            logger.info('[PanelWrapper] Результат проверки доступа:', result)
          }
          setHasAccess(result.has_access)
          if (!result.has_access) {
            setAccessError(
              'У вас нет доступа к панели управления. Используйте команду /panel в боте для получения доступа.'
            )
          }
        })
        .catch((error) => {
          logger.error('[PanelWrapper] Ошибка при проверке доступа к панели:', error)
          setHasAccess(false)
          setAccessError(
            error instanceof Error
              ? `Ошибка при проверке доступа: ${error.message}`
              : 'Не удалось проверить доступ к панели. Попробуйте обновить страницу.'
          )
        })
        .finally(() => {
          setIsCheckingAccess(false)
        })
    }
  }, [initData, isReady, waitingForInitData])

  // Визуальный индикатор для отладки
  const debugInfo = webApp && import.meta.env.DEV ? (
    <div style={{
      position: 'fixed',
      top: '50px',
      right: '10px',
      padding: '8px 12px',
      background: 'rgba(0,0,0,0.8)',
      color: 'white',
      borderRadius: '8px',
      fontSize: '11px',
      zIndex: 9998,
      fontFamily: 'monospace',
      maxWidth: '200px',
    }}>
      <div><strong>isReady:</strong> {isReady ? '✅' : '❌'}</div>
      <div><strong>hasAccess:</strong> {hasAccess ? '✅' : '❌'}</div>
    </div>
  ) : null

  // Показываем индикатор загрузки
  if (isCheckingAccess || waitingForInitData) {
    return (
      <div className="app-loading">
        {debugInfo}
        <div className="loading-spinner">⏳</div>
        <p>
          {waitingForInitData
            ? 'Ожидание инициализации Telegram WebApp...'
            : 'Проверка доступа к панели...'}
        </p>
      </div>
    )
  }

  // Если доступа нет, показываем сообщение об ошибке
  if (!hasAccess) {
    return (
      <div className="app-loading">
        {debugInfo}
        <div className="app-error-message" style={{ position: 'relative', marginTop: '20px' }}>
          <p>⚠️ {accessError || 'У вас нет доступа к панели управления.'}</p>
          <p style={{ marginTop: '10px', fontSize: '14px' }}>Перенаправление на календарь...</p>
        </div>
      </div>
    )
  }

  // Panel рендерится только если есть доступ
  return (
    <>
      {debugInfo}
      <Panel />
    </>
  )
}

