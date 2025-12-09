# PowerShell скрипт для проверки проекта после исправлений

$ErrorActionPreference = "Stop"
$Errors = 0

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "Проверка Проекта Telegram Birthday Bot" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

function Check-Result {
    param(
        [string]$Message,
        [bool]$Success
    )
    if ($Success) {
        Write-Host "✅ $Message" -ForegroundColor Green
        return $true
    } else {
        Write-Host "❌ $Message" -ForegroundColor Red
        $script:Errors++
        return $false
    }
}

Write-Host "1. Проверка Backend кода..." -ForegroundColor Yellow
Set-Location backend

Write-Host "   - Проверка синтаксиса Python..."
try {
    python -m py_compile src/infrastructure/database/models.py
    Check-Result "Синтаксис models.py корректен" $true
} catch {
    Check-Result "Синтаксис models.py корректен" $false
}

try {
    python -m py_compile src/presentation/telegram/middleware/database_middleware.py
    Check-Result "Синтаксис database_middleware.py корректен" $true
} catch {
    Check-Result "Синтаксис database_middleware.py корректен" $false
}

try {
    python -m py_compile src/infrastructure/database/repositories/panel_access_repository_impl.py
    Check-Result "Синтаксис panel_access_repository_impl.py корректен" $true
} catch {
    Check-Result "Синтаксис panel_access_repository_impl.py корректен" $false
}

Write-Host ""
Write-Host "2. Проверка миграций..." -ForegroundColor Yellow
if (Test-Path "migrations/versions/002_fix_user_id_bigint.py") {
    Check-Result "Миграция 002_fix_user_id_bigint.py найдена" $true
    try {
        python -m py_compile migrations/versions/002_fix_user_id_bigint.py
        Check-Result "Синтаксис миграции корректен" $true
    } catch {
        Check-Result "Синтаксис миграции корректен" $false
    }
} else {
    Check-Result "Миграция 002_fix_user_id_bigint.py не найдена" $false
}

Write-Host ""
Write-Host "3. Проверка тестов..." -ForegroundColor Yellow
if (Test-Path "tests/infrastructure/test_panel_access_repository_bigint.py") {
    Check-Result "Тест test_panel_access_repository_bigint.py найден" $true
} else {
    Check-Result "Тест test_panel_access_repository_bigint.py не найден" $false
}

if (Test-Path "tests/presentation/telegram/middleware/test_database_middleware.py") {
    Check-Result "Тест test_database_middleware.py найден" $true
} else {
    Check-Result "Тест test_database_middleware.py не найден" $false
}

Write-Host ""
Write-Host "4. Применение миграции..." -ForegroundColor Yellow
try {
    alembic upgrade head
    Check-Result "Миграция применена успешно" $true
} catch {
    Check-Result "Миграция применена успешно" $false
}

Write-Host ""
Write-Host "5. Запуск тестов..." -ForegroundColor Yellow
try {
    pytest tests/infrastructure/test_panel_access_repository_bigint.py -v
    Check-Result "Тесты для BigInteger прошли" $true
} catch {
    Check-Result "Тесты для BigInteger прошли" $false
}

try {
    pytest tests/presentation/telegram/middleware/test_database_middleware.py -v
    Check-Result "Тесты для middleware прошли" $true
} catch {
    Check-Result "Тесты для middleware прошли" $false
}

try {
    pytest tests/infrastructure/test_panel_access_repository.py -v
    Check-Result "Обновленные тесты repository прошли" $true
} catch {
    Check-Result "Обновленные тесты repository прошли" $false
}

try {
    pytest tests/presentation/telegram/handlers/test_panel_handler.py -v
    Check-Result "Обновленные тесты handler прошли" $true
} catch {
    Check-Result "Обновленные тесты handler прошли" $false
}

Set-Location ..

Write-Host ""
Write-Host "6. Проверка Frontend..." -ForegroundColor Yellow
Set-Location frontend

if (Test-Path "package.json") {
    Check-Result "package.json найден" $true
} else {
    Check-Result "package.json не найден" $false
}

if (Test-Path "node_modules") {
    Check-Result "node_modules установлены" $true
} else {
    Write-Host "⚠️  node_modules не найдены, запустите: npm install" -ForegroundColor Yellow
}

Write-Host "   - Проверка TypeScript..."
if (Get-Command npx -ErrorAction SilentlyContinue) {
    try {
        npx tsc --noEmit
        Check-Result "TypeScript компиляция прошла успешно" $true
    } catch {
        Check-Result "TypeScript компиляция прошла успешно" $false
    }
} else {
    Write-Host "⚠️  npx не найден, пропускаем проверку TypeScript" -ForegroundColor Yellow
}

Set-Location ..

Write-Host ""
Write-Host "7. Проверка Docker конфигурации..." -ForegroundColor Yellow
if (Test-Path "docker-compose.yml") {
    Check-Result "docker-compose.yml найден" $true
    
    try {
        docker compose config | Out-Null
        Check-Result "docker-compose.yml синтаксис корректен" $true
    } catch {
        Check-Result "docker-compose.yml синтаксис корректен" $false
    }
} else {
    Check-Result "docker-compose.yml не найден" $false
}

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
if ($Errors -eq 0) {
    Write-Host "✅ Все проверки пройдены успешно!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Следующие шаги:" -ForegroundColor Yellow
    Write-Host "1. Запустите: docker compose build"
    Write-Host "2. Запустите: docker compose up"
    Write-Host "3. Проверьте работу бота в Telegram"
    exit 0
} else {
    Write-Host "❌ Найдено ошибок: $Errors" -ForegroundColor Red
    Write-Host ""
    Write-Host "Исправьте ошибки и запустите проверку снова."
    exit 1
}

