from src.application.ports.holiday_repository import HolidayRepository


class DeleteHolidayUseCase:
    def __init__(self, holiday_repository: HolidayRepository):
        self.holiday_repository = holiday_repository

    async def execute(self, holiday_id: int) -> None:
        """Удалить праздник."""
        existing = await self.holiday_repository.get_by_id(holiday_id)
        if not existing:
            raise ValueError(f"Holiday with id {holiday_id} not found")
        await self.holiday_repository.delete(holiday_id)
