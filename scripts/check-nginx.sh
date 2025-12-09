#!/bin/bash

# Скрипт проверки конфигурации Nginx для Telegram Mini App
# Проверяет синтаксис конфигурации и доступность портов

set -e

echo "🔍 Проверка конфигурации Nginx для Telegram Mini App"
echo ""

# Цвета для вывода
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Проверка прав доступа
if [ "$EUID" -ne 0 ]; then
    echo -e "${YELLOW}⚠️  Для полной проверки требуются права root (sudo)${NC}"
    echo "Некоторые проверки могут быть пропущены."
    echo ""
    SUDO=""
else
    SUDO="sudo"
fi

# 1. Проверка синтаксиса конфигурации Nginx
echo "1️⃣  Проверка синтаксиса конфигурации Nginx..."
if $SUDO nginx -t 2>&1; then
    echo -e "${GREEN}✅ Синтаксис конфигурации Nginx корректен${NC}"
else
    echo -e "${RED}❌ Ошибка в конфигурации Nginx${NC}"
    exit 1
fi
echo ""

# 2. Проверка доступности портов
echo "2️⃣  Проверка доступности портов..."

check_port() {
    local port=$1
    local service=$2
    
    if command -v netstat >/dev/null 2>&1; then
        if $SUDO netstat -tlnp 2>/dev/null | grep -q ":$port "; then
            echo -e "${GREEN}✅ Порт $port открыт ($service)${NC}"
            return 0
        fi
    elif command -v ss >/dev/null 2>&1; then
        if $SUDO ss -tlnp 2>/dev/null | grep -q ":$port "; then
            echo -e "${GREEN}✅ Порт $port открыт ($service)${NC}"
            return 0
        fi
    elif command -v lsof >/dev/null 2>&1; then
        if $SUDO lsof -i :$port >/dev/null 2>&1; then
            echo -e "${GREEN}✅ Порт $port открыт ($service)${NC}"
            return 0
        fi
    fi
    
    echo -e "${YELLOW}⚠️  Порт $port не прослушивается ($service)${NC}"
    return 1
}

check_port 8001 "Backend (Nginx)"
check_port 3001 "Frontend (Nginx)"
echo ""

# 3. Проверка статуса Nginx
echo "3️⃣  Проверка статуса Nginx..."
if systemctl is-active --quiet nginx 2>/dev/null || service nginx status >/dev/null 2>&1; then
    echo -e "${GREEN}✅ Nginx запущен${NC}"
else
    echo -e "${RED}❌ Nginx не запущен${NC}"
    echo "Запустите Nginx: sudo systemctl start nginx"
fi
echo ""

# 4. Проверка конфигурационных файлов
echo "4️⃣  Проверка наличия конфигурационных файлов..."

check_file() {
    local file=$1
    if [ -f "$file" ]; then
        echo -e "${GREEN}✅ $file существует${NC}"
        return 0
    else
        echo -e "${YELLOW}⚠️  $file не найден${NC}"
        return 1
    fi
}

check_file "/etc/nginx/nginx.conf"
check_file "/etc/nginx/conf.d/backend.conf"
check_file "/etc/nginx/conf.d/frontend.conf"
echo ""

# 5. Проверка SSL сертификатов (если указаны в конфиге)
echo "5️⃣  Проверка SSL сертификатов..."

if [ -f "/etc/nginx/conf.d/backend.conf" ]; then
    cert_path=$(grep -E "^\s*ssl_certificate\s+" /etc/nginx/conf.d/backend.conf | head -1 | awk '{print $2}' | tr -d ';')
    if [ -n "$cert_path" ] && [ "$cert_path" != "/etc/nginx/ssl/cert.pem" ]; then
        if [ -f "$cert_path" ]; then
            echo -e "${GREEN}✅ SSL сертификат найден: $cert_path${NC}"
        else
            echo -e "${RED}❌ SSL сертификат не найден: $cert_path${NC}"
        fi
    else
        echo -e "${YELLOW}⚠️  Путь к SSL сертификату не указан или использует значение по умолчанию${NC}"
    fi
fi
echo ""

# 6. Проверка доступности backend и frontend на localhost
echo "6️⃣  Проверка доступности сервисов на localhost..."

check_localhost() {
    local port=$1
    local service=$2
    
    if curl -s -f "http://localhost:$port" >/dev/null 2>&1; then
        echo -e "${GREEN}✅ $service доступен на localhost:$port${NC}"
        return 0
    else
        echo -e "${YELLOW}⚠️  $service недоступен на localhost:$port${NC}"
        echo "   Убедитесь, что Docker контейнеры запущены: docker compose ps"
        return 1
    fi
}

check_localhost 8000 "Backend"
check_localhost 3000 "Frontend"
echo ""

# Итоговая сводка
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 Итоговая сводка:"
echo ""
echo "Для проверки доступности через Nginx выполните:"
echo "  curl https://your-domain.com:8001/  # Backend"
echo "  curl https://your-domain.com:3001/  # Frontend"
echo ""
echo "Для просмотра логов Nginx:"
echo "  sudo tail -f /var/log/nginx/backend_error.log"
echo "  sudo tail -f /var/log/nginx/frontend_error.log"
echo ""

