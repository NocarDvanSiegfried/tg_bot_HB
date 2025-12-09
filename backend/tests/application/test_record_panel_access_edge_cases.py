"""Дополнительные тесты для RecordPanelAccessUseCase с edge cases."""

import pytest
from unittest.mock import AsyncMock

from src.application.use_cases.panel.record_panel_access import RecordPanelAccessUseCase
from src.application.ports.panel_access_repository import PanelAccessRepository


class TestRecordPanelAccessUseCaseEdgeCases:
    """Тесты для edge cases в RecordPanelAccessUseCase."""

    @pytest.fixture
    def mock_repository(self):
        """Мок репозитория."""
        return AsyncMock(spec=PanelAccessRepository)

    @pytest.fixture
    def use_case(self, mock_repository):
        """Use case с мок репозиторием."""
        return RecordPanelAccessUseCase(mock_repository)

    @pytest.mark.asyncio
    async def test_execute_with_large_user_id(self, use_case, mock_repository):
        """Тест выполнения с большим user_id."""
        # Arrange
        large_user_id = 8091328122

        # Act
        await use_case.execute(large_user_id)

        # Assert
        mock_repository.record_access.assert_called_once_with(large_user_id)

    @pytest.mark.asyncio
    async def test_execute_repository_error(self, use_case, mock_repository):
        """Тест обработки ошибки репозитория."""
        # Arrange
        user_id = 123
        mock_repository.record_access.side_effect = Exception("Repository error")

        # Act & Assert
        with pytest.raises(Exception, match="Repository error"):
            await use_case.execute(user_id)

    @pytest.mark.asyncio
    async def test_execute_zero_user_id(self, use_case, mock_repository):
        """Тест выполнения с user_id = 0."""
        # Arrange
        user_id = 0

        # Act
        await use_case.execute(user_id)

        # Assert
        mock_repository.record_access.assert_called_once_with(user_id)

