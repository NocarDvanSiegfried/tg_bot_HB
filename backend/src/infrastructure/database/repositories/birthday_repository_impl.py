from datetime import date

from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.ports.birthday_repository import BirthdayRepository
from src.domain.entities.birthday import Birthday
from src.domain.exceptions.validation import ValidationError
from src.infrastructure.database.models import BirthdayModel
from src.infrastructure.database.repositories.base_repository import BaseRepositoryImpl
from src.infrastructure.database.repositories.search_validator import (
    validate_and_sanitize_search_query,
)


class BirthdayRepositoryImpl(BaseRepositoryImpl[Birthday, BirthdayModel], BirthdayRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, BirthdayModel)

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
            id=entity.id if entity.id else None,
            full_name=entity.full_name,
            company=entity.company,
            position=entity.position,
            birth_date=entity.birth_date,
            comment=entity.comment,
        )

    async def get_by_date(self, check_date: date) -> list[Birthday]:
        result = await self.session.execute(
            select(BirthdayModel).where(BirthdayModel.birth_date == check_date)
        )
        models = result.scalars().all()
        return [self._to_entity(model) for model in models]

    async def get_by_date_range(self, start_date: date, end_date: date) -> list[Birthday]:
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

    async def search(self, query: str) -> list[Birthday]:
        """
        Поиск по ФИО, компании, должности.

        Args:
            query: Поисковый запрос (валидируется и санитизируется)

        Returns:
            Список найденных дней рождения

        Raises:
            ValidationError: Если запрос невалиден или пуст
        """
        # Валидация и санитизация запроса
        sanitized_query, is_valid = validate_and_sanitize_search_query(query)
        if not is_valid:
            raise ValidationError(
                f"Invalid search query. Query must be between {1} and {200} characters "
                "and contain only letters, numbers, spaces, and basic punctuation."
            )

        # Используем параметризованный запрос для безопасности
        # SQLAlchemy автоматически экранирует параметры
        search_pattern = f"%{sanitized_query}%"
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

