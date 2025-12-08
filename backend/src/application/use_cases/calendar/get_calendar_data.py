from datetime import date

from src.application.ports.birthday_repository import BirthdayRepository
from src.application.ports.holiday_repository import HolidayRepository
from src.application.ports.responsible_repository import ResponsibleRepository


class GetCalendarDataUseCase:
    def __init__(
        self,
        birthday_repository: BirthdayRepository,
        holiday_repository: HolidayRepository,
        responsible_repository: ResponsibleRepository,
    ):
        self.birthday_repository = birthday_repository
        self.holiday_repository = holiday_repository
        self.responsible_repository = responsible_repository

    async def execute(
        self,
        check_date: date,
    ) -> dict:
        """Получить данные календаря на указанную дату."""
        birthdays = await self.birthday_repository.get_by_date(check_date)
        holidays = await self.holiday_repository.get_by_date(check_date)
        responsible = await self.responsible_repository.get_by_date(check_date)

        return {
            "date": check_date.isoformat(),
            "birthdays": [
                {
                    "id": b.id,
                    "full_name": b.full_name,
                    "company": b.company,
                    "position": b.position,
                    "age": b.calculate_age(check_date),
                    "comment": b.comment,
                }
                for b in birthdays
            ],
            "holidays": [
                {
                    "id": h.id,
                    "name": h.name,
                    "description": h.description,
                }
                for h in holidays
            ],
            "responsible": {
                "id": responsible.id,
                "full_name": responsible.full_name,
                "company": responsible.company,
                "position": responsible.position,
            } if responsible else None,
        }

