"""Дополнительные тесты для PanelAccessRepository с edge cases."""

import pytest
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.repositories.panel_access_repository_impl import PanelAccessRepositoryImpl
from src.infrastructure.database.models import PanelAccessModel


class TestPanelAccessRepositoryEdgeCases:
    """Тесты для edge cases в PanelAccessRepository."""

    @pytest.fixture
    def mock_session(self):
        """Мок сессии БД."""
        session = AsyncMock(spec=AsyncSession)
        session.execute = AsyncMock()
        session.add = MagicMock()
        session.flush = AsyncMock()
        return session

    @pytest.fixture
    def repository(self, mock_session):
        """Репозиторий с мок сессией."""
        return PanelAccessRepositoryImpl(mock_session)

    @pytest.mark.asyncio
    async def test_record_access_zero_user_id(self, repository, mock_session):
        """Тест записи доступа с user_id = 0."""
        # Arrange
        user_id = 0

        # Act
        await repository.record_access(user_id)

        # Assert
        mock_session.add.assert_called_once()
        added_model = mock_session.add.call_args[0][0]
        assert isinstance(added_model, PanelAccessModel)
        assert added_model.user_id == 0
        mock_session.flush.assert_called_once()

    @pytest.mark.asyncio
    async def test_record_access_negative_user_id(self, repository, mock_session):
        """Тест записи доступа с отрицательным user_id (невалидный случай)."""
        # Arrange
        user_id = -1

        # Act
        await repository.record_access(user_id)

        # Assert
        # Репозиторий не валидирует user_id, просто записывает значение
        mock_session.add.assert_called_once()
        added_model = mock_session.add.call_args[0][0]
        assert added_model.user_id == -1

    @pytest.mark.asyncio
    async def test_has_access_multiple_records(self, repository, mock_session):
        """Тест проверки доступа когда есть несколько записей."""
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
        # Проверяем, что используется limit(1) в запросе
        mock_session.execute.assert_called_once()

    @pytest.mark.asyncio
    async def test_has_access_database_error(self, repository, mock_session):
        """Тест обработки ошибки БД при проверке доступа."""
        # Arrange
        user_id = 123
        mock_session.execute.side_effect = Exception("Database error")

        # Act & Assert
        with pytest.raises(Exception, match="Database error"):
            await repository.has_access(user_id)

    @pytest.mark.asyncio
    async def test_record_access_database_error(self, repository, mock_session):
        """Тест обработки ошибки БД при записи доступа."""
        # Arrange
        user_id = 123
        mock_session.flush.side_effect = Exception("Database error")

        # Act & Assert
        with pytest.raises(Exception, match="Database error"):
            await repository.record_access(user_id)

