from datetime import date

from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.ports.responsible_repository import ResponsibleRepository
from src.domain.entities.responsible_person import ResponsiblePerson
from src.infrastructure.database.models import (
    DateResponsibleAssignmentModel,
    ResponsiblePersonModel,
)


class ResponsibleRepositoryImpl(ResponsibleRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    def _to_entity(self, model: ResponsiblePersonModel) -> ResponsiblePerson:
        """Преобразовать модель в entity."""
        return ResponsiblePerson(
            id=model.id,
            full_name=model.full_name,
            company=model.company,
            position=model.position,
        )

    async def create(self, responsible: ResponsiblePerson) -> ResponsiblePerson:
        model = ResponsiblePersonModel(
            full_name=responsible.full_name,
            company=responsible.company,
            position=responsible.position,
        )
        self.session.add(model)
        await self.session.flush()
        await self.session.refresh(model)
        return self._to_entity(model)

    async def get_by_id(self, responsible_id: int) -> ResponsiblePerson | None:
        result = await self.session.execute(
            select(ResponsiblePersonModel).where(ResponsiblePersonModel.id == responsible_id)
        )
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None

    async def get_by_date(self, check_date: date) -> ResponsiblePerson | None:
        result = await self.session.execute(
            select(DateResponsibleAssignmentModel).where(
                DateResponsibleAssignmentModel.assignment_date == check_date
            )
        )
        assignment = result.scalar_one_or_none()
        if not assignment:
            return None

        result = await self.session.execute(
            select(ResponsiblePersonModel).where(
                ResponsiblePersonModel.id == assignment.responsible_person_id
            )
        )
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None

    async def update(self, responsible: ResponsiblePerson) -> ResponsiblePerson:
        if not responsible.id:
            raise ValueError("Responsible ID is required for update")

        result = await self.session.execute(
            select(ResponsiblePersonModel).where(ResponsiblePersonModel.id == responsible.id)
        )
        model = result.scalar_one_or_none()
        if not model:
            raise ValueError(f"Responsible with id {responsible.id} not found")

        model.full_name = responsible.full_name
        model.company = responsible.company
        model.position = responsible.position

        await self.session.flush()
        await self.session.refresh(model)
        return self._to_entity(model)

    async def delete(self, responsible_id: int) -> None:
        result = await self.session.execute(
            select(ResponsiblePersonModel).where(ResponsiblePersonModel.id == responsible_id)
        )
        model = result.scalar_one_or_none()
        if model:
            await self.session.delete(model)
            await self.session.flush()

    async def assign_to_date(self, responsible_id: int, assignment_date: date) -> None:
        # Удаляем существующее назначение на эту дату
        result = await self.session.execute(
            select(DateResponsibleAssignmentModel).where(
                DateResponsibleAssignmentModel.assignment_date == assignment_date
            )
        )
        existing = result.scalar_one_or_none()
        if existing:
            await self.session.delete(existing)

        # Создаем новое назначение
        assignment = DateResponsibleAssignmentModel(
            assignment_date=assignment_date,
            responsible_person_id=responsible_id,
        )
        self.session.add(assignment)
        await self.session.flush()

    async def search(self, query: str) -> list[ResponsiblePerson]:
        search_pattern = f"%{query}%"
        result = await self.session.execute(
            select(ResponsiblePersonModel).where(
                or_(
                    ResponsiblePersonModel.full_name.ilike(search_pattern),
                    ResponsiblePersonModel.company.ilike(search_pattern),
                    ResponsiblePersonModel.position.ilike(search_pattern),
                )
            )
        )
        models = result.scalars().all()
        return [self._to_entity(model) for model in models]

    async def get_all(self) -> list[ResponsiblePerson]:
        result = await self.session.execute(select(ResponsiblePersonModel))
        models = result.scalars().all()
        return [self._to_entity(model) for model in models]
