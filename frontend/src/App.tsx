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
  const [accessError, setAccessError] = useState<string | null>(null)

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
    // Сбрасываем состояние при изменении initData
    setIsPanel(false)
    setAccessError(null)

    // Показываем календарь по умолчанию, если нет initData
    if (!initData) {
      if (import.meta.env.DEV) {
        logger.info('[App] initData отсутствует, показываем календарь')
      }
      setIsPanel(false)
      return
    }

    // Если есть initData и WebApp готов, проверяем доступ к панели
    if (isReady && initData) {
      if (import.meta.env.DEV) {
        logger.info('[App] Проверка доступа к панели...', { initDataLength: initData.length })
      }
      setIsCheckingAccess(true)
      setAccessError(null)

      api.checkPanelAccess()
        .then((result) => {
          if (import.meta.env.DEV) {
            logger.info('[App] Результат проверки доступа:', result)
          }
          setIsPanel(result.has_access)
          if (!result.has_access) {
            setAccessError(
              'У вас нет доступа к панели управления. Используйте команду /panel в боте для получения доступа.'
            )
          }
        })
        .catch((error) => {
          logger.error('[App] Ошибка при проверке доступа к панели:', error)
          // По умолчанию показываем календарь при ошибке
          setIsPanel(false)
          setAccessError(
            error instanceof Error
              ? `Ошибка при проверке доступа: ${error.message}`
              : 'Не удалось проверить доступ к панели. Попробуйте обновить страницу.'
          )
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
      {isCheckingAccess ? (
        <div className="app-loading">
          <div className="loading-spinner">⏳</div>
          <p>Проверка доступа к панели...</p>
        </div>
      ) : isPanel ? (
        <Panel />
      ) : (
        <>
          <Calendar />
          {accessError && (
            <div className="app-error-message">
              <p>⚠️ {accessError}</p>
            </div>
          )}
        </>
      )}
      <Diagnostics />
    </div>
  )
}

export default App

