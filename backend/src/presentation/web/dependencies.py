"""Dependencies для FastAPI endpoints."""

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.factories.use_case_factory import UseCaseFactory
from src.infrastructure.database.database_factory import get_database


async def get_db_session() -> AsyncSession:
    """
    Dependency для получения сессии БД.

    Сессия автоматически закрывается после завершения запроса.
    """
    db = get_database()
    async for session in db.get_session():
        yield session


async def get_use_case_factory(session: AsyncSession = Depends(get_db_session)) -> UseCaseFactory:
    """
    Dependency для получения фабрики use-cases.

    Args:
        session: Сессия БД, получаемая через dependency injection.

    Returns:
        UseCaseFactory с настроенными зависимостями
    """
    return UseCaseFactory(session=session)


async def get_readonly_use_case_factory() -> UseCaseFactory:
    """
    Dependency для получения фабрики use-cases для read-only операций.

    Используется для endpoints, которые только читают данные и не требуют транзакций.
    Создает новую сессию БД для каждого запроса.
    """
    db = get_database()
    async for session in db.get_session():
        try:
            factory = UseCaseFactory(session=session)
            yield factory
        finally:
            # Сессия автоматически закроется после завершения запроса
            pass

