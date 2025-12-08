import pytest
from unittest.mock import AsyncMock

from src.application.use_cases.responsible.create_responsible import CreateResponsibleUseCase
from src.domain.entities.responsible_person import ResponsiblePerson


class TestCreateResponsibleUseCase:
    """Тесты для use-case создания ответственного лица."""

    @pytest.mark.asyncio
    async def test_create_responsible_success(self):
        """Тест успешного создания ответственного лица."""
        # Arrange
        mock_repository = AsyncMock()
        expected_responsible = ResponsiblePerson(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Менеджер",
        )
        mock_repository.create.return_value = expected_responsible

        use_case = CreateResponsibleUseCase(mock_repository)

        # Act
        result = await use_case.execute(
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Менеджер",
        )

        # Assert
        assert result.id == 1
        assert result.full_name == "Иван Иванов"
        assert result.company == "ООО Тест"
        assert result.position == "Менеджер"
        mock_repository.create.assert_called_once()

