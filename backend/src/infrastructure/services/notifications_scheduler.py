from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from src.infrastructure.database.database import Database
from src.infrastructure.services.notification_service_impl import NotificationServiceImpl


async def setup_notifications(bot: Bot, db: Database):
    """Настроить расписание уведомлений."""
    scheduler = AsyncIOScheduler(timezone="Asia/Tokyo")

    async def send_today():
        async for session in db.get_session():
            from src.infrastructure.database.repositories.birthday_repository_impl import (
                BirthdayRepositoryImpl,
            )

            birthday_repo = BirthdayRepositoryImpl(session)
            service = NotificationServiceImpl(bot, birthday_repo, session)
            await service.send_today_notifications()

    async def send_week():
        async for session in db.get_session():
            from src.infrastructure.database.repositories.birthday_repository_impl import (
                BirthdayRepositoryImpl,
            )

            birthday_repo = BirthdayRepositoryImpl(session)
            service = NotificationServiceImpl(bot, birthday_repo, session)
            await service.send_week_notifications()

    async def send_month():
        async for session in db.get_session():
            from src.infrastructure.database.repositories.birthday_repository_impl import (
                BirthdayRepositoryImpl,
            )

            birthday_repo = BirthdayRepositoryImpl(session)
            service = NotificationServiceImpl(bot, birthday_repo, session)
            await service.send_month_notifications()

    # Ежедневно в 09:00 UTC+9
    scheduler.add_job(
        send_today,
        trigger=CronTrigger(hour=9, minute=0),
        id="daily_birthdays",
    )

    # Каждый понедельник в 09:00 UTC+9
    scheduler.add_job(
        send_week,
        trigger=CronTrigger(day_of_week=0, hour=9, minute=0),
        id="weekly_birthdays",
    )

    # 1 число каждого месяца в 09:00 UTC+9
    scheduler.add_job(
        send_month,
        trigger=CronTrigger(day=1, hour=9, minute=0),
        id="monthly_birthdays",
    )

    scheduler.start()
    return scheduler
