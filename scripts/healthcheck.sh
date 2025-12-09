#!/bin/bash

# Healthcheck скрипт для проверки работы бота и API

set -e

echo "=== Health Check для Telegram Birthday Calendar ==="
echo ""

# Цвета для вывода
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Проверка Docker контейнеров
echo "1. Проверка Docker контейнеров..."
if command -v docker &> /dev/null; then
    if docker compose ps | grep -q "Up"; then
        echo -e "${GREEN}✓${NC} Docker контейнеры запущены"
        docker compose ps
    else
        echo -e "${RED}✗${NC} Docker контейнеры не запущены"
        echo "   Запустите: docker compose up -d"
    fi
else
    echo -e "${YELLOW}⚠${NC} Docker не установлен, пропускаем проверку контейнеров"
fi

echo ""

# Проверка API
echo "2. Проверка API (http://localhost:8000)..."
if curl -s -f http://localhost:8000/ > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} API доступен"
    API_RESPONSE=$(curl -s http://localhost:8000/)
    echo "   Ответ: $API_RESPONSE"
else
    echo -e "${RED}✗${NC} API недоступен"
    echo "   Проверьте, что backend запущен и слушает порт 8000"
fi

echo ""

# Проверка календаря API
echo "3. Проверка календаря API..."
TODAY=$(date +%Y-%m-%d)
if curl -s -f "http://localhost:8000/api/calendar/$TODAY" > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} Календарь API работает"
else
    echo -e "${YELLOW}⚠${NC} Календарь API недоступен (может требовать аутентификации)"
fi

echo ""

# Проверка базы данных
echo "4. Проверка подключения к базе данных..."
if command -v docker &> /dev/null && docker compose ps | grep -q "postgres.*Up"; then
    if docker compose exec -T postgres pg_isready -U postgres > /dev/null 2>&1; then
        echo -e "${GREEN}✓${NC} PostgreSQL доступен"
    else
        echo -e "${RED}✗${NC} PostgreSQL недоступен"
    fi
else
    echo -e "${YELLOW}⚠${NC} PostgreSQL контейнер не запущен или Docker недоступен"
fi

echo ""

# Проверка Frontend
echo "5. Проверка Frontend (http://localhost:3000)..."
if curl -s -f http://localhost:3000/ > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} Frontend доступен"
else
    echo -e "${YELLOW}⚠${NC} Frontend недоступен (может быть в процессе запуска)"
fi

echo ""

# Проверка логов на ошибки
echo "6. Проверка последних ошибок в логах..."
if command -v docker &> /dev/null; then
    ERROR_COUNT=$(docker compose logs backend --tail 50 2>&1 | grep -i "error\|exception\|failed" | wc -l)
    if [ "$ERROR_COUNT" -gt 0 ]; then
        echo -e "${YELLOW}⚠${NC} Найдено $ERROR_COUNT потенциальных ошибок в логах backend"
        echo "   Проверьте: docker compose logs backend"
    else
        echo -e "${GREEN}✓${NC} Ошибок в последних логах не найдено"
    fi
else
    echo -e "${YELLOW}⚠${NC} Docker недоступен, пропускаем проверку логов"
fi

echo ""
echo "=== Проверка завершена ==="
echo ""
echo "Для детальной диагностики используйте:"
echo "  docker compose logs backend"
echo "  docker compose logs postgres"
echo "  curl http://localhost:8000/docs"

