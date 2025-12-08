from abc import ABC, abstractmethod
from datetime import date

from src.domain.entities.birthday import Birthday


class NotificationService(ABC):
    @abstractmethod
    def get_birthdays_today(self, check_date: date) -> list[Birthday]:
        """Получить дни рождения на указанную дату."""
        pass

    @abstractmethod
    def get_birthdays_this_week(self, week_start: date) -> list[Birthday]:
        """Получить дни рождения на неделю, начиная с указанной даты."""
        pass

    @abstractmethod
    def get_birthdays_this_month(self, month_start: date) -> list[Birthday]:
        """Получить дни рождения в месяце, начиная с указанной даты."""
        pass
