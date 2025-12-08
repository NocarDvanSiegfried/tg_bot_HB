import pytest
from datetime import date
from unittest.mock import AsyncMock

from src.application.use_cases.responsible.assign_responsible_to_date import AssignResponsibleToDateUseCase
from src.domain.entities.responsible_person import ResponsiblePerson


class TestAssignResponsibleToDateUseCase:
    """Тесты для use-case назначения ответственного лица на дату."""

    @pytest.mark.asyncio
    async def test_assign_responsible_success(self):
        """Тест успешного назначения ответственного лица."""
        # Arrange
        mock_repository = AsyncMock()
        responsible = ResponsiblePerson(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Менеджер",
        )
        mock_repository.get_by_id.return_value = responsible

        use_case = AssignResponsibleToDateUseCase(mock_repository)

        # Act
        await use_case.execute(
            responsible_id=1,
            assignment_date=date(2024, 5, 15),
        )

        # Assert
        mock_repository.get_by_id.assert_called_once_with(1)
        mock_repository.assign_to_date.assert_called_once_with(1, date(2024, 5, 15))

    @pytest.mark.asyncio
    async def test_assign_responsible_not_found(self):
        """Тест назначения несуществующего ответственного лица."""
        # Arrange
        mock_repository = AsyncMock()
        mock_repository.get_by_id.return_value = None

        use_case = AssignResponsibleToDateUseCase(mock_repository)

        # Act & Assert
        with pytest.raises(ValueError, match="Responsible with id 999 not found"):
            await use_case.execute(
                responsible_id=999,
                assignment_date=date(2024, 5, 15),
            )
        
        mock_repository.assign_to_date.assert_not_called()

