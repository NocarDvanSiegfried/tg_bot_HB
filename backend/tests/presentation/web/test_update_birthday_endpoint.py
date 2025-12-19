"""Тесты для PUT /api/panel/birthdays/{id} endpoint."""

import pytest
from datetime import date
from unittest.mock import AsyncMock, MagicMock, patch
from fastapi import Request
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.presentation.web.app import app
from src.presentation.web.routes.api import update_birthday
from src.domain.entities.birthday import Birthday


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
    request.method = "PUT"
    request.url.path = "/api/panel/birthdays/1"
    request.headers = {"X-Init-Data": "user=%7B%22id%22%3A123456%7D&hash=abc123"}
    return request


@pytest.fixture
def mock_birthday():
    """Мок объекта Birthday."""
    birthday = MagicMock(spec=Birthday)
    birthday.id = 1
    birthday.full_name = "Test User"
    birthday.company = "Test Company"
    birthday.position = "Test Position"
    birthday.birth_date = date(1990, 1, 1)
    birthday.comment = "Test comment"
    return birthday


@pytest.mark.asyncio
async def test_update_birthday_success(mock_session, mock_request, mock_birthday):
    """Тест успешного обновления дня рождения."""
    from src.presentation.web.routes.api import BirthdayUpdate
    
    update_data = BirthdayUpdate(
        full_name="Updated Name",
        company="Updated Company",
        position="Updated Position",
        birth_date=date(1990, 2, 2),
        comment="Updated comment"
    )
    
    with patch("src.presentation.web.routes.api._authenticate_and_check_access") as mock_auth, \
         patch("src.presentation.web.routes.api.UseCaseFactory") as mock_factory_class:
        
        # Мок аутентификации
        mock_auth.return_value = {"id": 123456}
        
        # Мок фабрики и use case
        mock_factory = MagicMock()
        mock_use_cases = {"update": AsyncMock()}
        mock_use_cases["update"].execute = AsyncMock(return_value=mock_birthday)
        mock_factory.create_birthday_use_cases.return_value = mock_use_cases
        mock_factory_class.return_value = mock_factory
        
        # Выполняем тест
        result = await update_birthday(
            request=mock_request,
            birthday_id=1,
            data=update_data,
            session=mock_session
        )
        
        # Проверяем результат
        assert result["id"] == 1
        assert result["full_name"] == "Test User"
        mock_auth.assert_called_once_with(mock_session, mock_request)
        mock_use_cases["update"].execute.assert_called_once()
        mock_session.commit.assert_called_once()


@pytest.mark.asyncio
async def test_update_birthday_authentication_failed(mock_session, mock_request):
    """Тест ошибки аутентификации."""
    from fastapi import HTTPException
    from src.presentation.web.routes.api import BirthdayUpdate
    
    update_data = BirthdayUpdate(
        full_name="Updated Name",
        birth_date=date(1990, 2, 2)
    )
    
    with patch("src.presentation.web.routes.api._authenticate_and_check_access") as mock_auth:
        mock_auth.side_effect = HTTPException(status_code=401, detail="Missing initData")
        
        with pytest.raises(HTTPException) as exc_info:
            await update_birthday(
                request=mock_request,
                birthday_id=1,
                data=update_data,
                session=mock_session
            )
        
        assert exc_info.value.status_code == 401
        mock_session.rollback.assert_not_called()  # Rollback не вызывается при ошибке аутентификации


@pytest.mark.asyncio
async def test_update_birthday_access_denied(mock_session, mock_request):
    """Тест отказа в доступе."""
    from fastapi import HTTPException
    from src.presentation.web.routes.api import BirthdayUpdate
    
    update_data = BirthdayUpdate(
        full_name="Updated Name",
        birth_date=date(1990, 2, 2)
    )
    
    with patch("src.presentation.web.routes.api._authenticate_and_check_access") as mock_auth:
        mock_auth.side_effect = HTTPException(status_code=403, detail="Access denied")
        
        with pytest.raises(HTTPException) as exc_info:
            await update_birthday(
                request=mock_request,
                birthday_id=1,
                data=update_data,
                session=mock_session
            )
        
        assert exc_info.value.status_code == 403
        mock_session.rollback.assert_not_called()


@pytest.mark.asyncio
async def test_update_birthday_validation_error(mock_session, mock_request, mock_birthday):
    """Тест ошибки валидации."""
    from src.presentation.web.routes.api import BirthdayUpdate
    
    update_data = BirthdayUpdate(
        full_name="Updated Name",
        birth_date=date(1990, 2, 2)
    )
    
    with patch("src.presentation.web.routes.api._authenticate_and_check_access") as mock_auth, \
         patch("src.presentation.web.routes.api.UseCaseFactory") as mock_factory_class:
        
        mock_auth.return_value = {"id": 123456}
        
        mock_factory = MagicMock()
        mock_use_cases = {"update": AsyncMock()}
        mock_use_cases["update"].execute = AsyncMock(side_effect=ValueError("Invalid data"))
        mock_factory.create_birthday_use_cases.return_value = mock_use_cases
        mock_factory_class.return_value = mock_factory
        
        with pytest.raises(ValueError):
            await update_birthday(
                request=mock_request,
                birthday_id=1,
                data=update_data,
                session=mock_session
            )
        
        mock_session.rollback.assert_called_once()


@pytest.mark.asyncio
async def test_update_birthday_rollback_on_error(mock_session, mock_request):
    """Тест rollback при ошибке."""
    from src.presentation.web.routes.api import BirthdayUpdate
    
    update_data = BirthdayUpdate(
        full_name="Updated Name",
        birth_date=date(1990, 2, 2)
    )
    
    with patch("src.presentation.web.routes.api._authenticate_and_check_access") as mock_auth, \
         patch("src.presentation.web.routes.api.UseCaseFactory") as mock_factory_class:
        
        mock_auth.return_value = {"id": 123456}
        
        mock_factory = MagicMock()
        mock_use_cases = {"update": AsyncMock()}
        mock_use_cases["update"].execute = AsyncMock(side_effect=Exception("Unexpected error"))
        mock_factory.create_birthday_use_cases.return_value = mock_use_cases
        mock_factory_class.return_value = mock_factory
        
        with pytest.raises(Exception):
            await update_birthday(
                request=mock_request,
                birthday_id=1,
                data=update_data,
                session=mock_session
            )
        
        mock_session.rollback.assert_called_once()

