from abc import ABC, abstractmethod
from typing import Optional


class OpenRouterClient(ABC):
    @abstractmethod
    async def generate_greeting(
        self,
        person_name: str,
        person_company: str,
        person_position: str,
        style: str,
        length: str,
        theme: Optional[str] = None,
    ) -> str:
        """Сгенерировать поздравление через DeepSeek."""
        pass

