import { useEffect, useState } from 'react'
import { useTelegram } from './hooks/useTelegram'
import Calendar from './components/Calendar/Calendar'
import Panel from './components/Panel/Panel'
import { api } from './services/api'

function App() {
  const { webApp, initData } = useTelegram()
  const [isPanel, setIsPanel] = useState(false)

  useEffect(() => {
    if (webApp) {
      webApp.ready()
      webApp.expand()
    }
  }, [webApp])

  // Проверяем, открыт ли панель управления через initData
  useEffect(() => {
    if (initData) {
      api.checkPanelAccess()
        .then((result) => {
          setIsPanel(result.has_access)
        })
        .catch(() => {
          setIsPanel(false) // По умолчанию показываем календарь при ошибке
        })
    }
  }, [initData])

  return (
    <div className="app">
      {isPanel ? <Panel /> : <Calendar />}
    </div>
  )
}

export default App

