import { useEffect, useState } from 'react'
import { logger } from '../utils/logger'

/**
 * Режимы работы Mini App
 */
export type AppMode = 'user' | 'panel'

/**
 * Хук для определения режима работы Mini App
 * 
 * Режим определяется из startParam Telegram WebApp:
 * - 'panel' - если startParam === 'panel' (открыто через команду /panel)
 * - 'user' - во всех остальных случаях (по умолчанию, открыто через /start)
 * 
 * @returns Объект с режимом приложения и флагом готовности
 */
export function useAppMode(): { mode: AppMode; isReady: boolean } {
  const [mode, setMode] = useState<AppMode>('user')
  const [isReady, setIsReady] = useState(false)

  useEffect(() => {
    // Проверяем наличие Telegram WebApp
    if (typeof window === 'undefined' || !window.Telegram?.WebApp) {
      // Если WebApp недоступен, используем режим по умолчанию
      setMode('user')
      setIsReady(true)
      if (import.meta.env.DEV) {
        logger.info('[useAppMode] Telegram WebApp not available, using default user mode')
      }
      return
    }

    const webApp = window.Telegram.WebApp
    const startParam = webApp.startParam

    // Определяем режим на основе startParam
    if (startParam === 'panel') {
      setMode('panel')
      if (import.meta.env.DEV) {
        logger.info('[useAppMode] Panel mode detected (startParam=panel)')
      }
    } else {
      setMode('user')
      if (import.meta.env.DEV) {
        logger.info('[useAppMode] User mode detected (startParam:', startParam || 'null', ')')
      }
    }

    setIsReady(true)
  }, [])

  return { mode, isReady }
}

