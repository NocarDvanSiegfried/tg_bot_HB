import logging
from datetime import date, timedelta

from aiogram import Bot
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.ports.birthday_repository import BirthdayRepository
from src.domain.entities.birthday import Birthday
from src.infrastructure.database.models import PanelAccessModel

logger = logging.getLogger(__name__)


class NotificationServiceImpl:
    def __init__(
        self,
        bot: Bot,
        birthday_repository: BirthdayRepository,
        session: AsyncSession,
    ):
        self.bot = bot
        self.birthday_repository = birthday_repository
        self.session = session

    async def get_active_users(self) -> list[int]:
        """Получить список активных пользователей (тех, кто взаимодействовал с ботом)."""
        result = await self.session.execute(
            select(PanelAccessModel).distinct(PanelAccessModel.user_id)
        )
        users = result.scalars().all()
        return [user.user_id for user in users]

    async def send_today_notifications(self):
        """Отправить уведомления о ДР сегодня."""
        today = date.today()
        birthdays = await self.birthday_repository.get_by_date(today)

        if not birthdays:
            return

        users = await self.get_active_users()
        message = self._format_today_message(birthdays, today)

        for user_id in users:
            try:
                await self.bot.send_message(user_id, message)
            except Exception as e:
                logger.error(
                    "Failed to send notification",
                    extra={
                        "user_id": user_id,
                        "error_type": type(e).__name__,
                        "error_message": str(e),
                    }
                )

    async def send_week_notifications(self):
        """Отправить уведомления о ДР на этой неделе."""
        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)

        birthdays = await self.birthday_repository.get_by_date_range(week_start, week_end)

        if not birthdays:
            return

        users = await self.get_active_users()
        message = self._format_week_message(birthdays, week_start, week_end)

        for user_id in users:
            try:
                await self.bot.send_message(user_id, message)
            except Exception as e:
                logger.error(
                    "Failed to send notification",
                    extra={
                        "user_id": user_id,
                        "error_type": type(e).__name__,
                        "error_message": str(e),
                    }
                )

    async def send_month_notifications(self):
        """Отправить уведомления о ДР в этом месяце."""
        today = date.today()
        month_start = date(today.year, today.month, 1)
        if today.month == 12:
            month_end = date(today.year + 1, 1, 1) - timedelta(days=1)
        else:
            month_end = date(today.year, today.month + 1, 1) - timedelta(days=1)

        birthdays = await self.birthday_repository.get_by_date_range(month_start, month_end)

        if not birthdays:
            return

        users = await self.get_active_users()
        message = self._format_month_message(birthdays, month_start)

        for user_id in users:
            try:
                await self.bot.send_message(user_id, message)
            except Exception as e:
                logger.error(
                    "Failed to send notification",
                    extra={
                        "user_id": user_id,
                        "error_type": type(e).__name__,
                        "error_message": str(e),
                    }
                )

    def _format_today_message(self, birthdays: list[Birthday], check_date: date) -> str:
        """Форматировать сообщение о ДР сегодня."""
        text = f"🎂 Сегодня ({check_date.strftime('%d.%m.%Y')}) дни рождения:\n\n"
        for bd in birthdays:
            age = bd.calculate_age(check_date)
            text += f"• {bd.full_name}\n"
            text += f"  {bd.company}, {bd.position}\n"
            text += f"  Исполняется {age} лет\n"
            if bd.comment:
                text += f"  Комментарий: {bd.comment}\n"
            text += "\n"
        return text

    def _format_week_message(
        self, birthdays: list[Birthday], week_start: date, week_end: date
    ) -> str:
        """Форматировать сообщение о ДР на неделе."""
        text = f"📅 На этой неделе ({week_start.strftime('%d.%m')} - {week_end.strftime('%d.%m.%Y')}) дни рождения:\n\n"
        for bd in birthdays:
            age = bd.calculate_age(bd.birth_date)
            text += f"• {bd.full_name} - {bd.birth_date.strftime('%d.%m')}\n"
            text += f"  {bd.company}, {bd.position}\n"
            text += f"  Исполняется {age} лет\n\n"
        return text

    def _format_month_message(self, birthdays: list[Birthday], month_start: date) -> str:
        """Форматировать сообщение о ДР в месяце."""
        text = f"📅 В этом месяце ({month_start.strftime('%B %Y')}) дни рождения:\n\n"
        for bd in birthdays:
            age = bd.calculate_age(bd.birth_date)
            text += f"• {bd.full_name} - {bd.birth_date.strftime('%d.%m')}\n"
            text += f"  {bd.company}, {bd.position}\n"
            text += f"  Исполняется {age} лет\n\n"
        return text

