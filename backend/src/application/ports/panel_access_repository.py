from abc import ABC, abstractmethod


class PanelAccessRepository(ABC):
    @abstractmethod
    async def has_access(self, user_id: int) -> bool:
        """Проверить, есть ли у пользователя доступ к панели."""
        pass

    @abstractmethod
    async def record_access(self, user_id: int) -> None:
        """Записать факт доступа пользователя к панели."""
        pass