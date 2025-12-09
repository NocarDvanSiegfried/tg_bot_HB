# Скрипт для настройки прокси для Docker daemon (PowerShell)

Write-Host "=== Настройка прокси для Docker ===" -ForegroundColor Cyan
Write-Host ""

# Запрос данных прокси
$HTTP_PROXY = Read-Host "HTTP прокси (например, http://proxy.example.com:8080)"
$HTTPS_PROXY = Read-Host "HTTPS прокси (или Enter для использования HTTP прокси)"
$NO_PROXY = Read-Host "Исключения для прокси (через запятую, например, localhost,127.0.0.1)"

if ([string]::IsNullOrWhiteSpace($HTTPS_PROXY)) {
    $HTTPS_PROXY = $HTTP_PROXY
}

if ([string]::IsNullOrWhiteSpace($NO_PROXY)) {
    $NO_PROXY = "localhost,127.0.0.1"
}

# Путь к конфигурации Docker для Windows
$DOCKER_CONFIG_DIR = "$env:USERPROFILE\.docker"
$DOCKER_CONFIG = "$DOCKER_CONFIG_DIR\config.json"

# Создание директории, если не существует
if (-not (Test-Path $DOCKER_CONFIG_DIR)) {
    New-Item -ItemType Directory -Path $DOCKER_CONFIG_DIR -Force | Out-Null
}

# Создание резервной копии
if (Test-Path $DOCKER_CONFIG) {
    $backupName = "$DOCKER_CONFIG.backup.$(Get-Date -Format 'yyyyMMdd_HHmmss')"
    Copy-Item $DOCKER_CONFIG $backupName
    Write-Host "✓ Создана резервная копия: $backupName" -ForegroundColor Green
}

# Чтение существующей конфигурации или создание новой
$config = @{}
if (Test-Path $DOCKER_CONFIG) {
    $existingConfig = Get-Content $DOCKER_CONFIG | ConvertFrom-Json
    $config = $existingConfig | ConvertTo-Hashtable
}

# Добавление настроек прокси
$config["proxies"] = @{
    "default" = @{
        "httpProxy" = $HTTP_PROXY
        "httpsProxy" = $HTTPS_PROXY
        "noProxy" = $NO_PROXY
    }
}

# Сохранение конфигурации
$config | ConvertTo-Json -Depth 10 | Set-Content $DOCKER_CONFIG

Write-Host ""
Write-Host "✓ Конфигурация сохранена в: $DOCKER_CONFIG" -ForegroundColor Green
Write-Host ""
Write-Host "Для применения изменений перезапустите Docker Desktop" -ForegroundColor Yellow
Write-Host ""
Write-Host "Проверка настроек:" -ForegroundColor Yellow
Write-Host "  docker info | Select-String -Pattern 'proxy' -CaseSensitive:`$false" -ForegroundColor Gray

