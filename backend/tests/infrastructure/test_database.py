import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.database import Database


class TestDatabase:
    """Тесты для класса Database."""

    @pytest.fixture
    def database_url(self):
        """URL тестовой БД."""
        return "sqlite+aiosqlite:///:memory:"

    @pytest.fixture
    def database(self, database_url):
        """Экземпляр Database."""
        return Database(database_url)

    @pytest.mark.asyncio
    async def test_database_initialization(self, database, database_url):
        """Тест создания Database instance."""
        assert database is not None
        assert database.engine is not None
        assert database.async_session_maker is not None

    @pytest.mark.asyncio
    async def test_get_session(self, database):
        """Тест получения сессии."""
        session_count = 0
        async for session in database.get_session():
            session_count += 1
            assert session is not None
            assert isinstance(session, AsyncSession)
        
        assert session_count == 1

    @pytest.mark.asyncio
    async def test_create_tables(self, database):
        """Тест создания таблиц."""
        # Проверяем, что метод не вызывает ошибок
        try:
            await database.create_tables()
        except Exception as e:
            # Может быть ошибка из-за отсутствия моделей, но структура должна работать
            pytest.fail(f"create_tables raised {e} unexpectedly")

    @pytest.mark.asyncio
    async def test_multiple_sessions(self, database):
        """Тест получения нескольких сессий."""
        sessions = []
        async for session in database.get_session():
            sessions.append(session)
        
        async for session in database.get_session():
            sessions.append(session)
        
        assert len(sessions) == 2
        # Сессии должны быть разными объектами
        assert sessions[0] is not sessions[1]

