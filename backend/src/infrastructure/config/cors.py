"""Конфигурация CORS для приложения.

Модуль содержит логику определения разрешенных origins для CORS middleware.
"""

import logging
import os

from src.infrastructure.config.constants import TELEGRAM_ORIGINS

logger = logging.getLogger(__name__)


def get_allowed_origins() -> list[str]:
    """Определить список разрешенных origins для CORS.
    
    Логика определения:
    - В production: использует только конкретные домены из ALLOWED_ORIGINS
      и автоматически добавляет Telegram origins
    - В development: разрешает все origins для удобства разработки,
      если ALLOWED_ORIGINS не указан или равен "*"
    
    Returns:
        list[str]: Список разрешенных origins для CORS middleware
    """
    # Определяем окружение (development или production)
    is_production = os.getenv("ENVIRONMENT", "development").lower() == "production"
    
    # Получаем разрешенные origins из переменной окружения
    allowed_origins_env = os.getenv("ALLOWED_ORIGINS", "")
    
    if is_production:
        # В production используем только конкретные домены
        if not allowed_origins_env:
            # Если не указано, используем только Telegram origins
            allowed_origins = TELEGRAM_ORIGINS.copy()
            logger.info("CORS: Используются только Telegram origins (ALLOWED_ORIGINS не указан)")
        elif "," in allowed_origins_env:
            # Если указано несколько доменов через запятую
            allowed_origins = [origin.strip() for origin in allowed_origins_env.split(",")]
            # Добавляем Telegram origins, если их еще нет
            for tg_origin in TELEGRAM_ORIGINS:
                if tg_origin not in allowed_origins:
                    allowed_origins.append(tg_origin)
            logger.info(f"CORS: Используются указанные домены + Telegram origins ({len(allowed_origins)} origins)")
        else:
            # Один домен
            allowed_origins = [allowed_origins_env.strip()]
            # Добавляем Telegram origins
            allowed_origins.extend(TELEGRAM_ORIGINS)
            logger.info(f"CORS: Используется указанный домен + Telegram origins ({len(allowed_origins)} origins)")
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
            logger.info(f"CORS (dev): Используются указанные домены + Telegram origins ({len(allowed_origins)} origins)")
        else:
            # Разрешаем все для разработки
            allowed_origins = ["*"]
            logger.warning("CORS (dev): Разрешены все origins (ALLOWED_ORIGINS='*' или не указан)")
    
    return allowed_origins

