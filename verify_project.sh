#!/bin/bash
# Скрипт для проверки проекта после исправлений

set -e  # Остановить при ошибке

echo "========================================="
echo "Проверка Проекта Telegram Birthday Bot"
echo "========================================="
echo ""

# Цвета для вывода
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Функция для проверки результата
check_result() {
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ $1${NC}"
        return 0
    else
        echo -e "${RED}❌ $1${NC}"
        return 1
    fi
}

# Счетчик ошибок
ERRORS=0

echo "1. Проверка Backend кода..."
cd backend

echo "   - Проверка синтаксиса Python..."
python -m py_compile src/infrastructure/database/models.py
check_result "Синтаксис models.py корректен" || ((ERRORS++))

python -m py_compile src/presentation/telegram/middleware/database_middleware.py
check_result "Синтаксис database_middleware.py корректен" || ((ERRORS++))

python -m py_compile src/infrastructure/database/repositories/panel_access_repository_impl.py
check_result "Синтаксис panel_access_repository_impl.py корректен" || ((ERRORS++))

echo ""
echo "2. Проверка миграций..."
if [ -f "migrations/versions/002_fix_user_id_bigint.py" ]; then
    check_result "Миграция 002_fix_user_id_bigint.py найдена"
    python -m py_compile migrations/versions/002_fix_user_id_bigint.py
    check_result "Синтаксис миграции корректен" || ((ERRORS++))
else
    echo -e "${RED}❌ Миграция 002_fix_user_id_bigint.py не найдена${NC}"
    ((ERRORS++))
fi

echo ""
echo "3. Проверка тестов..."
if [ -f "tests/infrastructure/test_panel_access_repository_bigint.py" ]; then
    check_result "Тест test_panel_access_repository_bigint.py найден"
else
    echo -e "${RED}❌ Тест test_panel_access_repository_bigint.py не найден${NC}"
    ((ERRORS++))
fi

if [ -f "tests/presentation/telegram/middleware/test_database_middleware.py" ]; then
    check_result "Тест test_database_middleware.py найден"
else
    echo -e "${RED}❌ Тест test_database_middleware.py не найден${NC}"
    ((ERRORS++))
fi

echo ""
echo "4. Применение миграции..."
alembic upgrade head
check_result "Миграция применена успешно" || ((ERRORS++))

echo ""
echo "5. Запуск тестов..."
pytest tests/infrastructure/test_panel_access_repository_bigint.py -v
check_result "Тесты для BigInteger прошли" || ((ERRORS++))

pytest tests/presentation/telegram/middleware/test_database_middleware.py -v
check_result "Тесты для middleware прошли" || ((ERRORS++))

pytest tests/infrastructure/test_panel_access_repository.py -v
check_result "Обновленные тесты repository прошли" || ((ERRORS++))

pytest tests/presentation/telegram/handlers/test_panel_handler.py -v
check_result "Обновленные тесты handler прошли" || ((ERRORS++))

cd ..

echo ""
echo "6. Проверка Frontend..."
cd frontend

echo "   - Проверка package.json..."
if [ -f "package.json" ]; then
    check_result "package.json найден"
else
    echo -e "${RED}❌ package.json не найден${NC}"
    ((ERRORS++))
fi

echo "   - Проверка зависимостей..."
if [ -d "node_modules" ]; then
    check_result "node_modules установлены"
else
    echo -e "${YELLOW}⚠️  node_modules не найдены, запустите: npm install${NC}"
fi

echo "   - Проверка TypeScript..."
if command -v npx &> /dev/null; then
    npx tsc --noEmit
    check_result "TypeScript компиляция прошла успешно" || ((ERRORS++))
else
    echo -e "${YELLOW}⚠️  npx не найден, пропускаем проверку TypeScript${NC}"
fi

cd ..

echo ""
echo "7. Проверка Docker конфигурации..."
if [ -f "docker-compose.yml" ]; then
    check_result "docker-compose.yml найден"
    
    # Проверка синтаксиса docker-compose.yml
    docker compose config > /dev/null 2>&1
    check_result "docker-compose.yml синтаксис корректен" || ((ERRORS++))
else
    echo -e "${RED}❌ docker-compose.yml не найден${NC}"
    ((ERRORS++))
fi

echo ""
echo "========================================="
if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}✅ Все проверки пройдены успешно!${NC}"
    echo ""
    echo "Следующие шаги:"
    echo "1. Запустите: docker compose build"
    echo "2. Запустите: docker compose up"
    echo "3. Проверьте работу бота в Telegram"
    exit 0
else
    echo -e "${RED}❌ Найдено ошибок: $ERRORS${NC}"
    echo ""
    echo "Исправьте ошибки и запустите проверку снова."
    exit 1
fi

