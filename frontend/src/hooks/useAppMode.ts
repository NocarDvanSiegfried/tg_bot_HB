import { useEffect, useState, useRef } from 'react'
import { logger } from '../utils/logger'

/**
 * Режимы работы Mini App
 */
export type AppMode = 'user' | 'panel'

/**
 * Хук для определения режима работы Mini App
 * 
 * КРИТИЧНО: Режим определяется из startParam Telegram WebApp:
 * - 'panel' - если startParam === 'panel' (открыто через команду /panel)
 * - 'user' - во всех остальных случаях (по умолчанию, открыто через /start)
 * 
 * ВАЖНО: Хук ждет полной инициализации Telegram.WebApp перед чтением startParam.
 * undefined не считается валидным значением - в этом случае режим определяется как 'user'.
 * 
 * @returns Объект с режимом приложения и флагом готовности
 */
export function useAppMode(): { mode: AppMode; isReady: boolean } {
  const [mode, setMode] = useState<AppMode>('user')
  const [isReady, setIsReady] = useState(false)
  const detectedRef = useRef(false)
  const checkIntervalRef = useRef<number | null>(null)
  const timeoutRef = useRef<number | null>(null)

  useEffect(() => {
    // Предотвращаем повторное определение режима
    if (detectedRef.current) {
      return
    }

    // ЖЕСТКОЕ ЛОГИРОВАНИЕ: начало определения режима
    logger.info('[useAppMode] ===== START MODE DETECTION =====')
    logger.info('[useAppMode] Window available:', typeof window !== 'undefined')
    
    // Функция для определения режима - вызывается только когда WebApp готов
    const detectMode = () => {
      if (detectedRef.current) {
        logger.warn('[useAppMode] Mode already detected, skipping')
        return
      }

      // КРИТИЧНО: Проверяем наличие Telegram WebApp
      if (typeof window === 'undefined' || !window.Telegram?.WebApp) {
        logger.info('[useAppMode] WebApp not available yet')
        return false // Возвращаем false, чтобы продолжить ожидание
      }

      const webApp = window.Telegram.WebApp
      
      // КРИТИЧНО: Проверяем, что startParam доступен (не undefined)
      // undefined означает, что WebApp еще не полностью инициализирован
      if (!('startParam' in webApp)) {
        logger.info('[useAppMode] startParam property not available yet')
        return false
      }

      // ЖЕСТКОЕ ЛОГИРОВАНИЕ: проверка startParam
      const startParam = webApp.startParam
      logger.info('[useAppMode] ===== START PARAM CHECK =====')
      logger.info('[useAppMode] Raw startParam value:', startParam)
      logger.info('[useAppMode] startParam type:', typeof startParam)
      logger.info('[useAppMode] startParam === "panel":', startParam === 'panel')
      logger.info('[useAppMode] startParam === null:', startParam === null)
      logger.info('[useAppMode] startParam === undefined:', startParam === undefined)
      logger.info('[useAppMode] startParam truthy:', !!startParam)
      logger.info('[useAppMode] String comparison:', String(startParam) === 'panel')

      // КРИТИЧНО: undefined не считается валидным значением
      // Если startParam === undefined, это означает, что WebApp еще не готов
      if (startParam === undefined) {
        logger.info('[useAppMode] startParam is undefined - WebApp not fully initialized yet')
        return false
      }

      // Определяем режим на основе startParam
      // panel → если startParam === "panel"
      // user → во всех остальных случаях (null, пустая строка, любое другое значение)
      const detectedMode: AppMode = startParam === 'panel' ? 'panel' : 'user'
      
      if (detectedMode === 'panel') {
        logger.info('[useAppMode] ✅✅✅ PANEL MODE DETECTED (startParam === "panel") ✅✅✅')
      } else {
        logger.info('[useAppMode] ✅ USER MODE DETECTED (startParam:', startParam || 'null/undefined', ')')
      }

      setMode(detectedMode)
      setIsReady(true)
      detectedRef.current = true
      logger.info('[useAppMode] ===== MODE DETECTION COMPLETE =====')
      logger.info('[useAppMode] Final mode:', detectedMode === 'panel' ? 'PANEL' : 'USER')
      logger.info('[useAppMode] isReady:', true)
      
      // Очищаем интервалы
      if (checkIntervalRef.current) {
        clearInterval(checkIntervalRef.current)
        checkIntervalRef.current = null
      }
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current)
        timeoutRef.current = null
      }
      
      return true // Режим успешно определен
    }

    // Пробуем определить режим сразу
    const immediateResult = detectMode()
    
    // Если режим не определен (WebApp не готов), ждем его инициализации
    if (!immediateResult && !detectedRef.current) {
      logger.info('[useAppMode] WebApp not ready, waiting for initialization...')
      
      // КРИТИЧНО: Ждем появления WebApp с интервалом 50ms (быстрее, чем 100ms)
      checkIntervalRef.current = setInterval(() => {
        if (detectedRef.current) {
          // Режим уже определен, очищаем интервал
          if (checkIntervalRef.current) {
            clearInterval(checkIntervalRef.current)
            checkIntervalRef.current = null
          }
          return
        }
        
        const result = detectMode()
        if (result) {
          // Режим успешно определен
          if (checkIntervalRef.current) {
            clearInterval(checkIntervalRef.current)
            checkIntervalRef.current = null
          }
        }
      }, 50) // Проверяем каждые 50ms для более быстрого определения

      // Останавливаем проверку через 5 секунд
      timeoutRef.current = setTimeout(() => {
        if (checkIntervalRef.current) {
          clearInterval(checkIntervalRef.current)
          checkIntervalRef.current = null
        }
        if (!detectedRef.current) {
          logger.warn('[useAppMode] WebApp not found after 5 seconds, using default user mode')
          setMode('user')
          setIsReady(true)
          detectedRef.current = true
        }
      }, 5000)
    }

    return () => {
      // Cleanup: очищаем интервалы при размонтировании
      if (checkIntervalRef.current) {
        clearInterval(checkIntervalRef.current)
        checkIntervalRef.current = null
      }
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current)
        timeoutRef.current = null
      }
    }
  }, [])

  return { mode, isReady }
}

