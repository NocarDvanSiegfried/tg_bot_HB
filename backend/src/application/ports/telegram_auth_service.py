from abc import ABC, abstractmethod


class TelegramAuthService(ABC):
    """Порт для верификации Telegram WebApp initData."""

    @abstractmethod
    def verify_init_data(self, init_data: str, bot_token: str) -> bool:
        """Верифицировать initData от Telegram WebApp через HMAC SHA256."""
        pass

    @abstractmethod
    def parse_init_data(self, init_data: str) -> dict | None:
        """Парсить initData и извлечь данные пользователя."""
        pass

