
from src.application.ports.telegram_auth_service import TelegramAuthService


class VerifyTelegramAuthUseCase:
    """Use-case для верификации Telegram WebApp initData."""

    def __init__(self, auth_service: TelegramAuthService, bot_token: str):
        self.auth_service = auth_service
        self.bot_token = bot_token

    async def execute(self, init_data: str) -> dict:
        """Верифицировать initData и вернуть данные пользователя."""
        if not self.auth_service.verify_init_data(init_data, self.bot_token):
            raise ValueError("Invalid initData")

        user_data = self.auth_service.parse_init_data(init_data)
        return user_data or {}

