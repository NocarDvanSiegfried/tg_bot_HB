import logging
import os

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


def get_main_menu_keyboard() -> ReplyKeyboardMarkup:
    """Главное меню - кнопка Календарь и Mini App."""
    webapp_url = os.getenv("TELEGRAM_WEBAPP_URL", "")
    buttons = [[KeyboardButton(text="📅 Календарь")]]

    # Добавляем кнопку Mini App, если URL настроен
    if is_webapp_url_configured(webapp_url):
        buttons.append([KeyboardButton(text="🌐 Открыть Mini App", web_app=WebAppInfo(url=webapp_url))])
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
    """Меню панели управления."""
    webapp_url = os.getenv("TELEGRAM_WEBAPP_URL", "")
    inline_keyboard = [
        [InlineKeyboardButton(text="🎂 Управление ДР", callback_data="panel_birthdays")],
        [
            InlineKeyboardButton(
                text="👤 Управление ответственными", callback_data="panel_responsible"
            )
        ],
        [
            InlineKeyboardButton(
                text="🎉 Генерация поздравлений", callback_data="panel_greetings"
            )
        ],
        [InlineKeyboardButton(text="📅 Календарь", callback_data="panel_calendar")],
    ]

    # Добавляем кнопку Mini App, если URL настроен
    if is_webapp_url_configured(webapp_url):
        inline_keyboard.append([
            InlineKeyboardButton(
                text="🌐 Открыть Mini App",
                web_app=WebAppInfo(url=webapp_url)
            )
        ])

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
    """Меню управления ДР."""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="➕ Добавить ДР", callback_data="birthday_add")],
            [InlineKeyboardButton(text="✏️ Редактировать ДР", callback_data="birthday_edit")],
            [InlineKeyboardButton(text="🗑️ Удалить ДР", callback_data="birthday_delete")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="panel_main")],
        ]
    )
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
