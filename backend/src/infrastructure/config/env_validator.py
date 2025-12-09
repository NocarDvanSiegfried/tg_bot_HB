"""Валидация переменных окружения."""

from urllib.parse import urlparse


def validate_database_url(database_url: str) -> tuple[bool, str | None, str | None]:
    """
    Валидирует формат DATABASE_URL и извлекает информацию о базе данных.

    Args:
        database_url: URL базы данных для валидации

    Returns:
        Tuple[bool, Optional[str], Optional[str]]:
            - bool: True если URL валиден, False иначе
            - Optional[str]: Имя базы данных (если извлечено)
            - Optional[str]: Сообщение об ошибке (если есть)
    """
    if not database_url or not database_url.strip():
        return False, None, "DATABASE_URL не может быть пустым"

    # Проверяем формат URL
    try:
        parsed = urlparse(database_url)
    except Exception as e:
        return False, None, f"Неверный формат URL: {e}"

    # Проверяем схему (должна быть postgresql+asyncpg или postgresql)
    if not parsed.scheme or not parsed.scheme.startswith("postgresql"):
        return False, None, f"Неподдерживаемая схема: {parsed.scheme}. Ожидается postgresql или postgresql+asyncpg"

    # Извлекаем имя базы данных из пути
    database_name = parsed.path.lstrip("/") if parsed.path else None

    if not database_name:
        return False, None, "Имя базы данных не указано в URL"

    # Извлекаем имя пользователя
    username = parsed.username

    if not username:
        return False, None, "Имя пользователя не указано в URL"

    # Проверяем, что имя базы данных не равно имени пользователя
    if database_name == username:
        return (
            False,
            database_name,
            f"Имя базы данных ('{database_name}') не должно совпадать с именем пользователя ('{username}'). "
            f"Используйте POSTGRES_DB для имени базы данных, а не POSTGRES_USER.",
        )

    return True, database_name, None


def get_database_name_from_url(database_url: str) -> str | None:
    """
    Извлекает имя базы данных из DATABASE_URL.

    Args:
        database_url: URL базы данных

    Returns:
        Optional[str]: Имя базы данных или None если не удалось извлечь
    """
    try:
        parsed = urlparse(database_url)
        database_name = parsed.path.lstrip("/") if parsed.path else None
        return database_name
    except Exception:
        return None


def mask_database_url(database_url: str) -> str:
    """
    Маскирует пароль в DATABASE_URL для безопасного логирования.

    Args:
        database_url: URL базы данных

    Returns:
        str: URL с замаскированным паролем
    """
    if not database_url:
        return ""

    try:
        parsed = urlparse(database_url)
        if parsed.password:
            # Заменяем пароль на звездочки
            masked_netloc = f"{parsed.username}:***@{parsed.hostname}"
            if parsed.port:
                masked_netloc += f":{parsed.port}"
            return parsed._replace(netloc=masked_netloc).geturl()
        return database_url
    except Exception:
        # Если не удалось распарсить, возвращаем как есть
        return database_url


def validate_telegram_token(token: str) -> tuple[bool, str | None]:
    """
    Валидирует формат Telegram Bot Token.

    Telegram токены имеют формат: число:строка (например, "123456789:ABCdefGHIjklMNOpqrsTUVwxyz")
    Минимальная длина токена обычно около 40 символов.

    Args:
        token: Telegram Bot Token для валидации

    Returns:
        Tuple[bool, Optional[str]]:
            - bool: True если токен валиден по формату, False иначе
            - Optional[str]: Сообщение об ошибке (если есть)
    """
    if not token or not token.strip():
        return False, "TELEGRAM_BOT_TOKEN не может быть пустым"

    token = token.strip()

    # Проверяем базовый формат: число:строка
    if ":" not in token:
        return (
            False,
            "TELEGRAM_BOT_TOKEN имеет неверный формат. Ожидается формат: число:строка (например, '123456789:ABCdefGHIjklMNOpqrsTUVwxyz'). "
            "Получите токен от @BotFather в Telegram.",
        )

    parts = token.split(":", 1)
    if len(parts) != 2:
        return (
            False,
            "TELEGRAM_BOT_TOKEN имеет неверный формат. Ожидается формат: число:строка. "
            "Получите токен от @BotFather в Telegram.",
        )

    bot_id, token_part = parts

    # Проверяем, что первая часть - число
    if not bot_id.isdigit():
        return (
            False,
            "TELEGRAM_BOT_TOKEN: первая часть (ID бота) должна быть числом. "
            "Получите токен от @BotFather в Telegram.",
        )

    # Проверяем минимальную длину токена
    if len(token) < 35:
        return (
            False,
            f"TELEGRAM_BOT_TOKEN слишком короткий ({len(token)} символов). Минимальная длина обычно 40+ символов. "
            "Убедитесь, что вы скопировали полный токен от @BotFather.",
        )

    # Проверяем, что это не placeholder
    placeholder_patterns = [
        "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz1234567890",
        "your_bot_token_here",
        "YOUR_BOT_TOKEN",
        "test_token",
    ]
    if token in placeholder_patterns:
        return (
            False,
            "TELEGRAM_BOT_TOKEN содержит placeholder значение. "
            "Замените его на реальный токен, полученный от @BotFather в Telegram. "
            "Инструкция: https://core.telegram.org/bots/tutorial#obtain-your-bot-token",
        )

    return True, None
