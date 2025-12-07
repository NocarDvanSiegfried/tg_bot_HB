import pytest
from datetime import date
from unittest.mock import AsyncMock

from src.application.use_cases.birthday.delete_birthday import DeleteBirthdayUseCase
from src.domain.entities.birthday import Birthday


class TestDeleteBirthdayUseCase:
    """Тесты для use-case удаления дня рождения."""

    @pytest.mark.asyncio
    async def test_delete_birthday_success(self):
        """Тест успешного удаления дня рождения."""
        # Arrange
        existing_birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )

        mock_repository = AsyncMock()
        mock_repository.get_by_id.return_value = existing_birthday
        mock_repository.delete.return_value = None

        use_case = DeleteBirthdayUseCase(mock_repository)

        # Act
        await use_case.execute(1)

        # Assert
        mock_repository.get_by_id.assert_called_once_with(1)
        mock_repository.delete.assert_called_once_with(1)

    @pytest.mark.asyncio
    async def test_delete_birthday_not_found(self):
        """Тест удаления несуществующего дня рождения."""
        # Arrange
        mock_repository = AsyncMock()
        mock_repository.get_by_id.return_value = None

        use_case = DeleteBirthdayUseCase(mock_repository)

        # Act & Assert
        with pytest.raises(ValueError, match="Birthday with id 999 not found"):
            await use_case.execute(999)

