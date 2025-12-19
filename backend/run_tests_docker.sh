#!/bin/bash
# Скрипт для запуска backend тестов в Docker контейнере
# Использование: ./run_tests_docker.sh [опции pytest]

# Цвета для вывода
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Аргументы pytest по умолчанию
PYTEST_ARGS=("-v" "--tb=short")

# Если переданы аргументы, используем их
if [ $# -gt 0 ]; then
    PYTEST_ARGS=("$@")
fi

echo -e "${GREEN}Запуск backend тестов в Docker контейнере...${NC}"
echo ""

# Проверяем, что Docker Compose запущен
if ! docker compose ps > /dev/null 2>&1; then
    echo -e "${RED}Ошибка: Docker Compose не запущен или не настроен${NC}"
    echo -e "${YELLOW}Запустите: docker compose up -d${NC}"
    exit 1
fi

# Проверяем, что backend контейнер запущен
if ! docker compose ps backend | grep -q "running"; then
    echo -e "${YELLOW}Backend контейнер не запущен. Запускаю...${NC}"
    docker compose up -d backend
    if [ $? -ne 0 ]; then
        echo -e "${RED}Ошибка: Не удалось запустить backend контейнер${NC}"
        exit 1
    fi
    echo -e "${YELLOW}Ожидание готовности backend контейнера...${NC}"
    sleep 5
fi

# Устанавливаем тестовые зависимости и запускаем тесты
# Используем docker compose run для создания временного контейнера с тестовыми зависимостями
echo -e "${CYAN}Установка тестовых зависимостей...${NC}"
echo -e "${CYAN}Запуск pytest с аргументами: ${PYTEST_ARGS[*]}${NC}"

# Запускаем тесты в новом контейнере с установкой тестовых зависимостей
# Перенаправляем вывод pip в /dev/null, чтобы не мешать выводу pytest
docker compose run --rm backend sh -c "pip install -q -r requirements.txt 2>&1 >/dev/null && python -m pytest tests/ ${PYTEST_ARGS[*]}"

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo ""
    echo -e "${GREEN}Все тесты прошли успешно!${NC}"
else
    echo ""
    echo -e "${RED}Некоторые тесты не прошли. Код выхода: $EXIT_CODE${NC}"
fi

exit $EXIT_CODE

