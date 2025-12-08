import pytest
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.repositories.panel_access_repository_impl import PanelAccessRepositoryImpl
from src.infrastructure.database.models import PanelAccessModel


class TestPanelAccessRepositoryImpl:
    """Тесты для репозитория доступа к панели."""

    @pytest.fixture
    def mock_session(self):
        """Мок сессии БД."""
        session = AsyncMock(spec=AsyncSession)
        session.execute = AsyncMock()
        return session

    @pytest.fixture
    def repository(self, mock_session):
        """Репозиторий с мок сессией."""
        return PanelAccessRepositoryImpl(mock_session)

    @pytest.mark.asyncio
    async def test_has_access_true(self, repository, mock_session):
        """Тест проверки доступа (есть доступ)."""
        # Arrange
        user_id = 123
        mock_model = PanelAccessModel(user_id=user_id)
        
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_model
        mock_session.execute.return_value = mock_result

        # Act
        result = await repository.has_access(user_id)

        # Assert
        assert result is True

    @pytest.mark.asyncio
    async def test_has_access_false(self, repository, mock_session):
        """Тест проверки доступа (нет доступа)."""
        # Arrange
        user_id = 999
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_session.execute.return_value = mock_result

        # Act
        result = await repository.has_access(user_id)

        # Assert
        assert result is False

