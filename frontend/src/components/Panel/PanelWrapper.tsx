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

  useEffect(() => {
    // Если нет initData, редиректим на календарь
    if (!initData) {
      if (import.meta.env.DEV) {
        logger.info('[PanelWrapper] initData отсутствует, редирект на календарь')
      }
      navigate('/')
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
  }, [initData, isReady, navigate])

  // Показываем индикатор загрузки
  if (isCheckingAccess) {
    return (
      <div className="app-loading">
        <div className="loading-spinner">⏳</div>
        <p>Проверка доступа к панели...</p>
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

