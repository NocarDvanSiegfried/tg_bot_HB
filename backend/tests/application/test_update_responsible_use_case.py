import pytest
from unittest.mock import AsyncMock

from src.application.use_cases.responsible.update_responsible import UpdateResponsibleUseCase
from src.domain.entities.responsible_person import ResponsiblePerson


class TestUpdateResponsibleUseCase:
    """Тесты для use-case обновления ответственного лица."""

    @pytest.mark.asyncio
    async def test_update_responsible_success(self):
        """Тест успешного обновления ответственного лица."""
        # Arrange
        mock_repository = AsyncMock()
        existing_responsible = ResponsiblePerson(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Менеджер",
        )
        updated_responsible = ResponsiblePerson(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Старший менеджер",
        )
        
        mock_repository.get_by_id.return_value = existing_responsible
        mock_repository.update.return_value = updated_responsible

        use_case = UpdateResponsibleUseCase(mock_repository)

        # Act
        result = await use_case.execute(
            responsible_id=1,
            position="Старший менеджер",
        )

        # Assert
        assert result.position == "Старший менеджер"
        mock_repository.get_by_id.assert_called_once_with(1)
        mock_repository.update.assert_called_once()

    @pytest.mark.asyncio
    async def test_update_responsible_not_found(self):
        """Тест обновления несуществующего ответственного лица."""
        # Arrange
        mock_repository = AsyncMock()
        mock_repository.get_by_id.return_value = None

        use_case = UpdateResponsibleUseCase(mock_repository)

        # Act & Assert
        with pytest.raises(ValueError, match="Responsible with id 999 not found"):
            await use_case.execute(responsible_id=999, full_name="Новое имя")
        
        mock_repository.update.assert_not_called()

