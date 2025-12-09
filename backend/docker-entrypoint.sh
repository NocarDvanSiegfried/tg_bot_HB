#!/bin/bash
set -e

# Entrypoint скрипт для создания пользователя appuser при запуске контейнера
# Это необходимо, когда используется volume монтирование, которое может перезаписать пользователя

# Проверяем, существует ли пользователь appuser
if ! id -u appuser > /dev/null 2>&1; then
    echo "Creating appuser (UID 1000)..."
    # Создаем пользователя с UID 1000
    useradd -m -u 1000 appuser || true
fi

# Устанавливаем права на /app для appuser
# Это важно при использовании volume монтирования
if [ -d /app ]; then
    chown -R appuser:appuser /app 2>/dev/null || true
fi

# Переключаемся на appuser и выполняем переданную команду
# Используем su для переключения пользователя
# Важно: сохраняем environment variables при переключении пользователя
if [ "$(id -u)" = "0" ]; then
    # Если запущены от root, переключаемся на appuser
    # Сохраняем все environment variables
    # Используем su без - чтобы сохранить environment
    # Передаем все переменные окружения явно
    export $(printenv | grep -v '^_' | xargs)
    exec su appuser -c "cd /app && exec $*"
else
    # Если уже не root, просто выполняем команду
    exec "$@"
fi

