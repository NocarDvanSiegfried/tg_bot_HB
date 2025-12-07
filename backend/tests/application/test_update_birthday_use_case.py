import pytest
from datetime import date
from unittest.mock import AsyncMock

from src.application.use_cases.birthday.update_birthday import UpdateBirthdayUseCase
from src.domain.entities.birthday import Birthday


class TestUpdateBirthdayUseCase:
    """Тесты для use-case обновления дня рождения."""

    @pytest.mark.asyncio
    async def test_update_birthday_success(self):
        """Тест успешного обновления дня рождения."""
        # Arrange
        existing_birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment="Старый комментарий",
        )

        updated_birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Новое",
            position="Старший разработчик",
            birth_date=date(1990, 5, 15),
            comment="Новый комментарий",
        )

        mock_repository = AsyncMock()
        mock_repository.get_by_id.return_value = existing_birthday
        mock_repository.update.return_value = updated_birthday

        use_case = UpdateBirthdayUseCase(mock_repository)

        # Act
        result = await use_case.execute(
            birthday_id=1,
            company="ООО Новое",
            position="Старший разработчик",
            comment="Новый комментарий",
        )

        # Assert
        assert result.company == "ООО Новое"
        assert result.position == "Старший разработчик"
        assert result.comment == "Новый комментарий"
        assert result.full_name == "Иван Иванов"  # Не изменилось
        mock_repository.get_by_id.assert_called_once_with(1)
        mock_repository.update.assert_called_once()

    @pytest.mark.asyncio
    async def test_update_birthday_not_found(self):
        """Тест обновления несуществующего дня рождения."""
        # Arrange
        mock_repository = AsyncMock()
        mock_repository.get_by_id.return_value = None

        use_case = UpdateBirthdayUseCase(mock_repository)

        # Act & Assert
        with pytest.raises(ValueError, match="Birthday with id 999 not found"):
            await use_case.execute(
                birthday_id=999,
                full_name="Новое имя",
            )

