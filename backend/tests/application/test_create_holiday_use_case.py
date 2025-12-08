import pytest
from datetime import date
from unittest.mock import AsyncMock

from src.application.use_cases.holiday.create_holiday import CreateHolidayUseCase
from src.domain.entities.professional_holiday import ProfessionalHoliday


class TestCreateHolidayUseCase:
    """Тесты для use-case создания праздника."""

    @pytest.mark.asyncio
    async def test_create_holiday_success(self):
        """Тест успешного создания праздника."""
        # Arrange
        mock_repository = AsyncMock()
        expected_holiday = ProfessionalHoliday(
            id=1,
            name="День программиста",
            description="Профессиональный праздник",
            date=date(2024, 9, 13),
        )
        mock_repository.create.return_value = expected_holiday

        use_case = CreateHolidayUseCase(mock_repository)

        # Act
        result = await use_case.execute(
            name="День программиста",
            date=date(2024, 9, 13),
            description="Профессиональный праздник",
        )

        # Assert
        assert result.id == 1
        assert result.name == "День программиста"
        assert result.description == "Профессиональный праздник"
        assert result.date == date(2024, 9, 13)
        mock_repository.create.assert_called_once()

    @pytest.mark.asyncio
    async def test_create_holiday_without_description(self):
        """Тест создания праздника без описания."""
        # Arrange
        mock_repository = AsyncMock()
        expected_holiday = ProfessionalHoliday(
            id=1,
            name="День программиста",
            description=None,
            date=date(2024, 9, 13),
        )
        mock_repository.create.return_value = expected_holiday

        use_case = CreateHolidayUseCase(mock_repository)

        # Act
        result = await use_case.execute(
            name="День программиста",
            date=date(2024, 9, 13),
            description=None,
        )

        # Assert
        assert result.description is None
        mock_repository.create.assert_called_once()

