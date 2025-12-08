import pytest
from unittest.mock import AsyncMock

from src.application.use_cases.responsible.delete_responsible import DeleteResponsibleUseCase
from src.domain.entities.responsible_person import ResponsiblePerson


class TestDeleteResponsibleUseCase:
    """Тесты для use-case удаления ответственного лица."""

    @pytest.mark.asyncio
    async def test_delete_responsible_success(self):
        """Тест успешного удаления ответственного лица."""
        # Arrange
        mock_repository = AsyncMock()
        existing_responsible = ResponsiblePerson(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Менеджер",
        )
        mock_repository.get_by_id.return_value = existing_responsible

        use_case = DeleteResponsibleUseCase(mock_repository)

        # Act
        await use_case.execute(responsible_id=1)

        # Assert
        mock_repository.get_by_id.assert_called_once_with(1)
        mock_repository.delete.assert_called_once_with(1)

    @pytest.mark.asyncio
    async def test_delete_responsible_not_found(self):
        """Тест удаления несуществующего ответственного лица."""
        # Arrange
        mock_repository = AsyncMock()
        mock_repository.get_by_id.return_value = None

        use_case = DeleteResponsibleUseCase(mock_repository)

        # Act & Assert
        with pytest.raises(ValueError, match="Responsible with id 999 not found"):
            await use_case.execute(responsible_id=999)
        
        mock_repository.delete.assert_not_called()

