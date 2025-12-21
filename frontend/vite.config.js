import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 3000,
    allowedHosts: [
      "micro-tab.ru",
      "miniapp.micro-tab.ru",
      "www.micro-tab.ru",
      "api.micro-tab.ru",
      "mini.micro-tab.ru",
      "0.0.0.0",
    ],
  },
})
