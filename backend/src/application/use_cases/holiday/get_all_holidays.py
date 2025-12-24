from src.application.ports.holiday_repository import HolidayRepository
from src.domain.entities.professional_holiday import ProfessionalHoliday


class GetAllHolidaysUseCase:
    """Use-case для получения всех профессиональных праздников."""

    def __init__(self, holiday_repository: HolidayRepository):
        self.holiday_repository = holiday_repository

    async def execute(self) -> list[ProfessionalHoliday]:
        """Получить все профессиональные праздники."""
        return await self.holiday_repository.get_all()

