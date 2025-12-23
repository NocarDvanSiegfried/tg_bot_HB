from datetime import date

from src.application.ports.birthday_repository import BirthdayRepository
from src.domain.entities.birthday import Birthday


class CreateBirthdayUseCase:
    def __init__(self, birthday_repository: BirthdayRepository):
        self.birthday_repository = birthday_repository

    async def execute(
        self,
        full_name: str,
        company: str,
        position: str,
        birth_date: date,
        comment: str | None = None,
        responsible: str | None = None,
    ) -> Birthday:
        """Создать новый день рождения."""
        birthday = Birthday(
            id=None,
            full_name=full_name,
            company=company,
            position=position,
            birth_date=birth_date,
            comment=comment,
            responsible=responsible,
        )
        return await self.birthday_repository.create(birthday)
