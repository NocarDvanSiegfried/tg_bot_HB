from dataclasses import dataclass
from datetime import date


@dataclass
class DateRange:
    start_date: date
    end_date: date

    def contains(self, check_date: date) -> bool:
        """Проверяет, входит ли дата в диапазон."""
        return self.start_date <= check_date <= self.end_date
