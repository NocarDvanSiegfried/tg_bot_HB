#!/bin/bash
# Универсальный скрипт для загрузки всех необходимых Docker образов для проекта
# Использование: ./scripts/download-all-images.sh
#
# Этот скрипт пытается загрузить все необходимые образы с несколькими попытками
# и альтернативными тегами, если основной тег недоступен.

set -e

# Список всех необходимых образов с альтернативными вариантами
declare -A IMAGES_CONFIG=(
    ["postgres:15"]="postgres:15-alpine postgres:15"
    ["node:20-alpine"]="node:20-alpine node:20 node:alpine"
    ["python:3.11-slim"]="python:3.11-slim python:3.11 python:slim"
)

MAX_RETRIES=5
INITIAL_RETRY_DELAY=3
MAX_RETRY_DELAY=30
DOCKER_HUB_TIMEOUT=15

echo "=== Загрузка всех необходимых Docker образов ==="
echo ""

# Функция для проверки доступности Docker Hub
test_docker_hub() {
    echo "Проверка доступности Docker Hub..."
    if curl -s --head --max-time $DOCKER_HUB_TIMEOUT "https://registry-1.docker.io/v2/" > /dev/null 2>&1; then
        echo "✓ Docker Hub доступен"
        return 0
    else
        echo "✗ Docker Hub недоступен"
        echo "  Попробуйте использовать VPN или настроить прокси"
        return 1
    fi
}

# Функция для попытки загрузки образа с экспоненциальной задержкой
download_image() {
    local image=$1
    echo "  Загрузка: $image"
    
    local attempt=1
    while [ $attempt -le $MAX_RETRIES ]; do
        echo "    Попытка $attempt из $MAX_RETRIES..."
        
        # Увеличиваем таймаут для Docker pull при повторных попытках
        local pull_timeout=$((DOCKER_HUB_TIMEOUT * attempt))
        
        if timeout $pull_timeout docker pull "$image" 2>/dev/null; then
            echo "    ✓ Образ $image успешно загружен"
            return 0
        else
            local exit_code=$?
            if [ $exit_code -eq 124 ]; then
                echo "    ✗ Таймаут при загрузке (превышен лимит $pull_timeout секунд)"
            else
                echo "    ✗ Попытка не удалась (код ошибки: $exit_code)"
            fi
        fi
        
        if [ $attempt -lt $MAX_RETRIES ]; then
            # Экспоненциальная задержка: 3, 6, 12, 24, 30 секунд
            local delay=$((INITIAL_RETRY_DELAY * (2 ** (attempt - 1))))
            if [ $delay -gt $MAX_RETRY_DELAY ]; then
                delay=$MAX_RETRY_DELAY
            fi
            echo "    Повтор через $delay секунд..."
            sleep $delay
        fi
        
        attempt=$((attempt + 1))
    done
    
    echo "    ✗ Не удалось загрузить образ $image после $MAX_RETRIES попыток"
    return 1
}

# Функция для проверки наличия образа локально
test_local_image() {
    local image=$1
    if docker images --format "{{.Repository}}:{{.Tag}}" 2>/dev/null | grep -q "^${image}$"; then
        return 0
    fi
    return 1
}

# Функция для загрузки образа с альтернативами
download_image_with_alternatives() {
    local primary_image=$1
    local alternatives=$2
    
    echo ""
    echo "Образ: $primary_image"
    
    # Проверяем, существует ли основной образ локально
    if test_local_image "$primary_image"; then
        echo "  ✓ Образ $primary_image уже существует локально"
        return 0
    fi
    
    # Пробуем загрузить основной образ
    if download_image "$primary_image"; then
        return 0
    fi
    
    # Если основной образ не загрузился, пробуем альтернативы
    if [ -n "$alternatives" ]; then
        echo "  Пробуем альтернативные варианты..."
        for alt in $alternatives; do
            if [ "$alt" = "$primary_image" ]; then
                continue  # Пропускаем основной образ
            fi
            
            if test_local_image "$alt"; then
                echo "  ✓ Альтернативный образ $alt уже существует локально"
                echo "  ⚠ ВНИМАНИЕ: Используется альтернативный образ $alt вместо $primary_image"
                echo "    Обновите Dockerfile, если хотите использовать этот образ постоянно"
                return 0
            fi
            
            if download_image "$alt"; then
                echo "  ⚠ ВНИМАНИЕ: Загружен альтернативный образ $alt вместо $primary_image"
                echo "    Обновите Dockerfile, если хотите использовать этот образ постоянно"
                return 0
            fi
        done
    fi
    
    return 1
}

# Основная логика
if ! test_docker_hub; then
    echo ""
    echo "⚠ Docker Hub недоступен, но попробуем загрузить образы из локального кеша"
fi

failed_images=()
success_count=0
total_images=${#IMAGES_CONFIG[@]}

for primary_image in "${!IMAGES_CONFIG[@]}"; do
    alternatives="${IMAGES_CONFIG[$primary_image]}"
    
    if download_image_with_alternatives "$primary_image" "$alternatives"; then
        success_count=$((success_count + 1))
    else
        failed_images+=("$primary_image")
    fi
done

# Итоговый отчет
echo ""
echo "=== Итоговый отчет ==="
echo "Успешно загружено: $success_count из $total_images"

if [ ${#failed_images[@]} -gt 0 ]; then
    echo ""
    echo "✗ Не удалось загрузить следующие образы:"
    for img in "${failed_images[@]}"; do
        echo "  - $img"
    done
    
    echo ""
    echo "Альтернативные решения:"
    echo "1. Проверьте интернет-соединение"
    echo "2. Настройте прокси для Docker: ./scripts/setup-docker-proxy.sh"
    echo "3. Используйте VPN или другой DNS сервер"
    echo "4. Попробуйте загрузить образы вручную:"
    for img in "${failed_images[@]}"; do
        echo "   docker pull $img"
    done
    echo "5. Используйте локальную разработку без Docker (см. README.md)"
    echo "6. Используйте docker compose build --pull=never (если образы уже есть локально)"
    
    exit 1
else
    echo ""
    echo "✓ Все образы успешно загружены!"
    echo "Теперь можно запустить: docker compose up --build"
    exit 0
fi
