import { useEffect, useState, Suspense, lazy } from 'react'
import { useTelegram } from './hooks/useTelegram'
import { logger } from './utils/logger'

// Lazy loading для оптимизации bundle
const Calendar = lazy(() => import('./components/Calendar/Calendar'))
// Diagnostics загружается только в development режиме
const Diagnostics = import.meta.env.DEV
  ? lazy(() => import('./components/Diagnostics/Diagnostics'))
  : null

function App() {
  // КРИТИЧНО: Все хуки вызываются всегда, на верхнем уровне, без условий
  // Это правило React hooks - нарушение приводит к ошибке #310
  const { webApp, isReady } = useTelegram()
  const [initError, setInitError] = useState<string | null>(null)

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
        initError,
      })
    }
  }, [webApp, isReady, initError])

  // КРИТИЧНО: Bot = Launcher архитектура
  // Mini App всегда открывается в режиме календаря
  // Все управление выполняется внутри Mini App через UI

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
      {/* КРИТИЧНО: Всегда рендерим Calendar
          Редактирование доступно через UI внутри Calendar */}
      <Suspense fallback={<div className="app-loading">Загрузка календаря...</div>}>
        <Calendar />
      </Suspense>
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

