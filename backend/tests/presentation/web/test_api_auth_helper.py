"""Тесты для вспомогательной функции _authenticate_and_check_access."""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from fastapi import HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.presentation.web.routes.api import _authenticate_and_check_access
from src.application.factories.use_case_factory import UseCaseFactory


@pytest.fixture
def mock_session():
    """Мок сессии БД."""
    return AsyncMock(spec=AsyncSession)


@pytest.fixture
def mock_request():
    """Мок Request объекта."""
    request = MagicMock(spec=Request)
    request.headers = {}
    return request


@pytest.fixture
def valid_init_data():
    """Валидный initData для тестов."""
    return "user=%7B%22id%22%3A123456%7D&hash=abc123"


@pytest.mark.asyncio
async def test_authenticate_and_check_access_success(mock_session, mock_request, valid_init_data):
    """Тест успешной аутентификации и проверки доступа."""
    # Настраиваем моки
    mock_request.headers.get.return_value = valid_init_data
    
    mock_user = {"id": 123456, "first_name": "Test", "username": "testuser"}
    
    with patch.object(UseCaseFactory, "__new__") as mock_factory_new:
        # Мок для auth factory
        mock_auth_factory = MagicMock()
        mock_auth_use_case = AsyncMock()
        mock_auth_use_case.execute = AsyncMock(return_value=mock_user)
        mock_auth_factory.create_auth_use_case.return_value = mock_auth_use_case
        mock_factory_new.return_value = mock_auth_factory
        
        # Мок для panel access factory
        mock_panel_factory = MagicMock()
        mock_panel_use_case = AsyncMock()
        mock_panel_use_case.execute = AsyncMock(return_value=True)
        mock_panel_factory.create_panel_access_use_case.return_value = mock_panel_use_case
        
        # Настраиваем UseCaseFactory для разных вызовов
        def factory_side_effect(*args, **kwargs):
            if kwargs.get("session") is None:
                return mock_auth_factory
            return mock_panel_factory
        
        mock_factory_new.side_effect = factory_side_effect
        
        # Выполняем тест
        result = await _authenticate_and_check_access(mock_session, mock_request)
        
        # Проверяем результат
        assert result == mock_user
        assert result["id"] == 123456
        mock_auth_use_case.execute.assert_called_once_with(valid_init_data)
        mock_panel_use_case.execute.assert_called_once_with(123456)


@pytest.mark.asyncio
async def test_authenticate_and_check_access_missing_header(mock_session, mock_request):
    """Тест ошибки при отсутствии X-Init-Data header."""
    mock_request.headers.get.return_value = None
    
    with pytest.raises(HTTPException) as exc_info:
        await _authenticate_and_check_access(mock_session, mock_request)
    
    assert exc_info.value.status_code == 401
    assert "Missing initData" in str(exc_info.value.detail)


@pytest.mark.asyncio
async def test_authenticate_and_check_access_invalid_init_data(mock_session, mock_request):
    """Тест ошибки при невалидном initData."""
    mock_request.headers.get.return_value = "invalid_data"
    
    with patch.object(UseCaseFactory, "__new__") as mock_factory_new:
        mock_auth_factory = MagicMock()
        mock_auth_use_case = AsyncMock()
        mock_auth_use_case.execute = AsyncMock(side_effect=ValueError("Invalid initData"))
        mock_auth_factory.create_auth_use_case.return_value = mock_auth_use_case
        mock_factory_new.return_value = mock_auth_factory
        
        with pytest.raises(HTTPException) as exc_info:
            await _authenticate_and_check_access(mock_session, mock_request)
        
        assert exc_info.value.status_code == 401
        assert "Invalid initData" in str(exc_info.value.detail)


@pytest.mark.asyncio
async def test_authenticate_and_check_access_no_user_id(mock_session, mock_request, valid_init_data):
    """Тест ошибки при отсутствии user_id в initData."""
    mock_request.headers.get.return_value = valid_init_data
    
    mock_user = {"first_name": "Test"}  # Нет 'id'
    
    with patch.object(UseCaseFactory, "__new__") as mock_factory_new:
        mock_auth_factory = MagicMock()
        mock_auth_use_case = AsyncMock()
        mock_auth_use_case.execute = AsyncMock(return_value=mock_user)
        mock_auth_factory.create_auth_use_case.return_value = mock_auth_use_case
        mock_factory_new.return_value = mock_auth_factory
        
        with pytest.raises(HTTPException) as exc_info:
            await _authenticate_and_check_access(mock_session, mock_request)
        
        assert exc_info.value.status_code == 401
        assert "User ID not found" in str(exc_info.value.detail)


@pytest.mark.asyncio
async def test_authenticate_and_check_access_denied(mock_session, mock_request, valid_init_data):
    """Тест отказа в доступе к панели."""
    mock_request.headers.get.return_value = valid_init_data
    
    mock_user = {"id": 123456, "first_name": "Test"}
    
    with patch.object(UseCaseFactory, "__new__") as mock_factory_new:
        # Мок для auth factory
        mock_auth_factory = MagicMock()
        mock_auth_use_case = AsyncMock()
        mock_auth_use_case.execute = AsyncMock(return_value=mock_user)
        mock_auth_factory.create_auth_use_case.return_value = mock_auth_use_case
        
        # Мок для panel access factory (доступ запрещен)
        mock_panel_factory = MagicMock()
        mock_panel_use_case = AsyncMock()
        mock_panel_use_case.execute = AsyncMock(return_value=False)
        mock_panel_factory.create_panel_access_use_case.return_value = mock_panel_use_case
        
        def factory_side_effect(*args, **kwargs):
            if kwargs.get("session") is None:
                return mock_auth_factory
            return mock_panel_factory
        
        mock_factory_new.side_effect = factory_side_effect
        
        with pytest.raises(HTTPException) as exc_info:
            await _authenticate_and_check_access(mock_session, mock_request)
        
        assert exc_info.value.status_code == 403
        assert "Access denied" in str(exc_info.value.detail)
        mock_panel_use_case.execute.assert_called_once_with(123456)

