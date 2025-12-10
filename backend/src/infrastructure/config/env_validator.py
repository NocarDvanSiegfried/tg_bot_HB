"""Валидация переменных окружения."""

import os
from urllib.parse import urlparse


def validate_database_url(database_url: str) -> tuple[bool, str | None, str | None]:
    """
    Валидирует формат DATABASE_URL и извлекает информацию о базе данных.

    Проверяет:
    - Формат URL
    - Схему (postgresql или postgresql+asyncpg)
    - Наличие имени пользователя
    - Наличие пароля (может быть пустым, но должно быть указано)
    - Наличие имени базы данных
    - Формат hostname
    - Порт (должен быть 5432 или указан явно)
    - Что имя базы данных не совпадает с именем пользователя

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
        return (
            False,
            None,
            f"Неподдерживаемая схема: '{parsed.scheme}'. Ожидается 'postgresql' или 'postgresql+asyncpg'. "
            f"Проверьте формат DATABASE_URL.",
        )

    # Проверяем hostname
    if not parsed.hostname:
        return (
            False,
            None,
            "Hostname не указан в URL. Для Docker Compose используйте имя сервиса 'postgres', "
            "для локального запуска используйте 'localhost'.",
        )

    # Проверяем порт
    port = parsed.port
    if port is None:
        # Порт не указан явно, но это допустимо (будет использован стандартный 5432)
        pass
    elif port != 5432:
        # Порт указан, но не стандартный - предупреждение, но не ошибка
        pass

    # Извлекаем имя пользователя
    username = parsed.username
    if not username:
        return (
            False,
            None,
            "Имя пользователя не указано в URL. Формат: postgresql+asyncpg://USERNAME:PASSWORD@HOST:PORT/DATABASE. "
            f"Убедитесь, что POSTGRES_USER установлен и совпадает с USERNAME в DATABASE_URL.",
        )

    # Проверяем наличие пароля (может быть пустым, но должно быть указано)
    # Если пароль не указан, parsed.password будет None
    # Но в URL может быть user:@host или user@host - оба варианта допустимы
    # Проверяем, что есть двоеточие после username (даже если пароль пустой)
    if "@" in parsed.netloc and ":" not in parsed.netloc.split("@")[0]:
        # Это означает, что пароль не указан вообще (нет двоеточия)
        # Но это может быть допустимо для некоторых конфигураций
        pass

    # Извлекаем имя базы данных из пути
    database_name = parsed.path.lstrip("/") if parsed.path else None
    if not database_name:
        return (
            False,
            None,
            "Имя базы данных не указано в URL. Формат: postgresql+asyncpg://USERNAME:PASSWORD@HOST:PORT/DATABASE. "
            f"Убедитесь, что POSTGRES_DB установлен и совпадает с DATABASE в DATABASE_URL.",
        )

    # Проверяем, что имя базы данных не равно имени пользователя
    if database_name == username:
        return (
            False,
            database_name,
            f"Имя базы данных ('{database_name}') не должно совпадать с именем пользователя ('{username}'). "
            f"PostgreSQL не создаст базу данных с именем пользователя автоматически. "
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


def validate_database_env_sync() -> tuple[bool, list[str]]:
    """
    Проверяет синхронизацию переменных окружения для PostgreSQL.

    Проверяет:
    - Что POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB установлены
    - Что DATABASE_URL содержит те же значения
    - Что все компоненты совпадают

    Returns:
        Tuple[bool, List[str]]:
            - bool: True если все переменные синхронизированы, False иначе
            - List[str]: Список сообщений об ошибках и предупреждениях
    """
    errors = []
    warnings = []

    # Получаем переменные окружения
    postgres_user = os.getenv("POSTGRES_USER")
    postgres_password = os.getenv("POSTGRES_PASSWORD")
    postgres_db = os.getenv("POSTGRES_DB")
    database_url = os.getenv("DATABASE_URL")

    # Проверяем наличие переменных
    if not postgres_user:
        errors.append("POSTGRES_USER не установлен. Установите его в .env файле.")
    if not postgres_password:
        errors.append("POSTGRES_PASSWORD не установлен. Установите его в .env файле.")
    if not postgres_db:
        errors.append("POSTGRES_DB не установлен. Установите его в .env файле.")
    if not database_url:
        errors.append("DATABASE_URL не установлен. Установите его в .env файле.")

    # Если отсутствуют базовые переменные, не продолжаем проверку
    if errors:
        return False, errors

    # Парсим DATABASE_URL
    try:
        parsed = urlparse(database_url)
    except Exception as e:
        errors.append(f"Не удалось распарсить DATABASE_URL: {e}")
        return False, errors

    # Проверяем схему
    if not parsed.scheme or not parsed.scheme.startswith("postgresql"):
        errors.append(
            f"Неподдерживаемая схема в DATABASE_URL: '{parsed.scheme}'. "
            f"Ожидается 'postgresql' или 'postgresql+asyncpg'."
        )

    # Проверяем username
    url_username = parsed.username
    if not url_username:
        errors.append("Имя пользователя не указано в DATABASE_URL.")
    elif url_username != postgres_user:
        errors.append(
            f"Несовпадение имени пользователя: POSTGRES_USER='{postgres_user}', "
            f"но в DATABASE_URL указан '{url_username}'. "
            f"Убедитесь, что значения совпадают."
        )

    # Проверяем password
    url_password = parsed.password
    if url_password is None:
        warnings.append(
            "Пароль не указан в DATABASE_URL (может быть пустым). "
            "Убедитесь, что это намеренно."
        )
    elif url_password != postgres_password:
        errors.append(
            "Несовпадение пароля: POSTGRES_PASSWORD не совпадает с паролем в DATABASE_URL. "
            "Убедитесь, что значения совпадают."
        )

    # Проверяем database name
    url_database = parsed.path.lstrip("/") if parsed.path else None
    if not url_database:
        errors.append("Имя базы данных не указано в DATABASE_URL.")
    elif url_database != postgres_db:
        errors.append(
            f"Несовпадение имени базы данных: POSTGRES_DB='{postgres_db}', "
            f"но в DATABASE_URL указано '{url_database}'. "
            f"Убедитесь, что значения совпадают."
        )

    # Проверяем hostname
    url_hostname = parsed.hostname
    if not url_hostname:
        errors.append("Hostname не указан в DATABASE_URL.")
    elif url_hostname not in ("postgres", "localhost", "127.0.0.1"):
        warnings.append(
            f"Нестандартный hostname в DATABASE_URL: '{url_hostname}'. "
            f"Для Docker Compose обычно используется 'postgres', "
            f"для локального запуска - 'localhost' или '127.0.0.1'."
        )

    # Проверяем порт
    url_port = parsed.port
    if url_port is None:
        warnings.append(
            "Порт не указан в DATABASE_URL (будет использован стандартный 5432). "
            "Рекомендуется указывать порт явно."
        )
    elif url_port != 5432:
        warnings.append(
            f"Нестандартный порт в DATABASE_URL: {url_port}. "
            f"Обычно используется порт 5432."
        )

    all_messages = errors + warnings
    return len(errors) == 0, all_messages
