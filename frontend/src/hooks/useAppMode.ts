/**
 * Режимы работы Mini App
 */
export type AppMode = 'user' | 'panel'

/**
 * Хук для определения режима работы Mini App
 * 
 * КРИТИЧНО: Bot = Launcher архитектура
 * Mini App всегда открывается в режиме календаря (user mode)
 * Режим 'panel' больше не используется
 * 
 * @returns Объект с режимом приложения и флагом готовности
 */
export function useAppMode(): { mode: AppMode; isReady: boolean } {
  // КРИТИЧНО: Bot = Launcher архитектура
  // Mini App всегда открывается в режиме календаря (user mode)
  // Режим 'panel' больше не используется
  return { mode: 'user', isReady: true }
}

