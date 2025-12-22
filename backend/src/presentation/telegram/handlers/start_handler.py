from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message

from src.presentation.telegram.keyboards import get_calendar_keyboard

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message, bot: Bot):
    """
    Обработчик команды /start - точка входа в приложение.
    
    КРИТИЧНО: Bot = Launcher архитектура.
    - Отправляет одно сообщение с кнопкой открытия календаря
    - Не использует ReplyKeyboard
    - Не редактирует старые сообщения
    - Идемпотентно: повторный вызов не создает дубликатов
    - Кнопка web_app не генерирует callback_query, обработчик не требуется
    
    МИГРАЦИЯ:
    - Все старые callback handlers (birthday_*, panel_*, responsible_*, greeting_*) удалены
    - Если пользователь видит BOT_RESPONSE_TIMEOUT при нажатии на старые кнопки:
      → Это устаревшие UI-артефакты в истории чата
      → Решение: пользователь должен удалить старые сообщения вручную
      → НЕ добавлять catch-all handler (нарушает архитектуру)
      → См. MIGRATION_GUIDE.md для деталей
    """
    keyboard = get_calendar_keyboard()
    await message.answer(
        "Добро пожаловать! Откройте календарь дней рождения для просмотра и управления.",
        reply_markup=keyboard,
    )
