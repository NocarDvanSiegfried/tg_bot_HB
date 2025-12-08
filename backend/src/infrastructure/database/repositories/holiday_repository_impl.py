from datetime import date

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.ports.holiday_repository import HolidayRepository
from src.domain.entities.professional_holiday import ProfessionalHoliday
from src.infrastructure.database.models import ProfessionalHolidayModel


class HolidayRepositoryImpl(HolidayRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    def _to_entity(self, model: ProfessionalHolidayModel) -> ProfessionalHoliday:
        """Преобразовать модель в entity."""
        return ProfessionalHoliday(
            id=model.id,
            name=model.name,
            description=model.description,
            date=model.holiday_date,
        )

    async def create(self, holiday: ProfessionalHoliday) -> ProfessionalHoliday:
        model = ProfessionalHolidayModel(
            name=holiday.name,
            description=holiday.description,
            holiday_date=holiday.date,
        )
        self.session.add(model)
        await self.session.flush()
        await self.session.refresh(model)
        return self._to_entity(model)

    async def get_by_id(self, holiday_id: int) -> ProfessionalHoliday | None:
        result = await self.session.execute(
            select(ProfessionalHolidayModel).where(ProfessionalHolidayModel.id == holiday_id)
        )
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None

    async def get_by_date(self, check_date: date) -> list[ProfessionalHoliday]:
        result = await self.session.execute(
            select(ProfessionalHolidayModel).where(
                ProfessionalHolidayModel.holiday_date == check_date
            )
        )
        models = result.scalars().all()
        return [self._to_entity(model) for model in models]

    async def update(self, holiday: ProfessionalHoliday) -> ProfessionalHoliday:
        if not holiday.id:
            raise ValueError("Holiday ID is required for update")

        result = await self.session.execute(
            select(ProfessionalHolidayModel).where(ProfessionalHolidayModel.id == holiday.id)
        )
        model = result.scalar_one_or_none()
        if not model:
            raise ValueError(f"Holiday with id {holiday.id} not found")

        model.name = holiday.name
        model.description = holiday.description
        model.holiday_date = holiday.date

        await self.session.flush()
        await self.session.refresh(model)
        return self._to_entity(model)

    async def delete(self, holiday_id: int) -> None:
        result = await self.session.execute(
            select(ProfessionalHolidayModel).where(ProfessionalHolidayModel.id == holiday_id)
        )
        model = result.scalar_one_or_none()
        if model:
            await self.session.delete(model)
            await self.session.flush()

    async def get_all(self) -> list[ProfessionalHoliday]:
        result = await self.session.execute(select(ProfessionalHolidayModel))
        models = result.scalars().all()
        return [self._to_entity(model) for model in models]

