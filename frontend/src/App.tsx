import { useEffect, useState, Suspense, lazy } from 'react'
import { Routes, Route, useLocation, useNavigate } from 'react-router-dom'
import { useTelegram } from './hooks/useTelegram'
import { useAppMode } from './hooks/useAppMode'
import { logger } from './utils/logger'

// Lazy loading для оптимизации bundle
const Calendar = lazy(() => import('./components/Calendar/Calendar'))
const PanelWrapper = lazy(() => import('./components/Panel/PanelWrapper'))
// Diagnostics загружается только в development режиме
const Diagnostics = import.meta.env.DEV
  ? lazy(() => import('./components/Diagnostics/Diagnostics'))
  : null

function App() {
  const { webApp, isReady } = useTelegram()
  const { mode, isReady: modeReady } = useAppMode()
  const location = useLocation()
  const navigate = useNavigate()
  const [initError, setInitError] = useState<string | null>(null)
  const [hasRedirected, setHasRedirected] = useState(false)

  useEffect(() => {
    if (webApp) {
      try {
        webApp.ready()
        webApp.expand()
        setInitError(null)
        if (import.meta.env.DEV) {
          logger.info('[App] Telegram WebApp initialized successfully')
        }
      } catch (error) {
        const errorMessage = error instanceof Error ? error.message : 'Unknown error'
        logger.error('[App] Error initializing Telegram WebApp:', error)
        setInitError(`Ошибка инициализации: ${errorMessage}`)
      }
    }
  }, [webApp])

  // Логирование текущего пути для отладки
  useEffect(() => {
    if (import.meta.env.DEV) {
      logger.info('[App] Current path:', location.pathname, 'hash:', location.hash)
    }
  }, [location])

  // Логирование состояния готовности
  useEffect(() => {
    if (import.meta.env.DEV) {
      logger.info('[App] App state:', {
        hasWebApp: !!webApp,
        isReady,
        mode,
        modeReady,
        initError,
        currentPath: location.pathname,
      })
    }
  }, [webApp, isReady, mode, modeReady, initError, location.pathname])

  // Автоматический редирект на основе режима приложения
  useEffect(() => {
    // ЖЕСТКОЕ ЛОГИРОВАНИЕ: состояние перед редиректом
    logger.info('[App] ===== REDIRECT CHECK =====')
    logger.info('[App] modeReady:', modeReady)
    logger.info('[App] isReady (Telegram):', isReady)
    logger.info('[App] hasRedirected:', hasRedirected)
    logger.info('[App] current mode:', mode)
    logger.info('[App] current path:', location.pathname)
    logger.info('[App] webApp available:', !!webApp)
    if (webApp) {
      logger.info('[App] webApp.startParam:', webApp.startParam)
      logger.info('[App] webApp.startParam type:', typeof webApp.startParam)
      logger.info('[App] webApp.startParam === "panel":', webApp.startParam === 'panel')
    }

    // КРИТИЧНО: Ждем готовности режима И WebApp
    // НЕ проверяем hasRedirected здесь - редирект может понадобиться если режим изменился
    if (!modeReady || !isReady || !webApp) {
      logger.info('[App] ⏳ Waiting for readiness:', {
        modeReady,
        isReady,
        hasWebApp: !!webApp,
      })
      return
    }

    // Дополнительная проверка: убеждаемся что startParam доступен
    const startParam = webApp.startParam
    logger.info('[App] startParam before redirect:', startParam)
    logger.info('[App] Expected mode:', startParam === 'panel' ? 'panel' : 'user')
    logger.info('[App] Detected mode:', mode)
    logger.info('[App] Mode matches startParam:', (startParam === 'panel' && mode === 'panel') || (startParam !== 'panel' && mode === 'user'))

    // КРИТИЧНО: Если режим не совпадает с startParam, это ошибка
    if (startParam === 'panel' && mode !== 'panel') {
      logger.error('[App] ❌❌❌ CRITICAL: MODE MISMATCH! startParam=panel but mode=user ❌❌❌')
      logger.error('[App] This indicates useAppMode() did not read startParam correctly!')
    }
    if (startParam !== 'panel' && mode === 'panel') {
      logger.error('[App] ❌❌❌ CRITICAL: MODE MISMATCH! startParam!=panel but mode=panel ❌❌❌')
    }

    // Если мы уже на правильном роуте, не делаем редирект
    if (mode === 'panel' && location.pathname === '/panel') {
      if (!hasRedirected) {
        setHasRedirected(true)
      }
      logger.info('[App] ✅ Already on /panel route, no redirect needed')
      return
    }

    if (mode === 'user' && location.pathname === '/') {
      if (!hasRedirected) {
        setHasRedirected(true)
      }
      logger.info('[App] ✅ Already on / route, no redirect needed')
      return
    }

    // КРИТИЧНО: Если пользователь на /panel, но режим user - редиректим на /
    if (location.pathname === '/panel' && mode === 'user') {
      logger.warn('[App] ⚠️ User on /panel but mode is user - redirecting to /')
      logger.warn('[App] startParam:', startParam || 'null/undefined')
      navigate('/', { replace: true })
      setHasRedirected(true)
      logger.info('[App] ✅ Redirect to / completed (user mode, was on /panel)')
      return
    }

    // Выполняем редирект на основе режима
    if (mode === 'panel') {
      // КРИТИЧНО: Редирект на /panel должен происходить немедленно
      // Это гарантирует, что Calendar не успеет отрендериться
      logger.info('[App] 🔀🔀🔀 REDIRECTING to /panel (panel mode detected) 🔀🔀🔀')
      logger.info('[App] startParam === "panel":', startParam === 'panel')
      logger.info('[App] Current path before redirect:', location.pathname)
      
      // Используем replace: true для немедленного редиректа без истории
      navigate('/panel', { replace: true })
      setHasRedirected(true)
      
      logger.info('[App] ✅✅✅ Redirect to /panel completed ✅✅✅')
      return // Важно: выходим сразу после редиректа
    }
    
    // Режим user - редиректим на календарь только если мы на /panel (уже обработано выше)
    // Если мы уже на /, ничего не делаем (уже обработано выше)
    
    logger.info('[App] ===== REDIRECT CHECK COMPLETE =====')
  }, [mode, modeReady, isReady, webApp, location.pathname, navigate, hasRedirected])

  // КРИТИЧНО: Пока !modeReady → НИЧЕГО не рендерить
  // Это предотвращает рендеринг Calendar до определения режима
  // и гарантирует, что редирект произойдет до первого рендера
  if (!modeReady) {
    logger.info('[App] ⏳ Waiting for mode to be ready, blocking render')
    return (
      <div className="app-loading">
        <div className="loading-spinner">⏳</div>
        <p>Инициализация приложения...</p>
      </div>
    )
  }

  return (
    <div className="app">
      {/* Визуальный индикатор режима (для отладки) */}
      {import.meta.env.DEV && modeReady && (
        <div style={{
          position: 'fixed',
          top: '10px',
          right: '10px',
          padding: '6px 12px',
          background: mode === 'panel' ? '#667eea' : '#28a745',
          color: 'white',
          borderRadius: '20px',
          fontSize: '11px',
          fontWeight: 'bold',
          zIndex: 9999,
          boxShadow: '0 2px 8px rgba(0,0,0,0.2)',
        }}>
          {mode === 'panel' ? '🔧 PANEL MODE' : '👤 USER MODE'}
        </div>
      )}
      {initError && import.meta.env.DEV && (
        <div style={{
          padding: '10px',
          backgroundColor: '#fff3cd',
          color: '#856404',
          textAlign: 'center',
          fontSize: '14px',
        }}>
          ⚠️ {initError}
        </div>
      )}
      <Routes>
        <Route
          path="/"
          element={
            <Suspense fallback={<div className="app-loading">Загрузка календаря...</div>}>
              <Calendar />
            </Suspense>
          }
        />
        <Route
          path="/panel"
          element={
            <Suspense fallback={<div className="app-loading">Загрузка панели...</div>}>
              <PanelWrapper />
            </Suspense>
          }
        />
        {/* Fallback route - все остальные пути ведут на календарь
            КРИТИЧНО: Этот роут НЕ должен перехватывать /panel, так как /panel уже определен выше
            Fallback срабатывает только для путей, которые не совпадают с / и /panel
        */}
        <Route
          path="*"
          element={
            <Suspense fallback={<div className="app-loading">Загрузка календаря...</div>}>
              <Calendar />
            </Suspense>
          }
        />
      </Routes>
      {/* Diagnostics загружается только в development режиме */}
      {import.meta.env.DEV && Diagnostics && (
        <Suspense fallback={null}>
          <Diagnostics />
        </Suspense>
      )}
    </div>
  )
}

export default App

