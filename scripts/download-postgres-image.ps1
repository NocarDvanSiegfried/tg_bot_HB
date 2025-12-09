# Скрипт для загрузки образа PostgreSQL с несколькими попытками и альтернативными источниками (PowerShell)

$ErrorActionPreference = "Stop"

$IMAGE_NAME = "postgres:15"
$MAX_RETRIES = 3
$RETRY_DELAY = 5

Write-Host "=== Загрузка образа PostgreSQL ===" -ForegroundColor Cyan
Write-Host "Образ: $IMAGE_NAME" -ForegroundColor Yellow
Write-Host ""

# Функция для попытки загрузки образа
function Download-Image {
    param(
        [string]$Source,
        [string]$Image
    )
    
    Write-Host "Попытка загрузки из: $Source" -ForegroundColor Yellow
    
    try {
        if ($Source -eq "docker-hub") {
            docker pull $Image
            return $true
        }
        elseif ($Source -eq "docker-hub-mirror") {
            # Попытка через альтернативный endpoint
            $env:DOCKER_REGISTRY_MIRROR = "https://registry-1.docker.io"
            docker pull $Image
            return $true
        }
    }
    catch {
        Write-Host "Ошибка: $_" -ForegroundColor Red
        return $false
    }
    
    return $false
}

# Проверка, существует ли образ локально
function Test-LocalImage {
    $images = docker images --format "{{.Repository}}:{{.Tag}}" 2>&1
    if ($images -match "^${IMAGE_NAME}$") {
        Write-Host "✓ Образ $IMAGE_NAME уже существует локально" -ForegroundColor Green
        return $true
    }
    return $false
}

# Основная логика
function Main {
    # Проверка наличия образа локально
    if (Test-LocalImage) {
        Write-Host ""
        Write-Host "Образ уже загружен. Можно использовать: docker compose up" -ForegroundColor Green
        exit 0
    }
    
    # Список источников для попыток
    $SOURCES = @("docker-hub", "docker-hub-mirror")
    
    foreach ($source in $SOURCES) {
        for ($attempt = 1; $attempt -le $MAX_RETRIES; $attempt++) {
            Write-Host ""
            Write-Host "Попытка $attempt из $MAX_RETRIES для источника: $source" -ForegroundColor Yellow
            
            if (Download-Image -Source $source -Image $IMAGE_NAME) {
                Write-Host ""
                Write-Host "✓ Образ успешно загружен!" -ForegroundColor Green
                Write-Host "Теперь можно запустить: docker compose up" -ForegroundColor Green
                exit 0
            }
            else {
                if ($attempt -lt $MAX_RETRIES) {
                    Write-Host "✗ Попытка не удалась. Повтор через $RETRY_DELAY секунд..." -ForegroundColor Yellow
                    Start-Sleep -Seconds $RETRY_DELAY
                }
                else {
                    Write-Host "✗ Все попытки для источника $source исчерпаны" -ForegroundColor Red
                }
            }
        }
    }
    
    Write-Host ""
    Write-Host "✗ Не удалось загрузить образ из всех источников" -ForegroundColor Red
    Write-Host ""
    Write-Host "Альтернативные решения:" -ForegroundColor Yellow
    Write-Host "1. Проверьте интернет-соединение" -ForegroundColor Gray
    Write-Host "2. Настройте прокси для Docker (см. README.md)" -ForegroundColor Gray
    Write-Host "3. Используйте локальную установку PostgreSQL (см. README.md)" -ForegroundColor Gray
    Write-Host "4. Попробуйте другой тег: docker pull postgres:15-alpine" -ForegroundColor Gray
    Write-Host "5. Используйте VPN или другой DNS сервер" -ForegroundColor Gray
    Write-Host "6. Попробуйте загрузить вручную: docker pull postgres:15 --platform linux/amd64" -ForegroundColor Gray
    
    exit 1
}

Main

