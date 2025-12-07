from typing import Optional

from src.application.ports.responsible_repository import ResponsibleRepository
from src.domain.entities.responsible_person import ResponsiblePerson


class UpdateResponsibleUseCase:
    def __init__(self, responsible_repository: ResponsibleRepository):
        self.responsible_repository = responsible_repository

    async def execute(
        self,
        responsible_id: int,
        full_name: Optional[str] = None,
        company: Optional[str] = None,
        position: Optional[str] = None,
    ) -> ResponsiblePerson:
        """Обновить ответственного."""
        existing = await self.responsible_repository.get_by_id(responsible_id)
        if not existing:
            raise ValueError(f"Responsible with id {responsible_id} not found")

        updated = ResponsiblePerson(
            id=responsible_id,
            full_name=full_name if full_name is not None else existing.full_name,
            company=company if company is not None else existing.company,
            position=position if position is not None else existing.position,
        )
        return await self.responsible_repository.update(updated)

