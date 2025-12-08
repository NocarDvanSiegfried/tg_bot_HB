from datetime import date

from src.application.ports.birthday_repository import BirthdayRepository
from src.domain.entities.birthday import Birthday


class GetBirthdaysByDateUseCase:
    def __init__(self, birthday_repository: BirthdayRepository):
        self.birthday_repository = birthday_repository

    async def execute(self, check_date: date) -> list[Birthday]:
        """Получить дни рождения на указанную дату."""
        return await self.birthday_repository.get_by_date(check_date)
