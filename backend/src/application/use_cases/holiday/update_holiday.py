from datetime import date

from src.application.ports.holiday_repository import HolidayRepository
from src.domain.entities.professional_holiday import ProfessionalHoliday


class UpdateHolidayUseCase:
    def __init__(self, holiday_repository: HolidayRepository):
        self.holiday_repository = holiday_repository

    async def execute(
        self,
        holiday_id: int,
        name: str | None = None,
        description: str | None = None,
        date: date | None = None,
    ) -> ProfessionalHoliday:
        """Обновить праздник."""
        existing = await self.holiday_repository.get_by_id(holiday_id)
        if not existing:
            raise ValueError(f"Holiday with id {holiday_id} not found")

        updated = ProfessionalHoliday(
            id=holiday_id,
            name=name if name is not None else existing.name,
            description=description if description is not None else existing.description,
            date=date if date is not None else existing.date,
        )
        return await self.holiday_repository.update(updated)

