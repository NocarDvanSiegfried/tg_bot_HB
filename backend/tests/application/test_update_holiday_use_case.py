import pytest
from datetime import date
from unittest.mock import AsyncMock

from src.application.use_cases.holiday.update_holiday import UpdateHolidayUseCase
from src.domain.entities.professional_holiday import ProfessionalHoliday


class TestUpdateHolidayUseCase:
    """Тесты для use-case обновления праздника."""

    @pytest.mark.asyncio
    async def test_update_holiday_success(self):
        """Тест успешного обновления праздника."""
        # Arrange
        mock_repository = AsyncMock()
        existing_holiday = ProfessionalHoliday(
            id=1,
            name="День программиста",
            description="Старое описание",
            date=date(2024, 9, 13),
        )
        updated_holiday = ProfessionalHoliday(
            id=1,
            name="День программиста",
            description="Новое описание",
            date=date(2024, 9, 13),
        )
        
        mock_repository.get_by_id.return_value = existing_holiday
        mock_repository.update.return_value = updated_holiday

        use_case = UpdateHolidayUseCase(mock_repository)

        # Act
        result = await use_case.execute(
            holiday_id=1,
            description="Новое описание",
        )

        # Assert
        assert result.description == "Новое описание"
        mock_repository.get_by_id.assert_called_once_with(1)
        mock_repository.update.assert_called_once()

    @pytest.mark.asyncio
    async def test_update_holiday_partial(self):
        """Тест частичного обновления праздника."""
        # Arrange
        mock_repository = AsyncMock()
        existing_holiday = ProfessionalHoliday(
            id=1,
            name="День программиста",
            description="Описание",
            date=date(2024, 9, 13),
        )
        updated_holiday = ProfessionalHoliday(
            id=1,
            name="День программиста",
            description="Описание",
            date=date(2024, 10, 1),
        )
        
        mock_repository.get_by_id.return_value = existing_holiday
        mock_repository.update.return_value = updated_holiday

        use_case = UpdateHolidayUseCase(mock_repository)

        # Act
        result = await use_case.execute(
            holiday_id=1,
            date=date(2024, 10, 1),
        )

        # Assert
        assert result.date == date(2024, 10, 1)
        assert result.name == "День программиста"  # Не изменилось

    @pytest.mark.asyncio
    async def test_update_holiday_not_found(self):
        """Тест обновления несуществующего праздника."""
        # Arrange
        mock_repository = AsyncMock()
        mock_repository.get_by_id.return_value = None

        use_case = UpdateHolidayUseCase(mock_repository)

        # Act & Assert
        with pytest.raises(ValueError, match="Holiday with id 999 not found"):
            await use_case.execute(holiday_id=999, name="Новое имя")
        
        mock_repository.update.assert_not_called()

