import asyncio
import logging
import os
import uvicorn
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.infrastructure.config.env_validator import (
    get_database_name_from_url,
    mask_database_url,
    validate_database_url,
    validate_telegram_token,
)
from src.infrastructure.database.database_factory import get_database
from src.presentation.telegram.handlers import (
    start_handler,
    panel_handler,
    calendar_handler,
    birthday_handlers,
    responsible_handlers,
    greeting_handlers,
)
from src.presentation.telegram.middleware.database_middleware import DatabaseMiddleware
from src.presentation.web.app import app as web_app
from src.infrastructure.services.notifications_scheduler import setup_notifications

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def start_bot():
    """Запуск Telegram бота."""
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        raise ValueError(
            "TELEGRAM_BOT_TOKEN environment variable is required. "
            "Получите токен от @BotFather в Telegram и добавьте его в .env файл."
        )

    # Валидация формата токена
    is_valid, error_message = validate_telegram_token(bot_token)
    if not is_valid:
        logger.error(f"Ошибка валидации TELEGRAM_BOT_TOKEN: {error_message}")
        raise ValueError(f"Неверный TELEGRAM_BOT_TOKEN: {error_message}")
    
    # Логирование успешной валидации (без токена)
    logger.info("TELEGRAM_BOT_TOKEN валиден по формату. Длина токена: %d символов", len(bot_token))
    logger.info("Попытка подключения к Telegram API...")

    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE_URL environment variable is required")

    # Валидация DATABASE_URL
    is_valid, db_name, error_message = validate_database_url(database_url)
    if not is_valid:
        masked_url = mask_database_url(database_url)
        logger.error(f"Ошибка валидации DATABASE_URL: {error_message}")
        logger.error(f"DATABASE_URL (замаскирован): {masked_url}")
        raise ValueError(f"Неверный формат DATABASE_URL: {error_message}")

    # Логирование информации о подключении (без пароля)
    masked_url = mask_database_url(database_url)
    logger.info(f"Подключение к базе данных: {masked_url}")
    if db_name:
        logger.info(f"Имя базы данных: {db_name}")

    # Инициализация бота
    logger.info("Инициализация Telegram бота...")
    bot = Bot(token=bot_token)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    logger.info("Telegram бот инициализирован. Проверка подключения к API...")

    # Инициализация БД через factory
    os.environ["DATABASE_URL"] = database_url
    db = get_database()
    await db.create_tables()

    # Настройка уведомлений
    await setup_notifications(bot, db)

    # Регистрация middleware для инжекции сессий БД
    logger.info("Регистрация middleware для сессий БД...")
    dp.message.middleware(DatabaseMiddleware())
    dp.callback_query.middleware(DatabaseMiddleware())

    # Регистрация роутеров
    dp.include_router(start_handler.router)
    dp.include_router(panel_handler.router)
    dp.include_router(calendar_handler.router)
    dp.include_router(birthday_handlers.router)
    dp.include_router(responsible_handlers.router)
    dp.include_router(greeting_handlers.router)

    # Запуск polling с обработкой ошибок
    try:
        logger.info("Запуск Telegram polling...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Критическая ошибка при работе Telegram бота: {type(e).__name__}: {e}")
        # Пробуем получить более детальную информацию об ошибке
        if "Unauthorized" in str(e) or "TelegramUnauthorizedError" in str(type(e).__name__):
            logger.error(
                "Telegram API вернул ошибку 'Unauthorized'. Возможные причины:\n"
                "1. Токен недействителен или был отозван\n"
                "2. Бот был удален в @BotFather\n"
                "3. Токен был изменен, но контейнер использует старый (перезапустите контейнер)\n"
                "4. Проблемы с сетью при обращении к Telegram API\n"
                "Проверьте токен в .env файле и убедитесь, что бот активен в @BotFather."
            )
        raise


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
    # Валидация DATABASE_URL при старте приложения
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        is_valid, db_name, error_message = validate_database_url(database_url)
        if not is_valid:
            masked_url = mask_database_url(database_url)
            logger.error(f"Критическая ошибка валидации DATABASE_URL: {error_message}")
            logger.error(f"DATABASE_URL (замаскирован): {masked_url}")
            raise ValueError(f"Неверный формат DATABASE_URL: {error_message}")
        else:
            masked_url = mask_database_url(database_url)
            logger.info(f"DATABASE_URL валиден. База данных: {db_name}")
            logger.info(f"Подключение (замаскировано): {masked_url}")
    else:
        logger.warning("DATABASE_URL не установлен. Будет проверен позже при инициализации.")

    # Запускаем бота и веб-сервер параллельно
    # Используем return_exceptions=True, чтобы ошибка бота не блокировала веб-сервер
    results = await asyncio.gather(
        start_bot(),
        start_web(),
        return_exceptions=True,
    )
    
    # Проверяем результаты
    bot_result, web_result = results
    
    if isinstance(bot_result, Exception):
        logger.error(f"Telegram бот завершился с ошибкой: {bot_result}")
        logger.warning("Веб-сервер продолжает работать, но функционал бота недоступен")
        # Если веб-сервер тоже упал, поднимаем ошибку
        if isinstance(web_result, Exception):
            logger.error(f"Веб-сервер также завершился с ошибкой: {web_result}")
            raise web_result
    elif isinstance(web_result, Exception):
        logger.error(f"Веб-сервер завершился с ошибкой: {web_result}")
        raise web_result


if __name__ == "__main__":
    asyncio.run(main())

