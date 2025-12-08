from src.application.ports.panel_access_repository import PanelAccessRepository


class RecordPanelAccessUseCase:
    def __init__(self, panel_access_repository: PanelAccessRepository):
        self.panel_access_repository = panel_access_repository

    async def execute(self, user_id: int) -> None:
        """Записать факт доступа пользователя к панели управления."""
        await self.panel_access_repository.record_access(user_id)
