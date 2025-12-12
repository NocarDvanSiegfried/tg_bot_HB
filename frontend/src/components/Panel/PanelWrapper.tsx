import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useTelegram } from '../../hooks/useTelegram'
import { api } from '../../services/api'
import { logger } from '../../utils/logger'
import Panel from './Panel'

export default function PanelWrapper() {
  const { initData, isReady } = useTelegram()
  const navigate = useNavigate()
  const [isCheckingAccess, setIsCheckingAccess] = useState(true)
  const [hasAccess, setHasAccess] = useState(false)
  const [accessError, setAccessError] = useState<string | null>(null)
  const [waitingForInitData, setWaitingForInitData] = useState(true)

  useEffect(() => {
    // Если initData появился, прекращаем ожидание
    if (initData && waitingForInitData) {
      setWaitingForInitData(false)
      return
    }

    // Ждем появления initData до 5 секунд
    if (!initData && waitingForInitData) {
      const timeoutId = setTimeout(() => {
        // Проверяем еще раз, может initData появился за это время
        if (!initData) {
          if (import.meta.env.DEV) {
            logger.info('[PanelWrapper] initData не появился через 5 секунд, редирект на календарь')
          }
          setWaitingForInitData(false)
          setIsCheckingAccess(false)
          setAccessError(
            'Не удалось получить данные авторизации. Убедитесь, что приложение открыто через Telegram Mini App.'
          )
          // Редиректим на календарь через 3 секунды
          setTimeout(() => {
            navigate('/')
          }, 3000)
        }
      }, 5000)

      return () => clearTimeout(timeoutId)
    }

    // Ждем пока isReady станет true
    if (!isReady) {
      setIsCheckingAccess(true)
      return
    }

    // Если WebApp готов и есть initData, проверяем доступ
    if (isReady && initData) {
      if (import.meta.env.DEV) {
        logger.info('[PanelWrapper] Проверка доступа к панели...', { initDataLength: initData.length })
      }
      setIsCheckingAccess(true)
      setAccessError(null)

      api.checkPanelAccess()
        .then((result) => {
          if (import.meta.env.DEV) {
            logger.info('[PanelWrapper] Результат проверки доступа:', result)
          }
          setHasAccess(result.has_access)
          if (!result.has_access) {
            setAccessError(
              'У вас нет доступа к панели управления. Используйте команду /panel в боте для получения доступа.'
            )
            // Редиректим на календарь через 3 секунды
            setTimeout(() => {
              navigate('/')
            }, 3000)
          }
        })
        .catch((error) => {
          logger.error('[PanelWrapper] Ошибка при проверке доступа к панели:', error)
          setHasAccess(false)
          setAccessError(
            error instanceof Error
              ? `Ошибка при проверке доступа: ${error.message}`
              : 'Не удалось проверить доступ к панели. Попробуйте обновить страницу.'
          )
          // Редиректим на календарь через 3 секунды
          setTimeout(() => {
            navigate('/')
          }, 3000)
        })
        .finally(() => {
          setIsCheckingAccess(false)
        })
    }
  }, [initData, isReady, navigate, waitingForInitData])

  // Показываем индикатор загрузки
  if (isCheckingAccess || waitingForInitData) {
    return (
      <div className="app-loading">
        <div className="loading-spinner">⏳</div>
        <p>
          {waitingForInitData
            ? 'Ожидание инициализации Telegram WebApp...'
            : 'Проверка доступа к панели...'}
        </p>
      </div>
    )
  }

  // Если доступа нет, показываем сообщение об ошибке
  if (!hasAccess) {
    return (
      <div className="app-loading">
        <div className="app-error-message" style={{ position: 'relative', marginTop: '20px' }}>
          <p>⚠️ {accessError || 'У вас нет доступа к панели управления.'}</p>
          <p style={{ marginTop: '10px', fontSize: '14px' }}>Перенаправление на календарь...</p>
        </div>
      </div>
    )
  }

  // Если доступ есть, рендерим панель
  return <Panel />
}

