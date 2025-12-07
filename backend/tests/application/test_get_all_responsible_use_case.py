import pytest
from unittest.mock import AsyncMock

from src.application.use_cases.responsible.get_all_responsible import GetAllResponsibleUseCase
from src.domain.entities.responsible_person import ResponsiblePerson


class TestGetAllResponsibleUseCase:
    """Тесты для use-case получения всех ответственных."""

    @pytest.mark.asyncio
    async def test_get_all_responsible_success(self):
        """Тест успешного получения всех ответственных."""
        # Arrange
        mock_repository = AsyncMock()
        expected_responsible = [
            ResponsiblePerson(
                id=1,
                full_name="Иван Иванов",
                company="ООО Тест",
                position="Менеджер",
            ),
            ResponsiblePerson(
                id=2,
                full_name="Петр Петров",
                company="ООО Другой",
                position="Директор",
            ),
        ]
        mock_repository.get_all.return_value = expected_responsible

        use_case = GetAllResponsibleUseCase(mock_repository)

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
    async def test_get_all_responsible_empty(self):
        """Тест получения всех ответственных, когда список пуст."""
        # Arrange
        mock_repository = AsyncMock()
        mock_repository.get_all.return_value = []

        use_case = GetAllResponsibleUseCase(mock_repository)

        # Act
        result = await use_case.execute()

        # Assert
        assert len(result) == 0
        assert result == []
        mock_repository.get_all.assert_called_once()

