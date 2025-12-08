import pytest

from src.presentation.telegram.keyboards import (
    get_main_menu_keyboard,
    get_panel_menu_keyboard,
    get_calendar_navigation_keyboard,
    get_birthday_management_keyboard,
    get_responsible_management_keyboard,
    get_greeting_options_keyboard,
)


class TestKeyboards:
    """Тесты для генерации клавиатур."""

    def test_get_main_menu_keyboard(self):
        """Тест генерации главного меню."""
        keyboard = get_main_menu_keyboard()
        
        assert keyboard is not None
        assert len(keyboard.keyboard) == 1
        assert len(keyboard.keyboard[0]) == 1
        assert keyboard.keyboard[0][0].text == "📅 Календарь"
        assert keyboard.resize_keyboard is True

    def test_get_panel_menu_keyboard(self):
        """Тест генерации меню панели управления."""
        keyboard = get_panel_menu_keyboard()
        
        assert keyboard is not None
        assert len(keyboard.inline_keyboard) == 4
        assert keyboard.inline_keyboard[0][0].text == "🎂 Управление ДР"
        assert keyboard.inline_keyboard[0][0].callback_data == "panel_birthdays"
        assert keyboard.inline_keyboard[1][0].text == "👤 Управление ответственными"
        assert keyboard.inline_keyboard[2][0].text == "🎉 Генерация поздравлений"
        assert keyboard.inline_keyboard[3][0].text == "📅 Календарь"

    def test_get_calendar_navigation_keyboard(self):
        """Тест генерации навигации по календарю."""
        keyboard = get_calendar_navigation_keyboard(2024, 5)
        
        assert keyboard is not None
        assert len(keyboard.inline_keyboard) == 1
        assert len(keyboard.inline_keyboard[0]) == 3
        assert keyboard.inline_keyboard[0][0].text == "◀️"
        assert keyboard.inline_keyboard[0][0].callback_data == "cal_prev_2024_5"
        assert keyboard.inline_keyboard[0][1].text == "2024-05"
        assert keyboard.inline_keyboard[0][2].text == "▶️"
        assert keyboard.inline_keyboard[0][2].callback_data == "cal_next_2024_5"

    def test_get_birthday_management_keyboard(self):
        """Тест генерации меню управления ДР."""
        keyboard = get_birthday_management_keyboard()
        
        assert keyboard is not None
        assert len(keyboard.inline_keyboard) == 4
        assert keyboard.inline_keyboard[0][0].text == "➕ Добавить ДР"
        assert keyboard.inline_keyboard[1][0].text == "✏️ Редактировать ДР"
        assert keyboard.inline_keyboard[2][0].text == "🗑️ Удалить ДР"
        assert keyboard.inline_keyboard[3][0].text == "🔙 Назад"

    def test_get_responsible_management_keyboard(self):
        """Тест генерации меню управления ответственными."""
        keyboard = get_responsible_management_keyboard()
        
        assert keyboard is not None
        assert len(keyboard.inline_keyboard) == 5
        assert keyboard.inline_keyboard[0][0].text == "➕ Добавить ответственного"
        assert keyboard.inline_keyboard[1][0].text == "✏️ Редактировать ответственного"
        assert keyboard.inline_keyboard[2][0].text == "🗑️ Удалить ответственного"
        assert keyboard.inline_keyboard[3][0].text == "📅 Назначить на дату"
        assert keyboard.inline_keyboard[4][0].text == "🔙 Назад"

    def test_get_greeting_options_keyboard(self):
        """Тест генерации меню генерации поздравлений."""
        keyboard = get_greeting_options_keyboard()
        
        assert keyboard is not None
        assert len(keyboard.inline_keyboard) == 4
        assert keyboard.inline_keyboard[0][0].text == "✏️ Написать вручную"
        assert keyboard.inline_keyboard[1][0].text == "🤖 Сгенерировать через DeepSeek"
        assert keyboard.inline_keyboard[2][0].text == "🖼️ Создать открытку"
        assert keyboard.inline_keyboard[3][0].text == "🔙 Назад"

