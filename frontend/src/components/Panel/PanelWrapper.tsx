import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useTelegram } from '../../hooks/useTelegram'
import { useAppMode } from '../../hooks/useAppMode'
import { api } from '../../services/api'
import { logger } from '../../utils/logger'
import Panel from './Panel'

export default function PanelWrapper() {
  const { initData, isReady, webApp } = useTelegram()
  const { mode, isReady: modeReady } = useAppMode()
  const navigate = useNavigate()
  const [isCheckingAccess, setIsCheckingAccess] = useState(true)
  const [hasAccess, setHasAccess] = useState(false)
  const [accessError, setAccessError] = useState<string | null>(null)
  const [waitingForInitData, setWaitingForInitData] = useState(true)

  // КРИТИЧНО: PanelWrapper НИКОГДА не должен рендериться в режиме user
  // Эта проверка должна быть ПЕРВОЙ, до любых эффектов и API запросов
  // Это архитектурная блокировка, а не визуальная
  if (!modeReady) {
    logger.info('[PanelWrapper] ⏳ Waiting for mode to be ready, blocking render')
    return (
      <div className="app-loading">
        <div className="loading-spinner">⏳</div>
        <p>Инициализация панели управления...</p>
      </div>
    )
  }

  if (mode !== 'panel') {
    logger.warn('[PanelWrapper] ❌❌❌ BLOCKING RENDER - NOT IN PANEL MODE ❌❌❌')
    logger.warn('[PanelWrapper] Current mode:', mode)
    logger.warn('[PanelWrapper] PanelWrapper is NOT allowed in user mode. Redirecting to /')
    // Немедленный редирект без задержки
    navigate('/', { replace: true })
    return (
      <div className="app-loading">
        <div className="app-error-message" style={{ position: 'relative', marginTop: '20px' }}>
          <p>⚠️ Откройте панель через команду /panel в боте</p>
          <p style={{ marginTop: '10px', fontSize: '14px' }}>Перенаправление на календарь...</p>
        </div>
      </div>
    )
  }

  // КРИТИЧНО: Проверка режима завершена, режим panel подтвержден
  // Только теперь можно выполнять API запросы
  logger.info('[PanelWrapper] ✅✅✅ PANEL MODE CONFIRMED - Proceeding with access check ✅✅✅')

  useEffect(() => {
    // Если режим не panel, не проверяем доступ
    if (mode !== 'panel' || !modeReady) {
      return
    }

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
          // КРИТИЧНО: Немедленный редирект без задержки
          navigate('/', { replace: true })
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
    if (isReady && initData && mode === 'panel') {
      if (import.meta.env.DEV) {
        logger.info('[PanelWrapper] Проверка доступа к панели...', { initDataLength: initData.length, mode })
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
            // КРИТИЧНО: Немедленный редирект без задержки
            navigate('/', { replace: true })
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
          // КРИТИЧНО: Немедленный редирект без задержки
          navigate('/', { replace: true })
        })
        .finally(() => {
          setIsCheckingAccess(false)
        })
    }
  }, [initData, isReady, mode, modeReady, navigate, waitingForInitData])

  // Визуальный индикатор режима для отладки
  const debugInfo = modeReady && webApp ? (
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
      <div><strong>Режим:</strong> {mode === 'panel' ? '🔧 PANEL' : '👤 USER'}</div>
      <div><strong>startParam:</strong> {webApp.startParam || 'null'}</div>
      <div><strong>modeReady:</strong> {modeReady ? '✅' : '❌'}</div>
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
        {modeReady && (
          <p style={{ marginTop: '10px', fontSize: '12px', color: '#666' }}>
            Режим: {mode === 'panel' ? '🔧 PANEL' : '👤 USER'} | startParam: {webApp?.startParam || 'null'}
          </p>
        )}
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
          {modeReady && (
            <p style={{ marginTop: '10px', fontSize: '12px', color: '#666' }}>
              Режим: {mode === 'panel' ? '🔧 PANEL' : '👤 USER'} | startParam: {webApp?.startParam || 'null'}
            </p>
          )}
        </div>
      </div>
    )
  }

  // Если доступ есть, рендерим панель
  return (
    <>
      {debugInfo}
      <Panel />
    </>
  )
}

