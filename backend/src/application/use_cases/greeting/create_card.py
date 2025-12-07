from typing import Optional

from src.application.ports.birthday_repository import BirthdayRepository
from src.application.ports.card_generator import CardGeneratorPort
from src.domain.exceptions.not_found import BirthdayNotFoundError


class CreateCardUseCase:
    def __init__(
        self,
        birthday_repository: BirthdayRepository,
        card_generator: CardGeneratorPort,
    ):
        self.birthday_repository = birthday_repository
        self.card_generator = card_generator

    async def execute(
        self,
        birthday_id: int,
        greeting_text: str,
        qr_url: Optional[str] = None,
    ) -> bytes:
        """Создать открытку для сотрудника."""
        birthday = await self.birthday_repository.get_by_id(birthday_id)
        if not birthday:
            raise BirthdayNotFoundError(f"Birthday with id {birthday_id} not found")

        return self.card_generator.generate_card(
            full_name=birthday.full_name,
            company=birthday.company,
            position=birthday.position,
            greeting_text=greeting_text,
            comment=birthday.comment,
            qr_url=qr_url,
        )

