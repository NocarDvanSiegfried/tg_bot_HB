import { useEffect, useState } from 'react'
import { logger } from '../utils/logger'

export function useTelegram() {
  const [webApp, setWebApp] = useState<any | null>(null)
  const [initData, setInitData] = useState<string | null>(null)
  const [isReady, setIsReady] = useState(false)

  useEffect(() => {
    // Функция для проверки и инициализации Telegram WebApp
    const initTelegram = () => {
      if (typeof window === 'undefined') {
        return
      }

      // Проверяем наличие Telegram WebApp
      if (window.Telegram?.WebApp) {
        const tg = window.Telegram.WebApp
        setWebApp(tg)
        setInitData(tg.initData || null)
        setIsReady(true)
        
        // Логирование для отладки (только в dev режиме)
              logger.log('Telegram WebApp initialized:', {
                hasWebApp: !!tg,
                hasInitData: !!tg.initData,
              })
      } else {
        // Если WebApp еще не загружен, ждем немного и пробуем снова
        // Это может произойти, если скрипт загружается асинхронно
        const checkInterval = setInterval(() => {
          if (window.Telegram?.WebApp) {
            const tg = window.Telegram.WebApp
            setWebApp(tg)
            setInitData(tg.initData || null)
            setIsReady(true)
            clearInterval(checkInterval)
            
                  logger.log('Telegram WebApp initialized (delayed)')
          }
        }, 100)

        // Останавливаем проверку через 5 секунд, если WebApp не загрузился
                setTimeout(() => {
                  clearInterval(checkInterval)
                  if (!isReady) {
                    logger.warn('Telegram WebApp not found. Running outside Telegram?')
                  }
                }, 5000)
      }
    }

    // Пробуем инициализировать сразу
    initTelegram()

    // Также слушаем событие загрузки страницы на случай, если скрипт загружается позже
    if (typeof window !== 'undefined') {
      window.addEventListener('load', initTelegram)
      
      return () => {
        window.removeEventListener('load', initTelegram)
      }
    }
  }, [isReady])

  return { webApp, initData, isReady }
}

