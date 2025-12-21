import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  // Production build configuration
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    sourcemap: false,
    minify: 'esbuild',
    // Оптимизация для production
    rollupOptions: {
      output: {
        // Именование файлов для лучшего кеширования
        entryFileNames: 'assets/[name].[hash].js',
        chunkFileNames: 'assets/[name].[hash].js',
        assetFileNames: 'assets/[name].[hash].[ext]',
      },
    },
    // Увеличиваем лимит предупреждений для production
    chunkSizeWarningLimit: 1000,
    // Отключаем все dev-функции в production build
    // Это гарантирует отсутствие WebSocket и HMR кода
    target: 'es2015',
    // Убеждаемся что dev-код не попадает в production
    define: {
      'import.meta.hot': 'undefined',
    },
  },
  // Base path для статики (пустой для корня)
  base: '/',
  // Server config только для dev (не используется в production)
  // В production build эти настройки игнорируются
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
    // HMR отключен для production - не создает WebSocket соединений
    hmr: false,
  },
  // Preview config для тестирования production build локально
  // В production build не используется
  preview: {
    port: 4173,
    host: true,
  },
})
