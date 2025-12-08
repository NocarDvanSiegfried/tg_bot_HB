import pytest
from datetime import date
from unittest.mock import AsyncMock

from src.application.use_cases.calendar.get_calendar_data import GetCalendarDataUseCase
from src.domain.entities.birthday import Birthday
from src.domain.entities.professional_holiday import ProfessionalHoliday
from src.domain.entities.responsible_person import ResponsiblePerson


class TestGetCalendarDataUseCase:
    """Тесты для use-case получения данных календаря."""

    @pytest.mark.asyncio
    async def test_get_calendar_data_success(self):
        """Тест успешного получения данных календаря."""
        # Arrange
        mock_birthday_repo = AsyncMock()
        mock_holiday_repo = AsyncMock()
        mock_responsible_repo = AsyncMock()
        
        check_date = date(2024, 5, 15)
        
        birthdays = [
            Birthday(
                id=1,
                full_name="Иван Иванов",
                company="ООО Тест",
                position="Разработчик",
                birth_date=date(1990, 5, 15),
                comment="Комментарий",
            )
        ]
        holidays = [
            ProfessionalHoliday(
                id=1,
                name="День программиста",
                description="Описание",
                date=check_date,
            )
        ]
        responsible = ResponsiblePerson(
            id=1,
            full_name="Петр Петров",
            company="ООО Тест",
            position="Менеджер",
        )
        
        mock_birthday_repo.get_by_date.return_value = birthdays
        mock_holiday_repo.get_by_date.return_value = holidays
        mock_responsible_repo.get_by_date.return_value = responsible
        
        use_case = GetCalendarDataUseCase(
            mock_birthday_repo,
            mock_holiday_repo,
            mock_responsible_repo,
        )

        # Act
        result = await use_case.execute(check_date)

        # Assert
        assert result["date"] == "2024-05-15"
        assert len(result["birthdays"]) == 1
        assert result["birthdays"][0]["id"] == 1
        assert result["birthdays"][0]["full_name"] == "Иван Иванов"
        assert result["birthdays"][0]["age"] == 34
        assert len(result["holidays"]) == 1
        assert result["holidays"][0]["id"] == 1
        assert result["holidays"][0]["name"] == "День программиста"
        assert result["responsible"] is not None
        assert result["responsible"]["id"] == 1
        assert result["responsible"]["full_name"] == "Петр Петров"
        
        mock_birthday_repo.get_by_date.assert_called_once_with(check_date)
        mock_holiday_repo.get_by_date.assert_called_once_with(check_date)
        mock_responsible_repo.get_by_date.assert_called_once_with(check_date)

    @pytest.mark.asyncio
    async def test_get_calendar_data_empty(self):
        """Тест получения данных календаря для пустой даты."""
        # Arrange
        mock_birthday_repo = AsyncMock()
        mock_holiday_repo = AsyncMock()
        mock_responsible_repo = AsyncMock()
        
        check_date = date(2024, 5, 15)
        
        mock_birthday_repo.get_by_date.return_value = []
        mock_holiday_repo.get_by_date.return_value = []
        mock_responsible_repo.get_by_date.return_value = None
        
        use_case = GetCalendarDataUseCase(
            mock_birthday_repo,
            mock_holiday_repo,
            mock_responsible_repo,
        )

        # Act
        result = await use_case.execute(check_date)

        # Assert
        assert result["date"] == "2024-05-15"
        assert result["birthdays"] == []
        assert result["holidays"] == []
        assert result["responsible"] is None

    @pytest.mark.asyncio
    async def test_get_calendar_data_repository_error(self):
        """Тест обработки ошибок репозиториев."""
        # Arrange
        mock_birthday_repo = AsyncMock()
        mock_holiday_repo = AsyncMock()
        mock_responsible_repo = AsyncMock()
        
        check_date = date(2024, 5, 15)
        mock_birthday_repo.get_by_date.side_effect = Exception("Database connection error")
        
        use_case = GetCalendarDataUseCase(
            mock_birthday_repo,
            mock_holiday_repo,
            mock_responsible_repo,
        )

        # Act & Assert
        with pytest.raises(Exception, match="Database connection error"):
            await use_case.execute(check_date)

