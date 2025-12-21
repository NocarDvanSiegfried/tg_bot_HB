import { useEffect, useState, useRef } from 'react'
import { logger } from '../utils/logger'

export function useTelegram() {
  const [webApp, setWebApp] = useState<any | null>(null)
  const [initData, setInitData] = useState<string | null>(null)
  const [isReady, setIsReady] = useState(false)
  const initializedRef = useRef(false)
  const checkIntervalRef = useRef<number | null>(null)
  const timeoutRef = useRef<number | null>(null)

  useEffect(() => {
    // Если уже инициализирован, не делаем ничего
    if (initializedRef.current) {
      return
    }

    // Функция для проверки и инициализации Telegram WebApp
    const initTelegram = () => {
      if (typeof window === 'undefined') {
        return
      }

      // Если уже инициализирован, выходим
      if (initializedRef.current) {
        return
      }

      // Проверяем наличие Telegram WebApp
      if (window.Telegram?.WebApp) {
        const tg = window.Telegram.WebApp
        setWebApp(tg)
        setInitData(tg.initData || null)
        setIsReady(true)
        initializedRef.current = true
        
        // Очищаем интервалы если они были установлены
        if (checkIntervalRef.current) {
          clearInterval(checkIntervalRef.current)
          checkIntervalRef.current = null
        }
        if (timeoutRef.current) {
          clearTimeout(timeoutRef.current)
          timeoutRef.current = null
        }
        
        // ЖЕСТКОЕ ЛОГИРОВАНИЕ: инициализация Telegram WebApp
        logger.info('[useTelegram] ===== TELEGRAM WEBAPP INITIALIZED =====')
        logger.info('[useTelegram] WebApp object:', !!tg)
        logger.info('[useTelegram] initData available:', !!tg.initData)
        logger.info('[useTelegram] initData length:', tg.initData?.length || 0)
        logger.info('[useTelegram] startParam available:', 'startParam' in tg)
        logger.info('[useTelegram] startParam value:', tg.startParam)
        logger.info('[useTelegram] startParam type:', typeof tg.startParam)
        logger.info('[useTelegram] ===== INITIALIZATION COMPLETE =====')
      } else {
        // Если WebApp еще не загружен, ждем немного и пробуем снова
        // Это может произойти, если скрипт загружается асинхронно
        if (!checkIntervalRef.current) {
          checkIntervalRef.current = setInterval(() => {
            if (window.Telegram?.WebApp && !initializedRef.current) {
              const tg = window.Telegram.WebApp
              setWebApp(tg)
              setInitData(tg.initData || null)
              setIsReady(true)
              initializedRef.current = true
              
              if (checkIntervalRef.current) {
                clearInterval(checkIntervalRef.current)
                checkIntervalRef.current = null
              }
              if (timeoutRef.current) {
                clearTimeout(timeoutRef.current)
                timeoutRef.current = null
              }
              
              logger.info('[useTelegram] ===== TELEGRAM WEBAPP INITIALIZED (DELAYED) =====')
              logger.info('[useTelegram] startParam value:', tg.startParam)
              logger.info('[useTelegram] startParam type:', typeof tg.startParam)
            }
          }, 100)

          // Останавливаем проверку через 5 секунд, если WebApp не загрузился
          timeoutRef.current = setTimeout(() => {
            if (checkIntervalRef.current) {
              clearInterval(checkIntervalRef.current)
              checkIntervalRef.current = null
            }
            if (!initializedRef.current) {
              logger.warn('Telegram WebApp not found. Running outside Telegram?')
            }
          }, 5000)
        }
      }
    }

    // Пробуем инициализировать сразу
    initTelegram()

    // Также слушаем событие загрузки страницы на случай, если скрипт загружается позже
    if (typeof window !== 'undefined') {
      window.addEventListener('load', initTelegram)
      
      return () => {
        window.removeEventListener('load', initTelegram)
        if (checkIntervalRef.current) {
          clearInterval(checkIntervalRef.current)
          checkIntervalRef.current = null
        }
        if (timeoutRef.current) {
          clearTimeout(timeoutRef.current)
          timeoutRef.current = null
        }
      }
    }
  }, []) // Пустой массив зависимостей - эффект выполняется только один раз

  return { webApp, initData, isReady }
}

