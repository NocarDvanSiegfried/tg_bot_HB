from src.application.ports.responsible_repository import ResponsibleRepository


class DeleteResponsibleUseCase:
    def __init__(self, responsible_repository: ResponsibleRepository):
        self.responsible_repository = responsible_repository

    async def execute(self, responsible_id: int) -> None:
        """Удалить ответственного."""
        existing = await self.responsible_repository.get_by_id(responsible_id)
        if not existing:
            raise ValueError(f"Responsible with id {responsible_id} not found")
        await self.responsible_repository.delete(responsible_id)

