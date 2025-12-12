import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from src.infrastructure.config.constants import TELEGRAM_ORIGINS
from src.presentation.web.routes.api import router

# Инициализация rate limiter
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="Telegram Birthday Calendar API")

# Подключение rate limiter к приложению
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS для Telegram Mini App
# Определяем окружение (development или production)
is_production = os.getenv("ENVIRONMENT", "development").lower() == "production"

# Получаем разрешенные origins из переменной окружения
allowed_origins_env = os.getenv("ALLOWED_ORIGINS", "")

if is_production:
    # В production используем только конкретные домены
    if not allowed_origins_env:
        # Если не указано, используем только Telegram origins
        allowed_origins = TELEGRAM_ORIGINS.copy()
    elif "," in allowed_origins_env:
        # Если указано несколько доменов через запятую
        allowed_origins = [origin.strip() for origin in allowed_origins_env.split(",")]
        # Добавляем Telegram origins, если их еще нет
        for tg_origin in TELEGRAM_ORIGINS:
            if tg_origin not in allowed_origins:
                allowed_origins.append(tg_origin)
    else:
        # Один домен
        allowed_origins = [allowed_origins_env.strip()]
        # Добавляем Telegram origins
        allowed_origins.extend(TELEGRAM_ORIGINS)
else:
    # В development разрешаем все для удобства разработки
    if allowed_origins_env and allowed_origins_env != "*":
        # Если указаны конкретные домены, используем их
        if "," in allowed_origins_env:
            allowed_origins = [origin.strip() for origin in allowed_origins_env.split(",")]
        else:
            allowed_origins = [allowed_origins_env.strip()]
        # Добавляем Telegram origins для разработки
        for tg_origin in TELEGRAM_ORIGINS:
            if tg_origin not in allowed_origins:
                allowed_origins.append(tg_origin)
    else:
        # Разрешаем все для разработки
        allowed_origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Telegram Birthday Calendar API"}


@app.get("/health")
async def health():
    """Health check endpoint для проверки доступности API."""
    return {
        "status": "ok",
        "service": "Telegram Birthday Calendar API",
        "message": "API is running",
    }