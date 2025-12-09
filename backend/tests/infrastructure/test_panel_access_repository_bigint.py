"""Тесты для проверки поддержки больших user_id (BigInteger)."""

import pytest
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.repositories.panel_access_repository_impl import PanelAccessRepositoryImpl
from src.infrastructure.database.models import PanelAccessModel


class TestPanelAccessRepositoryBigInt:
    """Тесты для проверки поддержки больших user_id (BigInteger)."""

    @pytest.fixture
    def mock_session(self):
        """Мок сессии БД."""
        session = AsyncMock(spec=AsyncSession)
        session.execute = AsyncMock()
        session.add = MagicMock()
        session.flush = AsyncMock()  # Изменено: flush вместо commit
        return session

    @pytest.fixture
    def repository(self, mock_session):
        """Репозиторий с мок сессией."""
        return PanelAccessRepositoryImpl(mock_session)

    @pytest.mark.asyncio
    async def test_record_access_with_large_user_id(self, repository, mock_session):
        """Тест записи доступа с большим user_id (больше int32)."""
        # Arrange - user_id больше максимального значения int32 (2,147,483,647)
        large_user_id = 8091328122  # Реальный Telegram user_id из ошибки
        
        # Act
        await repository.record_access(large_user_id)
        
        # Assert
        mock_session.add.assert_called_once()
        added_model = mock_session.add.call_args[0][0]
        assert isinstance(added_model, PanelAccessModel)
        assert added_model.user_id == large_user_id
        # Проверяем, что используется flush, а не commit
        mock_session.flush.assert_called_once()
        mock_session.commit.assert_not_called()

    @pytest.mark.asyncio
    async def test_has_access_with_large_user_id(self, repository, mock_session):
        """Тест проверки доступа с большим user_id."""
        # Arrange
        large_user_id = 8091328122
        mock_model = PanelAccessModel(user_id=large_user_id)
        
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_model
        mock_session.execute.return_value = mock_result

        # Act
        result = await repository.has_access(large_user_id)

        # Assert
        assert result is True
        # Проверяем, что execute был вызван
        mock_session.execute.assert_called_once()

