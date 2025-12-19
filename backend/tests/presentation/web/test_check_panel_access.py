"""
Тесты для функции _check_panel_access.

Проверяют:
- Успешную проверку доступа
- Отказ в доступе
- Различные сценарии пользователей
"""

import pytest
from unittest.mock import AsyncMock, patch
from sqlalchemy.ext.asyncio import AsyncSession

from src.presentation.web.routes.api import _check_panel_access


@pytest.mark.asyncio
async def test_check_panel_access_success():
    """Тест успешной проверки доступа к панели."""
    # Arrange
    session = AsyncMock(spec=AsyncSession)
    user_id = 123
    
    with patch("src.presentation.web.routes.api.UseCaseFactory") as mock_factory:
        mock_use_case = AsyncMock()
        mock_use_case.execute.return_value = True
        mock_factory_instance = mock_factory.return_value
        mock_factory_instance.create_panel_access_use_case.return_value = mock_use_case
        
        # Act
        result = await _check_panel_access(session, user_id)
        
        # Assert
        assert result is True
        mock_use_case.execute.assert_called_once_with(user_id)


@pytest.mark.asyncio
async def test_check_panel_access_denied():
    """Тест отказа в доступе к панели."""
    # Arrange
    session = AsyncMock(spec=AsyncSession)
    user_id = 456
    
    with patch("src.presentation.web.routes.api.UseCaseFactory") as mock_factory:
        mock_use_case = AsyncMock()
        mock_use_case.execute.return_value = False
        mock_factory_instance = mock_factory.return_value
        mock_factory_instance.create_panel_access_use_case.return_value = mock_use_case
        
        # Act
        result = await _check_panel_access(session, user_id)
        
        # Assert
        assert result is False
        mock_use_case.execute.assert_called_once_with(user_id)


@pytest.mark.asyncio
async def test_check_panel_access_different_users():
    """Тест проверки доступа для разных пользователей."""
    # Arrange
    session = AsyncMock(spec=AsyncSession)
    
    test_cases = [
        (1, True),
        (2, False),
        (999, True),
        (1000, False),
    ]
    
    for user_id, expected_access in test_cases:
        with patch("src.presentation.web.routes.api.UseCaseFactory") as mock_factory:
            mock_use_case = AsyncMock()
            mock_use_case.execute.return_value = expected_access
            mock_factory_instance = mock_factory.return_value
            mock_factory_instance.create_panel_access_use_case.return_value = mock_use_case
            
            # Act
            result = await _check_panel_access(session, user_id)
            
            # Assert
            assert result == expected_access
            mock_use_case.execute.assert_called_once_with(user_id)


@pytest.mark.asyncio
async def test_check_panel_access_use_case_error():
    """Тест обработки ошибки use case при проверке доступа."""
    # Arrange
    session = AsyncMock(spec=AsyncSession)
    user_id = 789
    
    with patch("src.presentation.web.routes.api.UseCaseFactory") as mock_factory:
        mock_use_case = AsyncMock()
        mock_use_case.execute.side_effect = Exception("Database error")
        mock_factory_instance = mock_factory.return_value
        mock_factory_instance.create_panel_access_use_case.return_value = mock_use_case
        
        # Act & Assert
        with pytest.raises(Exception, match="Database error"):
            await _check_panel_access(session, user_id)

