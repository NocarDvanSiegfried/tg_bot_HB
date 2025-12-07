from typing import List

from src.application.ports.responsible_repository import ResponsibleRepository
from src.domain.entities.responsible_person import ResponsiblePerson


class GetAllResponsibleUseCase:
    """Use-case для получения всех ответственных."""

    def __init__(self, responsible_repository: ResponsibleRepository):
        self.responsible_repository = responsible_repository

    async def execute(self) -> List[ResponsiblePerson]:
        """Получить всех ответственных."""
        return await self.responsible_repository.get_all()

