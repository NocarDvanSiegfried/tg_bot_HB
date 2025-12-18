from datetime import date

from src.application.ports.birthday_repository import BirthdayRepository
from src.domain.entities.birthday import Birthday


class GetBirthdaysByDateUseCase:
    def __init__(self, birthday_repository: BirthdayRepository):
        self.birthday_repository = birthday_repository

    async def execute(self, check_date: date) -> list[Birthday]:
        """Получить дни рождения на указанную дату."""
        # Используем поиск по дню и месяцу, игнорируя год
        return await self.birthday_repository.get_by_day_and_month(
            check_date.day, check_date.month
        )
