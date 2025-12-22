import logging
import time
from typing import Dict, Optional

from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.factories.use_case_factory import UseCaseFactory
from src.presentation.telegram.keyboards import get_panel_menu_keyboard

logger = logging.getLogger(__name__)

router = Router()

# КРИТИЧНО: Хранилище последних message_id с меню панели для каждого пользователя
# Ключ: user_id, Значение: message_id последнего сообщения с меню панели
_panel_menu_messages: Dict[int, int] = {}

# КРИТИЧНО: Защита от повторных вызовов обработчика /panel
# Ключ: (user_id, chat_id), Значение: timestamp последнего вызова
_panel_processing: Dict[tuple[int, int], float] = {}


def _get_panel_menu_text() -> str:
    """
    Получает единый текст меню панели управления.
    
    КРИТИЧНО: Это единственное место, где определяется текст панели.
    Все обработчики должны использовать этот текст.
    
    Returns:
        Текст меню панели управления
    """
    return (
        "🎛️ Панель управления\n\n"
        "Управление днями рождения, ответственными лицами и генерация поздравлений."
    )


async def render_panel_menu(
    bot: Bot,
    chat_id: int,
    user_id: int,
    existing_message_id: Optional[int] = None
) -> int:
    """
    Рендерит меню панели управления.
    
    КРИТИЧНО: Mini App-first архитектура - только InlineKeyboard, без ReplyKeyboard.
    - Использует только InlineKeyboardMarkup с одной кнопкой WebApp
    - При повторном вызове редактирует существующее сообщение
    - Никогда не создает дубликаты - в чате всегда одно сообщение панели
    
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
            # КРИТИЧНО: Сначала удаляем ReplyKeyboardMarkup, если она была установлена
            remove_message_id = None
            try:
                remove_message = await bot.send_message(
                    chat_id=chat_id,
                    text="",  # Пустое сообщение для удаления клавиатуры
                    reply_markup=ReplyKeyboardRemove(remove_keyboard=True),
                )
                remove_message_id = remove_message.message_id
            except Exception:
                # Игнорируем ошибки при удалении клавиатуры
                pass
            
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id_to_edit,
                text=message_text,
                reply_markup=keyboard,  # Только InlineKeyboardMarkup
            )
            
            # Удаляем служебное сообщение с ReplyKeyboardRemove
            if remove_message_id:
                try:
                    await bot.delete_message(chat_id=chat_id, message_id=remove_message_id)
                except Exception:
                    # Игнорируем ошибки при удалении
                    pass
            
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
    
    # КРИТИЧНО: Сначала явно удаляем ReplyKeyboardMarkup, если она была установлена ранее
    # Это гарантирует, что старая клавиатура не будет показана
    # Затем отправляем основное сообщение с InlineKeyboard
    # Используем асинхронное удаление служебного сообщения для минимизации видимости
    remove_message_id = None
    try:
        # Отправляем пустое сообщение с ReplyKeyboardRemove для удаления старой клавиатуры
        remove_message = await bot.send_message(
            chat_id=chat_id,
            text="",  # Пустое сообщение для удаления клавиатуры
            reply_markup=ReplyKeyboardRemove(remove_keyboard=True),
        )
        remove_message_id = remove_message.message_id
    except Exception as e:
        # Игнорируем ошибки при удалении клавиатуры (может быть уже удалена)
        logger.debug(f"[Panel] ReplyKeyboardRemove не требуется или уже удалена: {e}")
    
    # Отправляем основное сообщение с меню панели (только InlineKeyboard)
    sent_message = await bot.send_message(
        chat_id=chat_id,
        text=message_text,
        reply_markup=keyboard,  # Только InlineKeyboardMarkup, без ReplyKeyboard
    )
    
    # КРИТИЧНО: Удаляем служебное сообщение с ReplyKeyboardRemove сразу после отправки основного
    # Это предотвращает появление лишних сообщений в чате
    if remove_message_id:
        try:
            await bot.delete_message(chat_id=chat_id, message_id=remove_message_id)
        except Exception:
            # Игнорируем ошибки при удалении (сообщение может быть уже удалено или недоступно)
            pass
    
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
    
    ВАЖНО: Это ЕДИНСТВЕННЫЙ handler для команды /panel.
    Никакие другие handlers не должны обрабатывать эту команду.
    
    КРИТИЧНО: Защита от повторных вызовов - предотвращает дублирование сообщений.
    """
    user_id = message.from_user.id
    chat_id = message.chat.id
    key = (user_id, chat_id)
    current_time = time.time()
    
    # КРИТИЧНО: Защита от повторных вызовов в течение 1 секунды
    # Это предотвращает обработку команды несколько раз подряд
    if key in _panel_processing:
        time_since_last = current_time - _panel_processing[key]
        if time_since_last < 1.0:  # Защита от повторных вызовов в течение 1 секунды
            logger.warning(
                f"[Panel] Игнорируем повторный вызов /panel для пользователя {user_id} "
                f"в чате {chat_id} (прошло {time_since_last:.2f} секунд)"
            )
            return  # Прерываем обработку, чтобы избежать дублирования
    
    # Сохраняем время текущего вызова
    _panel_processing[key] = current_time
    
    # Очищаем старые записи (старше 5 секунд) для экономии памяти
    if len(_panel_processing) > 1000:  # Если слишком много записей
        cutoff_time = current_time - 5.0
        keys_to_remove = [k for k, v in _panel_processing.items() if v <= cutoff_time]
        for k in keys_to_remove:
            _panel_processing.pop(k, None)
    
    logger.info(f"[Panel] Команда /panel получена от пользователя {user_id} в чате {chat_id}")
    
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
    # Это ЕДИНСТВЕННОЕ место, где вызывается render_panel_menu для команды /panel
    await render_panel_menu(
        bot=bot,
        chat_id=chat_id,
        user_id=user_id,
    )
    
    logger.info(f"[Panel] Команда /panel обработана для пользователя {user_id}")


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
