from src.application.ports.birthday_repository import BirthdayRepository


class DeleteBirthdayUseCase:
    def __init__(self, birthday_repository: BirthdayRepository):
        self.birthday_repository = birthday_repository

    async def execute(self, birthday_id: int) -> None:
        """Удалить день рождения."""
        existing = await self.birthday_repository.get_by_id(birthday_id)
        if not existing:
            raise ValueError(f"Birthday with id {birthday_id} not found")
        await self.birthday_repository.delete(birthday_id)
