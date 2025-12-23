import logging
import os

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from src.infrastructure.config.cors import get_allowed_origins
from src.infrastructure.utils.mask_sensitive import mask_sensitive_headers
from src.presentation.web.routes.api import router

logger = logging.getLogger(__name__)

# Инициализация rate limiter
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="Telegram Birthday Calendar API")

# Подключение rate limiter к приложению
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS для Telegram Mini App
# Используем централизованную функцию для определения allowed_origins
allowed_origins = get_allowed_origins()

# КРИТИЧНО: CORS middleware должен быть добавлен ПЕРВЫМ (до других middleware и роутов)
# Это гарантирует, что CORS заголовки применяются ко всем запросам и ответам
# Порядок важен: middleware выполняются в обратном порядке при ответе
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # Только https://miniapp.micro-tab.ru:4443
    allow_credentials=True,  # Разрешить cookies и credentials
    allow_methods=["*"],  # Разрешить все HTTP-методы (GET, POST, PUT, DELETE, OPTIONS, PATCH и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки (Content-Type, X-Init-Data, Authorization и т.д.)
    expose_headers=["*"],  # Разрешить клиенту читать все заголовки ответа
    max_age=3600,  # Кэшировать preflight ответы на 1 час
)

# Сжатие ответов (gzip) для уменьшения размера передаваемых данных
# Добавляется ПОСЛЕ CORS, чтобы CORS заголовки были в финальном ответе
app.add_middleware(GZipMiddleware, minimum_size=1000)  # Сжимать ответы больше 1KB

# Экспортируем allowed_origins для использования в других модулях
__all__ = ["app", "allowed_origins"]


# Middleware для логирования всех запросов
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Логирование всех входящих запросов для отладки."""
    method = request.method
    path = request.url.path
    
    # Детальное логирование для PUT/DELETE
    if method in ["PUT", "DELETE"]:
        logger.info(f"[REQUEST] ===== {method} {path} =====")
        logger.info(f"[REQUEST] Query params: {dict(request.query_params)}")
        headers_to_log = mask_sensitive_headers(dict(request.headers))
        logger.info(f"[REQUEST] Headers: {headers_to_log}")
    else:
        query_params = str(request.query_params) if request.query_params else ""
        logger.info(f"[REQUEST] {method} {path}{'?' + query_params if query_params else ''}")
        
        # Для OPTIONS запросов логируем заголовки (с маскировкой)
        if method == "OPTIONS":
            headers_to_log = mask_sensitive_headers(dict(request.headers))
            logger.debug(f"[OPTIONS] Headers: {headers_to_log}")
        
        # Логируем заголовки (без чувствительных данных)
        headers_to_log = mask_sensitive_headers(dict(request.headers))
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
        f"[VALIDATION ERROR] ===== {request.method} {request.url.path} - Pydantic Validation Failed ====="
    )
    logger.error(f"[VALIDATION ERROR] Request method: {request.method}")
    logger.error(f"[VALIDATION ERROR] Request path: {request.url.path}")
    logger.error(f"[VALIDATION ERROR] Validation errors count: {len(exc.errors())}")
    
    # Детальное логирование каждой ошибки валидации
    for i, error in enumerate(exc.errors(), 1):
        logger.error(
            f"[VALIDATION ERROR] Error {i}: "
            f"field={'.'.join(str(loc) for loc in error.get('loc', []))}, "
            f"type={error.get('type', 'unknown')}, "
            f"message={error.get('msg', 'no message')}"
        )
    
    logger.debug(f"[VALIDATION ERROR] Request body: {exc.body if hasattr(exc, 'body') else 'N/A'}")
    headers_to_log = mask_sensitive_headers(dict(request.headers))
    logger.debug(f"[VALIDATION ERROR] Request headers: {headers_to_log}")
    
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


# КРИТИЧНО: Явный обработчик OPTIONS не нужен
# CORSMiddleware автоматически обрабатывает все OPTIONS запросы (preflight)
# Удаляем явный обработчик, чтобы избежать конфликтов с middleware


@app.get("/health")
async def health():
    """Health check endpoint для проверки доступности API."""
    return {
        "status": "ok",
        "service": "Telegram Birthday Calendar API",
        "message": "API is running",
    }