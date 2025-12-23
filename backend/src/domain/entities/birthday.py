from dataclasses import dataclass
from datetime import date


@dataclass
class Birthday:
    id: int | None
    full_name: str
    company: str
    position: str
    birth_date: date
    comment: str | None = None
    responsible: str | None = None

    def calculate_age(self, reference_date: date) -> int:
        """Вычисляет возраст на указанную дату."""
        age = reference_date.year - self.birth_date.year
        if (reference_date.month, reference_date.day) < (
            self.birth_date.month,
            self.birth_date.day,
        ):
            age -= 1
        return age
