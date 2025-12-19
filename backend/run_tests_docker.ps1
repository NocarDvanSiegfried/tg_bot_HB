# Скрипт для запуска backend тестов в Docker контейнере
# Использование: .\run_tests_docker.ps1 [опции pytest]

param(
    [string[]]$PytestArgs = @("-v", "--tb=short")
)

Write-Host "Запуск backend тестов в Docker контейнере..." -ForegroundColor Green
Write-Host ""

# Проверяем, что Docker Compose запущен
$containers = docker compose ps --format json 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Ошибка: Docker Compose не запущен или не настроен" -ForegroundColor Red
    Write-Host "Запустите: docker compose up -d" -ForegroundColor Yellow
    exit 1
}

# Проверяем, что backend контейнер запущен
$backendRunning = docker compose ps backend --format json 2>&1 | ConvertFrom-Json | Where-Object { $_.State -eq "running" }
if (-not $backendRunning) {
    Write-Host "Backend контейнер не запущен. Запускаю..." -ForegroundColor Yellow
    docker compose up -d backend
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Ошибка: Не удалось запустить backend контейнер" -ForegroundColor Red
        exit 1
    }
    Write-Host "Ожидание готовности backend контейнера..." -ForegroundColor Yellow
    Start-Sleep -Seconds 5
}

# Устанавливаем тестовые зависимости и запускаем тесты
# Используем docker compose run для создания временного контейнера с тестовыми зависимостями
Write-Host "Установка тестовых зависимостей..." -ForegroundColor Cyan
Write-Host "Запуск pytest с аргументами: $($PytestArgs -join ' ')" -ForegroundColor Cyan

# Запускаем тесты в новом контейнере с установкой тестовых зависимостей
# Перенаправляем вывод pip в stderr, чтобы не мешать выводу pytest
docker compose run --rm backend sh -c "pip install -q -r requirements.txt 2>&1 >/dev/null && python -m pytest tests/ $($PytestArgs -join ' ')"

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "Все тесты прошли успешно!" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "Некоторые тесты не прошли. Код выхода: $LASTEXITCODE" -ForegroundColor Red
    exit $LASTEXITCODE
}

