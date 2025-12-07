from datetime import date
from typing import List, Optional

from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.ports.birthday_repository import BirthdayRepository
from src.domain.entities.birthday import Birthday
from src.infrastructure.database.models import BirthdayModel


class BirthdayRepositoryImpl(BirthdayRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    def _to_entity(self, model: BirthdayModel) -> Birthday:
        """Преобразовать модель в entity."""
        return Birthday(
            id=model.id,
            full_name=model.full_name,
            company=model.company,
            position=model.position,
            birth_date=model.birth_date,
            comment=model.comment,
        )

    def _to_model(self, entity: Birthday) -> BirthdayModel:
        """Преобразовать entity в модель."""
        return BirthdayModel(
            id=entity.id,
            full_name=entity.full_name,
            company=entity.company,
            position=entity.position,
            birth_date=entity.birth_date,
            comment=entity.comment,
        )

    async def create(self, birthday: Birthday) -> Birthday:
        model = BirthdayModel(
            full_name=birthday.full_name,
            company=birthday.company,
            position=birthday.position,
            birth_date=birthday.birth_date,
            comment=birthday.comment,
        )
        self.session.add(model)
        await self.session.flush()
        await self.session.refresh(model)
        return self._to_entity(model)

    async def get_by_id(self, birthday_id: int) -> Optional[Birthday]:
        result = await self.session.execute(
            select(BirthdayModel).where(BirthdayModel.id == birthday_id)
        )
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None

    async def get_by_date(self, check_date: date) -> List[Birthday]:
        result = await self.session.execute(
            select(BirthdayModel).where(
                BirthdayModel.birth_date == check_date
            )
        )
        models = result.scalars().all()
        return [self._to_entity(model) for model in models]

    async def get_by_date_range(self, start_date: date, end_date: date) -> List[Birthday]:
        result = await self.session.execute(
            select(BirthdayModel).where(
                BirthdayModel.birth_date >= start_date,
                BirthdayModel.birth_date <= end_date,
            )
        )
        models = result.scalars().all()
        return [self._to_entity(model) for model in models]

    async def update(self, birthday: Birthday) -> Birthday:
        if not birthday.id:
            raise ValueError("Birthday ID is required for update")
        
        result = await self.session.execute(
            select(BirthdayModel).where(BirthdayModel.id == birthday.id)
        )
        model = result.scalar_one_or_none()
        if not model:
            raise ValueError(f"Birthday with id {birthday.id} not found")
        
        model.full_name = birthday.full_name
        model.company = birthday.company
        model.position = birthday.position
        model.birth_date = birthday.birth_date
        model.comment = birthday.comment
        
        await self.session.flush()
        await self.session.refresh(model)
        return self._to_entity(model)

    async def delete(self, birthday_id: int) -> None:
        result = await self.session.execute(
            select(BirthdayModel).where(BirthdayModel.id == birthday_id)
        )
        model = result.scalar_one_or_none()
        if model:
            await self.session.delete(model)
            await self.session.flush()

    async def search(self, query: str) -> List[Birthday]:
        search_pattern = f"%{query}%"
        result = await self.session.execute(
            select(BirthdayModel).where(
                or_(
                    BirthdayModel.full_name.ilike(search_pattern),
                    BirthdayModel.company.ilike(search_pattern),
                    BirthdayModel.position.ilike(search_pattern),
                )
            )
        )
        models = result.scalars().all()
        return [self._to_entity(model) for model in models]

    async def get_all(self) -> List[Birthday]:
        result = await self.session.execute(select(BirthdayModel))
        models = result.scalars().all()
        return [self._to_entity(model) for model in models]

