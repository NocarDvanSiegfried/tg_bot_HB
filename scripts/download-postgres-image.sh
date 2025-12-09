#!/bin/bash

# Скрипт для загрузки образа PostgreSQL с несколькими попытками и альтернативными источниками

set -e

IMAGE_NAME="postgres:15"
MAX_RETRIES=3
RETRY_DELAY=5

echo "=== Загрузка образа PostgreSQL ==="
echo "Образ: $IMAGE_NAME"
echo ""

# Функция для попытки загрузки образа
download_image() {
    local source=$1
    local image=$2
    
    echo "Попытка загрузки из: $source"
    
    if [ "$source" = "docker-hub" ]; then
        docker pull "$image"
    elif [ "$source" = "docker-hub-mirror" ]; then
        # Попытка через альтернативный endpoint
        DOCKER_REGISTRY_MIRROR="https://registry-1.docker.io" docker pull "$image"
    elif [ "$source" = "ghcr" ]; then
        # GitHub Container Registry (если доступен)
        docker pull "ghcr.io/postgres/postgres:15" || return 1
    fi
}

# Проверка, существует ли образ локально
check_local_image() {
    if docker images --format "{{.Repository}}:{{.Tag}}" | grep -q "^${IMAGE_NAME}$"; then
        echo "✓ Образ $IMAGE_NAME уже существует локально"
        return 0
    fi
    return 1
}

# Основная логика
main() {
    # Проверка наличия образа локально
    if check_local_image; then
        echo ""
        echo "Образ уже загружен. Можно использовать: docker compose up"
        exit 0
    fi
    
    # Список источников для попыток
    SOURCES=("docker-hub" "docker-hub-mirror")
    
    for source in "${SOURCES[@]}"; do
        for attempt in $(seq 1 $MAX_RETRIES); do
            echo ""
            echo "Попытка $attempt из $MAX_RETRIES для источника: $source"
            
            if download_image "$source" "$IMAGE_NAME" 2>&1; then
                echo ""
                echo "✓ Образ успешно загружен!"
                echo "Теперь можно запустить: docker compose up"
                exit 0
            else
                if [ $attempt -lt $MAX_RETRIES ]; then
                    echo "✗ Попытка не удалась. Повтор через $RETRY_DELAY секунд..."
                    sleep $RETRY_DELAY
                else
                    echo "✗ Все попытки для источника $source исчерпаны"
                fi
            fi
        done
    done
    
    echo ""
    echo "✗ Не удалось загрузить образ из всех источников"
    echo ""
    echo "Альтернативные решения:"
    echo "1. Проверьте интернет-соединение"
    echo "2. Настройте прокси для Docker (см. README.md)"
    echo "3. Используйте локальную установку PostgreSQL (см. README.md)"
    echo "4. Попробуйте другой тег: docker pull postgres:15-alpine"
    echo "5. Используйте VPN или другой DNS сервер"
    
    exit 1
}

main

