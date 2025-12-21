import logging
import os
from typing import Dict, Optional

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


def _get_panel_menu_text() -> str:
    """
    Получает единый текст меню панели управления.
    
    КРИТИЧНО: Это единственное место, где определяется текст панели.
    Все обработчики должны использовать этот текст.
    
    Returns:
        Текст меню панели управления
    """
    webapp_url = os.getenv("TELEGRAM_WEBAPP_URL", "")
    
    if is_webapp_url_configured(webapp_url):
        return (
            "🎛️ Панель управления\n\n"
            "Здесь вы можете управлять днями рождения, ответственными лицами и генерировать поздравления.\n\n"
            "Нажмите кнопку ниже, чтобы открыть панель управления в Mini App."
        )
    else:
        return (
            "🎛️ Панель управления\n\n"
            "Здесь вы можете управлять днями рождения, ответственными лицами и генерировать поздравления.\n\n"
            "Используйте кнопки ниже для управления."
        )


async def render_panel_menu(
    bot: Bot,
    chat_id: int,
    user_id: int,
    existing_message_id: Optional[int] = None
) -> int:
    """
    Рендерит меню панели управления.
    
    КРИТИЧНО: Это единственная функция, которая создает/редактирует панель управления.
    - Если есть existing_message_id или сохраненный message_id - редактирует существующее сообщение
    - Если нет - отправляет новое сообщение
    - Никогда не создает дубликаты
    
    Args:
        bot: Экземпляр бота
        chat_id: ID чата
        user_id: ID пользователя
        existing_message_id: Опциональный message_id для редактирования (если None, берется из хранилища)
    
    Returns:
        message_id сообщения с панелью (нового или отредактированного)
    """
    message_text = _get_panel_menu_text()
    keyboard = get_panel_menu_keyboard()
    
    # Определяем message_id для редактирования
    message_id_to_edit = existing_message_id or _panel_menu_messages.get(user_id)
    
    if message_id_to_edit:
        # Пытаемся отредактировать существующее сообщение
        try:
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id_to_edit,
                text=message_text,
                reply_markup=keyboard,
            )
            # Сохраняем message_id в хранилище
            _panel_menu_messages[user_id] = message_id_to_edit
            logger.info(
                f"[Panel] Отредактировано существующее сообщение с меню для пользователя {user_id} "
                f"(chat_id={chat_id}, message_id={message_id_to_edit})"
            )
            return message_id_to_edit
        except Exception as e:
            # Если редактирование не удалось (сообщение удалено, недоступно и т.д.)
            # Удаляем из хранилища и отправляем новое
            logger.warning(
                f"[Panel] Не удалось отредактировать сообщение {message_id_to_edit} для пользователя {user_id}: "
                f"{type(e).__name__}: {e}. Отправляется новое сообщение."
            )
            _panel_menu_messages.pop(user_id, None)
    
    # Отправляем новое сообщение (либо меню не было, либо редактирование не удалось)
    sent_message = await bot.send_message(
        chat_id=chat_id,
        text=message_text,
        reply_markup=keyboard,
    )
    
    # Сохраняем message_id нового сообщения
    _panel_menu_messages[user_id] = sent_message.message_id
    logger.info(
        f"[Panel] Отправлено новое сообщение с меню для пользователя {user_id} "
        f"(chat_id={chat_id}, message_id={sent_message.message_id})"
    )
    
    return sent_message.message_id


@router.message(Command("panel"))
async def cmd_panel(message: Message, bot: Bot, session: AsyncSession):
    """
    Обработчик команды /panel - открывает панель управления.
    
    КРИТИЧНО: Использует единую функцию render_panel_menu().
    Никогда не создает дубликаты - только редактирует существующее или отправляет новое.
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

    # КРИТИЧНО: Используем единую функцию рендеринга панели
    await render_panel_menu(
        bot=bot,
        chat_id=message.chat.id,
        user_id=user_id,
    )


@router.callback_query(lambda c: c.data == "panel_main")
async def panel_main_callback(callback: CallbackQuery, bot: Bot):
    """
    Вернуться в главное меню панели.
    
    КРИТИЧНО: Использует единую функцию render_panel_menu().
    Только редактирует существующее сообщение, никогда не создает новое.
    """
    user_id = callback.from_user.id
    message_id = callback.message.message_id
    
    # КРИТИЧНО: Используем единую функцию рендеринга панели
    # Передаем existing_message_id для гарантии редактирования текущего сообщения
    await render_panel_menu(
        bot=bot,
        chat_id=callback.message.chat.id,
        user_id=user_id,
        existing_message_id=message_id,
    )
    
    await callback.answer()
