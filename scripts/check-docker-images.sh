#!/bin/bash
# Скрипт для проверки наличия всех необходимых Docker образов локально
# Использование: ./scripts/check-docker-images.sh

set -e

# Список всех необходимых образов
REQUIRED_IMAGES=(
    "postgres:15"
    "node:20-alpine"
    "python:3.11-slim"
)

echo "=== Проверка наличия Docker образов ==="
echo ""

# Функция для проверки наличия образа локально
test_local_image() {
    local image=$1
    if docker images --format "{{.Repository}}:{{.Tag}}" 2>/dev/null | grep -q "^${image}$"; then
        return 0
    fi
    return 1
}

# Функция для получения информации об образе
get_image_info() {
    local image=$1
    local info=$(docker images --format "{{.Repository}}:{{.Tag}} {{.Size}}" 2>/dev/null | grep "^${image} ")
    if [ -n "$info" ]; then
        echo "$info"
        return 0
    fi
    return 1
}

# Проверка каждого образа
missing_images=()
found_images=()

for image in "${REQUIRED_IMAGES[@]}"; do
    if test_local_image "$image"; then
        info=$(get_image_info "$image")
        size=$(echo "$info" | awk '{print $2}')
        echo "✓ $image (размер: $size)"
        found_images+=("$image")
    else
        echo "✗ $image (отсутствует)"
        missing_images+=("$image")
    fi
done

# Итоговый отчет
echo ""
echo "=== Итоговый отчет ==="
echo "Найдено: ${#found_images[@]} из ${#REQUIRED_IMAGES[@]}"

if [ ${#missing_images[@]} -gt 0 ]; then
    echo ""
    echo "Отсутствующие образы:"
    for img in "${missing_images[@]}"; do
        echo "  - $img"
    done
    
    echo ""
    echo "Рекомендации:"
    echo "1. Загрузите недостающие образы:"
    echo "   ./scripts/download-all-images.sh"
    echo ""
    echo "2. Или загрузите вручную:"
    for img in "${missing_images[@]}"; do
        echo "   docker pull $img"
    done
    echo ""
    echo "3. После загрузки образов запустите сборку:"
    echo "   docker compose up --build"
    echo ""
    echo "4. Если образы уже есть, но скрипт их не находит, используйте:"
    echo "   docker compose build --pull=never"
    
    exit 1
else
    echo ""
    echo "✓ Все необходимые образы найдены локально!"
    echo ""
    echo "Можно запускать сборку:"
    echo "  docker compose up --build"
    echo ""
    echo "Или без загрузки образов:"
    echo "  docker compose build --pull=never"
    
    exit 0
fi

