import { useEffect, useState } from 'react'
import { useTelegram } from './hooks/useTelegram'
import Calendar from './components/Calendar/Calendar'
import Panel from './components/Panel/Panel'
import Diagnostics from './components/Diagnostics/Diagnostics'
import { api } from './services/api'
import { logger } from './utils/logger'

function App() {
  const { webApp, initData, isReady } = useTelegram()
  const [isPanel, setIsPanel] = useState(false)
  const [isCheckingAccess, setIsCheckingAccess] = useState(false)

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

  // Проверяем, открыт ли панель управления через initData
  // Проверка опциональна - если initData нет или проверка не удалась, показываем календарь
  useEffect(() => {
    // Показываем календарь по умолчанию, если нет initData
    if (!initData) {
      setIsPanel(false)
      return
    }

    // Если есть initData и WebApp готов, проверяем доступ к панели
    if (isReady && initData) {
      setIsCheckingAccess(true)
      api.checkPanelAccess()
        .then((result) => {
          setIsPanel(result.has_access)
        })
        .catch((error) => {
          logger.error('Error checking panel access:', error)
          // По умолчанию показываем календарь при ошибке
          setIsPanel(false)
        })
        .finally(() => {
          setIsCheckingAccess(false)
        })
    }
  }, [initData, isReady])

  // Всегда показываем календарь по умолчанию, если проверка еще не завершена
  // или если проверка не удалась
  return (
    <div className="app">
      {isPanel && !isCheckingAccess ? <Panel /> : <Calendar />}
      <Diagnostics />
    </div>
  )
}

export default App

