# Telegram Birthday Calendar Mini App

[![CI](https://github.com/${{ github.repository_owner }}/${{ github.event.repository.name }}/actions/workflows/ci.yml/badge.svg)](https://github.com/${{ github.repository_owner }}/${{ github.event.repository.name }}/actions/workflows/ci.yml)
[![Tests](https://github.com/${{ github.repository_owner }}/${{ github.event.repository.name }}/actions/workflows/test.yml/badge.svg)](https://github.com/${{ github.repository_owner }}/${{ github.event.repository.name }}/actions/workflows/test.yml)
[![Build](https://github.com/${{ github.repository_owner }}/${{ github.event.repository.name }}/actions/workflows/build.yml/badge.svg)](https://github.com/${{ github.repository_owner }}/${{ github.event.repository.name }}/actions/workflows/build.yml)

**Примечание:** Замените `${{ github.repository_owner }}` и `${{ github.event.repository.name }}` на реальные значения вашего репозитория в формате: `https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg`

Telegram Mini App для управления календарем дней рождений с панелью управления, генерацией поздравлений через OpenRouter и уведомлениями.

## Структура проекта

- `backend/` - FastAPI + aiogram бэкенд
- `frontend/` - React + TypeScript фронтенд
- `docker-compose.yml` - Docker Compose конфигурация

## Технологический стек

**Backend:**
- FastAPI (web API)
- aiogram 3.x (Telegram bot)
- SQLAlchemy (ORM)
- Alembic (миграции)
- PostgreSQL
- OpenRouter API (DeepSeek)
- Pillow (генерация открыток)
- APScheduler (уведомления)

**Frontend:**
- React 18
- TypeScript
- Vite
- @twa-dev/sdk (Telegram Web App SDK)
- date-fns

## Установка и запуск

### Вариант 1: Запуск через Docker Compose (рекомендуется)

1. Скопируйте `env.example` в `.env` и заполните переменные окружения:
   ```bash
   cp env.example .env
   ```

2. Если возникают проблемы с загрузкой Docker образов (TLS handshake timeout):
   
   **Шаг 1: Проверьте наличие образов локально**
   ```bash
   # Windows PowerShell
   .\scripts\check-docker-images.ps1
   
   # Linux/macOS
   ./scripts/check-docker-images.sh
   ```
   
   **Шаг 2: Загрузите недостающие образы**
   ```bash
   # Вариант 1: Используйте универсальный скрипт (рекомендуется)
   # Автоматически пробует альтернативные теги при сбоях
   # Windows PowerShell:
   .\scripts\download-all-images.ps1
   
   # Linux/macOS:
   ./scripts/download-all-images.sh
   
   # Вариант 2: Загрузить только образ PostgreSQL
   # Windows PowerShell:
   .\scripts\download-postgres-image.ps1
   
   # Linux/macOS:
   ./scripts/download-postgres-image.sh
   
   # Вариант 3: Загрузить образы вручную:
   docker pull postgres:15
   docker pull node:20-alpine
   docker pull python:3.11-slim
   ```
   
   **Шаг 3: Запустите сборку**
   ```bash
   # Если образы уже загружены, используйте --pull=never для ускорения:
   docker compose build --pull=never
   docker compose up
   
   # Или обычная сборка:
   docker compose up --build
   ```
   
   **Альтернативные решения:**
   - Использовать локальную установку (см. "Вариант 2: Локальный запуск")
   - Настроить прокси для Docker (см. раздел Troubleshooting)
   - Использовать docker-compose.override.yml (см. docker-compose.override.yml.example)
   
   Подробнее о решении проблемы см. раздел [Troubleshooting](#troubleshooting)

3. Запустите через Docker Compose:
   ```bash
   docker compose up --build
   ```

4. Примените миграции:
   ```bash
   docker compose exec backend alembic upgrade head
   ```

### Вариант 2: Локальный запуск без Docker (для разработки)

#### Требования:
- Python 3.11+
- Node.js 20+
- PostgreSQL 15+ (локально установленный)

#### Шаги:

1. **Установите PostgreSQL локально:**
   - Windows: [PostgreSQL для Windows](https://www.postgresql.org/download/windows/)
   - macOS: `brew install postgresql@15`
   - Linux: `sudo apt-get install postgresql-15`

2. **Создайте базу данных:**
   ```bash
   createdb birthday_calendar_db
   # или через psql:
   psql -U postgres -c "CREATE DATABASE birthday_calendar_db;"
   ```

3. **Настройте переменные окружения:**
   ```bash
   # Скопируйте env.example в .env
   cp env.example .env
   
   # Отредактируйте .env, установите:
   DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/birthday_calendar_db
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   OPENROUTER_API_KEY=your_api_key_here
   ```

4. **Запустите Backend:**
   ```bash
   cd backend
   pip install -r requirements.txt
   alembic upgrade head
   python main.py
   ```

5. **Запустите Frontend (в отдельном терминале):**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

Теперь:
- Backend доступен на `http://localhost:8000`
- Frontend доступен на `http://localhost:3000`
- Telegram бот работает через polling

## Переменные окружения

- `TELEGRAM_BOT_TOKEN` - токен Telegram бота
- `OPENROUTER_API_KEY` - API ключ OpenRouter
- `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` - настройки БД
- `DATABASE_URL` - полный URL подключения к БД
- `VITE_API_URL` - URL API для фронтенда

## Функционал

### Для всех пользователей:
- Просмотр календаря
- Выбор даты и просмотр информации
- Уведомления о днях рождениях

### Для пользователей с доступом к /panel:
- Управление днями рождениями
- Управление ответственными лицами
- Генерация поздравлений через DeepSeek
- Создание открыток

## API Endpoints

- `GET /api/calendar/{date}` - данные календаря на дату
- `GET /api/panel/birthdays` - список ДР
- `POST /api/panel/birthdays` - создать ДР
- `PUT /api/panel/birthdays/{id}` - обновить ДР
- `DELETE /api/panel/birthdays/{id}` - удалить ДР
- И другие endpoints для управления данными

## Уведомления

Уведомления отправляются автоматически:
- Ежедневно в 09:00 UTC+9 - о ДР сегодня
- Каждый понедельник в 09:00 UTC+9 - о ДР на неделе
- 1 числа каждого месяца в 09:00 UTC+9 - о ДР в месяце

## CI/CD

Проект использует GitHub Actions для автоматизации:

- **CI** - автоматическая проверка кода при каждом push и PR
- **Tests** - расширенное тестирование с проверкой покрытия кода
- **Build** - автоматическая сборка и публикация Docker образов
- **Deploy** - автоматический деплой на staging/production

Подробнее о настройке секретов см. [.github/GITHUB_SECRETS.md](.github/GITHUB_SECRETS.md)

## Проверка работы бота

### 1. Проверка через Telegram

1. Найдите вашего бота в Telegram по username (указанному при создании бота)
2. Отправьте команду `/start`
3. Бот должен ответить приветственным сообщением с главным меню

### 2. Проверка логов Docker

```bash
# Логи всех сервисов
docker compose logs

# Логи только бэкенда (бота)
docker compose logs backend

# Логи в реальном времени
docker compose logs -f backend

# Логи базы данных
docker compose logs postgres
```

**Что искать в логах:**
- `Bot started` или `Polling started` - бот успешно запущен
- `Application startup complete` - FastAPI сервер запущен
- Ошибки подключения к БД или Telegram API

### 3. Проверка API

```bash
# Проверка корневого endpoint
curl http://localhost:8000/

# Проверка health check (если есть)
curl http://localhost:8000/health

# Проверка календаря
curl http://localhost:8000/api/calendar/2024-12-08

# Проверка через браузер
# Откройте http://localhost:8000/docs для Swagger UI
```

### 4. Проверка статуса контейнеров

```bash
# Статус всех сервисов
docker compose ps

# Детальная информация
docker compose top

# Проверка здоровья сервисов
docker compose ps --format "table {{.Name}}\t{{.Status}}\t{{.Ports}}"
```

### 5. Проверка подключения к базе данных

```bash
# Из контейнера backend
docker compose exec backend python -c "from src.infrastructure.database.database_factory import get_database; import asyncio; db = get_database(); asyncio.run(db.create_tables()); print('Database connection OK')"

# Или через psql
docker compose exec postgres psql -U postgres -d birthday_calendar_db -c "SELECT version();"
```

### 6. Типичные проблемы и решения

**Проблема: Бот не отвечает**
- Проверьте `TELEGRAM_BOT_TOKEN` в `.env`
- Проверьте логи: `docker compose logs backend`
- Убедитесь, что бот не заблокирован в Telegram

**Проблема: Ошибка подключения к БД**
- Проверьте, что PostgreSQL контейнер запущен: `docker compose ps`
- Проверьте `DATABASE_URL` в `.env`
- Проверьте логи БД: `docker compose logs postgres`

**Проблема: API не отвечает**
- Проверьте, что backend контейнер запущен
- Проверьте порт 8000: `curl http://localhost:8000/`
- Проверьте логи: `docker compose logs backend`

**Проблема: Frontend не подключается к API**
- Проверьте `VITE_API_URL` в `.env` (должен быть `http://localhost:8000`)
- Проверьте CORS настройки в `backend/src/presentation/web/app.py`
- Проверьте консоль браузера на ошибки

## Оптимизация Docker сборки

### Результаты оптимизации

Проект оптимизирован для быстрой сборки:

- ✅ **BuildKit оптимизации**: включены inline cache и параллельная сборка
- ✅ **Build context уменьшен**: исключены ненужные файлы через .dockerignore
- ✅ **Production зависимости**: только необходимые пакеты (13 вместо 19 для Python)
- ✅ **Multi-stage build**: оптимизированная структура для frontend
- ✅ **BuildKit cache mounts**: ускорение повторных сборок на 30-50%
  - Apt package cache для backend
  - Pip cache для Python зависимостей
  - NPM cache для frontend зависимостей
- ✅ **Layer optimization**: объединение RUN команд для уменьшения слоев
- ✅ **Cache from previous builds**: использование предыдущих образов как cache source

### Использование оптимизаций

**Для максимальной скорости повторных сборок:**

```bash
# BuildKit включен по умолчанию в Docker Desktop
# Для явного включения:
export DOCKER_BUILDKIT=1  # Linux/macOS
$env:DOCKER_BUILDKIT=1    # Windows PowerShell

# Параллельная сборка всех сервисов (рекомендуется)
docker compose build --parallel

# Сборка с использованием кеша
docker compose build

# Без загрузки образов из сети (если уже есть локально)
docker compose build --pull=never

# Сборка конкретного сервиса
docker compose build backend
docker compose build frontend
```

**Ожидаемое время сборки:**
- Первая сборка: ~120-150 секунд (с оптимизациями)
- Повторные сборки (с кешем): ~15-30 секунд
- Инкрементальные сборки (только изменения кода): ~5-10 секунд

### Конфигурация оптимизаций

Оптимизации настроены в `docker-compose.yml`:

- **BuildKit inline cache**: автоматически включен через `BUILDKIT_INLINE_CACHE=1`
- **Cache from**: предыдущие образы используются как источник кеша
- **Parallel builds**: сервисы собираются параллельно при использовании `--parallel`
- **Cache mounts**: автоматически используются для apt, pip и npm

### Проверка эффективности кеша

```bash
# Проверка использования кеша при сборке
docker compose build --progress=plain

# Просмотр размера образов
docker images | grep tg_bot_hb

# Очистка кеша (если нужно)
docker builder prune
```

### Проверка готовности к сборке

Перед сборкой проверьте наличие всех необходимых образов:

```bash
# Windows PowerShell
.\scripts\check-docker-images.ps1

# Linux/macOS
./scripts/check-docker-images.sh
```

## Troubleshooting

### Проблема: TLS handshake timeout при загрузке образа PostgreSQL

**Ошибка**: `failed to resolve reference "docker.io/library/postgres:15": TLS handshake timeout`

**Причины**:
- Проблемы с интернет-соединением
- Блокировка или ограничение доступа к Docker Hub
- Проблемы с DNS
- Настройки прокси/firewall
- Временная недоступность Docker Hub

**Решения** (в порядке приоритета):

#### Решение 1: Использовать скрипт для загрузки образа

Скрипт автоматически пытается загрузить образ из нескольких источников:

```bash
# Linux/macOS
./scripts/download-postgres-image.sh

# Windows PowerShell
.\scripts\download-postgres-image.ps1
```

#### Решение 2: Загрузить образ вручную

```bash
# Попытка 1: Стандартная загрузка
docker pull postgres:15

# Попытка 2: Альтернативный тег (меньший размер)
docker pull postgres:15-alpine

# Попытка 3: С указанием платформы
docker pull postgres:15 --platform linux/amd64

# Попытка 4: Через альтернативный registry
docker pull registry-1.docker.io/library/postgres:15
```

#### Решение 3: Настроить прокси для Docker

Если вы используете прокси, настройте Docker daemon:

1. Создайте/отредактируйте файл `~/.docker/config.json` (Linux/macOS) или `%USERPROFILE%\.docker\config.json` (Windows):

```json
{
  "proxies": {
    "default": {
      "httpProxy": "http://proxy.example.com:8080",
      "httpsProxy": "http://proxy.example.com:8080",
      "noProxy": "localhost,127.0.0.1"
    }
  }
}
```

2. Или настройте через переменные окружения:

```bash
# Linux/macOS
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080
export NO_PROXY=localhost,127.0.0.1

# Windows PowerShell
$env:HTTP_PROXY="http://proxy.example.com:8080"
$env:HTTPS_PROXY="http://proxy.example.com:8080"
$env:NO_PROXY="localhost,127.0.0.1"
```

3. Перезапустите Docker daemon

#### Решение 4: Изменить DNS сервер

```bash
# Linux: отредактируйте /etc/docker/daemon.json
{
  "dns": ["8.8.8.8", "8.8.4.4"]
}

# Windows: измените DNS в настройках сети
# Используйте публичные DNS: 8.8.8.8, 1.1.1.1
```

#### Решение 5: Использовать локальную установку PostgreSQL

Если Docker недоступен, используйте локальную установку PostgreSQL (см. раздел "Вариант 2: Локальный запуск без Docker" выше).

#### Решение 6: Использовать VPN

Если Docker Hub заблокирован в вашем регионе, используйте VPN для обхода блокировки.

#### Решение 7: Использовать альтернативный образ

В `docker-compose.yml` можно заменить образ на альтернативный:

```yaml
postgres:
  # Вместо postgres:15 используйте:
  image: postgres:15-alpine  # Меньший размер
  # или
  image: postgres:latest    # Последняя версия
```

#### Решение 8: Проверить настройки firewall

Убедитесь, что firewall не блокирует соединения с Docker Hub:
- Разрешите исходящие соединения на порты 80, 443
- Разрешите доступ к `docker.io` и `registry-1.docker.io`

### Дополнительная диагностика

```bash
# Проверка подключения к Docker Hub
curl -I https://registry-1.docker.io/v2/

# Проверка DNS
nslookup registry-1.docker.io

# Проверка сетевых настроек Docker
docker info | grep -i proxy
docker info | grep -i dns

# Очистка кэша Docker
docker system prune -a
```

## Разработка

### Запуск тестов

```bash
# Backend тесты
cd backend
pytest tests/ -v

# Frontend проверка типов
cd frontend
npm run build
```

### Линтинг и форматирование

```bash
# Backend
cd backend
ruff check src/
black --check src/

# Frontend
cd frontend
npm run lint
npm run format:check
```

### Проверка работоспособности

Используйте healthcheck скрипты для быстрой проверки всех сервисов:

```bash
# Linux/macOS
./scripts/healthcheck.sh

# Windows PowerShell
.\scripts\healthcheck.ps1
```

Скрипты проверяют:
- Статус Docker контейнеров
- Доступность API (порт 8000)
- Доступность Frontend (порт 3000)
- Подключение к базе данных
- Наличие ошибок в логах

