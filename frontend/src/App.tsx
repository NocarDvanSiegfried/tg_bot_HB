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
    // Ждем готовности режима и WebApp
    if (!modeReady || !isReady || hasRedirected) {
      return
    }

    // Если мы уже на правильном роуте, не делаем редирект
    if (mode === 'panel' && location.pathname === '/panel') {
      setHasRedirected(true)
      if (import.meta.env.DEV) {
        logger.info('[App] Already on /panel route, no redirect needed')
      }
      return
    }

    if (mode === 'user' && location.pathname === '/') {
      setHasRedirected(true)
      if (import.meta.env.DEV) {
        logger.info('[App] Already on / route, no redirect needed')
      }
      return
    }

    // Выполняем редирект на основе режима
    if (mode === 'panel') {
      if (import.meta.env.DEV) {
        logger.info('[App] Redirecting to /panel (panel mode)')
      }
      navigate('/panel', { replace: true })
      setHasRedirected(true)
    } else {
      // Режим user - редиректим на календарь
      if (location.pathname === '/panel') {
        if (import.meta.env.DEV) {
          logger.info('[App] Redirecting to / (user mode, was on /panel)')
        }
        navigate('/', { replace: true })
        setHasRedirected(true)
      }
    }
  }, [mode, modeReady, isReady, location.pathname, navigate, hasRedirected])

  return (
    <div className="app">
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
        {/* Fallback route - все остальные пути ведут на календарь */}
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

