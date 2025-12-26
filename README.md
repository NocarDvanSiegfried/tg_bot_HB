tg_bot_HB — Telegram-приложение для работы с днями рождения и праздниками, реализованное по архитектуре Telegram Bot + Mini App.

Система разделена на отдельные компоненты с чёткими зонами ответственности.

Общая схема работы
User
  ↓
Telegram Bot (/start)
  ↓
Open Mini App
  ↓
Telegram Mini App (Web)
  ↓
Backend API
  ↓
PostgreSQL

Роль Telegram Bot

Telegram Bot используется исключительно как точка входа.

Последовательность работы:

Пользователь открывает чат с ботом

Выполняет команду /start

Бот возвращает кнопку открытия Mini App

Дальнейшее взаимодействие происходит через Mini App

Бот не содержит бизнес-логики и не работает с данными напрямую.

Mini App (Web-приложение)

Mini App является основным пользовательским интерфейсом.

Функции Mini App:

загрузка пользовательских данных

отображение календаря

добавление и редактирование дат

отправка запросов в backend API

Mini App работает внутри Telegram WebView и получает контекст пользователя через Telegram WebApp API.

Backend API

Backend отвечает за серверную логику и хранение данных.

Основные задачи:

обработка HTTP-запросов от Mini App

валидация входных данных

работа с базой данных

возврат данных в формате JSON

Backend не взаимодействует напрямую с Telegram Bot API.

База данных

В качестве основного хранилища используется PostgreSQL.

Хранятся:

даты событий

тип события

привязка к пользователю

служебные метаданные

Запуск и взаимодействие сервисов

Проект разворачивается через Docker Compose.

Последовательность запуска:

PostgreSQL

Backend API

Frontend (Mini App)

Nginx (reverse proxy)

Telegram Bot

Все сервисы изолированы и взаимодействуют через внутреннюю сеть Docker.

Структура проекта
tg_bot_HB/
├── bot/            # Telegram Bot (launcher)
├── frontend/       # Mini App (Web UI)
├── backend/        # Backend API
├── nginx/          # Reverse proxy
├── docker-compose.yml
└── .env.example

Поток данных

Пользователь открывает Mini App

Frontend отправляет запросы в Backend API

Backend читает или изменяет данные в PostgreSQL

Backend возвращает данные Frontend

Интерфейс обновляется

Telegram Bot в потоке данных не участвует.

Архитектурная модель

Telegram Bot — launcher

Mini App — application

Backend — бизнес-логика

PostgreSQL — хранилище данных

Такое разделение упрощает поддержку и развитие проекта.
