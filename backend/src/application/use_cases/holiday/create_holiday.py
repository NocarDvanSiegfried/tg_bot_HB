from datetime import date
from typing import Optional

from src.application.ports.holiday_repository import HolidayRepository
from src.domain.entities.professional_holiday import ProfessionalHoliday


class CreateHolidayUseCase:
    def __init__(self, holiday_repository: HolidayRepository):
        self.holiday_repository = holiday_repository

    async def execute(
        self,
        name: str,
        date: date,
        description: Optional[str] = None,
    ) -> ProfessionalHoliday:
        """Создать новый профессиональный праздник."""
        holiday = ProfessionalHoliday(
            id=None,
            name=name,
            description=description,
            date=date,
        )
        return await self.holiday_repository.create(holiday)

