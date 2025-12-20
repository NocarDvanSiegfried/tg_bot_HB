#!/bin/bash
# Скрипт для проверки доступных обновлений безопасности
# Использование: ./check_security_updates.sh [package_name]

set -e

IMAGE_NAME="python:3.11-slim-bookworm"
PACKAGE="${1:-}"

echo "=== Проверка обновлений безопасности для $IMAGE_NAME ==="
echo ""

if [ -n "$PACKAGE" ]; then
    echo "Проверка пакета: $PACKAGE"
    echo ""
    docker run --rm "$IMAGE_NAME" bash -c "
        apt-get update -qq > /dev/null 2>&1 && \
        apt-cache policy $PACKAGE | grep -E '^[a-z]|Installed|Candidate'
    "
else
    echo "Проверка критичных пакетов:"
    echo ""
    
    PACKAGES=(
        "libsqlite3-0"
        "zlib1g"
        "libpam-modules"
        "libpam-modules-bin"
        "libpam-runtime"
        "libpam0g"
        "util-linux"
        "gpgv"
        "libncursesw6"
        "libtinfo6"
        "ncurses-base"
        "ncurses-bin"
        "libgnutls30"
    )
    
    for pkg in "${PACKAGES[@]}"; do
        echo "--- $pkg ---"
        docker run --rm "$IMAGE_NAME" bash -c "
            apt-get update -qq > /dev/null 2>&1 && \
            apt-cache policy $pkg | grep -E 'Installed|Candidate' | head -2
        " || echo "Ошибка при проверке $pkg"
        echo ""
    done
fi

echo ""
echo "=== Проверка завершена ==="
echo ""
echo "Для проверки конкретного пакета используйте:"
echo "  ./check_security_updates.sh <package_name>"
echo ""
echo "Для проверки всех доступных обновлений используйте:"
echo "  docker run --rm $IMAGE_NAME bash -c 'apt-get update && apt list --upgradable'"

