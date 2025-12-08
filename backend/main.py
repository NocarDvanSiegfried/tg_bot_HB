import asyncio
import os
import uvicorn
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.infrastructure.database.database_factory import get_database
from src.presentation.telegram.handlers import (
    start_handler,
    panel_handler,
    calendar_handler,
    birthday_handlers,
    responsible_handlers,
    greeting_handlers,
)
from src.presentation.web.app import app as web_app
from src.infrastructure.services.notifications_scheduler import setup_notifications


async def start_bot():
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

    # Инициализация БД через factory
    os.environ["DATABASE_URL"] = database_url
    db = get_database()
    await db.create_tables()

    # Настройка уведомлений
    await setup_notifications(bot, db)

    # Регистрация роутеров
    dp.include_router(start_handler.router)
    dp.include_router(panel_handler.router)
    dp.include_router(calendar_handler.router)
    dp.include_router(birthday_handlers.router)
    dp.include_router(responsible_handlers.router)
    dp.include_router(greeting_handlers.router)

    # Запуск polling
    await dp.start_polling(bot)


async def start_web():
    """Запуск FastAPI веб-сервера."""
    config = uvicorn.Config(
        web_app,
        host="0.0.0.0",
        port=int(os.getenv("WEB_PORT", "8000")),
        log_level="info",
    )
    server = uvicorn.Server(config)
    await server.serve()


async def main():
    """Главная функция запуска."""
    # Запускаем бота и веб-сервер параллельно
    await asyncio.gather(
        start_bot(),
        start_web(),
    )


if __name__ == "__main__":
    asyncio.run(main())

