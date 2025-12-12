/**
 * Утилита для логирования с поддержкой окружения.
 * 
 * В development режиме логирует все сообщения.
 * В production режиме логирует только ошибки.
 */

export const logger = {
  /**
   * Логирует сообщение (только в development режиме).
   */
  log: (...args: any[]): void => {
    if (import.meta.env.DEV) {
      console.log(...args)
    }
  },

  /**
   * Логирует информационное сообщение (только в development режиме).
   */
  info: (...args: any[]): void => {
    if (import.meta.env.DEV) {
      console.info(...args)
    }
  },

  /**
   * Логирует предупреждение (только в development режиме).
   */
  warn: (...args: any[]): void => {
    if (import.meta.env.DEV) {
      console.warn(...args)
    }
  },

  /**
   * Логирует ошибку (всегда, даже в production).
   * Ошибки важны для debugging в production.
   */
  error: (...args: any[]): void => {
    console.error(...args)
  },
}

