import { useEffect } from 'react'
import { Routes, Route } from 'react-router-dom'
import { useTelegram } from './hooks/useTelegram'
import Calendar from './components/Calendar/Calendar'
import PanelWrapper from './components/Panel/PanelWrapper'
import Diagnostics from './components/Diagnostics/Diagnostics'
import { logger } from './utils/logger'

function App() {
  const { webApp } = useTelegram()

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

  return (
    <div className="app">
      <Routes>
        <Route path="/" element={<Calendar />} />
        <Route path="/panel" element={<PanelWrapper />} />
      </Routes>
      <Diagnostics />
    </div>
  )
}

export default App

