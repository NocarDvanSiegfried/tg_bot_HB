from dataclasses import dataclass
from datetime import date


@dataclass
class ProfessionalHoliday:
    id: int | None
    name: str
    description: str | None
    date: date

