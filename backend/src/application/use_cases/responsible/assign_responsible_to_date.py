from datetime import date

from src.application.ports.responsible_repository import ResponsibleRepository


class AssignResponsibleToDateUseCase:
    def __init__(self, responsible_repository: ResponsibleRepository):
        self.responsible_repository = responsible_repository

    async def execute(self, responsible_id: int, assignment_date: date) -> None:
        """Назначить ответственного на дату."""
        existing = await self.responsible_repository.get_by_id(responsible_id)
        if not existing:
            raise ValueError(f"Responsible with id {responsible_id} not found")
        await self.responsible_repository.assign_to_date(responsible_id, assignment_date)

