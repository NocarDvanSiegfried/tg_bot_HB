declare global {
  interface Window {
    Telegram?: {
      WebApp: {
        ready: () => void
        expand: () => void
        initData: string
        initDataUnsafe: any
        startParam?: string | null // Параметр запуска Mini App (передается через start_param в WebAppInfo)
        [key: string]: any // Для поддержки других свойств WebApp API
      }
    }
  }
}

export {}

