import pytest
from datetime import date
from unittest.mock import AsyncMock

from src.application.use_cases.birthday.get_birthdays_by_date import GetBirthdaysByDateUseCase
from src.domain.entities.birthday import Birthday


class TestGetBirthdaysByDateUseCase:
    """Тесты для use-case получения дней рождения по дате."""

    @pytest.fixture
    def mock_birthday_repo(self):
        """Мок репозитория дней рождения."""
        return AsyncMock()

    @pytest.fixture
    def use_case(self, mock_birthday_repo):
        """Use-case для получения дней рождения по дате."""
        return GetBirthdaysByDateUseCase(mock_birthday_repo)

    @pytest.mark.asyncio
    async def test_get_birthdays_by_date_success(self, use_case, mock_birthday_repo):
        """Тест успешного получения дней рождения по дате."""
        # Arrange
        check_date = date(2024, 5, 15)
        birthdays = [
            Birthday(
                id=1,
                full_name="Иван Иванов",
                company="ООО Тест",
                position="Разработчик",
                birth_date=date(1990, 5, 15),
                comment="Комментарий",
            ),
            Birthday(
                id=2,
                full_name="Петр Петров",
                company="ООО Тест",
                position="Менеджер",
                birth_date=date(1985, 5, 15),
                comment=None,
            ),
        ]
        mock_birthday_repo.get_by_date.return_value = birthdays

        # Act
        result = await use_case.execute(check_date)

        # Assert
        assert len(result) == 2
        assert result[0].id == 1
        assert result[0].full_name == "Иван Иванов"
        assert result[1].id == 2
        assert result[1].full_name == "Петр Петров"
        mock_birthday_repo.get_by_date.assert_called_once_with(check_date)

    @pytest.mark.asyncio
    async def test_get_birthdays_by_date_empty(self, use_case, mock_birthday_repo):
        """Тест получения дней рождения для даты без результатов."""
        # Arrange
        check_date = date(2024, 6, 1)
        mock_birthday_repo.get_by_date.return_value = []

        # Act
        result = await use_case.execute(check_date)

        # Assert
        assert len(result) == 0
        assert result == []
        mock_birthday_repo.get_by_date.assert_called_once_with(check_date)

    @pytest.mark.asyncio
    async def test_get_birthdays_by_date_repository_error(self, use_case, mock_birthday_repo):
        """Тест обработки ошибок репозитория."""
        # Arrange
        check_date = date(2024, 5, 15)
        mock_birthday_repo.get_by_date.side_effect = Exception("Database connection error")

        # Act & Assert
        with pytest.raises(Exception, match="Database connection error"):
            await use_case.execute(check_date)

