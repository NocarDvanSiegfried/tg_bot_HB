from typing import List

from src.application.ports.birthday_repository import BirthdayRepository
from src.domain.entities.birthday import Birthday


class GetAllBirthdaysUseCase:
    """Use-case для получения всех дней рождения."""

    def __init__(self, birthday_repository: BirthdayRepository):
        self.birthday_repository = birthday_repository

    async def execute(self) -> List[Birthday]:
        """Получить все дни рождения."""
        return await self.birthday_repository.get_all()

