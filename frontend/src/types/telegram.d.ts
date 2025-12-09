declare global {
  interface Window {
    Telegram?: {
      WebApp: {
        ready: () => void
        expand: () => void
        initData: string
        initDataUnsafe: any
        [key: string]: any // Для поддержки других свойств WebApp API
      }
    }
  }
}

export {}

