from src.application.ports.panel_access_repository import PanelAccessRepository


class CheckPanelAccessUseCase:
    def __init__(self, panel_access_repository: PanelAccessRepository):
        self.panel_access_repository = panel_access_repository

    async def execute(self, user_id: int) -> bool:
        """Проверить доступ пользователя к панели управления."""
        return await self.panel_access_repository.has_access(user_id)

