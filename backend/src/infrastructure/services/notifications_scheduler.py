import os

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.database import Database
from src.infrastructure.database.repositories.birthday_repository_impl import (
    BirthdayRepositoryImpl,
)
from src.infrastructure.services.notification_service_impl import NotificationServiceImpl


def _create_notification_service(
    bot: Bot, session: AsyncSession
) -> NotificationServiceImpl:
    """
    Создать экземпляр NotificationServiceImpl.

    Args:
        bot: Экземпляр Telegram бота
        session: Асинхронная сессия базы данных

    Returns:
        NotificationServiceImpl: Экземпляр сервиса уведомлений
    """
    birthday_repo = BirthdayRepositoryImpl(session)
    return NotificationServiceImpl(bot, birthday_repo, session)


async def setup_notifications(bot: Bot, db: Database):
    """Настроить расписание уведомлений."""
    # Получаем настройки из переменных окружения
    timezone = os.getenv("TIMEZONE", "Asia/Tokyo")
    notification_hour = int(os.getenv("NOTIFICATION_HOUR", "9"))
    notification_minute = int(os.getenv("NOTIFICATION_MINUTE", "0"))

    scheduler = AsyncIOScheduler(timezone=timezone)

    async def send_today():
        async for session in db.get_session():
            service = _create_notification_service(bot, session)
            await service.send_today_notifications()

    async def send_week():
        async for session in db.get_session():
            service = _create_notification_service(bot, session)
            await service.send_week_notifications()

    async def send_month():
        async for session in db.get_session():
            service = _create_notification_service(bot, session)
            await service.send_month_notifications()

    # Ежедневно в указанное время
    scheduler.add_job(
        send_today,
        trigger=CronTrigger(hour=notification_hour, minute=notification_minute),
        id="daily_birthdays",
    )

    # Каждый понедельник в указанное время
    scheduler.add_job(
        send_week,
        trigger=CronTrigger(
            day_of_week=0, hour=notification_hour, minute=notification_minute
        ),
        id="weekly_birthdays",
    )

    # 1 число каждого месяца в указанное время
    scheduler.add_job(
        send_month,
        trigger=CronTrigger(day=1, hour=notification_hour, minute=notification_minute),
        id="monthly_birthdays",
    )

    scheduler.start()
    return scheduler
