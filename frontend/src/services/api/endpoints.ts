/**
 * API Endpoints - константы для всех API endpoints
 * 
 * Централизованное хранение всех URL endpoints для упрощения поддержки
 * и предотвращения опечаток в URL.
 */

/**
 * Базовые endpoints для календаря
 */
export const API_ENDPOINTS = {
  /**
   * Получить данные календаря для конкретной даты
   * @param date - дата в формате YYYY-MM-DD
   */
  CALENDAR: (date: string) => `/api/calendar/${date}`,

  /**
   * Получить дни рождения за месяц
   * @param year - год
   * @param month - месяц (1-12)
   */
  CALENDAR_MONTH: (year: number, month: number) => `/api/calendar/month/${year}/${month}`,

  /**
   * Endpoints для управления днями рождения (USER API для Mini App)
   */
  BIRTHDAYS: {
    /** Список всех дней рождения */
    LIST: '/api/birthdays',
    /** Конкретный день рождения по ID */
    BY_ID: (id: number) => `/api/birthdays/${id}`,
  },

  /**
   * Endpoints для управления профессиональными праздниками (USER API для Mini App)
   */
  HOLIDAYS: {
    /** Список всех праздников */
    LIST: '/api/holidays',
    /** Конкретный праздник по ID */
    BY_ID: (id: number) => `/api/holidays/${id}`,
  },

  /**
   * Endpoints для управления ответственными лицами
   */
  RESPONSIBLE: {
    /** Список всех ответственных */
    LIST: '/api/panel/responsible',
    /** Конкретный ответственный по ID */
    BY_ID: (id: number) => `/api/panel/responsible/${id}`,
    /** Назначить ответственного на дату */
    ASSIGN: '/api/panel/assign-responsible',
  },

  /**
   * Endpoints для поиска
   */
  SEARCH: {
    /** Поиск людей (дни рождения и ответственные) */
    PEOPLE: (query: string) => `/api/panel/search?q=${encodeURIComponent(query)}`,
  },

  /**
   * Endpoints для генерации поздравлений
   */
  GREETING: {
    /** Сгенерировать поздравление */
    GENERATE: '/api/panel/generate-greeting',
    /** Создать открытку с поздравлением */
    CREATE_CARD: '/api/panel/create-card',
  },

  /**
   * Endpoints для проверки доступа
   */
  PANEL: {
    /** Проверить доступ к панели управления */
    CHECK_ACCESS: '/api/panel/check-access',
  },
} as const

