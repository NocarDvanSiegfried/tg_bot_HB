"""Декораторы для обработки ошибок в API endpoints."""

import logging
from collections.abc import Callable
from functools import wraps
from typing import Any

from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.exceptions.api_exceptions import (
    OpenRouterAPIError,
    OpenRouterRateLimitError,
    OpenRouterTimeoutError,
)
from src.domain.exceptions.business import BusinessRuleError
from src.domain.exceptions.not_found import (
    BirthdayNotFoundError,
    ResponsibleNotFoundError,
)
from src.domain.exceptions.validation import ValidationError

logger = logging.getLogger(__name__)


def handle_api_errors(func: Callable) -> Callable:
    """
    Декоратор для централизованной обработки ошибок в API endpoints.

    Автоматически обрабатывает:
    - NotFound ошибки (404)
    - Validation ошибки (400)
    - Business rule ошибки (400)
    - API ошибки (502, 503, 504)
    - Неожиданные ошибки (500)

    Автоматически выполняет rollback сессии при ошибках.

    Примечание: session должен быть передан через Depends(get_db_session) в FastAPI.
    """

    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Извлекаем session из kwargs (FastAPI передает через Depends)
        # FastAPI передает зависимости через kwargs с именами параметров функции
        session: AsyncSession | None = None

        # Ищем session в kwargs по имени параметра
        if "session" in kwargs:
            session = kwargs.get("session")

        # Если не нашли в kwargs, проверяем позиционные аргументы
        # (на случай, если session передана напрямую)
        if session is None:
            for arg in args:
                if isinstance(arg, AsyncSession):
                    session = arg
                    break

        try:
            return await func(*args, **kwargs)
        except (BirthdayNotFoundError, ResponsibleNotFoundError) as e:
            if session:
                await session.rollback()
            logger.warning(f"Resource not found: {e}")
            raise HTTPException(status_code=404, detail=str(e)) from e
        except ValidationError as e:
            if session:
                await session.rollback()
            logger.warning(f"Validation error: {e}")
            raise HTTPException(status_code=400, detail=str(e)) from e
        except BusinessRuleError as e:
            if session:
                await session.rollback()
            logger.warning(f"Business rule error: {e}")
            raise HTTPException(status_code=400, detail=str(e)) from e
        except OpenRouterRateLimitError as e:
            logger.error(f"OpenRouter rate limit error: {e}")
            raise HTTPException(
                status_code=503, detail="Service temporarily unavailable due to rate limiting"
            ) from e
        except OpenRouterTimeoutError as e:
            logger.error(f"OpenRouter timeout error: {e}")
            raise HTTPException(status_code=504, detail="External service timeout") from e
        except OpenRouterAPIError as e:
            logger.error(f"OpenRouter API error: {e}")
            raise HTTPException(status_code=502, detail="External service error") from e
        except ValueError as e:
            if session:
                await session.rollback()
            logger.warning(f"Value error: {e}")
            raise HTTPException(status_code=400, detail=str(e)) from e
        except Exception as e:
            if session:
                await session.rollback()
            logger.error(f"Unexpected error in {func.__name__}", exc_info=True)
            raise HTTPException(status_code=500, detail="Internal server error") from e

    return wrapper
