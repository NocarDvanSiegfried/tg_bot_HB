import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.infrastructure.database.database import Database
from src.presentation.telegram.handlers import (
    start_handler,
    panel_handler,
    calendar_handler,
    birthday_handlers,
    responsible_handlers,
    greeting_handlers,
)


async def main():
    """Запуск Telegram бота."""
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable is required")

    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE_URL environment variable is required")

    # Инициализация бота
    bot = Bot(token=bot_token)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Инициализация БД
    db = Database(database_url)
    await db.create_tables()

    # Регистрация роутеров
    dp.include_router(start_handler.router)
    dp.include_router(panel_handler.router)
    dp.include_router(calendar_handler.router)
    dp.include_router(birthday_handlers.router)
    dp.include_router(responsible_handlers.router)
    dp.include_router(greeting_handlers.router)

    # Запуск polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

