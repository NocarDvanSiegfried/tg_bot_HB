import pytest
from datetime import date
from unittest.mock import AsyncMock, MagicMock, patch
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.presentation.web.app import app
from src.domain.entities.birthday import Birthday
from src.domain.entities.responsible_person import ResponsiblePerson


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
    import os
    os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite:///:memory:")
    os.environ.setdefault("TELEGRAM_BOT_TOKEN", "test_token")
    os.environ.setdefault("OPENROUTER_API_KEY", "test_key")
    
    with patch(
        "src.presentation.web.routes.api.get_database"
    ) as mock_get_db, patch(
        "src.presentation.web.routes.api.get_use_case_factory"
    ) as mock_get_factory:
        mock_db = MagicMock()
        async def get_session():
            yield mock_session
        mock_db.get_session = get_session
        mock_get_db.return_value = mock_db
        
        # Используем переданный mock_factory
        mock_get_factory.return_value = mock_factory
        
        yield TestClient(app)


class TestAdditionalEndpoints:
    """Дополнительные тесты для endpoints."""

    def test_update_responsible_success(self, client, mock_factory):
        """Тест обновления ответственного."""
        mock_use_cases = {
            "update": AsyncMock()
        }
        mock_responsible = ResponsiblePerson(
            id=1,
            full_name="Петр Петров Обновленный",
            company="ООО Тест",
            position="Менеджер",
        )
        mock_use_cases["update"].execute = AsyncMock(return_value=mock_responsible)
        mock_factory.create_responsible_use_cases.return_value = mock_use_cases
        
        response = client.put(
            "/api/panel/responsible/1",
            json={
                "full_name": "Петр Петров Обновленный",
            }
        )
        
        assert response.status_code == 200
        assert response.json()["full_name"] == "Петр Петров Обновленный"

    def test_delete_responsible_success(self, client, mock_factory):
        """Тест удаления ответственного."""
        mock_use_cases = {
            "delete": AsyncMock()
        }
        mock_use_cases["delete"].execute = AsyncMock()
        mock_factory.create_responsible_use_cases.return_value = mock_use_cases
        
        response = client.delete("/api/panel/responsible/1")
        
        assert response.status_code == 200
        assert response.json()["status"] == "deleted"

    def test_assign_responsible_success(self, client, mock_factory):
        """Тест назначения ответственного."""
        mock_use_cases = {
            "assign_to_date": AsyncMock()
        }
        mock_use_cases["assign_to_date"].execute = AsyncMock()
        mock_factory.create_responsible_use_cases.return_value = mock_use_cases
        
        response = client.post(
            "/api/panel/assign-responsible",
            json={
                "responsible_id": 1,
                "date": "2024-01-15",
            }
        )
        
        assert response.status_code == 200
        assert response.json()["status"] == "assigned"

    def test_search_people(self, client, mock_factory):
        """Тест поиска людей."""
        mock_use_case = AsyncMock()
        mock_birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )
        mock_use_case.execute = AsyncMock(return_value=[mock_birthday])
        mock_factory.create_search_use_case.return_value = mock_use_case
        
        response = client.get("/api/panel/search?q=Иван")
        
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["full_name"] == "Иван Иванов"

    def test_generate_greeting_success(self, client, mock_factory):
        """Тест генерации поздравления."""
        mock_use_cases = {
            "generate": AsyncMock()
        }
        mock_use_cases["generate"].execute = AsyncMock(return_value="Поздравляю!")
        mock_factory.create_greeting_use_cases.return_value = mock_use_cases
        
        response = client.post(
            "/api/panel/generate-greeting",
            json={
                "birthday_id": 1,
                "style": "formal",
                "length": "short",
            }
        )
        
        assert response.status_code == 200
        assert "greeting" in response.json()

    def test_create_card_success(self, client, mock_factory):
        """Тест создания открытки."""
        mock_use_cases = {
            "create_card": AsyncMock()
        }
        mock_use_cases["create_card"].execute = AsyncMock(return_value=b"fake_image_data")
        mock_factory.create_greeting_use_cases.return_value = mock_use_cases
        
        response = client.post(
            "/api/panel/create-card",
            json={
                "birthday_id": 1,
                "greeting_text": "Поздравляю!",
            }
        )
        
        assert response.status_code == 200
        assert response.headers["content-type"] == "image/png"

    def test_generate_greeting_not_found(self, client, mock_factory):
        """Тест генерации поздравления для несуществующего ДР."""
        from src.domain.exceptions.not_found import BirthdayNotFoundError
        
        mock_use_cases = {
            "generate": AsyncMock()
        }
        mock_use_cases["generate"].execute = AsyncMock(side_effect=BirthdayNotFoundError("Not found"))
        mock_factory.create_greeting_use_cases.return_value = mock_use_cases
        
        response = client.post(
            "/api/panel/generate-greeting",
            json={
                "birthday_id": 999,
                "style": "formal",
                "length": "short",
            }
        )
        
        assert response.status_code == 404

    def test_create_birthday_validation_error(self, client, mock_factory):
        """Тест создания ДР с ошибкой валидации."""
        from src.domain.exceptions.validation import ValidationError
        
        mock_use_cases = {
            "create": AsyncMock()
        }
        mock_use_cases["create"].execute = AsyncMock(side_effect=ValidationError("Invalid data"))
        mock_factory.create_birthday_use_cases.return_value = mock_use_cases
        
        response = client.post(
            "/api/panel/birthdays",
            json={
                "full_name": "",
                "company": "ООО Тест",
                "position": "Разработчик",
                "birth_date": "1990-05-15",
            }
        )
        
        assert response.status_code == 400

    def test_delete_birthday_not_found(self, client, mock_factory):
        """Тест удаления несуществующего ДР."""
        from src.domain.exceptions.not_found import BirthdayNotFoundError
        
        mock_use_cases = {
            "delete": AsyncMock()
        }
        mock_use_cases["delete"].execute = AsyncMock(side_effect=BirthdayNotFoundError("Not found"))
        mock_factory.create_birthday_use_cases.return_value = mock_use_cases
        
        response = client.delete("/api/panel/birthdays/999")
        
        assert response.status_code == 404

