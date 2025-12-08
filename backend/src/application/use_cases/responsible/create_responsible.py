from src.application.ports.responsible_repository import ResponsibleRepository
from src.domain.entities.responsible_person import ResponsiblePerson


class CreateResponsibleUseCase:
    def __init__(self, responsible_repository: ResponsibleRepository):
        self.responsible_repository = responsible_repository

    async def execute(
        self,
        full_name: str,
        company: str,
        position: str,
    ) -> ResponsiblePerson:
        """Создать нового ответственного."""
        responsible = ResponsiblePerson(
            id=None,
            full_name=full_name,
            company=company,
            position=position,
        )
        return await self.responsible_repository.create(responsible)
