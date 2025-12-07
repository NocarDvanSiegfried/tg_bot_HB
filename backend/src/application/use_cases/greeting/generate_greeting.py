from typing import Optional

from src.application.ports.birthday_repository import BirthdayRepository
from src.application.ports.openrouter_client import OpenRouterClient


class GenerateGreetingUseCase:
    def __init__(
        self,
        birthday_repository: BirthdayRepository,
        openrouter_client: OpenRouterClient,
    ):
        self.birthday_repository = birthday_repository
        self.openrouter_client = openrouter_client

    async def execute(
        self,
        birthday_id: int,
        style: str,
        length: str,
        theme: Optional[str] = None,
    ) -> str:
        """Сгенерировать поздравление для сотрудника."""
        birthday = await self.birthday_repository.get_by_id(birthday_id)
        if not birthday:
            raise ValueError(f"Birthday with id {birthday_id} not found")

        return await self.openrouter_client.generate_greeting(
            person_name=birthday.full_name,
            person_company=birthday.company,
            person_position=birthday.position,
            style=style,
            length=length,
            theme=theme,
        )

