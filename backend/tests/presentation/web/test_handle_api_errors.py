"""
Тесты для декоратора @handle_api_errors.

Проверяют:
- Обработку различных типов ошибок
- Проверку rollback транзакций
- Проверку HTTP статус кодов
"""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.presentation.web.decorators import handle_api_errors


@pytest.mark.asyncio
async def test_handle_api_errors_success():
    """Тест успешного выполнения функции без ошибок."""
    # Arrange
    @handle_api_errors
    async def test_func(session: AsyncSession):
        return {"status": "ok"}
    
    session = AsyncMock(spec=AsyncSession)
    
    # Act
    result = await test_func(session)
    
    # Assert
    assert result == {"status": "ok"}
    session.rollback.assert_not_called()


@pytest.mark.asyncio
async def test_handle_api_errors_http_exception():
    """Тест обработки HTTPException - должен пробрасываться дальше без обработки."""
    # Arrange
    @handle_api_errors
    async def test_func(session: AsyncSession):
        raise HTTPException(status_code=404, detail="Not found")
    
    session = AsyncMock(spec=AsyncSession)
    
    # Act & Assert
    # HTTPException не перехватывается декоратором в except блоках,
    # поэтому он пробрасывается дальше без обработки
    # Это правильное поведение - декоратор обрабатывает только специфические исключения
    with pytest.raises(HTTPException) as exc_info:
        await test_func(session)
    
    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Not found"
    # HTTPException не должен вызывать rollback, так как не перехватывается
    # (он пробрасывается до того, как декоратор может выполнить rollback)
    session.rollback.assert_not_called()


@pytest.mark.asyncio
async def test_handle_api_errors_value_error():
    """Тест обработки ValueError с rollback."""
    # Arrange
    @handle_api_errors
    async def test_func(session: AsyncSession):
        raise ValueError("Validation error")
    
    session = AsyncMock(spec=AsyncSession)
    
    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        await test_func(session)
    
    assert exc_info.value.status_code == 400
    assert "Validation error" in exc_info.value.detail
    session.rollback.assert_called_once()


@pytest.mark.asyncio
async def test_handle_api_errors_generic_exception():
    """Тест обработки общего Exception с rollback."""
    # Arrange
    @handle_api_errors
    async def test_func(session: AsyncSession):
        raise Exception("Unexpected error")
    
    session = AsyncMock(spec=AsyncSession)
    
    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        await test_func(session)
    
    assert exc_info.value.status_code == 500
    assert "Internal server error" in exc_info.value.detail
    session.rollback.assert_called_once()


@pytest.mark.asyncio
async def test_handle_api_errors_no_session():
    """Тест обработки ошибки без сессии."""
    # Arrange
    @handle_api_errors
    async def test_func(session=None):
        raise ValueError("Error without session")
    
    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        await test_func(None)
    
    assert exc_info.value.status_code == 400


@pytest.mark.asyncio
async def test_handle_api_errors_rollback_on_exception():
    """Тест что rollback вызывается при любом исключении (кроме HTTPException)."""
    # Arrange
    exceptions = [
        ValueError("Value error"),
        TypeError("Type error"),
        RuntimeError("Runtime error"),
        Exception("Generic error"),
    ]
    
    for exc in exceptions:
        @handle_api_errors
        async def test_func(session: AsyncSession):
            raise exc
        
        session = AsyncMock(spec=AsyncSession)
        
        # Act
        with pytest.raises(HTTPException):
            await test_func(session)
        
        # Assert
        session.rollback.assert_called_once()
        session.reset_mock()


@pytest.mark.asyncio
async def test_handle_api_errors_preserves_http_status():
    """Тест что HTTPException сохраняет свой статус код при пробросе."""
    # Arrange
    status_codes = [400, 401, 403, 404, 422, 500]
    
    for status_code in status_codes:
        @handle_api_errors
        async def test_func(session: AsyncSession):
            raise HTTPException(status_code=status_code, detail=f"Error {status_code}")
        
        session = AsyncMock(spec=AsyncSession)
        
        # Act & Assert
        # HTTPException не перехватывается декоратором, пробрасывается дальше
        with pytest.raises(HTTPException) as exc_info:
            await test_func(session)
        
        assert exc_info.value.status_code == status_code
        assert exc_info.value.detail == f"Error {status_code}"
        # HTTPException не должен вызывать rollback, так как не перехватывается
        session.rollback.assert_not_called()
        session.reset_mock()

