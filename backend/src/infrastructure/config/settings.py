"""
Settings - централизованная конфигурация приложения

Использует pydantic Settings для валидации и управления настройками.
Все настройки приложения должны быть определены здесь.
"""

import os
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Настройки приложения."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )
    
    # Telegram Bot
    TELEGRAM_BOT_TOKEN: str = Field(..., description="Токен Telegram бота")
    
    # Database
    DATABASE_URL: str = Field(..., description="URL подключения к базе данных")
    
    # CORS
    MINIAPP_ORIGIN: str = Field(
        default="https://miniapp.micro-tab.ru:4443",
        description="Origin Mini App для CORS"
    )
    
    # Logging
    LOG_LEVEL: str = Field(
        default="INFO",
        description="Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)"
    )
    
    # API
    API_HOST: str = Field(default="0.0.0.0", description="Хост для API сервера")
    API_PORT: int = Field(default=8000, description="Порт для API сервера")
    
    # Environment
    ENVIRONMENT: str = Field(
        default="production",
        description="Окружение (development, staging, production)"
    )
    
    def get_allowed_origins(self) -> List[str]:
        """Получить список разрешенных origins для CORS."""
        return [self.MINIAPP_ORIGIN]
    
    @property
    def is_development(self) -> bool:
        """Проверить, является ли окружение development."""
        return self.ENVIRONMENT.lower() == "development"
    
    @property
    def is_production(self) -> bool:
        """Проверить, является ли окружение production."""
        return self.ENVIRONMENT.lower() == "production"


# Глобальный экземпляр настроек
_settings: Settings | None = None


def get_settings() -> Settings:
    """Получить глобальный экземпляр настроек (singleton)."""
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings


# Экспорт для удобства
settings = get_settings()

