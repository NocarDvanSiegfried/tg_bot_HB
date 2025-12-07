import pytest
from datetime import date
from unittest.mock import AsyncMock

from src.application.use_cases.birthday.get_all_birthdays import GetAllBirthdaysUseCase
from src.domain.entities.birthday import Birthday


class TestGetAllBirthdaysUseCase:
    """Тесты для use-case получения всех дней рождения."""

    @pytest.mark.asyncio
    async def test_get_all_birthdays_success(self):
        """Тест успешного получения всех дней рождения."""
        # Arrange
        mock_repository = AsyncMock()
        expected_birthdays = [
            Birthday(
                id=1,
                full_name="Иван Иванов",
                company="ООО Тест",
                position="Разработчик",
                birth_date=date(1990, 5, 15),
                comment="Комментарий 1",
            ),
            Birthday(
                id=2,
                full_name="Петр Петров",
                company="ООО Тест",
                position="Менеджер",
                birth_date=date(1985, 3, 20),
                comment=None,
            ),
        ]
        mock_repository.get_all.return_value = expected_birthdays

        use_case = GetAllBirthdaysUseCase(mock_repository)

        # Act
        result = await use_case.execute()

        # Assert
        assert len(result) == 2
        assert result[0].id == 1
        assert result[0].full_name == "Иван Иванов"
        assert result[1].id == 2
        assert result[1].full_name == "Петр Петров"
        mock_repository.get_all.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_all_birthdays_empty(self):
        """Тест получения всех дней рождения, когда список пуст."""
        # Arrange
        mock_repository = AsyncMock()
        mock_repository.get_all.return_value = []

        use_case = GetAllBirthdaysUseCase(mock_repository)

        # Act
        result = await use_case.execute()

        # Assert
        assert len(result) == 0
        assert result == []
        mock_repository.get_all.assert_called_once()

