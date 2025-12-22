from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from src.presentation.telegram.keyboards import get_panel_menu_keyboard

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message, bot: Bot):
    """
    Обработчик команды /start.
    
    КРИТИЧНО: Mini App-first UX - только InlineKeyboard, без ReplyKeyboard.
    Явно удаляет любую ранее показанную ReplyKeyboard.
    """
    # КРИТИЧНО: Сначала явно удаляем ReplyKeyboardMarkup, если она была установлена
    # Это гарантирует, что старая клавиатура не будет показана
    remove_message_id = None
    try:
        remove_message = await bot.send_message(
            chat_id=message.chat.id,
            text="",  # Пустое сообщение для удаления клавиатуры
            reply_markup=ReplyKeyboardRemove(remove_keyboard=True),
        )
        remove_message_id = remove_message.message_id
    except Exception:
        # Игнорируем ошибки при удалении клавиатуры (может быть уже удалена)
        pass
    
    # Отправляем приветственное сообщение с InlineKeyboard (только кнопка Mini App)
    keyboard = get_panel_menu_keyboard()
    await message.answer(
        "Добро пожаловать! Используйте панель управления для управления днями рождения и ответственными лицами.",
        reply_markup=keyboard,
    )
    
    # Удаляем служебное сообщение с ReplyKeyboardRemove сразу после отправки основного
    if remove_message_id:
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=remove_message_id)
        except Exception:
            # Игнорируем ошибки при удалении (сообщение может быть уже удалено или недоступно)
            pass
