import logging

from src.application.ports.telegram_auth_service import TelegramAuthService

logger = logging.getLogger(__name__)


class VerifyTelegramAuthUseCase:
    """Use-case для верификации Telegram WebApp initData."""

    def __init__(self, auth_service: TelegramAuthService, bot_token: str):
        self.auth_service = auth_service
        self.bot_token = bot_token

    async def execute(self, init_data: str) -> dict:
        """Верифицировать initData и вернуть данные пользователя."""
        logger.debug(f"Starting init_data verification (length={len(init_data)})")

        # Проверка формата перед обработкой
        if not init_data or not init_data.strip():
            logger.warning("Empty or whitespace-only init_data in use case")
            raise ValueError("Invalid initData format: empty or whitespace")

        if "=" not in init_data:
            logger.warning("Invalid init_data format: missing '=' separator")
            raise ValueError("Invalid initData format: expected query string format")

        # Этап 1: Верификация подписи
        logger.debug("Step 1: Verifying init_data signature")
        is_valid = self.auth_service.verify_init_data(init_data, self.bot_token)
        if not is_valid:
            logger.warning(
                f"InitData signature verification failed (init_data_length={len(init_data)})"
            )
            raise ValueError("Invalid initData signature: verification failed")

        logger.debug("Step 2: Signature verification passed, parsing user data")

        # Этап 2: Парсинг данных пользователя
        try:
            user_data = self.auth_service.parse_init_data(init_data)
            if not user_data:
                logger.warning("Parsed init_data returned empty user_data")
                raise ValueError("Invalid initData: missing required user fields")

            user_id = user_data.get("id")
            if not user_id:
                logger.warning("Parsed user_data missing 'id' field")
                raise ValueError("Invalid initData: missing required 'id' field in user data")

            logger.info(f"Successfully verified and parsed init_data for user_id={user_id}")
            return user_data
        except ValueError:
            # Перебрасываем ValueError как есть
            raise
        except Exception as e:
            logger.error(f"Unexpected error during init_data parsing: {type(e).__name__}: {e}", exc_info=True)
            raise ValueError(f"Invalid initData format: unable to parse - {str(e)}") from e
