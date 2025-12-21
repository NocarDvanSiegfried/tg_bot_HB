import logging
import os
from typing import Dict

from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.factories.use_case_factory import UseCaseFactory
from src.presentation.telegram.keyboards import get_panel_menu_keyboard, is_webapp_url_configured

logger = logging.getLogger(__name__)

router = Router()

# КРИТИЧНО: Хранилище последних message_id с меню панели для каждого пользователя
# Ключ: user_id, Значение: message_id последнего сообщения с меню панели
_panel_menu_messages: Dict[int, int] = {}


@router.message(Command("panel"))
async def cmd_panel(message: Message, bot: Bot, session: AsyncSession):
    """
    Обработчик команды /panel - открывает панель управления.
    
    КРИТИЧНО: Предотвращает дублирование сообщений.
    - Если меню уже существует - редактирует его
    - Если меню нет - отправляет новое
    """
    user_id = message.from_user.id
    
    # Записываем доступ к панели через use-case
    factory = UseCaseFactory(session)
    record_access_use_case = factory.create_record_panel_access_use_case()
    
    try:
        await record_access_use_case.execute(user_id)
        await session.commit()
        logger.info(f"Доступ к панели записан для пользователя {user_id}")
    except Exception as e:
        await session.rollback()
        logger.error(f"Ошибка при записи доступа к панели для пользователя {user_id}: {type(e).__name__}: {e}")
        # Продолжаем выполнение, даже если не удалось записать доступ
        # Пользователь все равно получит меню панели

    webapp_url = os.getenv("TELEGRAM_WEBAPP_URL", "")
    
    # Формируем сообщение в зависимости от наличия Mini App
    if is_webapp_url_configured(webapp_url):
        message_text = (
            "🎛️ Панель управления\n\n"
            "Здесь вы можете управлять днями рождения, ответственными лицами и генерировать поздравления.\n\n"
            "Нажмите кнопку ниже, чтобы открыть панель управления в Mini App."
        )
    else:
        message_text = (
            "🎛️ Панель управления\n\n"
            "Здесь вы можете управлять днями рождения, ответственными лицами и генерировать поздравления.\n\n"
            "Используйте кнопки ниже для управления."
        )
    
    # КРИТИЧНО: Проверяем, есть ли уже сообщение с меню панели
    existing_message_id = _panel_menu_messages.get(user_id)
    
    if existing_message_id:
        # Пытаемся отредактировать существующее сообщение
        try:
            await bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=existing_message_id,
                text=message_text,
                reply_markup=get_panel_menu_keyboard(),
            )
            logger.info(f"[Panel] Отредактировано существующее сообщение с меню для пользователя {user_id} (message_id={existing_message_id})")
            return  # Выходим, не создавая новое сообщение
        except Exception as e:
            # Если редактирование не удалось (сообщение удалено, недоступно и т.д.)
            # Удаляем из хранилища и отправляем новое
            logger.warning(
                f"[Panel] Не удалось отредактировать сообщение {existing_message_id} для пользователя {user_id}: {type(e).__name__}: {e}. "
                "Отправляется новое сообщение."
            )
            _panel_menu_messages.pop(user_id, None)
    
    # Отправляем новое сообщение (либо меню не было, либо редактирование не удалось)
    sent_message = await message.answer(
        message_text,
        reply_markup=get_panel_menu_keyboard(),
    )
    
    # Сохраняем message_id нового сообщения
    _panel_menu_messages[user_id] = sent_message.message_id
    logger.info(f"[Panel] Отправлено новое сообщение с меню для пользователя {user_id} (message_id={sent_message.message_id})")


@router.callback_query(lambda c: c.data == "panel_main")
async def panel_main_callback(callback: CallbackQuery):
    """
    Вернуться в главное меню панели.
    
    КРИТИЧНО: Только редактирует существующее сообщение, никогда не создает новое.
    Обновляет хранилище message_id для отслеживания.
    """
    user_id = callback.from_user.id
    message_id = callback.message.message_id
    
    webapp_url = os.getenv("TELEGRAM_WEBAPP_URL", "")
    
    # Формируем текст сообщения в зависимости от наличия Mini App
    if is_webapp_url_configured(webapp_url):
        message_text = (
            "🎛️ Панель управления\n\n"
            "Здесь вы можете управлять днями рождения, ответственными лицами и генерировать поздравления.\n\n"
            "Нажмите кнопку ниже, чтобы открыть панель управления в Mini App."
        )
    else:
        message_text = (
            "🎛️ Панель управления\n\n"
            "Здесь вы можете управлять днями рождения, ответственными лицами и генерировать поздравления.\n\n"
            "Используйте кнопки ниже для управления."
        )
    
    # КРИТИЧНО: Только редактируем существующее сообщение
    await callback.message.edit_text(
        message_text,
        reply_markup=get_panel_menu_keyboard(),
    )
    
    # Обновляем хранилище message_id для отслеживания
    _panel_menu_messages[user_id] = message_id
    logger.info(f"[Panel] Обновлено сообщение с меню для пользователя {user_id} (message_id={message_id}) через callback panel_main")
    
    await callback.answer()
