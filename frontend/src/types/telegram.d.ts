declare global {
  interface Window {
    Telegram?: {
      WebApp: {
        ready: () => void
        expand: () => void
        initData: string
        initDataUnsafe: any
        startParam?: string | null // Параметр запуска Mini App (передается через start_param в WebAppInfo)
        openLink?: (url: string, options?: { try_instant_view?: boolean }) => void // Открытие ссылки вне sandbox
        [key: string]: any // Для поддержки других свойств WebApp API
      }
    }
  }
}

export {}

