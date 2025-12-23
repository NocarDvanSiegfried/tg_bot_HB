"""
Временный защитный обработчик для старых CallbackQuery.

КРИТИЧНО: Это временный migration-guard handler.
Цель: предотвратить BOT_RESPONSE_TIMEOUT при нажатии на старые InlineKeyboard кнопки
в истории чата пользователей после миграции на архитектуру "Bot = launcher".

ПОВЕДЕНИЕ:
- Ловит любой callback_data, для которого нет специализированного handler'а
- Мгновенно отвечает на callback, чтобы Telegram не ждал 30 секунд
- Не содержит CRUD-логики, не взаимодействует с БД, не меняет состояние

УДАЛЕНИЕ:
- Этот handler можно удалить через N недель после полной миграции пользователей
- После удаления пользователи должны удалить старые сообщения вручную
- Новые пользователи не имеют проблемы (видят только /start с WebApp-кнопкой)

АРХИТЕКТУРА:
- Не нарушает принцип "Bot = launcher, Mini App = application"
- Не обрабатывает CRUD-операции (только отвечает на callback)
- Mini App остается единственным местом для CRUD
- /start остается единственной точкой входа
"""

import logging

from aiogram import Router
from aiogram.types import CallbackQuery

logger = logging.getLogger(__name__)

router = Router()


@router.callback_query()
async def migration_guard_callback(callback: CallbackQuery):
    """
    Временный защитный обработчик для старых CallbackQuery.
    
    Ловит любой callback_data, для которого нет специализированного handler'а.
    Мгновенно отвечает на callback, чтобы предотвратить BOT_RESPONSE_TIMEOUT.
    
    КРИТИЧНО: Это временное решение для миграции.
    Не содержит бизнес-логики, не обрабатывает CRUD, не взаимодействует с БД.
    
    Args:
        callback: CallbackQuery от Telegram
    """
    # Логируем для мониторинга использования старых кнопок
    logger.info(
        f"[Migration Guard] Получен callback от старой кнопки: "
        f"callback_data={callback.data}, user_id={callback.from_user.id}"
    )
    
    # Мгновенно отвечаем на callback, чтобы предотвратить BOT_RESPONSE_TIMEOUT
    # show_alert = False - не показываем всплывающее окно, только уведомление
    await callback.answer(
        text="Функция больше недоступна. Используйте Mini App.",
        show_alert=False
    )

