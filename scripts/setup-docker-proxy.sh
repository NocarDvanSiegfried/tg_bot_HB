#!/bin/bash

# Скрипт для настройки прокси для Docker daemon

set -e

echo "=== Настройка прокси для Docker ==="
echo ""

# Запрос данных прокси
read -p "HTTP прокси (например, http://proxy.example.com:8080): " HTTP_PROXY
read -p "HTTPS прокси (или Enter для использования HTTP прокси): " HTTPS_PROXY
read -p "Исключения для прокси (через запятую, например, localhost,127.0.0.1): " NO_PROXY

HTTPS_PROXY=${HTTPS_PROXY:-$HTTP_PROXY}
NO_PROXY=${NO_PROXY:-"localhost,127.0.0.1"}

# Определение пути к конфигурации Docker
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    DOCKER_CONFIG="/etc/docker/daemon.json"
    DOCKER_SERVICE="docker"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    DOCKER_CONFIG="$HOME/.docker/daemon.json"
    DOCKER_SERVICE="com.docker.dockerd"
else
    echo "Неизвестная ОС. Используйте ручную настройку."
    exit 1
fi

# Создание резервной копии
if [ -f "$DOCKER_CONFIG" ]; then
    cp "$DOCKER_CONFIG" "${DOCKER_CONFIG}.backup.$(date +%Y%m%d_%H%M%S)"
    echo "✓ Создана резервная копия: ${DOCKER_CONFIG}.backup"
fi

# Создание/обновление конфигурации
cat > "$DOCKER_CONFIG" <<EOF
{
  "proxies": {
    "default": {
      "httpProxy": "$HTTP_PROXY",
      "httpsProxy": "$HTTPS_PROXY",
      "noProxy": "$NO_PROXY"
    }
  }
}
EOF

echo ""
echo "✓ Конфигурация сохранена в: $DOCKER_CONFIG"
echo ""
echo "Для применения изменений перезапустите Docker:"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "  sudo systemctl restart docker"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "  Перезапустите Docker Desktop"
fi
echo ""
echo "Проверка настроек:"
echo "  docker info | grep -i proxy"

