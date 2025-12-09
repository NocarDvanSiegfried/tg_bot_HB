#!/bin/bash
# Скрипт для очистки проблемных Docker образов и кэша
# Используйте этот скрипт, если возникают ошибки при сборке из-за поврежденного кэша

echo "Очистка проблемных Docker образов и кэша..."

# Удаляем проблемные образы, если они существуют
images=("tg_bot_hb-backend:latest" "tg_bot_hb-frontend:latest")

for image in "${images[@]}"; do
    echo "Проверка образа: $image"
    if docker images -q "$image" 2>/dev/null | grep -q .; then
        echo "Удаление образа: $image"
        if docker rmi -f "$image" 2>/dev/null; then
            echo "Образ $image успешно удален"
        else
            echo "Не удалось удалить образ $image (возможно, используется контейнером)"
        fi
    else
        echo "Образ $image не найден"
    fi
done

# Очистка build cache (опционально, раскомментируйте при необходимости)
# echo "Очистка build cache..."
# docker builder prune -f

echo ""
echo "Готово! Теперь можно запустить: docker compose build"

