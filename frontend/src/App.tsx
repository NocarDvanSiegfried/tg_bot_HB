import { useEffect, useState, Suspense, lazy } from 'react'
import { useNavigate } from 'react-router-dom'
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
  // КРИТИЧНО: Все хуки вызываются всегда, на верхнем уровне, без условий
  // Это правило React hooks - нарушение приводит к ошибке #310
  const { webApp, isReady } = useTelegram()
  const { mode, isReady: modeReady } = useAppMode()
  const navigate = useNavigate()
  const [initError, setInitError] = useState<string | null>(null)
  const [hasRedirected, setHasRedirected] = useState(false)

  useEffect(() => {
    if (webApp) {
      try {
        webApp.ready()
        webApp.expand()
        
        // КРИТИЧНО: Отключаем системное меню Mini App (Menu Button)
        // Это предотвращает дублирование элементов управления в чате
        // Управление выполняется только через собственный UI приложения
        if (typeof webApp.setupMenuButton === 'function') {
          webApp.setupMenuButton({ is_visible: false })
          if (import.meta.env.DEV) {
            logger.info('[App] Menu Button отключен (setupMenuButton)')
          }
        }
        
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

  // Логирование состояния готовности
  useEffect(() => {
    if (import.meta.env.DEV) {
      logger.info('[App] App state:', {
        hasWebApp: !!webApp,
        isReady,
        mode,
        modeReady,
        initError,
      })
    }
  }, [webApp, isReady, mode, modeReady, initError])

  // КРИТИЧНО: Единственная точка навигации - App.tsx
  // Навигация выполняется только внутри useEffect
  // После определения режима выполняется редирект на правильный роут
  useEffect(() => {
    // Ждем готовности режима И WebApp
    if (!modeReady || !isReady || !webApp) {
      return
    }

    // Если уже был редирект, не делаем повторный
    if (hasRedirected) {
      return
    }

    // Выполняем редирект на основе режима
    if (mode === 'panel') {
      logger.info('[App] 🔀 Redirecting to /panel (panel mode)')
      navigate('/panel', { replace: true })
      setHasRedirected(true)
      return // Немедленный выход после редиректа
    }

    // Режим user - редиректим на /
    if (mode === 'user') {
      logger.info('[App] 🔀 Redirecting to / (user mode)')
      navigate('/', { replace: true })
      setHasRedirected(true)
      return // Немедленный выход после редиректа
    }
  }, [mode, modeReady, isReady, webApp, navigate, hasRedirected])

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

  // КРИТИЧНО: Единственная точка выбора режима - App.tsx
  // В зависимости от режима выбирается одно дерево компонентов
  // Calendar и Panel никогда не рендерятся одновременно

  return (
    <div className="app">
      {/* Визуальный индикатор режима (для отладки) */}
      {import.meta.env.DEV && (
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
      {/* КРИТИЧНО: Условный рендер на основе режима
          Calendar и Panel никогда не рендерятся одновременно */}
      {mode === 'panel' ? (
        <Suspense fallback={<div className="app-loading">Загрузка панели...</div>}>
          <PanelWrapper />
        </Suspense>
      ) : (
        <Suspense fallback={<div className="app-loading">Загрузка календаря...</div>}>
          <Calendar />
        </Suspense>
      )}
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

