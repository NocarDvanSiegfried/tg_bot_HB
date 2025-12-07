import pytest
from datetime import date
from unittest.mock import AsyncMock

from src.application.use_cases.birthday.create_birthday import CreateBirthdayUseCase
from src.domain.entities.birthday import Birthday


class TestCreateBirthdayUseCase:
    """Тесты для use-case создания дня рождения."""

    @pytest.mark.asyncio
    async def test_create_birthday_success(self):
        """Тест успешного создания дня рождения."""
        # Arrange
        mock_repository = AsyncMock()
        expected_birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment="Комментарий",
        )
        mock_repository.create.return_value = expected_birthday

        use_case = CreateBirthdayUseCase(mock_repository)

        # Act
        result = await use_case.execute(
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment="Комментарий",
        )

        # Assert
        assert result.id == 1
        assert result.full_name == "Иван Иванов"
        assert result.company == "ООО Тест"
        assert result.position == "Разработчик"
        assert result.birth_date == date(1990, 5, 15)
        assert result.comment == "Комментарий"
        mock_repository.create.assert_called_once()

    @pytest.mark.asyncio
    async def test_create_birthday_without_comment(self):
        """Тест создания дня рождения без комментария."""
        # Arrange
        mock_repository = AsyncMock()
        expected_birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )
        mock_repository.create.return_value = expected_birthday

        use_case = CreateBirthdayUseCase(mock_repository)

        # Act
        result = await use_case.execute(
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )

        # Assert
        assert result.comment is None
        mock_repository.create.assert_called_once()

