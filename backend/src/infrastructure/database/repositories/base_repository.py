"""Базовый класс для репозиториев с общими методами."""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

# Type variables для generic repository
TEntity = TypeVar("TEntity")
TModel = TypeVar("TModel", bound=DeclarativeBase)


class BaseRepositoryImpl(ABC, Generic[TEntity, TModel]):
    """Базовый класс для репозиториев с общими CRUD операциями."""

    def __init__(self, session: AsyncSession, model_class: type[TModel]):
        """
        Инициализация базового репозитория.

        Args:
            session: Сессия БД
            model_class: Класс модели SQLAlchemy
        """
        self.session = session
        self.model_class = model_class

    @abstractmethod
    def _to_entity(self, model: TModel) -> TEntity:
        """
        Преобразовать модель в entity.

        Args:
            model: Модель SQLAlchemy

        Returns:
            Domain entity
        """
        pass

    @abstractmethod
    def _to_model(self, entity: TEntity) -> TModel:
        """
        Преобразовать entity в модель.

        Args:
            entity: Domain entity

        Returns:
            Модель SQLAlchemy
        """
        pass

    async def create(self, entity: TEntity) -> TEntity:
        """
        Создать новую запись.

        Args:
            entity: Domain entity для создания

        Returns:
            Созданная entity с ID
        """
        model = self._to_model(entity)
        self.session.add(model)
        await self.session.flush()
        await self.session.refresh(model)
        return self._to_entity(model)

    async def get_by_id(self, entity_id: int) -> TEntity | None:
        """
        Получить запись по ID.

        Args:
            entity_id: ID записи

        Returns:
            Entity или None, если не найдено
        """
        result = await self.session.execute(
            select(self.model_class).where(self.model_class.id == entity_id)
        )
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None

    async def get_all(self) -> list[TEntity]:
        """
        Получить все записи.

        Returns:
            Список entities
        """
        result = await self.session.execute(select(self.model_class))
        models = result.scalars().all()
        return [self._to_entity(model) for model in models]

    async def update(self, entity: TEntity) -> TEntity:
        """
        Обновить запись.

        Args:
            entity: Entity с обновленными данными (должен иметь id)

        Returns:
            Обновленная entity

        Raises:
            ValueError: Если entity не имеет id или запись не найдена
        """
        # Проверка наличия id должна быть в дочерних классах,
        # так как не все entities могут иметь id
        # Но для базовой реализации предполагаем, что entity имеет атрибут id
        if not hasattr(entity, "id") or not entity.id:
            raise ValueError(f"{type(entity).__name__} ID is required for update")

        result = await self.session.execute(
            select(self.model_class).where(self.model_class.id == entity.id)
        )
        model = result.scalar_one_or_none()
        if not model:
            raise ValueError(f"{type(entity).__name__} with id {entity.id} not found")

        # Обновление полей должно быть в дочерних классах,
        # так как структура полей разная
        # Этот метод должен быть переопределен в дочерних классах
        raise NotImplementedError(
            "update() должен быть переопределен в дочернем классе для обновления конкретных полей"
        )

    async def delete(self, entity_id: int) -> None:
        """
        Удалить запись по ID.

        Args:
            entity_id: ID записи для удаления
        """
        result = await self.session.execute(
            select(self.model_class).where(self.model_class.id == entity_id)
        )
        model = result.scalar_one_or_none()
        if model:
            await self.session.delete(model)
            await self.session.flush()

