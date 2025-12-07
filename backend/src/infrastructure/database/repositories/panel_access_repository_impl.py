from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.ports.panel_access_repository import PanelAccessRepository
from src.infrastructure.database.models import PanelAccessModel


class PanelAccessRepositoryImpl(PanelAccessRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def has_access(self, user_id: int) -> bool:
        """Проверить, есть ли у пользователя доступ к панели."""
        stmt = select(PanelAccessModel).where(PanelAccessModel.user_id == user_id).limit(1)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none() is not None

