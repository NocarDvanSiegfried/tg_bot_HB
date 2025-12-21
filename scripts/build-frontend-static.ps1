# Скрипт для production-сборки фронтенда в статические файлы
# Использование: .\scripts\build-frontend-static.ps1

$ErrorActionPreference = "Stop"

Write-Host "🔨 Начинаем production-сборку фронтенда..." -ForegroundColor Cyan

Set-Location frontend

# Проверяем наличие node_modules
if (-not (Test-Path "node_modules")) {
    Write-Host "📦 Устанавливаем зависимости..." -ForegroundColor Yellow
    npm ci
}

# Проверяем наличие VITE_API_URL
if (-not $env:VITE_API_URL) {
    Write-Host "⚠️  ВНИМАНИЕ: VITE_API_URL не установлен!" -ForegroundColor Red
    Write-Host "   Установите переменную окружения VITE_API_URL перед сборкой"
    Write-Host "   Пример: `$env:VITE_API_URL='https://api.micro-tab.ru:9443'"
    exit 1
}

Write-Host "✅ VITE_API_URL: $env:VITE_API_URL" -ForegroundColor Green

# Очищаем предыдущую сборку
Write-Host "🧹 Очищаем предыдущую сборку..." -ForegroundColor Yellow
if (Test-Path "dist") {
    Remove-Item -Recurse -Force dist
}

# Выполняем production-сборку
Write-Host "🔨 Выполняем production-сборку..." -ForegroundColor Cyan
npm run build

# Проверяем результат
if (-not (Test-Path "dist")) {
    Write-Host "❌ Ошибка: папка dist не создана!" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path "dist/index.html")) {
    Write-Host "❌ Ошибка: index.html не найден в dist!" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Production-сборка завершена успешно!" -ForegroundColor Green
Write-Host "📁 Статические файлы находятся в: frontend/dist" -ForegroundColor Cyan
Write-Host ""
Write-Host "📋 Следующие шаги:" -ForegroundColor Yellow
Write-Host "   1. Скопируйте содержимое frontend/dist в /var/www/miniapp на сервере"
Write-Host "   2. Убедитесь, что nginx конфигурация указывает на /var/www/miniapp"
Write-Host "   3. Перезапустите nginx: sudo systemctl reload nginx"

Set-Location ..

