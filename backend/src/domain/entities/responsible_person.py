from dataclasses import dataclass


@dataclass
class ResponsiblePerson:
    id: int | None
    full_name: str
    company: str
    position: str
