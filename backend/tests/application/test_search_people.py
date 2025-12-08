import pytest
from unittest.mock import AsyncMock

from src.application.use_cases.search.search_people import SearchPeopleUseCase
from src.domain.entities.birthday import Birthday
from src.domain.entities.responsible_person import ResponsiblePerson
from datetime import date


class TestSearchPeopleUseCase:
    """Тесты для use-case поиска людей."""

    @pytest.fixture
    def mock_birthday_repo(self):
        """Мок репозитория дней рождения."""
        return AsyncMock()

    @pytest.fixture
    def mock_responsible_repo(self):
        """Мок репозитория ответственных."""
        return AsyncMock()

    @pytest.fixture
    def use_case(self, mock_birthday_repo, mock_responsible_repo):
        """Use-case для поиска."""
        return SearchPeopleUseCase(mock_birthday_repo, mock_responsible_repo)

    @pytest.mark.asyncio
    async def test_search_success(self, use_case, mock_birthday_repo, mock_responsible_repo):
        """Тест успешного поиска."""
        # Arrange
        query = "Иван"
        birthdays = [
            Birthday(
                id=1,
                full_name="Иван Иванов",
                company="ООО Тест",
                position="Разработчик",
                birth_date=date(1990, 5, 15),
                comment=None,
            )
        ]
        responsible = [
            ResponsiblePerson(
                id=1,
                full_name="Иван Петров",
                company="ООО Тест",
                position="Менеджер",
            )
        ]
        
        mock_birthday_repo.search.return_value = birthdays
        mock_responsible_repo.search.return_value = responsible

        # Act
        results = await use_case.execute(query)

        # Assert
        assert len(results) == 2
        assert isinstance(results[0], Birthday)
        assert isinstance(results[1], ResponsiblePerson)
        mock_birthday_repo.search.assert_called_once_with(query)
        mock_responsible_repo.search.assert_called_once_with(query)

    @pytest.mark.asyncio
    async def test_search_empty_result(self, use_case, mock_birthday_repo, mock_responsible_repo):
        """Тест поиска с пустым результатом."""
        # Arrange
        query = "Несуществующий"
        mock_birthday_repo.search.return_value = []
        mock_responsible_repo.search.return_value = []

        # Act
        results = await use_case.execute(query)

        # Assert
        assert len(results) == 0
        mock_birthday_repo.search.assert_called_once_with(query)
        mock_responsible_repo.search.assert_called_once_with(query)

    @pytest.mark.asyncio
    async def test_search_only_birthdays(self, use_case, mock_birthday_repo, mock_responsible_repo):
        """Тест поиска только в днях рождения."""
        # Arrange
        query = "Иван"
        birthdays = [
            Birthday(
                id=1,
                full_name="Иван Иванов",
                company="ООО Тест",
                position="Разработчик",
                birth_date=date(1990, 5, 15),
                comment=None,
            )
        ]
        mock_birthday_repo.search.return_value = birthdays

        # Act
        results = await use_case.execute(query, search_birthdays=True, search_responsible=False)

        # Assert
        assert len(results) == 1
        assert isinstance(results[0], Birthday)
        mock_birthday_repo.search.assert_called_once_with(query)
        mock_responsible_repo.search.assert_not_called()

    @pytest.mark.asyncio
    async def test_search_only_responsible(self, use_case, mock_birthday_repo, mock_responsible_repo):
        """Тест поиска только в ответственных."""
        # Arrange
        query = "Петр"
        responsible = [
            ResponsiblePerson(
                id=1,
                full_name="Петр Петров",
                company="ООО Тест",
                position="Менеджер",
            )
        ]
        mock_responsible_repo.search.return_value = responsible

        # Act
        results = await use_case.execute(query, search_birthdays=False, search_responsible=True)

        # Assert
        assert len(results) == 1
        assert isinstance(results[0], ResponsiblePerson)
        mock_birthday_repo.search.assert_not_called()
        mock_responsible_repo.search.assert_called_once_with(query)

    @pytest.mark.asyncio
    async def test_search_repository_error(self, use_case, mock_birthday_repo, mock_responsible_repo):
        """Тест обработки ошибок репозиториев."""
        # Arrange
        query = "Иван"
        mock_birthday_repo.search.side_effect = Exception("Database error")

        # Act & Assert
        with pytest.raises(Exception, match="Database error"):
            await use_case.execute(query)

