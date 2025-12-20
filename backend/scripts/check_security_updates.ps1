# Скрипт для проверки доступных обновлений безопасности (PowerShell)
# Использование: .\check_security_updates.ps1 [package_name]

param(
    [string]$Package = ""
)

$ImageName = "python:3.11-slim-bookworm"

Write-Host "=== Проверка обновлений безопасности для $ImageName ===" -ForegroundColor Cyan
Write-Host ""

if ($Package) {
    Write-Host "Проверка пакета: $Package" -ForegroundColor Yellow
    Write-Host ""
    docker run --rm $ImageName bash -c "apt-get update -qq > /dev/null 2>&1 && apt-cache policy $Package | grep -E '^[a-z]|Installed|Candidate'"
} else {
    Write-Host "Проверка критичных пакетов:" -ForegroundColor Yellow
    Write-Host ""
    
    $Packages = @(
        "libsqlite3-0",
        "zlib1g",
        "libpam-modules",
        "libpam-modules-bin",
        "libpam-runtime",
        "libpam0g",
        "util-linux",
        "gpgv",
        "libncursesw6",
        "libtinfo6",
        "ncurses-base",
        "ncurses-bin",
        "libgnutls30"
    )
    
    foreach ($pkg in $Packages) {
        Write-Host "--- $pkg ---" -ForegroundColor Green
        try {
            docker run --rm $ImageName bash -c "apt-get update -qq > /dev/null 2>&1 && apt-cache policy $pkg | grep -E 'Installed|Candidate' | head -2"
        } catch {
            Write-Host "Ошибка при проверке $pkg" -ForegroundColor Red
        }
        Write-Host ""
    }
}

Write-Host ""
Write-Host "=== Проверка завершена ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Для проверки конкретного пакета используйте:" -ForegroundColor Yellow
Write-Host "  .\check_security_updates.ps1 -Package <package_name>"
Write-Host ""
Write-Host "Для проверки всех доступных обновлений используйте:" -ForegroundColor Yellow
Write-Host "  docker run --rm $ImageName bash -c 'apt-get update && apt list --upgradable'"

