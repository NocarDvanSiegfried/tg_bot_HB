import { useEffect } from 'react'
import { Routes, Route, useLocation } from 'react-router-dom'
import { useTelegram } from './hooks/useTelegram'
import Calendar from './components/Calendar/Calendar'
import PanelWrapper from './components/Panel/PanelWrapper'
import Diagnostics from './components/Diagnostics/Diagnostics'
import { logger } from './utils/logger'

function App() {
  const { webApp } = useTelegram()
  const location = useLocation()

  useEffect(() => {
    if (webApp) {
      try {
        webApp.ready()
        webApp.expand()
      } catch (error) {
        logger.error('Error initializing Telegram WebApp:', error)
      }
    }
  }, [webApp])

  // Логирование текущего пути для отладки
  useEffect(() => {
    if (import.meta.env.DEV) {
      logger.info('[App] Current path:', location.pathname, 'hash:', location.hash)
    }
  }, [location])

  return (
    <div className="app">
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

