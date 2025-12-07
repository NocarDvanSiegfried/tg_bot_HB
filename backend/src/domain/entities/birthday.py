from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Birthday:
    id: Optional[int]
    full_name: str
    company: str
    position: str
    birth_date: date
    comment: Optional[str]

    def calculate_age(self, reference_date: date) -> int:
        """Вычисляет возраст на указанную дату."""
        age = reference_date.year - self.birth_date.year
        if (reference_date.month, reference_date.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

