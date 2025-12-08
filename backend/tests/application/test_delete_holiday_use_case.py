import pytest
from datetime import date
from unittest.mock import AsyncMock

from src.application.use_cases.holiday.delete_holiday import DeleteHolidayUseCase
from src.domain.entities.professional_holiday import ProfessionalHoliday


class TestDeleteHolidayUseCase:
    """Тесты для use-case удаления праздника."""

    @pytest.mark.asyncio
    async def test_delete_holiday_success(self):
        """Тест успешного удаления праздника."""
        # Arrange
        mock_repository = AsyncMock()
        existing_holiday = ProfessionalHoliday(
            id=1,
            name="День программиста",
            description="Описание",
            date=date(2024, 9, 13),
        )
        mock_repository.get_by_id.return_value = existing_holiday

        use_case = DeleteHolidayUseCase(mock_repository)

        # Act
        await use_case.execute(holiday_id=1)

        # Assert
        mock_repository.get_by_id.assert_called_once_with(1)
        mock_repository.delete.assert_called_once_with(1)

    @pytest.mark.asyncio
    async def test_delete_holiday_not_found(self):
        """Тест удаления несуществующего праздника."""
        # Arrange
        mock_repository = AsyncMock()
        mock_repository.get_by_id.return_value = None

        use_case = DeleteHolidayUseCase(mock_repository)

        # Act & Assert
        with pytest.raises(ValueError, match="Holiday with id 999 not found"):
            await use_case.execute(holiday_id=999)
        
        mock_repository.delete.assert_not_called()

