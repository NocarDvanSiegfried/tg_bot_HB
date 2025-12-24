import logging

from src.application.ports.birthday_repository import BirthdayRepository
from src.application.ports.openrouter_client import OpenRouterClient
from src.domain.exceptions.not_found import BirthdayNotFoundError

logger = logging.getLogger(__name__)


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
        theme: str | None = None,
    ) -> str:
        """Сгенерировать поздравление для сотрудника."""
        logger.info(
            f"[GenerateGreetingUseCase] Starting greeting generation",
            extra={
                "birthday_id": birthday_id,
                "style": style,
                "length": length,
                "theme": theme,
            },
        )

        # Получаем birthday из репозитория
        logger.debug(f"[GenerateGreetingUseCase] Fetching birthday with id {birthday_id}")
        birthday = await self.birthday_repository.get_by_id(birthday_id)
        
        if not birthday:
            logger.warning(
                f"[GenerateGreetingUseCase] Birthday with id {birthday_id} not found in database"
            )
            raise BirthdayNotFoundError(f"Birthday with id {birthday_id} not found")

        logger.info(
            f"[GenerateGreetingUseCase] Birthday found: {birthday.full_name} "
            f"({birthday.company}, {birthday.position})"
        )

        # Генерируем поздравление через OpenRouter
        logger.info(
            f"[GenerateGreetingUseCase] Calling OpenRouter API for greeting generation",
            extra={
                "person_name": birthday.full_name,
                "person_company": birthday.company,
                "person_position": birthday.position,
                "style": style,
                "length": length,
                "theme": theme,
            },
        )

        try:
            greeting_text = await self.openrouter_client.generate_greeting(
                person_name=birthday.full_name,
                person_company=birthday.company,
                person_position=birthday.position,
                style=style,
                length=length,
                theme=theme,
            )
            logger.info(
                f"[GenerateGreetingUseCase] Greeting generated successfully, length: {len(greeting_text)} characters"
            )
            return greeting_text
        except Exception as e:
            # Логируем детальную информацию об ошибке для диагностики
            error_type = type(e).__name__
            error_message = str(e)
            
            logger.error(
                f"[GenerateGreetingUseCase] Error generating greeting via OpenRouter: {error_type}: {error_message}",
                extra={
                    "error_type": error_type,
                    "error_message": error_message,
                    "birthday_id": birthday_id,
                    "person_name": birthday.full_name,
                    "style": style,
                    "length": length,
                    "theme": theme,
                },
                exc_info=True,
            )
            # Пробрасываем исключение дальше для обработки в декораторе
            raise
