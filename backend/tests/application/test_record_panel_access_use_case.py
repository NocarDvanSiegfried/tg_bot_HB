import pytest
from unittest.mock import AsyncMock

from src.application.use_cases.panel.record_panel_access import RecordPanelAccessUseCase


class TestRecordPanelAccessUseCase:
    """Тесты для use-case записи доступа к панели."""

    @pytest.mark.asyncio
    async def test_record_panel_access_success(self):
        """Тест записи доступа к панели - успешный случай."""
        # Arrange
        mock_repository = AsyncMock()
        mock_repository.record_access = AsyncMock()
        
        use_case = RecordPanelAccessUseCase(mock_repository)

        # Act
        await use_case.execute(user_id=123)

        # Assert
        mock_repository.record_access.assert_called_once_with(123)

    @pytest.mark.asyncio
    async def test_record_panel_access_different_user(self):
        """Тест записи доступа к панели - другой пользователь."""
        # Arrange
        mock_repository = AsyncMock()
        mock_repository.record_access = AsyncMock()
        
        use_case = RecordPanelAccessUseCase(mock_repository)

        # Act
        await use_case.execute(user_id=456)

        # Assert
        mock_repository.record_access.assert_called_once_with(456)

