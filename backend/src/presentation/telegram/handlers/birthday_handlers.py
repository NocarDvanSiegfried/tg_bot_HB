import logging
import os
from datetime import datetime

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.factories.use_case_factory import UseCaseFactory
from src.presentation.telegram.keyboards import (
    get_birthday_management_keyboard,
    is_webapp_url_configured,
)

logger = logging.getLogger(__name__)

router = Router()


class BirthdayForm(StatesGroup):
    waiting_for_full_name = State()
    waiting_for_company = State()
    waiting_for_position = State()
    waiting_for_birth_date = State()
    waiting_for_comment = State()


@router.callback_query(lambda c: c.data == "panel_birthdays")
async def panel_birthdays_callback(callback: CallbackQuery):
    """
    Меню управления ДР.
    
    КРИТИЧНО: CRUD-операции (добавление, редактирование, удаление дней рождения) 
    выполняются исключительно через Telegram Mini App (панель управления).
    Командный интерфейс бота больше не содержит CRUD-логики.
    """
    webapp_url = os.getenv("TELEGRAM_WEBAPP_URL", "")
    
    if is_webapp_url_configured(webapp_url):
        message_text = (
            "🎂 Управление днями рождения\n\n"
            "Управление днями рождения (добавление, редактирование, удаление) "
            "доступно только через панель управления в Mini App.\n\n"
            "Нажмите кнопку ниже, чтобы открыть панель управления."
        )
    else:
        message_text = (
            "🎂 Управление днями рождения\n\n"
            "Управление днями рождения (добавление, редактирование, удаление) "
            "доступно только через панель управления в Mini App.\n\n"
            "Для использования панели управления необходимо настроить TELEGRAM_WEBAPP_URL."
        )
    
    await callback.message.edit_text(
        message_text,
        reply_markup=get_birthday_management_keyboard(),
    )
    await callback.answer()


@router.callback_query(lambda c: c.data == "birthday_add")
async def birthday_add_start(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки добавления ДР (обезврежен).
    
    КРИТИЧНО: CRUD-операции выполняются исключительно через Telegram Mini App.
    Этот handler больше не выполняет добавление, а только информирует пользователя.
    """
    webapp_url = os.getenv("TELEGRAM_WEBAPP_URL", "")
    
    if is_webapp_url_configured(webapp_url):
        message_text = (
            "Управление днями рождения доступно только через панель управления.\n\n"
            "Нажмите кнопку ниже, чтобы открыть панель управления в Mini App."
        )
    else:
        message_text = (
            "Управление днями рождения доступно только через панель управления.\n\n"
            "Для использования панели управления необходимо настроить TELEGRAM_WEBAPP_URL."
        )
    
    await callback.message.answer(message_text)
    await callback.answer("Используйте панель управления для добавления ДР")


# КРИТИЧНО: Все FSM handlers для добавления ДР удалены.
# CRUD-операции выполняются исключительно через Telegram Mini App.
# Следующие handlers больше не используются, но оставлены для совместимости
# (если пользователь случайно попадет в FSM состояние):

@router.message(BirthdayForm.waiting_for_full_name, ~Command())
async def process_full_name(message: Message, state: FSMContext):
    """
    Обработчик FSM состояния (обезврежен).
    
    КРИТИЧНО: CRUD-операции выполняются исключительно через Telegram Mini App.
    КРИТИЧНО: Фильтр ~Command() предотвращает перехват команд (например, /panel).
    """
    await state.clear()
    await message.answer(
        "Управление днями рождения доступно только через панель управления в Mini App."
    )


@router.message(BirthdayForm.waiting_for_company, ~Command())
async def process_company(message: Message, state: FSMContext):
    """
    Обработчик FSM состояния (обезврежен).
    
    КРИТИЧНО: CRUD-операции выполняются исключительно через Telegram Mini App.
    КРИТИЧНО: Фильтр ~Command() предотвращает перехват команд (например, /panel).
    """
    await state.clear()
    await message.answer(
        "Управление днями рождения доступно только через панель управления в Mini App."
    )


@router.message(BirthdayForm.waiting_for_position, ~Command())
async def process_position(message: Message, state: FSMContext):
    """
    Обработчик FSM состояния (обезврежен).
    
    КРИТИЧНО: CRUD-операции выполняются исключительно через Telegram Mini App.
    КРИТИЧНО: Фильтр ~Command() предотвращает перехват команд (например, /panel).
    """
    await state.clear()
    await message.answer(
        "Управление днями рождения доступно только через панель управления в Mini App."
    )


@router.message(BirthdayForm.waiting_for_birth_date, ~Command())
async def process_birth_date(message: Message, state: FSMContext, session: AsyncSession):
    """
    Обработчик FSM состояния (обезврежен).
    
    КРИТИЧНО: CRUD-операции выполняются исключительно через Telegram Mini App.
    КРИТИЧНО: Фильтр ~Command() предотвращает перехват команд (например, /panel).
    """
    await state.clear()
    await message.answer(
        "Управление днями рождения доступно только через панель управления в Mini App."
    )


@router.message(BirthdayForm.waiting_for_comment, ~Command())
async def process_comment(message: Message, state: FSMContext, session: AsyncSession):
    """
    Обработчик FSM состояния (обезврежен).
    
    КРИТИЧНО: CRUD-операции выполняются исключительно через Telegram Mini App.
    КРИТИЧНО: Фильтр ~Command() предотвращает перехват команд (например, /panel).
    """
    await state.clear()
    await message.answer(
        "Управление днями рождения доступно только через панель управления в Mini App."
    )
