from abc import ABC, abstractmethod
from typing import Optional


class CardGeneratorPort(ABC):
    """Порт для генерации открыток."""

    @abstractmethod
    def generate_card(
        self,
        full_name: str,
        company: str,
        position: str,
        greeting_text: str,
        comment: Optional[str] = None,
        qr_url: Optional[str] = None,
    ) -> bytes:
        """Сгенерировать открытку."""
        pass

