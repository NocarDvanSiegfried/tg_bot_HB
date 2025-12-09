from datetime import date

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.ports.holiday_repository import HolidayRepository
from src.domain.entities.professional_holiday import ProfessionalHoliday
from src.infrastructure.database.models import ProfessionalHolidayModel
from src.infrastructure.database.repositories.base_repository import BaseRepositoryImpl


class HolidayRepositoryImpl(
    BaseRepositoryImpl[ProfessionalHoliday, ProfessionalHolidayModel], HolidayRepository
):
    def __init__(self, session: AsyncSession):
        super().__init__(session, ProfessionalHolidayModel)

    def _to_entity(self, model: ProfessionalHolidayModel) -> ProfessionalHoliday:
        """Преобразовать модель в entity."""
        return ProfessionalHoliday(
            id=model.id,
            name=model.name,
            description=model.description,
            date=model.holiday_date,
        )

    def _to_model(self, entity: ProfessionalHoliday) -> ProfessionalHolidayModel:
        """Преобразовать entity в модель."""
        return ProfessionalHolidayModel(
            id=entity.id if entity.id else None,
            name=entity.name,
            description=entity.description,
            holiday_date=entity.date,
        )

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
