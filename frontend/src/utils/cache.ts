/**
 * Простой кэш для API запросов
 * Используется для уменьшения количества запросов к серверу
 */

interface CacheEntry<T> {
  data: T
  timestamp: number
  ttl: number // Time to live в миллисекундах
}

class SimpleCache {
  private cache: Map<string, CacheEntry<any>> = new Map()

  /**
   * Получить данные из кэша
   */
  get<T>(key: string): T | null {
    const entry = this.cache.get(key)
    if (!entry) {
      return null
    }

    // Проверяем, не истек ли срок действия
    const now = Date.now()
    if (now - entry.timestamp > entry.ttl) {
      this.cache.delete(key)
      return null
    }

    return entry.data as T
  }

  /**
   * Сохранить данные в кэш
   */
  set<T>(key: string, data: T, ttl: number): void {
    this.cache.set(key, {
      data,
      timestamp: Date.now(),
      ttl,
    })
  }

  /**
   * Удалить данные из кэша
   */
  delete(key: string): void {
    this.cache.delete(key)
  }

  /**
   * Очистить весь кэш
   */
  clear(): void {
    this.cache.clear()
  }

  /**
   * Инвалидировать кэш по паттерну ключа
   */
  invalidatePattern(pattern: string): void {
    const regex = new RegExp(pattern)
    for (const key of this.cache.keys()) {
      if (regex.test(key)) {
        this.cache.delete(key)
      }
    }
  }
}

// Singleton instance
export const cache = new SimpleCache()

/**
 * Ключи кэша для различных типов данных
 */
export const CacheKeys = {
  birthdays: 'birthdays:all',
  calendarMonth: (year: number, month: number) => `calendar:${year}:${month}`,
  birthday: (id: number) => `birthday:${id}`,
  responsibles: 'responsibles:all',
  responsible: (id: number) => `responsible:${id}`,
  holidays: 'holidays:all',
  holiday: (id: number) => `holiday:${id}`,
} as const

/**
 * TTL для различных типов данных (в миллисекундах)
 */
export const CacheTTL = {
  birthdays: 5 * 60 * 1000, // 5 минут
  calendarMonth: 60 * 60 * 1000, // 1 час
  birthday: 5 * 60 * 1000, // 5 минут
  responsibles: 5 * 60 * 1000, // 5 минут
  responsible: 5 * 60 * 1000, // 5 минут
  holidays: 5 * 60 * 1000, // 5 минут
  holiday: 5 * 60 * 1000, // 5 минут
} as const

