import logging
import os
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    WebAppInfo,
)

from src.infrastructure.config.constants import WEBAPP_URL_PLACEHOLDER

logger = logging.getLogger(__name__)


def is_webapp_url_configured(webapp_url: str) -> bool:
    """
    Проверяет, настроен ли URL для Mini App.

    Args:
        webapp_url: URL из переменной окружения TELEGRAM_WEBAPP_URL

    Returns:
        True, если URL настроен и не является placeholder значением
    """
    return bool(webapp_url and webapp_url != WEBAPP_URL_PLACEHOLDER)


def _get_app_version() -> str:
    """
    Получает версию приложения для cache-busting Telegram Mini App.

    Приоритет источников версии:
    1. APP_VERSION из переменных окружения (предпочтительно)
    2. GIT_COMMIT_HASH (короткий, первые 7 символов)
    3. BUILD_TIMESTAMP (unix time как fallback)

    Returns:
        Строка версии для использования в query-параметре
    """
    # Приоритет 1: APP_VERSION из .env
    app_version = os.getenv("APP_VERSION", "").strip()
    if app_version:
        logger.info(f"[Cache-Bust] Using APP_VERSION: {app_version}")
        return app_version

    # Приоритет 2: GIT_COMMIT_HASH (короткий)
    git_hash = os.getenv("GIT_COMMIT_HASH", "").strip()
    if git_hash:
        # Берем первые 7 символов для короткого хеша
        short_hash = git_hash[:7] if len(git_hash) >= 7 else git_hash
        logger.info(f"[Cache-Bust] Using GIT_COMMIT_HASH: {short_hash}")
        return short_hash

    # Приоритет 3: BUILD_TIMESTAMP (unix time)
    build_timestamp = os.getenv("BUILD_TIMESTAMP", "").strip()
    if build_timestamp:
        logger.info(f"[Cache-Bust] Using BUILD_TIMESTAMP: {build_timestamp}")
        return build_timestamp

    # Fallback: текущий unix timestamp
    import time
    fallback_version = str(int(time.time()))
    logger.warning(
        f"[Cache-Bust] No version source found (APP_VERSION, GIT_COMMIT_HASH, BUILD_TIMESTAMP), "
        f"using fallback timestamp: {fallback_version}"
    )
    return fallback_version


def _add_version_query_param(url: str, version: str) -> str:
    """
    Добавляет query-параметр версии к URL для обхода кэша Telegram.

    КРИТИЧНО: Telegram кэширует Mini App по URL. Изменение query-параметра
    используется как принудительный cache-bust, чтобы гарантировать актуальную версию.

    Args:
        url: Исходный URL Mini App
        version: Версия для добавления в query-параметр (строка)

    Returns:
        URL с добавленным query-параметром ?v={version} или &v={version}
    """
    try:
        parsed = urlparse(url)
        query_params = parse_qs(parsed.query)
        # Обновляем или добавляем параметр версии
        query_params['v'] = [str(version)]
        # Формируем новую query-строку
        new_query = urlencode(query_params, doseq=True)
        # Собираем URL обратно
        new_parsed = parsed._replace(query=new_query)
        result_url = urlunparse(new_parsed)
        logger.info(f"[Cache-Bust] Added version parameter to URL: {url} -> {result_url}")
        return result_url
    except Exception as e:
        # В случае ошибки парсинга URL, просто добавляем параметр в конец
        logger.warning(f"[Cache-Bust] Failed to parse URL for version param: {e}, using fallback")
        separator = '&' if '?' in url else '?'
        result_url = f"{url}{separator}v={version}"
        logger.info(f"[Cache-Bust] Added version parameter (fallback): {url} -> {result_url}")
        return result_url


def get_main_menu_keyboard() -> ReplyKeyboardMarkup:
    """Главное меню - кнопка Календарь и Mini App."""
    webapp_url = os.getenv("TELEGRAM_WEBAPP_URL", "")
    buttons = [[KeyboardButton(text="📅 Календарь")]]

    # Добавляем кнопку Mini App, если URL настроен
    if is_webapp_url_configured(webapp_url):
        buttons.append(
            [KeyboardButton(text="🌐 Открыть Mini App", web_app=WebAppInfo(url=webapp_url))]
        )
    else:
        # Логируем предупреждение, если URL не настроен
        logger.warning(
            "TELEGRAM_WEBAPP_URL не настроен или использует значение по умолчанию. "
            "Кнопка Mini App не будет отображаться. "
            "Установите TELEGRAM_WEBAPP_URL в переменных окружения (должен быть HTTPS URL)."
        )

    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
    )
    return keyboard


def get_panel_menu_keyboard() -> InlineKeyboardMarkup:
    """
    Меню панели управления.
    
    КРИТИЧНО: Mini App-first UX - только одна кнопка для открытия Mini App.
    Все CRUD-операции выполняются исключительно внутри Mini App.
    ReplyKeyboardMarkup не используется для избежания дублирования кнопок.
    """
    webapp_url = os.getenv("TELEGRAM_WEBAPP_URL", "")
    inline_keyboard = []

    # КРИТИЧНО: Только одна кнопка - открытие Mini App
    # Передаем start_param="panel" для открытия Mini App в режиме панели управления
    # Добавляем query-параметр версии для обхода кэша Telegram
    if is_webapp_url_configured(webapp_url):
        # Получаем версию автоматически из конфига/env
        app_version = _get_app_version()
        # Добавляем query-параметр версии к URL для обхода кэша
        panel_webapp_url = _add_version_query_param(webapp_url, version=app_version)
        
        inline_keyboard.append(
            [InlineKeyboardButton(
                text="🌐 Открыть панель управления",
                web_app=WebAppInfo(url=panel_webapp_url, start_param="panel")
            )]
        )
    else:
        # Логируем предупреждение, если URL не настроен
        logger.warning(
            "TELEGRAM_WEBAPP_URL не настроен или использует значение по умолчанию. "
            "Кнопка Mini App не будет отображаться в панели управления. "
            "Установите TELEGRAM_WEBAPP_URL в переменных окружения (должен быть HTTPS URL)."
        )

    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    return keyboard


def get_calendar_keyboard() -> InlineKeyboardMarkup:
    """
    Клавиатура для открытия календаря дней рождения.
    
    КРИТИЧНО: Bot = Launcher архитектура.
    - Только одна кнопка для открытия Mini App
    - Без start_param (Mini App всегда открывается в режиме календаря)
    - Все управление выполняется внутри Mini App
    """
    webapp_url = os.getenv("TELEGRAM_WEBAPP_URL", "")
    inline_keyboard = []

    if is_webapp_url_configured(webapp_url):
        # Получаем версию автоматически из конфига/env
        app_version = _get_app_version()
        # Добавляем query-параметр версии к URL для обхода кэша
        calendar_webapp_url = _add_version_query_param(webapp_url, version=app_version)
        
        inline_keyboard.append(
            [InlineKeyboardButton(
                text="🌐 Открыть календарь",
                web_app=WebAppInfo(url=calendar_webapp_url)  # БЕЗ start_param
            )]
        )
    else:
        # Логируем предупреждение, если URL не настроен
        logger.warning(
            "TELEGRAM_WEBAPP_URL не настроен или использует значение по умолчанию. "
            "Кнопка Mini App не будет отображаться. "
            "Установите TELEGRAM_WEBAPP_URL в переменных окружения (должен быть HTTPS URL)."
        )

    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    return keyboard


def get_calendar_navigation_keyboard(year: int, month: int) -> InlineKeyboardMarkup:
    """Навигация по календарю."""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="◀️", callback_data=f"cal_prev_{year}_{month}"),
                InlineKeyboardButton(text=f"{year}-{month:02d}", callback_data="cal_info"),
                InlineKeyboardButton(text="▶️", callback_data=f"cal_next_{year}_{month}"),
            ],
        ]
    )
    return keyboard


def get_birthday_management_keyboard() -> InlineKeyboardMarkup:
    """
    Меню управления ДР.
    
    КРИТИЧНО: CRUD-операции (добавление, редактирование, удаление) 
    выполняются исключительно через Telegram Mini App (панель управления).
    Командный интерфейс бота больше не содержит CRUD-логики.
    """
    webapp_url = os.getenv("TELEGRAM_WEBAPP_URL", "")
    inline_keyboard = []
    
    # Добавляем кнопку Mini App, если URL настроен
    if is_webapp_url_configured(webapp_url):
        app_version = _get_app_version()
        panel_webapp_url = _add_version_query_param(webapp_url, version=app_version)
        
        inline_keyboard.append(
            [InlineKeyboardButton(
                text="🌐 Открыть панель управления",
                web_app=WebAppInfo(url=panel_webapp_url, start_param="panel")
            )]
        )
    
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    return keyboard


def get_responsible_management_keyboard() -> InlineKeyboardMarkup:
    """Меню управления ответственными."""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="➕ Добавить ответственного", callback_data="responsible_add"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✏️ Редактировать ответственного", callback_data="responsible_edit"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🗑️ Удалить ответственного", callback_data="responsible_delete"
                )
            ],
            [InlineKeyboardButton(text="📅 Назначить на дату", callback_data="responsible_assign")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="panel_main")],
        ]
    )
    return keyboard


def get_greeting_options_keyboard() -> InlineKeyboardMarkup:
    """Меню генерации поздравлений."""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✏️ Написать вручную", callback_data="greeting_manual")],
            [
                InlineKeyboardButton(
                    text="🤖 Сгенерировать через DeepSeek", callback_data="greeting_generate"
                )
            ],
            [InlineKeyboardButton(text="🖼️ Создать открытку", callback_data="greeting_card")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="panel_main")],
        ]
    )
    return keyboard
