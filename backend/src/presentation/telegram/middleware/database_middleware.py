"""Middleware для инжекции сессий БД в обработчики aiogram."""

import logging
from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from src.infrastructure.database.database_factory import get_database

logger = logging.getLogger(__name__)


class DatabaseMiddleware(BaseMiddleware):
    """Middleware для предоставления сессии БД обработчикам."""

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        """
        Инжектирует сессию БД в data для обработчиков.

        Args:
            handler: Обработчик события
            event: Событие Telegram
            data: Данные для обработчика

        Returns:
            Результат выполнения обработчика
        """
        try:
            db = get_database()
            # get_session() возвращает async generator, который создает сессию
            # и автоматически закрывает её после использования через async with
            # async for правильно управляет жизненным циклом сессии
            async for session in db.get_session():
                # Инжектируем сессию в data для обработчиков
                # aiogram автоматически передаст её в параметр session обработчика
                # если он указан в сигнатуре функции
                data["session"] = session
                try:
                    # Выполняем обработчик
                    # Управление транзакциями (commit/rollback) должно быть в repository или use-case
                    result = await handler(event, data)
                    return result
                except Exception as e:
                    # Логируем ошибку, но НЕ управляем транзакциями
                    # Сессия автоматически закроется через async with в get_session()
                    logger.error(f"Ошибка в обработчике: {type(e).__name__}: {e}")
                    raise
                # Сессия автоматически закроется после выхода из async for
                # благодаря async with в get_session()
        except Exception as e:
            logger.error(f"Ошибка создания сессии БД: {type(e).__name__}: {e}")
            # Если не удалось создать сессию, пытаемся выполнить обработчик без неё
            # Некоторые обработчики могут работать без БД
            try:
                return await handler(event, data)
            except TypeError as te:
                # Если обработчик требует session, возвращаем понятную ошибку
                if "session" in str(te) or "missing 1 required positional argument" in str(te):
                    logger.error(
                        "Обработчик требует сессию БД, но она недоступна. "
                        "Проверьте подключение к базе данных."
                    )
                    # Пытаемся отправить сообщение об ошибке пользователю
                    if hasattr(event, "answer"):
                        try:
                            await event.answer(
                                "❌ Ошибка подключения к базе данных. "
                                "Попробуйте позже или обратитесь к администратору."
                            )
                        except Exception:
                            pass  # Не критично, если не удалось отправить сообщение
                raise
