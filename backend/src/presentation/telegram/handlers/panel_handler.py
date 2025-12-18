import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.factories.use_case_factory import UseCaseFactory
from src.presentation.telegram.keyboards import get_panel_menu_keyboard

logger = logging.getLogger(__name__)

router = Router()


@router.message(Command("panel"))
async def cmd_panel(message: Message, session: AsyncSession):
    """Обработчик команды /panel - открывает панель управления."""
    # Записываем доступ к панели через use-case
    factory = UseCaseFactory(session)
    record_access_use_case = factory.create_record_panel_access_use_case()
    
    try:
        await record_access_use_case.execute(message.from_user.id)
        await session.commit()
        logger.info(f"Доступ к панели записан для пользователя {message.from_user.id}")
    except Exception as e:
        await session.rollback()
        logger.error(f"Ошибка при записи доступа к панели для пользователя {message.from_user.id}: {type(e).__name__}: {e}")
        # Продолжаем выполнение, даже если не удалось записать доступ
        # Пользователь все равно получит меню панели

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
