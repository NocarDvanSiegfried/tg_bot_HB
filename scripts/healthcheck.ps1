# Healthcheck скрипт для проверки работы бота и API (PowerShell)

Write-Host "=== Health Check для Telegram Birthday Calendar ===" -ForegroundColor Cyan
Write-Host ""

$allOk = $true

# Проверка Docker контейнеров
Write-Host "1. Проверка Docker контейнеров..." -ForegroundColor Yellow
if (Get-Command docker -ErrorAction SilentlyContinue) {
    $containers = docker compose ps 2>&1
    if ($containers -match "Up") {
        Write-Host "✓ Docker контейнеры запущены" -ForegroundColor Green
        docker compose ps
    } else {
        Write-Host "✗ Docker контейнеры не запущены" -ForegroundColor Red
        Write-Host "   Запустите: docker compose up -d" -ForegroundColor Yellow
        $allOk = $false
    }
} else {
    Write-Host "⚠ Docker не установлен, пропускаем проверку контейнеров" -ForegroundColor Yellow
}

Write-Host ""

# Проверка API
Write-Host "2. Проверка API (http://localhost:8000)..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/" -UseBasicParsing -TimeoutSec 5 -ErrorAction Stop
    Write-Host "✓ API доступен" -ForegroundColor Green
    Write-Host "   Ответ: $($response.Content)" -ForegroundColor Gray
} catch {
    Write-Host "✗ API недоступен" -ForegroundColor Red
    Write-Host "   Проверьте, что backend запущен и слушает порт 8000" -ForegroundColor Yellow
    $allOk = $false
}

Write-Host ""

# Проверка календаря API
Write-Host "3. Проверка календаря API..." -ForegroundColor Yellow
$today = Get-Date -Format "yyyy-MM-dd"
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/api/calendar/$today" -UseBasicParsing -TimeoutSec 5 -ErrorAction Stop
    Write-Host "✓ Календарь API работает" -ForegroundColor Green
} catch {
    Write-Host "⚠ Календарь API недоступен (может требовать аутентификации)" -ForegroundColor Yellow
}

Write-Host ""

# Проверка базы данных
Write-Host "4. Проверка подключения к базе данных..." -ForegroundColor Yellow
if (Get-Command docker -ErrorAction SilentlyContinue) {
    $postgresStatus = docker compose ps postgres 2>&1
    if ($postgresStatus -match "Up") {
        try {
            docker compose exec -T postgres pg_isready -U postgres 2>&1 | Out-Null
            Write-Host "✓ PostgreSQL доступен" -ForegroundColor Green
        } catch {
            Write-Host "✗ PostgreSQL недоступен" -ForegroundColor Red
            $allOk = $false
        }
    } else {
        Write-Host "⚠ PostgreSQL контейнер не запущен" -ForegroundColor Yellow
    }
} else {
    Write-Host "⚠ Docker недоступен, пропускаем проверку БД" -ForegroundColor Yellow
}

Write-Host ""

# Проверка Frontend
Write-Host "5. Проверка Frontend (http://localhost:3000)..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:3000/" -UseBasicParsing -TimeoutSec 5 -ErrorAction Stop
    Write-Host "✓ Frontend доступен" -ForegroundColor Green
} catch {
    Write-Host "⚠ Frontend недоступен (может быть в процессе запуска)" -ForegroundColor Yellow
}

Write-Host ""

# Проверка логов на ошибки
Write-Host "6. Проверка последних ошибок в логах..." -ForegroundColor Yellow
if (Get-Command docker -ErrorAction SilentlyContinue) {
    $logs = docker compose logs backend --tail 50 2>&1
    $errorCount = ($logs | Select-String -Pattern "error|exception|failed" -CaseSensitive:$false).Count
    if ($errorCount -gt 0) {
        Write-Host "⚠ Найдено $errorCount потенциальных ошибок в логах backend" -ForegroundColor Yellow
        Write-Host "   Проверьте: docker compose logs backend" -ForegroundColor Yellow
    } else {
        Write-Host "✓ Ошибок в последних логах не найдено" -ForegroundColor Green
    }
} else {
    Write-Host "⚠ Docker недоступен, пропускаем проверку логов" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "=== Проверка завершена ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Для детальной диагностики используйте:" -ForegroundColor Yellow
Write-Host "  docker compose logs backend" -ForegroundColor Gray
Write-Host "  docker compose logs postgres" -ForegroundColor Gray
Write-Host "  Start-Process http://localhost:8000/docs" -ForegroundColor Gray

if ($allOk) {
    Write-Host ""
    Write-Host "✓ Все основные сервисы работают!" -ForegroundColor Green
    exit 0
} else {
    Write-Host ""
    Write-Host "✗ Обнаружены проблемы. Проверьте логи выше." -ForegroundColor Red
    exit 1
}

