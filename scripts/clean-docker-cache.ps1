# Скрипт для очистки проблемных Docker образов и кэша
# Используйте этот скрипт, если возникают ошибки при сборке из-за поврежденного кэша

Write-Host "Очистка проблемных Docker образов и кэша..." -ForegroundColor Yellow

# Удаляем проблемные образы, если они существуют
$images = @("tg_bot_hb-backend:latest", "tg_bot_hb-frontend:latest")

foreach ($image in $images) {
    Write-Host "Проверка образа: $image" -ForegroundColor Cyan
    $exists = docker images -q $image 2>$null
    if ($exists) {
        Write-Host "Удаление образа: $image" -ForegroundColor Yellow
        docker rmi -f $image 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Образ $image успешно удален" -ForegroundColor Green
        } else {
            Write-Host "Не удалось удалить образ $image (возможно, используется контейнером)" -ForegroundColor Red
        }
    } else {
        Write-Host "Образ $image не найден" -ForegroundColor Gray
    }
}

# Очистка build cache (опционально, раскомментируйте при необходимости)
# Write-Host "Очистка build cache..." -ForegroundColor Yellow
# docker builder prune -f

Write-Host "`nГотово! Теперь можно запустить: docker compose build" -ForegroundColor Green

