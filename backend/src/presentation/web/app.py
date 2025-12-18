import logging
import os

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from src.infrastructure.config.constants import TELEGRAM_ORIGINS
from src.presentation.web.routes.api import router

logger = logging.getLogger(__name__)

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


# Middleware для логирования всех запросов
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Логирование всех входящих запросов для отладки."""
    method = request.method
    path = request.url.path
    query_params = str(request.query_params) if request.query_params else ""
    
    # Логируем запрос
    logger.info(f"[REQUEST] {method} {path}{'?' + query_params if query_params else ''}")
    
    # Логируем заголовки (без чувствительных данных)
    headers_to_log = {}
    for key, value in request.headers.items():
        if key.lower() in ['x-init-data', 'authorization']:
            headers_to_log[key] = f"{value[:20]}..." if len(value) > 20 else "***"
        else:
            headers_to_log[key] = value
    logger.debug(f"[REQUEST] Headers: {headers_to_log}")
    
    try:
        response = await call_next(request)
        logger.info(f"[RESPONSE] {method} {path} - {response.status_code}")
        return response
    except Exception as e:
        logger.error(f"[ERROR] {method} {path}: {type(e).__name__}: {e}", exc_info=True)
        raise


# Exception handler для ошибок валидации Pydantic
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Обработка ошибок валидации Pydantic."""
    logger.error(
        f"[VALIDATION ERROR] {request.method} {request.url.path}: {exc.errors()}"
    )
    logger.debug(f"[VALIDATION ERROR] Body: {exc.body if hasattr(exc, 'body') else 'N/A'}")
    
    return JSONResponse(
        status_code=422,
        content={
            "detail": "Validation error",
            "errors": exc.errors(),
            "body": str(exc.body) if hasattr(exc, 'body') else None
        }
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