from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)


def get_main_menu_keyboard() -> ReplyKeyboardMarkup:
    """Главное меню - только кнопка Календарь."""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📅 Календарь")]],
        resize_keyboard=True,
    )
    return keyboard


def get_panel_menu_keyboard() -> InlineKeyboardMarkup:
    """Меню панели управления."""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎂 Управление ДР", callback_data="panel_birthdays")],
            [InlineKeyboardButton(text="👤 Управление ответственными", callback_data="panel_responsible")],
            [InlineKeyboardButton(text="🎉 Генерация поздравлений", callback_data="panel_greetings")],
            [InlineKeyboardButton(text="📅 Календарь", callback_data="panel_calendar")],
        ]
    )
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
            [InlineKeyboardButton(text="➕ Добавить ответственного", callback_data="responsible_add")],
            [InlineKeyboardButton(text="✏️ Редактировать ответственного", callback_data="responsible_edit")],
            [InlineKeyboardButton(text="🗑️ Удалить ответственного", callback_data="responsible_delete")],
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
            [InlineKeyboardButton(text="🤖 Сгенерировать через DeepSeek", callback_data="greeting_generate")],
            [InlineKeyboardButton(text="🖼️ Создать открытку", callback_data="greeting_card")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="panel_main")],
        ]
    )
    return keyboard

