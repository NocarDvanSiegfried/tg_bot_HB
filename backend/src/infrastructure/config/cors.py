"""Конфигурация CORS для приложения.

Модуль содержит логику определения разрешенных origins для CORS middleware.
КРИТИЧНО: Разрешен ТОЛЬКО origin Mini App для безопасности.
"""

import logging

logger = logging.getLogger(__name__)


def get_allowed_origins() -> list[str]:
    """Определить список разрешенных origins для CORS.
    
    КРИТИЧНО: Разрешен ТОЛЬКО origin Mini App (miniapp.micro-tab.ru:4443).
    Wildcard (*) не используется для безопасности.
    
    Returns:
        list[str]: Список разрешенных origins для CORS middleware
    """
    # КРИТИЧНО: Mini App origin для CORS - единственный разрешенный origin
    MINIAPP_ORIGIN = "https://miniapp.micro-tab.ru:4443"
    
    allowed_origins = [MINIAPP_ORIGIN]
    logger.info(f"CORS: Разрешен только Mini App origin: {MINIAPP_ORIGIN}")
    
    return allowed_origins

