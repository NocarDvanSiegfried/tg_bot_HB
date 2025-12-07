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

1. Скопируйте `.env.example` в `.env` и заполните переменные окружения:
   ```bash
   cp .env.example .env
   ```

2. Запустите через Docker Compose:
   ```bash
   docker compose up -d
   ```

3. Примените миграции:
   ```bash
   docker compose exec backend alembic upgrade head
   ```

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

