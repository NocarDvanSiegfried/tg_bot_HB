from abc import ABC, abstractmethod


class CardGeneratorPort(ABC):
    """Порт для генерации открыток."""

    @abstractmethod
    def generate_card(
        self,
        full_name: str,
        company: str,
        position: str,
        greeting_text: str,
        comment: str | None = None,
        qr_url: str | None = None,
    ) -> bytes:
        """Сгенерировать открытку."""
        pass











