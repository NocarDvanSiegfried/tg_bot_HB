import pytest
from datetime import date
from unittest.mock import AsyncMock, MagicMock, patch
from fastapi import Depends
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.presentation.web.app import app
from src.presentation.web.routes.api import get_use_case_factory, get_db_session
from src.domain.entities.birthday import Birthday
from src.domain.entities.responsible_person import ResponsiblePerson
from src.domain.entities.professional_holiday import ProfessionalHoliday


@pytest.fixture
def mock_session():
    """Мок сессии БД."""
    session = AsyncMock(spec=AsyncSession)
    # Настраиваем мок для session.execute() -> result.scalars().all() и result.scalar_one_or_none()
    mock_result = MagicMock()
    mock_scalars = MagicMock()
    mock_scalars.all.return_value = []
    mock_result.scalars.return_value = mock_scalars
    mock_result.scalar_one_or_none.return_value = None
    session.execute = AsyncMock(return_value=mock_result)
    session.add = MagicMock()
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    return session


@pytest.fixture
def mock_factory():
    """Мок фабрики use cases."""
    return MagicMock()


@pytest.fixture
def client(mock_session, mock_factory):
    """Тестовый клиент FastAPI."""
    # Устанавливаем переменные окружения для тестов
    import os
    os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite:///:memory:")
    os.environ.setdefault("TELEGRAM_BOT_TOKEN", "test_token")
    
    # Переопределяем зависимости через FastAPI dependency_overrides
    from src.presentation.web.routes.api import get_use_case_factory, get_db_session
    from src.application.factories.use_case_factory import UseCaseFactory
    
    async def get_mock_session():
        yield mock_session
    
    async def get_mock_factory(session: AsyncSession = Depends(get_mock_session)) -> UseCaseFactory:
        return mock_factory
    
    app.dependency_overrides[get_use_case_factory] = get_mock_factory
    app.dependency_overrides[get_db_session] = get_mock_session
    
    try:
        yield TestClient(app)
    finally:
        app.dependency_overrides.clear()


class TestAuthEndpoints:
    """Тесты для auth endpoints."""

    def test_verify_init_data_success(self, client):
        """Тест успешной верификации initData."""
        with patch(
            "src.presentation.web.routes.api.UseCaseFactory"
        ) as mock_factory_class:
            mock_factory = MagicMock()
            mock_use_case = AsyncMock()
            mock_use_case.execute = AsyncMock(return_value={"id": 123, "first_name": "Test"})
            mock_factory.create_auth_use_case.return_value = mock_use_case
            mock_factory_class.return_value = mock_factory
            
            response = client.post(
                "/api/auth/verify",
                json={"init_data": "test_data"}
            )
            
            assert response.status_code == 200
            assert response.json()["valid"] is True
            assert "user" in response.json()

    def test_verify_init_data_invalid(self, client):
        """Тест невалидного initData."""
        with patch(
            "src.presentation.web.routes.api.UseCaseFactory"
        ) as mock_factory_class:
            mock_factory = MagicMock()
            mock_use_case = AsyncMock()
            mock_use_case.execute = AsyncMock(side_effect=ValueError("Invalid"))
            mock_factory.create_auth_use_case.return_value = mock_use_case
            mock_factory_class.return_value = mock_factory
            
            response = client.post(
                "/api/auth/verify",
                json={"init_data": "invalid_data"}
            )
            
            assert response.status_code == 401


class TestCalendarEndpoints:
    """Тесты для calendar endpoints."""

    def test_get_calendar_success(self, client, mock_factory):
        """Тест получения календаря."""
        mock_use_case = AsyncMock()
        mock_use_case.execute = AsyncMock(return_value={
            "birthdays": [],
            "holidays": [],
        })
        mock_factory.create_calendar_use_case.return_value = mock_use_case
        
        response = client.get("/api/calendar/2024-01-15")
        
        assert response.status_code == 200
        assert "birthdays" in response.json()
        assert "holidays" in response.json()

    def test_get_calendar_invalid_date(self, client):
        """Тест получения календаря с невалидной датой."""
        response = client.get("/api/calendar/invalid-date")
        
        assert response.status_code == 400


class TestPanelEndpoints:
    """Тесты для panel endpoints."""

    def test_check_panel_access_success(self, client, mock_factory):
        """Тест проверки доступа к панели."""
        # Мокируем verify_telegram_auth через dependency override
        from src.presentation.web.routes.api import verify_telegram_auth
        async def mock_auth():
            return {"id": 123}
        app.dependency_overrides[verify_telegram_auth] = mock_auth
        
        try:
            mock_use_case = AsyncMock()
            mock_use_case.execute = AsyncMock(return_value=True)
            mock_factory.create_panel_access_use_case.return_value = mock_use_case
            
            response = client.get(
                "/api/panel/check-access",
                headers={"X-Init-Data": "test_data"}
            )
            
            assert response.status_code == 200
            assert response.json()["has_access"] is True
        finally:
            app.dependency_overrides.pop(verify_telegram_auth, None)

    def test_check_panel_access_no_auth(self, client):
        """Тест проверки доступа без авторизации."""
        response = client.get("/api/panel/check-access")
        
        assert response.status_code == 401

    def test_list_birthdays(self, client, mock_factory):
        """Тест получения списка дней рождения."""
        mock_use_cases = {
            "get_all": AsyncMock()
        }
        mock_birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )
        mock_use_cases["get_all"].execute = AsyncMock(return_value=[mock_birthday])
        mock_factory.create_birthday_use_cases.return_value = mock_use_cases
        
        response = client.get("/api/panel/birthdays")
        
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["id"] == 1

    def test_create_birthday_success(self, client, mock_factory, mock_session):
        """Тест создания дня рождения."""
        mock_use_cases = {
            "create": AsyncMock()
        }
        mock_birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )
        mock_use_cases["create"].execute = AsyncMock(return_value=mock_birthday)
        mock_factory.create_birthday_use_cases.return_value = mock_use_cases
        
        response = client.post(
            "/api/panel/birthdays",
            json={
                "full_name": "Иван Иванов",
                "company": "ООО Тест",
                "position": "Разработчик",
                "birth_date": "1990-05-15",
            }
        )
        
        assert response.status_code == 200
        assert response.json()["id"] == 1

    def test_update_birthday_success(self, client, mock_factory):
        """Тест обновления дня рождения."""
        mock_use_cases = {
            "update": AsyncMock()
        }
        mock_birthday = Birthday(
            id=1,
            full_name="Иван Иванов Обновленный",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )
        mock_use_cases["update"].execute = AsyncMock(return_value=mock_birthday)
        mock_factory.create_birthday_use_cases.return_value = mock_use_cases
        
        response = client.put(
            "/api/panel/birthdays/1",
            json={
                "full_name": "Иван Иванов Обновленный",
            }
        )
        
        assert response.status_code == 200
        assert response.json()["full_name"] == "Иван Иванов Обновленный"

    def test_delete_birthday_success(self, client, mock_factory):
        """Тест удаления дня рождения."""
        mock_use_cases = {
            "delete": AsyncMock()
        }
        mock_use_cases["delete"].execute = AsyncMock()
        mock_factory.create_birthday_use_cases.return_value = mock_use_cases
        
        response = client.delete("/api/panel/birthdays/1")
        
        assert response.status_code == 200
        assert response.json()["status"] == "deleted"

    def test_list_responsible(self, client, mock_factory):
        """Тест получения списка ответственных."""
        mock_use_cases = {
            "get_all": AsyncMock()
        }
        mock_responsible = ResponsiblePerson(
            id=1,
            full_name="Петр Петров",
            company="ООО Тест",
            position="Менеджер",
        )
        mock_use_cases["get_all"].execute = AsyncMock(return_value=[mock_responsible])
        mock_factory.create_responsible_use_cases.return_value = mock_use_cases
        
        response = client.get("/api/panel/responsible")
        
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["id"] == 1

    def test_create_responsible_success(self, client, mock_factory):
        """Тест создания ответственного."""
        mock_use_cases = {
            "create": AsyncMock()
        }
        mock_responsible = ResponsiblePerson(
            id=1,
            full_name="Петр Петров",
            company="ООО Тест",
            position="Менеджер",
        )
        mock_use_cases["create"].execute = AsyncMock(return_value=mock_responsible)
        mock_factory.create_responsible_use_cases.return_value = mock_use_cases
        
        response = client.post(
            "/api/panel/responsible",
            json={
                "full_name": "Петр Петров",
                "company": "ООО Тест",
                "position": "Менеджер",
            }
        )
        
        assert response.status_code == 200
        assert response.json()["id"] == 1

