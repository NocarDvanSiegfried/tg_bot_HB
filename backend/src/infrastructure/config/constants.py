"""Константы для конфигурации приложения."""

# Placeholder значения для проверки конфигурации
# Используется для определения, настроен ли URL или используется значение по умолчанию
WEBAPP_URL_PLACEHOLDER = "https://your-domain.com"

# Telegram WebApp origins для CORS
# Эти origins необходимы для работы Mini App в веб-версии Telegram
TELEGRAM_ORIGINS = [
    "https://web.telegram.org",
    "https://telegram.org",
    "https://webk.telegram.org",  # Альтернативный домен Telegram Web
]
