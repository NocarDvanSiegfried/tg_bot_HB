import { useEffect, useState } from 'react'

export function useTelegram() {
  const [webApp, setWebApp] = useState<any | null>(null)
  const [initData, setInitData] = useState<string | null>(null)

  useEffect(() => {
    if (typeof window !== 'undefined' && window.Telegram?.WebApp) {
      const tg = window.Telegram.WebApp
      setWebApp(tg)
      setInitData(tg.initData)
    }
  }, [])

  return { webApp, initData }
}

