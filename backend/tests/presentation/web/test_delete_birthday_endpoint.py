"""Тесты для DELETE /api/panel/birthdays/{id} endpoint."""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from fastapi import Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.presentation.web.routes.api import delete_birthday


@pytest.fixture
def mock_session():
    """Мок сессии БД."""
    session = AsyncMock(spec=AsyncSession)
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    return session


@pytest.fixture
def mock_request():
    """Мок Request объекта."""
    request = MagicMock(spec=Request)
    request.method = "DELETE"
    request.url.path = "/api/panel/birthdays/1"
    request.headers = {"X-Init-Data": "user=%7B%22id%22%3A123456%7D&hash=abc123"}
    return request


@pytest.mark.asyncio
async def test_delete_birthday_success(mock_session, mock_request):
    """Тест успешного удаления дня рождения."""
    with patch("src.presentation.web.routes.api._authenticate_and_check_access") as mock_auth, \
         patch("src.presentation.web.routes.api.UseCaseFactory") as mock_factory_class:
        
        # Мок аутентификации
        mock_auth.return_value = {"id": 123456}
        
        # Мок фабрики и use case
        mock_factory = MagicMock()
        mock_use_cases = {"delete": AsyncMock()}
        mock_use_cases["delete"].execute = AsyncMock(return_value=None)
        mock_factory.create_birthday_use_cases.return_value = mock_use_cases
        mock_factory_class.return_value = mock_factory
        
        # Выполняем тест
        result = await delete_birthday(
            request=mock_request,
            birthday_id=1,
            session=mock_session
        )
        
        # Проверяем результат
        assert result == {"status": "deleted"}
        mock_auth.assert_called_once_with(mock_session, mock_request)
        mock_use_cases["delete"].execute.assert_called_once_with(1)
        mock_session.commit.assert_called_once()


@pytest.mark.asyncio
async def test_delete_birthday_authentication_failed(mock_session, mock_request):
    """Тест ошибки аутентификации."""
    from fastapi import HTTPException
    
    with patch("src.presentation.web.routes.api._authenticate_and_check_access") as mock_auth:
        mock_auth.side_effect = HTTPException(status_code=401, detail="Missing initData")
        
        with pytest.raises(HTTPException) as exc_info:
            await delete_birthday(
                request=mock_request,
                birthday_id=1,
                session=mock_session
            )
        
        assert exc_info.value.status_code == 401
        mock_session.rollback.assert_not_called()


@pytest.mark.asyncio
async def test_delete_birthday_access_denied(mock_session, mock_request):
    """Тест отказа в доступе."""
    from fastapi import HTTPException
    
    with patch("src.presentation.web.routes.api._authenticate_and_check_access") as mock_auth:
        mock_auth.side_effect = HTTPException(status_code=403, detail="Access denied")
        
        with pytest.raises(HTTPException) as exc_info:
            await delete_birthday(
                request=mock_request,
                birthday_id=1,
                session=mock_session
            )
        
        assert exc_info.value.status_code == 403
        mock_session.rollback.assert_not_called()


@pytest.mark.asyncio
async def test_delete_birthday_validation_error(mock_session, mock_request):
    """Тест ошибки валидации."""
    with patch("src.presentation.web.routes.api._authenticate_and_check_access") as mock_auth, \
         patch("src.presentation.web.routes.api.UseCaseFactory") as mock_factory_class:
        
        mock_auth.return_value = {"id": 123456}
        
        mock_factory = MagicMock()
        mock_use_cases = {"delete": AsyncMock()}
        mock_use_cases["delete"].execute = AsyncMock(side_effect=ValueError("Invalid birthday_id"))
        mock_factory.create_birthday_use_cases.return_value = mock_use_cases
        mock_factory_class.return_value = mock_factory
        
        # Декоратор @handle_api_errors преобразует ValueError в HTTPException
        with pytest.raises(HTTPException) as exc_info:
            await delete_birthday(
                request=mock_request,
                birthday_id=1,
                session=mock_session
            )
        
        assert exc_info.value.status_code == 400
        assert "Invalid birthday_id" in str(exc_info.value.detail)
        # Rollback вызывается дважды: в endpoint и в декораторе
        assert mock_session.rollback.call_count >= 1


@pytest.mark.asyncio
async def test_delete_birthday_rollback_on_error(mock_session, mock_request):
    """Тест rollback при ошибке."""
    with patch("src.presentation.web.routes.api._authenticate_and_check_access") as mock_auth, \
         patch("src.presentation.web.routes.api.UseCaseFactory") as mock_factory_class:
        
        mock_auth.return_value = {"id": 123456}
        
        mock_factory = MagicMock()
        mock_use_cases = {"delete": AsyncMock()}
        mock_use_cases["delete"].execute = AsyncMock(side_effect=Exception("Unexpected error"))
        mock_factory.create_birthday_use_cases.return_value = mock_use_cases
        mock_factory_class.return_value = mock_factory
        
        # Декоратор @handle_api_errors преобразует Exception в HTTPException
        with pytest.raises(HTTPException) as exc_info:
            await delete_birthday(
                request=mock_request,
                birthday_id=1,
                session=mock_session
            )
        
        assert exc_info.value.status_code == 500
        assert "Internal server error" in str(exc_info.value.detail)
        # Rollback вызывается дважды: в endpoint и в декораторе
        assert mock_session.rollback.call_count >= 1

