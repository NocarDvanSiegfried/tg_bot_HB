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

# Запускаем тесты в контейнере
Write-Host "Запуск pytest с аргументами: $($PytestArgs -join ' ')" -ForegroundColor Cyan
docker compose exec -T backend pytest tests/ $PytestArgs

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "Все тесты прошли успешно!" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "Некоторые тесты не прошли. Код выхода: $LASTEXITCODE" -ForegroundColor Red
    exit $LASTEXITCODE
}

