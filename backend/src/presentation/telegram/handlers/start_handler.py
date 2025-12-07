from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from src.presentation.telegram.keyboards import get_main_menu_keyboard

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    """Обработчик команды /start."""
    await message.answer(
        "Добро пожаловать! Выберите действие:",
        reply_markup=get_main_menu_keyboard(),
    )

