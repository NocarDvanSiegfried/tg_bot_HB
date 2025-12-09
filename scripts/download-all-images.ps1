# Универсальный скрипт для загрузки всех необходимых Docker образов для проекта
# Использование: .\scripts\download-all-images.ps1
# 
# Этот скрипт пытается загрузить все необходимые образы с несколькими попытками
# и альтернативными тегами, если основной тег недоступен.

$ErrorActionPreference = "Stop"

# Список всех необходимых образов с альтернативными вариантами
$IMAGES_CONFIG = @{
    "postgres:15" = @("postgres:15-alpine", "postgres:15")
    "node:20-alpine" = @("node:20-alpine", "node:20", "node:alpine")
    "python:3.11-slim" = @("python:3.11-slim", "python:3.11", "python:slim")
}

$MAX_RETRIES = 5
$INITIAL_RETRY_DELAY = 3
$MAX_RETRY_DELAY = 30
$DOCKER_HUB_TIMEOUT = 15

Write-Host "=== Загрузка всех необходимых Docker образов ===" -ForegroundColor Cyan
Write-Host ""

# Функция для проверки доступности Docker Hub
function Test-DockerHub {
    Write-Host "Проверка доступности Docker Hub..." -ForegroundColor Yellow
    try {
        $response = Invoke-WebRequest -Uri "https://registry-1.docker.io/v2/" -Method Head -TimeoutSec $DOCKER_HUB_TIMEOUT -UseBasicParsing -ErrorAction Stop
        Write-Host "✓ Docker Hub доступен" -ForegroundColor Green
        return $true
    }
    catch {
        Write-Host "✗ Docker Hub недоступен: $_" -ForegroundColor Red
        Write-Host "  Попробуйте использовать VPN или настроить прокси" -ForegroundColor Yellow
        return $false
    }
}

# Функция для попытки загрузки образа с экспоненциальной задержкой
function Download-Image {
    param(
        [string]$Image
    )
    
    Write-Host "  Загрузка: $Image" -ForegroundColor Gray
    
    $attempt = 1
    while ($attempt -le $MAX_RETRIES) {
        Write-Host "    Попытка $attempt из $MAX_RETRIES..." -ForegroundColor DarkGray
        
        # Увеличиваем таймаут для Docker pull при повторных попытках
        $pullTimeout = $DOCKER_HUB_TIMEOUT * $attempt
        
        try {
            $job = Start-Job -ScriptBlock { param($img) docker pull $img 2>&1 } -ArgumentList $Image
            $result = Wait-Job -Job $job -Timeout $pullTimeout
            $output = Receive-Job -Job $job
            Remove-Job -Job $job
            
            if ($result -and $LASTEXITCODE -eq 0) {
                Write-Host "    ✓ Образ $Image успешно загружен" -ForegroundColor Green
                return $true
            }
            elseif (-not $result) {
                Write-Host "    ✗ Таймаут при загрузке (превышен лимит $pullTimeout секунд)" -ForegroundColor Red
            }
            else {
                Write-Host "    ✗ Ошибка: $output" -ForegroundColor Red
            }
        }
        catch {
            Write-Host "    ✗ Исключение: $_" -ForegroundColor Red
        }
        
        if ($attempt -lt $MAX_RETRIES) {
            # Экспоненциальная задержка: 3, 6, 12, 24, 30 секунд
            $delay = [Math]::Min($INITIAL_RETRY_DELAY * [Math]::Pow(2, $attempt - 1), $MAX_RETRY_DELAY)
            Write-Host "    Повтор через $delay секунд..." -ForegroundColor Yellow
            Start-Sleep -Seconds $delay
        }
        
        $attempt++
    }
    
    Write-Host "    ✗ Не удалось загрузить образ $Image после $MAX_RETRIES попыток" -ForegroundColor Red
    return $false
}

# Функция для проверки наличия образа локально
function Test-LocalImage {
    param(
        [string]$Image
    )
    
    $images = docker images --format "{{.Repository}}:{{.Tag}}" 2>&1
    if ($images -match "^${Image}$") {
        return $true
    }
    return $false
}

# Функция для загрузки образа с альтернативами
function Download-ImageWithAlternatives {
    param(
        [string]$PrimaryImage,
        [array]$Alternatives
    )
    
    Write-Host ""
    Write-Host "Образ: $PrimaryImage" -ForegroundColor Yellow
    
    # Проверяем, существует ли основной образ локально
    if (Test-LocalImage -Image $PrimaryImage) {
        Write-Host "  ✓ Образ $PrimaryImage уже существует локально" -ForegroundColor Green
        return $true
    }
    
    # Пробуем загрузить основной образ
    if (Download-Image -Image $PrimaryImage) {
        return $true
    }
    
    # Если основной образ не загрузился, пробуем альтернативы
    if ($Alternatives.Count -gt 0) {
        Write-Host "  Пробуем альтернативные варианты..." -ForegroundColor Yellow
        foreach ($alt in $Alternatives) {
            if ($alt -eq $PrimaryImage) {
                continue  # Пропускаем основной образ, он уже не загрузился
            }
            
            if (Test-LocalImage -Image $alt) {
                Write-Host "  ✓ Альтернативный образ $alt уже существует локально" -ForegroundColor Green
                Write-Host "  ⚠ ВНИМАНИЕ: Используется альтернативный образ $alt вместо $PrimaryImage" -ForegroundColor Yellow
                Write-Host "    Обновите Dockerfile, если хотите использовать этот образ постоянно" -ForegroundColor Yellow
                return $true
            }
            
            if (Download-Image -Image $alt) {
                Write-Host "  ⚠ ВНИМАНИЕ: Загружен альтернативный образ $alt вместо $PrimaryImage" -ForegroundColor Yellow
                Write-Host "    Обновите Dockerfile, если хотите использовать этот образ постоянно" -ForegroundColor Yellow
                return $true
            }
        }
    }
    
    return $false
}

# Основная логика
$dockerHubAvailable = Test-DockerHub
if (-not $dockerHubAvailable) {
    Write-Host ""
    Write-Host "⚠ Docker Hub недоступен, но попробуем загрузить образы из локального кеша" -ForegroundColor Yellow
}

$failedImages = @()
$successCount = 0
$totalImages = $IMAGES_CONFIG.Keys.Count

foreach ($primaryImage in $IMAGES_CONFIG.Keys) {
    $alternatives = $IMAGES_CONFIG[$primaryImage]
    
    if (Download-ImageWithAlternatives -PrimaryImage $primaryImage -Alternatives $alternatives) {
        $successCount++
    }
    else {
        $failedImages += $primaryImage
    }
}

# Итоговый отчет
Write-Host ""
Write-Host "=== Итоговый отчет ===" -ForegroundColor Cyan
Write-Host "Успешно загружено: $successCount из $totalImages" -ForegroundColor $(if ($successCount -eq $totalImages) { "Green" } else { "Yellow" })

if ($failedImages.Count -gt 0) {
    Write-Host ""
    Write-Host "✗ Не удалось загрузить следующие образы:" -ForegroundColor Red
    foreach ($img in $failedImages) {
        Write-Host "  - $img" -ForegroundColor Red
    }
    
    Write-Host ""
    Write-Host "Альтернативные решения:" -ForegroundColor Yellow
    Write-Host "1. Проверьте интернет-соединение" -ForegroundColor Gray
    Write-Host "2. Настройте прокси для Docker: .\scripts\setup-docker-proxy.ps1" -ForegroundColor Gray
    Write-Host "3. Используйте VPN или другой DNS сервер" -ForegroundColor Gray
    Write-Host "4. Попробуйте загрузить образы вручную:" -ForegroundColor Gray
    foreach ($img in $failedImages) {
        Write-Host "   docker pull $img" -ForegroundColor Gray
    }
    Write-Host "5. Используйте локальную разработку без Docker (см. README.md)" -ForegroundColor Gray
    Write-Host "6. Используйте docker compose build --pull=never (если образы уже есть локально)" -ForegroundColor Gray
    
    exit 1
}
else {
    Write-Host ""
    Write-Host "✓ Все образы успешно загружены!" -ForegroundColor Green
    Write-Host "Теперь можно запустить: docker compose up --build" -ForegroundColor Green
    exit 0
}
