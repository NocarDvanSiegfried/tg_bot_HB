import { useEffect, useState } from 'react'
import { Routes, Route, useLocation } from 'react-router-dom'
import { useTelegram } from './hooks/useTelegram'
import Calendar from './components/Calendar/Calendar'
import PanelWrapper from './components/Panel/PanelWrapper'
import Diagnostics from './components/Diagnostics/Diagnostics'
import { logger } from './utils/logger'

function App() {
  const { webApp, isReady } = useTelegram()
  const location = useLocation()
  const [initError, setInitError] = useState<string | null>(null)

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
        initError,
      })
    }
  }, [webApp, isReady, initError])

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
        <Route path="/" element={<Calendar />} />
        <Route path="/panel" element={<PanelWrapper />} />
        {/* Fallback route - все остальные пути ведут на календарь */}
        <Route path="*" element={<Calendar />} />
      </Routes>
      <Diagnostics />
    </div>
  )
}

export default App

