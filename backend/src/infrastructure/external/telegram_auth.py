import hashlib
import hmac
import json
import logging
import urllib.parse

from src.application.ports.telegram_auth_service import TelegramAuthService

logger = logging.getLogger(__name__)


class TelegramAuthServiceImpl(TelegramAuthService):
    """Реализация сервиса верификации Telegram WebApp initData."""

    def verify_init_data(self, init_data: str, bot_token: str) -> bool:
        """Верифицировать initData от Telegram WebApp через HMAC SHA256."""
        try:
            # Парсим init_data
            parsed_data = urllib.parse.parse_qs(init_data)

            # Извлекаем hash
            received_hash = parsed_data.get("hash", [None])[0]
            if not received_hash:
                logger.debug("verify_init_data: hash field missing in init_data")
                return False

            # Удаляем hash из данных и формируем строку для проверки
            data_check_string = []
            for key in sorted(parsed_data.keys()):
                if key != "hash":
                    data_check_string.append(f"{key}={parsed_data[key][0]}")

            data_check_string = "\n".join(data_check_string)

            # Вычисляем секретный ключ
            secret_key = hmac.new(b"WebAppData", bot_token.encode(), hashlib.sha256).digest()

            # Вычисляем hash
            calculated_hash = hmac.new(
                secret_key, data_check_string.encode(), hashlib.sha256
            ).hexdigest()

            # Сравниваем
            is_valid = calculated_hash == received_hash
            if not is_valid:
                logger.debug(
                    f"verify_init_data: signature mismatch (calculated_hash={calculated_hash[:16]}..., "
                    f"received_hash={received_hash[:16]}...)"
                )
            return is_valid
        except (ValueError, KeyError, IndexError, TypeError) as e:
            logger.warning(f"verify_init_data: parsing error - {type(e).__name__}: {e}")
            return False
        except UnicodeEncodeError as e:
            logger.warning(f"verify_init_data: encoding error - {e}")
            return False
        except Exception as e:
            logger.error(f"verify_init_data: unexpected error - {type(e).__name__}: {e}", exc_info=True)
            return False

    def parse_init_data(self, init_data: str) -> dict | None:
        """Парсить initData и извлечь данные пользователя."""
        try:
            parsed = urllib.parse.parse_qs(init_data)
            user_data = {}

            if "user" in parsed:
                try:
                    user_data = json.loads(parsed["user"][0])
                    logger.debug(f"parse_init_data: successfully parsed user data (user_id={user_data.get('id', 'unknown')})")
                except json.JSONDecodeError as e:
                    logger.warning(f"parse_init_data: JSON decode error in user field - {e}")
                    return None
            else:
                logger.debug("parse_init_data: 'user' field missing in parsed data")

            return user_data if user_data else None
        except (ValueError, KeyError, IndexError, TypeError) as e:
            logger.warning(f"parse_init_data: parsing error - {type(e).__name__}: {e}")
            return None
        except Exception as e:
            logger.error(f"parse_init_data: unexpected error - {type(e).__name__}: {e}", exc_info=True)
            return None


# Функции для обратной совместимости (deprecated, использовать TelegramAuthServiceImpl)
import warnings


def verify_telegram_init_data(init_data: str, bot_token: str) -> bool:
    """Верифицировать initData от Telegram WebApp через HMAC SHA256 (deprecated).
    
    .. deprecated:: 1.0.0
        Используйте :class:`TelegramAuthServiceImpl` вместо этой функции.
        Пример:
            service = TelegramAuthServiceImpl()
            service.verify_init_data(init_data, bot_token)
    
    Args:
        init_data: InitData строка от Telegram WebApp
        bot_token: Токен Telegram бота
        
    Returns:
        bool: True если initData валиден, False иначе
        
    .. warning::
        Эта функция устарела и будет удалена в будущих версиях.
        Используйте TelegramAuthServiceImpl для новых проектов.
    """
    warnings.warn(
        "verify_telegram_init_data() is deprecated. "
        "Use TelegramAuthServiceImpl.verify_init_data() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    service = TelegramAuthServiceImpl()
    return service.verify_init_data(init_data, bot_token)


def parse_init_data(init_data: str) -> dict | None:
    """Парсить initData и извлечь данные пользователя (deprecated).
    
    .. deprecated:: 1.0.0
        Используйте :class:`TelegramAuthServiceImpl` вместо этой функции.
        Пример:
            service = TelegramAuthServiceImpl()
            service.parse_init_data(init_data)
    
    Args:
        init_data: InitData строка от Telegram WebApp
        
    Returns:
        dict | None: Словарь с данными пользователя или None если невалидно
        
    .. warning::
        Эта функция устарела и будет удалена в будущих версиях.
        Используйте TelegramAuthServiceImpl для новых проектов.
    """
    warnings.warn(
        "parse_init_data() is deprecated. "
        "Use TelegramAuthServiceImpl.parse_init_data() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    service = TelegramAuthServiceImpl()
    return service.parse_init_data(init_data)


def get_user_id_from_init_data(init_data: str) -> int | None:
    """Извлечь user_id из initData (deprecated).
    
    .. deprecated:: 1.0.0
        Используйте :class:`TelegramAuthServiceImpl` вместо этой функции.
        Пример:
            service = TelegramAuthServiceImpl()
            user_data = service.parse_init_data(init_data)
            user_id = user_data.get("id") if user_data else None
    
    Args:
        init_data: InitData строка от Telegram WebApp
        
    Returns:
        int | None: ID пользователя или None если невалидно
        
    .. warning::
        Эта функция устарела и будет удалена в будущих версиях.
        Используйте TelegramAuthServiceImpl для новых проектов.
    """
    warnings.warn(
        "get_user_id_from_init_data() is deprecated. "
        "Use TelegramAuthServiceImpl.parse_init_data() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    service = TelegramAuthServiceImpl()
    user_data = service.parse_init_data(init_data)
    if user_data and "id" in user_data:
        return user_data["id"]
    return None
