import logging

from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from src.presentation.telegram.keyboards import get_calendar_keyboard

logger = logging.getLogger(__name__)

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
    """
    keyboard = get_calendar_keyboard()
    await message.answer(
        "Добро пожаловать! Откройте календарь дней рождения для просмотра и управления.",
        reply_markup=keyboard,
    )


@router.callback_query(lambda c: c.data and c.data.startswith("web_app_"))
async def webapp_callback_handler(callback: CallbackQuery):
    """
    Обработчик callback от кнопки WebApp (если Telegram его отправляет).
    
    КРИТИЧНО: Кнопки типа web_app обычно НЕ генерируют callback_query,
    но на всякий случай добавляем обработчик для предотвращения BOT_RESPONSE_TIMEOUT.
    
    Этот обработчик просто отвечает на callback, чтобы Telegram не ждал ответа.
    """
    logger.info(f"[WebApp] Получен callback от WebApp: {callback.data}")
    # Просто отвечаем на callback, чтобы предотвратить timeout
    await callback.answer()
