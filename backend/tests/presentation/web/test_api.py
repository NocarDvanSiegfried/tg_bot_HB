import pytest
from datetime import date
from unittest.mock import AsyncMock, MagicMock, patch
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
    # Настраиваем мок для session.execute() -> result.scalars().all()
    mock_result = MagicMock()
    mock_scalars = MagicMock()
    mock_scalars.all.return_value = []
    mock_result.scalars.return_value = mock_scalars
    session.execute = AsyncMock(return_value=mock_result)
    return session


@pytest.fixture
def client(mock_session):
    """Тестовый клиент FastAPI."""
    # Устанавливаем переменные окружения для тестов
    import os
    os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite:///:memory:")
    os.environ.setdefault("TELEGRAM_BOT_TOKEN", "test_token")
    
    # Патчим get_database и зависимости
    with patch(
        "src.presentation.web.routes.api.get_database"
    ) as mock_get_db, patch(
        "src.presentation.web.routes.api.get_use_case_factory"
    ) as mock_get_factory:
        # Мокируем database
        mock_db = MagicMock()
        async def get_session():
            yield mock_session
        mock_db.get_session = get_session
        mock_get_db.return_value = mock_db
        
        # Мокируем фабрику use cases
        mock_factory = MagicMock()
        mock_get_factory.return_value = mock_factory
        
        yield TestClient(app)


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

    def test_get_calendar_success(self, client, mock_session):
        """Тест получения календаря."""
        with patch(
            "src.presentation.web.routes.api.get_database"
        ) as mock_get_db, patch(
            "src.presentation.web.routes.api.get_use_case_factory"
        ) as mock_get_factory:
            # Мокируем database
            mock_db = MagicMock()
            async def get_session():
                yield mock_session
            mock_db.get_session = get_session
            mock_get_db.return_value = mock_db
            
            mock_factory = MagicMock()
            mock_use_case = AsyncMock()
            mock_use_case.execute = AsyncMock(return_value={
                "birthdays": [],
                "holidays": [],
            })
            mock_factory.create_calendar_use_case.return_value = mock_use_case
            mock_get_factory.return_value = mock_factory
            
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

    def test_check_panel_access_success(self, client, mock_session):
        """Тест проверки доступа к панели."""
        with patch(
            "src.presentation.web.routes.api.get_database"
        ) as mock_get_db, patch(
            "src.presentation.web.routes.api.UseCaseFactory"
        ) as mock_factory_class:
            # Мокируем database
            mock_db = MagicMock()
            async def get_session():
                yield mock_session
            mock_db.get_session = get_session
            mock_get_db.return_value = mock_db
            
            # Мокируем verify_telegram_auth через dependency override
            from src.presentation.web.routes.api import verify_telegram_auth
            async def mock_auth():
                return {"id": 123}
            app.dependency_overrides[verify_telegram_auth] = mock_auth
            
            try:
                mock_factory = MagicMock()
                mock_use_case = AsyncMock()
                mock_use_case.execute = AsyncMock(return_value=True)
                mock_factory.create_panel_access_use_case.return_value = mock_use_case
                mock_factory_class.return_value = mock_factory
                
                response = client.get(
                    "/api/panel/check-access",
                    headers={"X-Init-Data": "test_data"}
                )
                
                assert response.status_code == 200
                assert response.json()["has_access"] is True
            finally:
                app.dependency_overrides.clear()

    def test_check_panel_access_no_auth(self, client):
        """Тест проверки доступа без авторизации."""
        response = client.get("/api/panel/check-access")
        
        assert response.status_code == 401

    def test_list_birthdays(self, client, mock_session):
        """Тест получения списка дней рождения."""
        with patch(
            "src.presentation.web.routes.api.get_database"
        ) as mock_get_db, patch(
            "src.presentation.web.routes.api.get_use_case_factory"
        ) as mock_get_factory:
            # Мокируем database
            mock_db = MagicMock()
            async def get_session():
                yield mock_session
            mock_db.get_session = get_session
            mock_get_db.return_value = mock_db
            mock_factory = MagicMock()
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
            mock_get_factory.return_value = mock_factory
            
            response = client.get("/api/panel/birthdays")
            
            assert response.status_code == 200
            assert len(response.json()) == 1
            assert response.json()[0]["id"] == 1

    def test_create_birthday_success(self, client, mock_session):
        """Тест создания дня рождения."""
        with patch(
            "src.presentation.web.routes.api.get_database"
        ) as mock_get_db, patch(
            "src.presentation.web.routes.api.get_use_case_factory"
        ) as mock_get_factory:
            # Мокируем database
            mock_db = MagicMock()
            async def get_session():
                yield mock_session
            mock_db.get_session = get_session
            mock_get_db.return_value = mock_db
            mock_factory = MagicMock()
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
            mock_get_factory.return_value = mock_factory
            
            mock_session.commit = AsyncMock()
            
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

    def test_update_birthday_success(self, client, mock_session):
        """Тест обновления дня рождения."""
        with patch(
            "src.presentation.web.routes.api.get_database"
        ) as mock_get_db, patch(
            "src.presentation.web.routes.api.get_use_case_factory"
        ) as mock_get_factory:
            # Мокируем database
            mock_db = MagicMock()
            async def get_session():
                yield mock_session
            mock_db.get_session = get_session
            mock_get_db.return_value = mock_db
            mock_factory = MagicMock()
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
            mock_get_factory.return_value = mock_factory
            
            mock_session.commit = AsyncMock()
            
            response = client.put(
                "/api/panel/birthdays/1",
                json={
                    "full_name": "Иван Иванов Обновленный",
                }
            )
            
            assert response.status_code == 200
            assert response.json()["full_name"] == "Иван Иванов Обновленный"

    def test_delete_birthday_success(self, client, mock_session):
        """Тест удаления дня рождения."""
        with patch(
            "src.presentation.web.routes.api.get_database"
        ) as mock_get_db, patch(
            "src.presentation.web.routes.api.get_use_case_factory"
        ) as mock_get_factory:
            # Мокируем database
            mock_db = MagicMock()
            async def get_session():
                yield mock_session
            mock_db.get_session = get_session
            mock_get_db.return_value = mock_db
            mock_factory = MagicMock()
            mock_use_cases = {
                "delete": AsyncMock()
            }
            mock_use_cases["delete"].execute = AsyncMock()
            mock_factory.create_birthday_use_cases.return_value = mock_use_cases
            mock_get_factory.return_value = mock_factory
            
            mock_session.commit = AsyncMock()
            
            response = client.delete("/api/panel/birthdays/1")
            
            assert response.status_code == 200
            assert response.json()["status"] == "deleted"

    def test_list_responsible(self, client, mock_session):
        """Тест получения списка ответственных."""
        with patch(
            "src.presentation.web.routes.api.get_database"
        ) as mock_get_db, patch(
            "src.presentation.web.routes.api.get_use_case_factory"
        ) as mock_get_factory:
            # Мокируем database
            mock_db = MagicMock()
            async def get_session():
                yield mock_session
            mock_db.get_session = get_session
            mock_get_db.return_value = mock_db
            mock_factory = MagicMock()
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
            mock_get_factory.return_value = mock_factory
            
            response = client.get("/api/panel/responsible")
            
            assert response.status_code == 200
            assert len(response.json()) == 1
            assert response.json()[0]["id"] == 1

    def test_create_responsible_success(self, client, mock_session):
        """Тест создания ответственного."""
        with patch(
            "src.presentation.web.routes.api.get_database"
        ) as mock_get_db, patch(
            "src.presentation.web.routes.api.get_use_case_factory"
        ) as mock_get_factory:
            # Мокируем database
            mock_db = MagicMock()
            async def get_session():
                yield mock_session
            mock_db.get_session = get_session
            mock_get_db.return_value = mock_db
            mock_factory = MagicMock()
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
            mock_get_factory.return_value = mock_factory
            
            mock_session.commit = AsyncMock()
            
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

