import asyncio
import logging
import os
import uvicorn
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.infrastructure.config.env_validator import (
    get_database_name_from_url,
    mask_database_url,
    validate_database_env_sync,
    validate_database_url,
    validate_telegram_token,
)
from src.infrastructure.database.database_factory import get_database
from src.presentation.telegram.handlers import (
    start_handler,
)
from src.presentation.telegram.middleware.database_middleware import DatabaseMiddleware
from src.presentation.web.app import app as web_app
from src.infrastructure.services.notifications_scheduler import setup_notifications

# Экспорт app для совместимости с прямым запуском uvicorn
# Позволяет запускать как через `python main.py`, так и через `uvicorn backend.main:app`
app = web_app

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def start_bot():
    """Запуск Telegram бота."""
    # Проверяем, включен ли бот
    enable_bot = os.getenv("ENABLE_TELEGRAM_BOT", "true").lower() in ("true", "1", "yes")
    if not enable_bot:
        logger.info("Telegram бот отключен через ENABLE_TELEGRAM_BOT=false. Пропускаем запуск бота.")
        return
    
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        logger.warning(
            "TELEGRAM_BOT_TOKEN не установлен. Бот не будет запущен. "
            "Веб-сервер продолжит работать. "
            "Чтобы включить бота, установите TELEGRAM_BOT_TOKEN в .env файл."
        )
        return

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
    
    # Добавляем обработчик ошибок для конфликтов
    from aiogram.exceptions import TelegramConflictError
    
    @dp.errors()
    async def error_handler(update, exception):
        """Обработчик ошибок для перехвата конфликтов."""
        if isinstance(exception, TelegramConflictError):
            logger.error(
                "⚠️ КОНФЛИКТ: Другой экземпляр бота уже запущен с тем же токеном.\n"
                f"Ошибка: {exception}\n"
                "Возможные решения:\n"
                "1. Остановите другие экземпляры бота (локальные или на других серверах)\n"
                "2. Используйте webhook вместо polling (настройте через переменные окружения)\n"
                "3. Отключите бота, установив ENABLE_TELEGRAM_BOT=false в .env\n"
                "Веб-сервер продолжит работать без бота."
            )
            # Останавливаем polling при конфликте
            await dp.stop_polling()
            await bot.session.close()
            return True  # Обработано, не пробрасываем дальше
        return False  # Не обработано, пробрасываем дальше

    # Регистрация роутеров
    dp.include_router(start_handler.router)

    # Запуск polling с обработкой ошибок
    # Обработчик конфликтов уже зарегистрирован через @dp.errors() выше
    try:
        logger.info("Запуск Telegram polling...")
        await dp.start_polling(bot, allowed_updates=["message", "callback_query"])
    except Exception as e:
        error_type = type(e).__name__
        error_message = str(e)
        logger.error(f"Критическая ошибка при работе Telegram бота: {error_type}: {error_message}")
        
        # Обработка конфликта с другим экземпляром бота (fallback)
        if "Conflict" in error_message or "TelegramConflictError" in error_type:
            logger.error(
                "⚠️ КОНФЛИКТ: Другой экземпляр бота уже запущен с тем же токеном.\n"
                "Возможные решения:\n"
                "1. Остановите другие экземпляры бота (локальные или на других серверах)\n"
                "2. Используйте webhook вместо polling (настройте через переменные окружения)\n"
                "3. Отключите бота, установив ENABLE_TELEGRAM_BOT=false в .env\n"
                "Веб-сервер продолжит работать без бота."
            )
            # Пытаемся корректно закрыть сессию
            try:
                await bot.session.close()
            except:
                pass
            return
        
        # Пробуем получить более детальную информацию об ошибке
        if "Unauthorized" in error_message or "TelegramUnauthorizedError" in error_type:
            logger.error(
                "Telegram API вернул ошибку 'Unauthorized'. Возможные причины:\n"
                "1. Токен недействителен или был отозван\n"
                "2. Бот был удален в @BotFather\n"
                "3. Токен был изменен, но контейнер использует старый (перезапустите контейнер)\n"
                "4. Проблемы с сетью при обращении к Telegram API\n"
                "Проверьте токен в .env файле и убедитесь, что бот активен в @BotFather."
            )
            # Пытаемся корректно закрыть сессию
            try:
                await bot.session.close()
            except:
                pass
            return
        
        # Для других ошибок логируем и продолжаем работу веб-сервера
        logger.warning("Telegram бот не запущен, но веб-сервер продолжит работать")
        try:
            await bot.session.close()
        except:
            pass
        return


async def start_web():
    """Запуск FastAPI веб-сервера."""
    port = int(os.getenv("WEB_PORT", "8000"))
    logger.info(f"🌐 Инициализация веб-сервера на порту {port}...")
    
    config = uvicorn.Config(
        web_app,
        host="0.0.0.0",
        port=port,
        log_level="info",
    )
    server = uvicorn.Server(config)
    
    logger.info(f"✅ Веб-сервер готов к запуску на http://0.0.0.0:{port}")
    await server.serve()


async def main():
    """Главная функция запуска."""
    # Шаг 1: Проверка синхронизации переменных окружения
    logger.info("Проверка синхронизации переменных окружения PostgreSQL...")
    is_sync, messages = validate_database_env_sync()
    if not is_sync:
        errors = [msg for msg in messages if "не установлен" in msg.lower() or "несовпадение" in msg.lower()]
        warnings = [msg for msg in messages if msg not in errors]
        
        if errors:
            logger.error("Критические ошибки синхронизации переменных окружения:")
            for error in errors:
                logger.error(f"  - {error}")
            raise ValueError(
                "Ошибки синхронизации переменных окружения PostgreSQL. "
                "Проверьте, что POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB установлены "
                "и совпадают с значениями в DATABASE_URL. См. env.example для примеров."
            )
        
        if warnings:
            logger.warning("Предупреждения при проверке переменных окружения:")
            for warning in warnings:
                logger.warning(f"  - {warning}")
    else:
        logger.info("✅ Все переменные окружения синхронизированы")
        if messages:
            logger.warning("Предупреждения:")
            for msg in messages:
                logger.warning(f"  - {msg}")

    # Шаг 2: Валидация DATABASE_URL при старте приложения
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

    # ВСЕГДА запускаем веб-сервер независимо от бота
    logger.info("🚀 Запуск веб-сервера...")
    web_task = asyncio.create_task(start_web())
    
    # Даем веб-серверу время запуститься
    await asyncio.sleep(2)
    
    # Проверяем, что веб-сервер запустился
    if web_task.done():
        error = web_task.exception()
        if error:
            logger.error(f"❌ Веб-сервер завершился с ошибкой: {error}")
            raise error
        else:
            logger.error("❌ Веб-сервер завершился сразу после запуска!")
            raise RuntimeError("Веб-сервер не запустился")
    
    logger.info("✅ Веб-сервер успешно запущен и работает")
    
    # Запускаем бота отдельно, если включен
    enable_bot = os.getenv("ENABLE_TELEGRAM_BOT", "true").lower() in ("true", "1", "yes")
    
    if enable_bot:
        logger.info("🤖 Запуск Telegram бота...")
        try:
            await start_bot()
        except Exception as e:
            logger.error(f"❌ Бот не запущен: {e}")
            logger.warning("⚠️  Веб-сервер продолжает работать независимо от бота")
            # Веб-сервер продолжает работать независимо
    else:
        logger.info("ℹ️  Telegram бот отключен через ENABLE_TELEGRAM_BOT=false")
    
    # Ждем завершения веб-сервера (он должен работать бесконечно)
    try:
        await web_task
    except Exception as e:
        logger.error(f"❌ Веб-сервер завершился с ошибкой: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(main())

