import pytest
from unittest.mock import AsyncMock

from src.application.use_cases.panel.check_panel_access import CheckPanelAccessUseCase


class TestCheckPanelAccessUseCase:
    """Тесты для use-case проверки доступа к панели."""

    @pytest.mark.asyncio
    async def test_check_panel_access_has_access(self):
        """Тест проверки доступа - пользователь имеет доступ."""
        # Arrange
        mock_repository = AsyncMock()
        mock_repository.has_access.return_value = True
        
        use_case = CheckPanelAccessUseCase(mock_repository)

        # Act
        result = await use_case.execute(user_id=123)

        # Assert
        assert result is True
        mock_repository.has_access.assert_called_once_with(123)

    @pytest.mark.asyncio
    async def test_check_panel_access_no_access(self):
        """Тест проверки доступа - пользователь не имеет доступа."""
        # Arrange
        mock_repository = AsyncMock()
        mock_repository.has_access.return_value = False
        
        use_case = CheckPanelAccessUseCase(mock_repository)

        # Act
        result = await use_case.execute(user_id=456)

        # Assert
        assert result is False
        mock_repository.has_access.assert_called_once_with(456)





