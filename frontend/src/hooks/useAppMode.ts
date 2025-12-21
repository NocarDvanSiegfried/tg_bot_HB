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
    // ЖЕСТКОЕ ЛОГИРОВАНИЕ: начало определения режима
    logger.info('[useAppMode] ===== START MODE DETECTION =====')
    logger.info('[useAppMode] Window available:', typeof window !== 'undefined')
    logger.info('[useAppMode] Telegram available:', typeof window !== 'undefined' && !!window.Telegram)
    logger.info('[useAppMode] WebApp available:', typeof window !== 'undefined' && !!window.Telegram?.WebApp)

    // Проверяем наличие Telegram WebApp
    if (typeof window === 'undefined' || !window.Telegram?.WebApp) {
      // Если WebApp недоступен, используем режим по умолчанию
      logger.warn('[useAppMode] Telegram WebApp not available, using default user mode')
      setMode('user')
      setIsReady(true)
      return
    }

    const webApp = window.Telegram.WebApp
    
    // ЖЕСТКОЕ ЛОГИРОВАНИЕ: проверка startParam
    const startParam = webApp.startParam
    logger.info('[useAppMode] Raw startParam value:', startParam)
    logger.info('[useAppMode] startParam type:', typeof startParam)
    logger.info('[useAppMode] startParam === "panel":', startParam === 'panel')
    logger.info('[useAppMode] startParam === null:', startParam === null)
    logger.info('[useAppMode] startParam === undefined:', startParam === undefined)
    logger.info('[useAppMode] startParam truthy:', !!startParam)

    // Определяем режим на основе startParam
    const detectedMode: AppMode = startParam === 'panel' ? 'panel' : 'user'
    
    if (detectedMode === 'panel') {
      logger.info('[useAppMode] ✅ PANEL MODE DETECTED (startParam === "panel")')
    } else {
      logger.info('[useAppMode] ✅ USER MODE DETECTED (startParam:', startParam || 'null/undefined', ')')
    }

    setMode(detectedMode)
    setIsReady(true)
    logger.info('[useAppMode] ===== MODE DETECTION COMPLETE =====')
    logger.info('[useAppMode] Final mode:', detectedMode === 'panel' ? 'PANEL' : 'USER')
    logger.info('[useAppMode] isReady:', true)
  }, [])

  return { mode, isReady }
}

