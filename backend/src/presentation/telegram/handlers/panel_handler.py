from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.models import PanelAccessModel
from src.presentation.telegram.keyboards import get_panel_menu_keyboard

router = Router()


@router.message(Command("panel"))
async def cmd_panel(message: Message, session: AsyncSession):
    """Обработчик команды /panel - открывает панель управления."""
    # Записываем доступ к панели
    access = PanelAccessModel(user_id=message.from_user.id)
    session.add(access)
    await session.commit()

    await message.answer(
        "Панель управления",
        reply_markup=get_panel_menu_keyboard(),
    )


@router.callback_query(lambda c: c.data == "panel_main")
async def panel_main_callback(callback: CallbackQuery):
    """Вернуться в главное меню панели."""
    await callback.message.edit_text(
        "Панель управления",
        reply_markup=get_panel_menu_keyboard(),
    )
    await callback.answer()

