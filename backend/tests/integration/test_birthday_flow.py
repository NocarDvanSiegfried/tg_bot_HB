"""Интеграционные тесты для полного flow управления днями рождения."""

import pytest
from datetime import date
from unittest.mock import AsyncMock, MagicMock, patch
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.factories.use_case_factory import UseCaseFactory
from src.domain.entities.birthday import Birthday


@pytest.fixture
def mock_session():
    """Мок сессии БД для интеграционных тестов."""
    session = AsyncMock(spec=AsyncSession)
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    return session


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
async def test_create_update_delete_birthday_flow(mock_session, mock_birthday):
    """Интеграционный тест для полного flow: создание -> обновление -> удаление."""
    # Создаем фабрику с сессией
    factory = UseCaseFactory(session=mock_session)
    
    # 1. Создание дня рождения
    create_use_case = factory.create_birthday_use_cases()["create"]
    
    with patch.object(create_use_case.repository, 'create') as mock_create:
        mock_create.return_value = mock_birthday
        
        created = await create_use_case.execute(
            full_name="Test User",
            company="Test Company",
            position="Test Position",
            birth_date=date(1990, 1, 1),
            comment="Test comment"
        )
        
        assert created.id == 1
        assert created.full_name == "Test User"
        mock_create.assert_called_once()
    
    # 2. Обновление дня рождения
    update_use_case = factory.create_birthday_use_cases()["update"]
    
    updated_birthday = MagicMock(spec=Birthday)
    updated_birthday.id = 1
    updated_birthday.full_name = "Updated User"
    updated_birthday.company = "Updated Company"
    updated_birthday.position = "Updated Position"
    updated_birthday.birth_date = date(1990, 2, 2)
    updated_birthday.comment = "Updated comment"
    
    with patch.object(update_use_case.repository, 'get_by_id') as mock_get, \
         patch.object(update_use_case.repository, 'update') as mock_update:
        mock_get.return_value = mock_birthday
        mock_update.return_value = updated_birthday
        
        updated = await update_use_case.execute(
            birthday_id=1,
            full_name="Updated User",
            company="Updated Company",
            position="Updated Position",
            birth_date=date(1990, 2, 2),
            comment="Updated comment"
        )
        
        assert updated.id == 1
        assert updated.full_name == "Updated User"
        assert updated.company == "Updated Company"
        mock_get.assert_called_once_with(1)
        mock_update.assert_called_once()
    
    # 3. Удаление дня рождения
    delete_use_case = factory.create_birthday_use_cases()["delete"]
    
    with patch.object(delete_use_case.repository, 'get_by_id') as mock_get, \
         patch.object(delete_use_case.repository, 'delete') as mock_delete:
        mock_get.return_value = updated_birthday
        mock_delete.return_value = None
        
        await delete_use_case.execute(1)
        
        mock_get.assert_called_once_with(1)
        mock_delete.assert_called_once_with(1)


@pytest.mark.asyncio
async def test_update_birthday_with_validation_error(mock_session, mock_birthday):
    """Интеграционный тест для обработки ошибок валидации при обновлении."""
    factory = UseCaseFactory(session=mock_session)
    update_use_case = factory.create_birthday_use_cases()["update"]
    
    with patch.object(update_use_case.repository, 'get_by_id') as mock_get:
        mock_get.return_value = mock_birthday
        
        # Попытка обновить с невалидными данными (например, будущая дата)
        future_date = date(2100, 1, 1)
        
        with pytest.raises(ValueError):
            await update_use_case.execute(
                birthday_id=1,
                birth_date=future_date
            )
        
        mock_get.assert_called_once_with(1)


@pytest.mark.asyncio
async def test_delete_nonexistent_birthday(mock_session):
    """Интеграционный тест для удаления несуществующего дня рождения."""
    factory = UseCaseFactory(session=mock_session)
    delete_use_case = factory.create_birthday_use_cases()["delete"]
    
    with patch.object(delete_use_case.repository, 'get_by_id') as mock_get:
        mock_get.return_value = None
        
        with pytest.raises(ValueError, match="not found"):
            await delete_use_case.execute(999)
        
        mock_get.assert_called_once_with(999)

