# Скрипт для проверки наличия всех необходимых Docker образов локально
# Использование: .\scripts\check-docker-images.ps1

$ErrorActionPreference = "Continue"

# Список всех необходимых образов
$REQUIRED_IMAGES = @(
    "postgres:15",
    "node:20-alpine",
    "python:3.11-slim"
)

Write-Host "=== Проверка наличия Docker образов ===" -ForegroundColor Cyan
Write-Host ""

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

# Функция для получения информации об образе
function Get-ImageInfo {
    param(
        [string]$Image
    )
    
    $info = docker images --format "{{.Repository}}:{{.Tag}} {{.Size}}" 2>&1 | Select-String "^${Image} "
    if ($info) {
        $parts = $info.ToString().Split(" ", 2)
        return @{
            Exists = $true
            Size = if ($parts.Length -gt 1) { $parts[1] } else { "unknown" }
        }
    }
    return @{
        Exists = $false
        Size = "N/A"
    }
}

# Проверка каждого образа
$missingImages = @()
$foundImages = @()

foreach ($image in $REQUIRED_IMAGES) {
    $info = Get-ImageInfo -Image $image
    if ($info.Exists) {
        Write-Host "✓ $image" -ForegroundColor Green -NoNewline
        Write-Host " (размер: $($info.Size))" -ForegroundColor Gray
        $foundImages += $image
    }
    else {
        Write-Host "✗ $image" -ForegroundColor Red -NoNewline
        Write-Host " (отсутствует)" -ForegroundColor Gray
        $missingImages += $image
    }
}

# Итоговый отчет
Write-Host ""
Write-Host "=== Итоговый отчет ===" -ForegroundColor Cyan
Write-Host "Найдено: $($foundImages.Count) из $($REQUIRED_IMAGES.Count)" -ForegroundColor $(if ($missingImages.Count -eq 0) { "Green" } else { "Yellow" })

if ($missingImages.Count -gt 0) {
    Write-Host ""
    Write-Host "Отсутствующие образы:" -ForegroundColor Yellow
    foreach ($img in $missingImages) {
        Write-Host "  - $img" -ForegroundColor Red
    }
    
    Write-Host ""
    Write-Host "Рекомендации:" -ForegroundColor Yellow
    Write-Host "1. Загрузите недостающие образы:" -ForegroundColor Gray
    Write-Host "   .\scripts\download-all-images.ps1" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "2. Или загрузите вручную:" -ForegroundColor Gray
    foreach ($img in $missingImages) {
        Write-Host "   docker pull $img" -ForegroundColor Cyan
    }
    Write-Host ""
    Write-Host "3. После загрузки образов запустите сборку:" -ForegroundColor Gray
    Write-Host "   docker compose up --build" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "4. Если образы уже есть, но скрипт их не находит, используйте:" -ForegroundColor Gray
    Write-Host "   docker compose build --pull=never" -ForegroundColor Cyan
    
    exit 1
}
else {
    Write-Host ""
    Write-Host "✓ Все необходимые образы найдены локально!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Можно запускать сборку:" -ForegroundColor Green
    Write-Host "  docker compose up --build" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Или без загрузки образов:" -ForegroundColor Green
    Write-Host "  docker compose build --pull=never" -ForegroundColor Cyan
    
    exit 0
}

