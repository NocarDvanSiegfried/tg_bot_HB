from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class ProfessionalHoliday:
    id: Optional[int]
    name: str
    description: Optional[str]
    date: date

