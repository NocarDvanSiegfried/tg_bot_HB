# Скрипт проверки конфигурации Nginx для Telegram Mini App
# Проверяет синтаксис конфигурации и доступность портов

Write-Host "🔍 Проверка конфигурации Nginx для Telegram Mini App" -ForegroundColor Cyan
Write-Host ""

# Проверка прав доступа
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "⚠️  Для полной проверки требуются права администратора" -ForegroundColor Yellow
    Write-Host "Некоторые проверки могут быть пропущены."
    Write-Host ""
}

# 1. Проверка синтаксиса конфигурации Nginx
Write-Host "1️⃣  Проверка синтаксиса конфигурации Nginx..." -ForegroundColor Cyan

$nginxTest = & nginx -t 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Синтаксис конфигурации Nginx корректен" -ForegroundColor Green
} else {
    Write-Host "❌ Ошибка в конфигурации Nginx" -ForegroundColor Red
    Write-Host $nginxTest
    exit 1
}
Write-Host ""

# 2. Проверка доступности портов
Write-Host "2️⃣  Проверка доступности портов..." -ForegroundColor Cyan

function Test-Port {
    param(
        [int]$Port,
        [string]$Service
    )
    
    $connection = Test-NetConnection -ComputerName localhost -Port $Port -WarningAction SilentlyContinue -InformationLevel Quiet 2>$null
    if ($connection) {
        Write-Host "✅ Порт $Port открыт ($Service)" -ForegroundColor Green
        return $true
    } else {
        Write-Host "⚠️  Порт $Port не прослушивается ($Service)" -ForegroundColor Yellow
        return $false
    }
}

Test-Port -Port 8001 -Service "Backend (Nginx)"
Test-Port -Port 3001 -Service "Frontend (Nginx)"
Write-Host ""

# 3. Проверка статуса Nginx (только для Linux/WSL)
Write-Host "3️⃣  Проверка статуса Nginx..." -ForegroundColor Cyan
if (Get-Command systemctl -ErrorAction SilentlyContinue) {
    $nginxStatus = & systemctl is-active nginx 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Nginx запущен" -ForegroundColor Green
    } else {
        Write-Host "❌ Nginx не запущен" -ForegroundColor Red
        Write-Host "Запустите Nginx: sudo systemctl start nginx"
    }
} else {
    Write-Host "⚠️  Проверка статуса Nginx недоступна (требуется Linux/WSL)" -ForegroundColor Yellow
}
Write-Host ""

# 4. Проверка конфигурационных файлов
Write-Host "4️⃣  Проверка наличия конфигурационных файлов..." -ForegroundColor Cyan

function Test-ConfigFile {
    param(
        [string]$FilePath,
        [string]$Description
    )
    
    if (Test-Path $FilePath) {
        Write-Host "✅ $Description существует" -ForegroundColor Green
        return $true
    } else {
        Write-Host "⚠️  $Description не найден: $FilePath" -ForegroundColor Yellow
        return $false
    }
}

# Проверка файлов (пути для Linux/WSL)
$configFiles = @(
    @{Path="/etc/nginx/nginx.conf"; Desc="Основная конфигурация Nginx"},
    @{Path="/etc/nginx/conf.d/backend.conf"; Desc="Конфигурация Backend"},
    @{Path="/etc/nginx/conf.d/frontend.conf"; Desc="Конфигурация Frontend"}
)

foreach ($file in $configFiles) {
    if (Test-Path $file.Path) {
        Test-ConfigFile -FilePath $file.Path -Description $file.Desc
    } else {
        Write-Host "⚠️  $($file.Desc) не найден: $($file.Path)" -ForegroundColor Yellow
        Write-Host "   (Проверка пропущена, так как файл находится в Linux-пути)" -ForegroundColor Gray
    }
}
Write-Host ""

# 5. Проверка доступности backend и frontend на localhost
Write-Host "5️⃣  Проверка доступности сервисов на localhost..." -ForegroundColor Cyan

function Test-LocalhostService {
    param(
        [int]$Port,
        [string]$Service
    )
    
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:$Port" -TimeoutSec 2 -UseBasicParsing -ErrorAction Stop
        Write-Host "✅ $Service доступен на localhost:$Port" -ForegroundColor Green
        return $true
    } catch {
        Write-Host "⚠️  $Service недоступен на localhost:$Port" -ForegroundColor Yellow
        Write-Host "   Убедитесь, что Docker контейнеры запущены: docker compose ps" -ForegroundColor Gray
        return $false
    }
}

Test-LocalhostService -Port 8000 -Service "Backend"
Test-LocalhostService -Port 3000 -Service "Frontend"
Write-Host ""

# Итоговая сводка
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "📋 Итоговая сводка:" -ForegroundColor Cyan
Write-Host ""
Write-Host "Для проверки доступности через Nginx выполните:" -ForegroundColor White
Write-Host "  curl https://your-domain.com:8001/  # Backend" -ForegroundColor Gray
Write-Host "  curl https://your-domain.com:3001/  # Frontend" -ForegroundColor Gray
Write-Host ""
Write-Host "Для просмотра логов Nginx:" -ForegroundColor White
Write-Host "  sudo tail -f /var/log/nginx/backend_error.log" -ForegroundColor Gray
Write-Host "  sudo tail -f /var/log/nginx/frontend_error.log" -ForegroundColor Gray
Write-Host ""

