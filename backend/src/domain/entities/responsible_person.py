from dataclasses import dataclass
from typing import Optional


@dataclass
class ResponsiblePerson:
    id: Optional[int]
    full_name: str
    company: str
    position: str

