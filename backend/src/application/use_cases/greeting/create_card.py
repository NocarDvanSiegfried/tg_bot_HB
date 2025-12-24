import logging

from src.application.ports.birthday_repository import BirthdayRepository
from src.application.ports.card_generator import CardGeneratorPort
from src.domain.exceptions.not_found import BirthdayNotFoundError
from src.domain.exceptions.validation import (
    EmptyGreetingTextError,
    InvalidGreetingTextError,
    TextTooLongError,
)

logger = logging.getLogger(__name__)


class CreateCardUseCase:
    def __init__(
        self,
        birthday_repository: BirthdayRepository,
        card_generator: CardGeneratorPort,
    ):
        self.birthday_repository = birthday_repository
        self.card_generator = card_generator

    def _validate_greeting_text(self, text: str) -> None:
        """Валидировать текст поздравления перед генерацией карточки."""
        # Проверка на пустой текст
        if not text or not text.strip():
            logger.warning("[CreateCardUseCase] Empty greeting text provided")
            raise EmptyGreetingTextError("Текст поздравления не может быть пустым")

        # Проверка кодировки (должен быть валидный UTF-8)
        try:
            text.encode('utf-8')
        except UnicodeEncodeError:
            logger.warning("[CreateCardUseCase] Invalid UTF-8 encoding in greeting text")
            raise InvalidGreetingTextError("Текст содержит недопустимые символы")

        # Проверка на мусор (слишком много спецсимволов или нечитаемый текст)
        # Проверяем, что есть хотя бы один нормальный абзац
        lines = text.strip().split('\n')
        valid_lines = [line for line in lines if line.strip() and len(line.strip()) > 10]
        if not valid_lines:
            logger.warning("[CreateCardUseCase] No valid paragraphs in greeting text")
            raise InvalidGreetingTextError("Текст должен содержать хотя бы один связный абзац")

        # Проверка на markdown/reasoning (слишком много служебных символов)
        markdown_chars = text.count('*') + text.count('#') + text.count('`') + text.count('[')
        if markdown_chars > len(text) * 0.1:  # Более 10% служебных символов
            logger.warning(f"[CreateCardUseCase] Too many markdown characters in text: {markdown_chars}")
            raise InvalidGreetingTextError("Текст содержит слишком много служебных символов")

        # Проверка длины (строгие лимиты)
        text_length = len(text)
        if text_length > 1200:  # Максимальная длина для длинного поздравления
            logger.warning(f"[CreateCardUseCase] Text too long: {text_length} characters")
            raise TextTooLongError(
                f"Текст слишком длинный ({text_length} символов). "
                f"Максимальная длина: 1200 символов."
            )

    async def execute(
        self,
        birthday_id: int,
        greeting_text: str,
        qr_url: str | None = None,
    ) -> bytes:
        """Создать открытку для сотрудника."""
        # ВАЛИДАЦИЯ: Проверяем текст ПЕРЕД генерацией
        self._validate_greeting_text(greeting_text)

        # Получаем данные о дне рождения
        birthday = await self.birthday_repository.get_by_id(birthday_id)
        if not birthday:
            raise BirthdayNotFoundError(f"Birthday with id {birthday_id} not found")

        # Генерируем карточку с ВАЛИДИРОВАННЫМ текстом
        # ВАЖНО: greeting_text передаётся как есть, без изменений
        logger.info(
            f"[CreateCardUseCase] Generating card for birthday_id={birthday_id}, "
            f"text_length={len(greeting_text)}"
        )
        
        card_bytes = self.card_generator.generate_card(
            full_name=birthday.full_name,
            company=birthday.company,
            position=birthday.position,
            greeting_text=greeting_text,  # Текст передаётся байт-в-байт
            comment=birthday.comment,
            qr_url=qr_url,
        )

        # Проверяем, что карточка сгенерировалась
        if not card_bytes or len(card_bytes) < 100:  # Минимальный размер PNG
            logger.error("[CreateCardUseCase] Generated card is too small or empty")
            raise InvalidGreetingTextError("Не удалось сгенерировать открытку. Попробуйте позже.")

        return card_bytes
