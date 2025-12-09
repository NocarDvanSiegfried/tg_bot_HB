"""Тесты для DatabaseMiddleware с правильным управлением транзакциями."""

import pytest
from unittest.mock import AsyncMock, MagicMock
from aiogram.types import Message, User, Chat
from sqlalchemy.ext.asyncio import AsyncSession

from src.presentation.telegram.middleware.database_middleware import DatabaseMiddleware
from src.infrastructure.database.database import Database
from src.infrastructure.database import database_factory


class TestDatabaseMiddleware:
    """Тесты для DatabaseMiddleware с правильным управлением транзакциями."""

    @pytest.fixture(autouse=True)
    def clear_database_singleton(self):
        """Очистить singleton перед каждым тестом."""
        # Очищаем singleton перед тестом
        database_factory._database = None
        yield
        # Очищаем singleton после теста
        database_factory._database = None

    @pytest.fixture
    def mock_message(self):
        """Мок сообщения."""
        message = MagicMock(spec=Message)
        message.from_user = MagicMock(spec=User)
        message.from_user.id = 12345
        message.chat = MagicMock(spec=Chat)
        message.answer = AsyncMock()
        return message

    @pytest.fixture
    def mock_session(self):
        """Мок сессии БД."""
        session = AsyncMock(spec=AsyncSession)
        session.add = MagicMock()
        session.flush = AsyncMock()
        session.commit = AsyncMock()
        session.rollback = AsyncMock()
        session.close = AsyncMock()
        return session

    @pytest.fixture
    def mock_database(self, mock_session):
        """Мок базы данных."""
        async def get_session_generator():
            """Генератор сессий, имитирующий async with."""
            yield mock_session
            # Явный return для корректного завершения генератора в Python 3.7+
            return
        
        db = MagicMock(spec=Database)
        # get_session() возвращает async generator
        db.get_session = lambda: get_session_generator()
        return db

    @pytest.mark.asyncio
    async def test_middleware_injects_session_without_commit(self, mock_message, mock_session, mock_database, monkeypatch):
        """Тест: middleware инжектирует сессию, но НЕ делает commit."""
        # Arrange
        middleware = DatabaseMiddleware()
        
        async def handler(event, data):
            """Тестовый обработчик, который использует сессию."""
            session = data.get("session")
            assert session is not None
            assert session == mock_session
            # Обработчик может использовать сессию, но не должен делать commit
            return "handler_result"
        
        # Act - используем monkeypatch для изоляции патча
        monkeypatch.setattr('src.presentation.telegram.middleware.database_middleware.get_database', lambda: mock_database)
        result = await middleware(handler, mock_message, {})
        
        # Assert
        assert result == "handler_result"
        # Middleware НЕ должен делать commit - это делает repository или use-case
        mock_session.commit.assert_not_called()
        mock_session.rollback.assert_not_called()
        # Сессия должна быть инжектирована
        # (проверяется через handler)

    @pytest.mark.asyncio
    async def test_middleware_handles_exception_without_rollback(self, mock_message, mock_session, mock_database, monkeypatch):
        """Тест: middleware НЕ делает rollback при ошибке (сессия управляется через async with)."""
        # Arrange
        middleware = DatabaseMiddleware()
        test_exception = ValueError("Test error")
        
        async def handler(event, data):
            """Тестовый обработчик, который выбрасывает исключение."""
            raise test_exception
        
        # Act & Assert - используем monkeypatch для изоляции патча
        monkeypatch.setattr('src.presentation.telegram.middleware.database_middleware.get_database', lambda: mock_database)
        with pytest.raises(ValueError, match="Test error"):
            await middleware(handler, mock_message, {})
        
        # Assert
        # Middleware НЕ должен делать rollback - сессия управляется через async with
        mock_session.rollback.assert_not_called()
        mock_session.commit.assert_not_called()

    @pytest.mark.asyncio
    async def test_middleware_handles_database_error_gracefully(self, mock_message, monkeypatch):
        """Тест: middleware обрабатывает ошибку создания сессии."""
        # Arrange
        middleware = DatabaseMiddleware()
        
        async def handler(event, data):
            """Обработчик, который не требует сессию."""
            return "handler_result"
        
        # Act - имитируем ошибку создания сессии, используем monkeypatch для изоляции
        def raise_db_error():
            raise Exception("DB error")
        monkeypatch.setattr('src.presentation.telegram.middleware.database_middleware.get_database', raise_db_error)
        result = await middleware(handler, mock_message, {})
        
        # Assert
        assert result == "handler_result"
        # Обработчик должен выполниться даже без сессии

