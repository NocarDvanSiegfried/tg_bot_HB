import pytest
import os
from unittest.mock import AsyncMock, MagicMock, patch
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.factories.use_case_factory import UseCaseFactory


class TestUseCaseFactory:
    """Тесты для фабрики use-cases."""

    @pytest.fixture
    def mock_session(self):
        """Мок сессии БД."""
        return AsyncMock(spec=AsyncSession)

    @pytest.fixture
    def factory(self, mock_session):
        """Фабрика с мок сессией."""
        return UseCaseFactory(session=mock_session)

    @pytest.mark.asyncio
    async def test_create_birthday_use_cases(self, factory):
        """Тест создания use-cases для дней рождения."""
        use_cases = factory.create_birthday_use_cases()
        
        assert "create" in use_cases
        assert "update" in use_cases
        assert "delete" in use_cases
        assert "get_all" in use_cases

    @pytest.mark.asyncio
    async def test_create_calendar_use_case(self, factory):
        """Тест создания use-case для календаря."""
        use_case = factory.create_calendar_use_case()
        assert use_case is not None

    @pytest.mark.asyncio
    async def test_create_responsible_use_cases(self, factory):
        """Тест создания use-cases для ответственных."""
        use_cases = factory.create_responsible_use_cases()
        
        assert "create" in use_cases
        assert "update" in use_cases
        assert "delete" in use_cases
        assert "assign_to_date" in use_cases
        assert "get_all" in use_cases

    @pytest.mark.asyncio
    async def test_create_search_use_case(self, factory):
        """Тест создания use-case для поиска."""
        use_case = factory.create_search_use_case()
        assert use_case is not None

    @pytest.mark.asyncio
    async def test_create_greeting_use_cases(self, factory):
        """Тест создания use-cases для поздравлений."""
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test_key"}):
            use_cases = factory.create_greeting_use_cases()
            
            assert "generate" in use_cases
            assert "create_card" in use_cases

    @pytest.mark.asyncio
    async def test_create_panel_access_use_case(self, factory):
        """Тест создания use-case для проверки доступа к панели."""
        use_case = factory.create_panel_access_use_case()
        assert use_case is not None

    @pytest.mark.asyncio
    async def test_create_auth_use_case(self, factory):
        """Тест создания use-case для верификации Telegram auth."""
        with patch.dict(os.environ, {"TELEGRAM_BOT_TOKEN": "test_token"}):
            use_case = factory.create_auth_use_case()
            assert use_case is not None

    @pytest.mark.asyncio
    async def test_lazy_initialization_repositories(self, factory):
        """Тест lazy initialization репозиториев."""
        # Первый вызов создает репозиторий
        repo1 = factory.birthday_repo
        # Второй вызов возвращает тот же экземпляр
        repo2 = factory.birthday_repo
        assert repo1 is repo2

    @pytest.mark.asyncio
    async def test_factory_without_session(self):
        """Тест фабрики без сессии."""
        factory = UseCaseFactory(session=None)
        # Репозитории должны создаваться, но с None сессией
        repo = factory.birthday_repo
        assert repo is not None
        assert repo.session is None

    @pytest.mark.asyncio
    async def test_openrouter_client_missing_env(self, factory):
        """Тест обработки отсутствующего OPENROUTER_API_KEY."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
                factory.create_greeting_use_cases()

    @pytest.mark.asyncio
    async def test_auth_use_case_missing_token(self, factory):
        """Тест обработки отсутствующего TELEGRAM_BOT_TOKEN."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError, match="TELEGRAM_BOT_TOKEN"):
                factory.create_auth_use_case()

