from datetime import date

from src.application.ports.birthday_repository import BirthdayRepository
from src.domain.entities.birthday import Birthday


class UpdateBirthdayUseCase:
    def __init__(self, birthday_repository: BirthdayRepository):
        self.birthday_repository = birthday_repository

    async def execute(
        self,
        birthday_id: int,
        full_name: str | None = None,
        company: str | None = None,
        position: str | None = None,
        birth_date: date | None = None,
        comment: str | None = None,
        responsible: str | None = None,
    ) -> Birthday:
        """Обновить день рождения."""
        existing = await self.birthday_repository.get_by_id(birthday_id)
        if not existing:
            raise ValueError(f"Birthday with id {birthday_id} not found")

        # Обработка comment: если пустая строка, использовать None; если None, сохранить существующий
        comment_value = existing.comment
        if comment is not None:
            if comment.strip():  # Если не пустая после trim
                comment_value = comment.strip()
            else:  # Если пустая строка
                comment_value = None  # Использовать None вместо пустой строки

        # Обработка responsible: если пустая строка, использовать None; если None, сохранить существующий
        responsible_value = existing.responsible
        if responsible is not None:
            if responsible.strip():  # Если не пустая после trim
                responsible_value = responsible.strip()
            else:  # Если пустая строка
                responsible_value = None  # Использовать None вместо пустой строки

        updated = Birthday(
            id=birthday_id,
            full_name=full_name if full_name is not None else existing.full_name,
            company=company if company is not None else existing.company,
            position=position if position is not None else existing.position,
            birth_date=birth_date if birth_date is not None else existing.birth_date,
            comment=comment_value,
            responsible=responsible_value,
        )
        return await self.birthday_repository.update(updated)
