import pytest
from datetime import date
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.repositories.responsible_repository_impl import ResponsibleRepositoryImpl
from src.infrastructure.database.models import ResponsiblePersonModel, DateResponsibleAssignmentModel
from src.domain.entities.responsible_person import ResponsiblePerson


class TestResponsibleRepositoryImpl:
    """Тесты для репозитория ответственных лиц."""

    @pytest.fixture
    def mock_session(self):
        """Мок сессии БД."""
        session = AsyncMock(spec=AsyncSession)
        session.execute = AsyncMock()
        session.add = MagicMock()
        session.flush = AsyncMock()
        session.refresh = AsyncMock()
        session.delete = AsyncMock()
        return session

    @pytest.fixture
    def repository(self, mock_session):
        """Репозиторий с мок сессией."""
        return ResponsibleRepositoryImpl(mock_session)

    @pytest.mark.asyncio
    async def test_create_responsible(self, repository, mock_session):
        """Тест создания ответственного лица."""
        # Arrange
        responsible = ResponsiblePerson(
            id=None,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Менеджер",
        )
        
        mock_session.refresh.return_value = None

        # Act
        result = await repository.create(responsible)

        # Assert
        assert result.full_name == "Иван Иванов"
        assert result.company == "ООО Тест"
        assert result.position == "Менеджер"
        mock_session.add.assert_called_once()
        mock_session.flush.assert_called_once()
        mock_session.refresh.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_by_id_exists(self, repository, mock_session):
        """Тест получения ответственного лица по ID (существует)."""
        # Arrange
        mock_model = ResponsiblePersonModel(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Менеджер",
        )
        
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_model
        mock_session.execute.return_value = mock_result

        # Act
        result = await repository.get_by_id(1)

        # Assert
        assert result is not None
        assert result.id == 1
        assert result.full_name == "Иван Иванов"

    @pytest.mark.asyncio
    async def test_get_by_id_not_exists(self, repository, mock_session):
        """Тест получения ответственного лица по ID (не существует)."""
        # Arrange
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_session.execute.return_value = mock_result

        # Act
        result = await repository.get_by_id(999)

        # Assert
        assert result is None

    @pytest.mark.asyncio
    async def test_get_by_date_exists(self, repository, mock_session):
        """Тест получения ответственного лица по дате (существует)."""
        # Arrange
        check_date = date(2024, 5, 15)
        mock_assignment = DateResponsibleAssignmentModel(
            id=1,
            assignment_date=check_date,
            responsible_person_id=1,
        )
        mock_responsible = ResponsiblePersonModel(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Менеджер",
        )
        
        # Мокируем два вызова execute: первый для assignment, второй для responsible
        mock_result_assignment = MagicMock()
        mock_result_assignment.scalar_one_or_none.return_value = mock_assignment
        
        mock_result_responsible = MagicMock()
        mock_result_responsible.scalar_one_or_none.return_value = mock_responsible
        
        # Настраиваем execute для возврата разных результатов при разных вызовах
        mock_session.execute.side_effect = [mock_result_assignment, mock_result_responsible]

        # Act
        result = await repository.get_by_date(check_date)

        # Assert
        assert result is not None
        assert result.id == 1
        assert result.full_name == "Иван Иванов"

    @pytest.mark.asyncio
    async def test_get_by_date_not_exists(self, repository, mock_session):
        """Тест получения ответственного лица по дате (не существует)."""
        # Arrange
        check_date = date(2024, 5, 15)
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_session.execute.return_value = mock_result

        # Act
        result = await repository.get_by_date(check_date)

        # Assert
        assert result is None

    @pytest.mark.asyncio
    async def test_assign_to_date(self, repository, mock_session):
        """Тест назначения ответственного лица на дату."""
        # Arrange
        check_date = date(2024, 5, 15)
        responsible_id = 1
        
        # Мокируем удаление существующего назначения (если есть)
        mock_result_delete = MagicMock()
        mock_result_delete.scalar_one_or_none.return_value = None
        mock_session.execute.return_value = mock_result_delete
        mock_session.refresh.return_value = None

        # Act
        await repository.assign_to_date(responsible_id, check_date)

        # Assert
        mock_session.add.assert_called_once()
        mock_session.flush.assert_called_once()

    @pytest.mark.asyncio
    async def test_update_responsible(self, repository, mock_session):
        """Тест обновления ответственного лица."""
        # Arrange
        existing_responsible = ResponsiblePerson(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Менеджер",
        )
        
        mock_model = ResponsiblePersonModel(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Старший менеджер",
        )
        
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_model
        mock_session.execute.return_value = mock_result
        mock_session.refresh.return_value = None

        # Act
        result = await repository.update(existing_responsible)

        # Assert
        assert result.id == 1
        mock_session.flush.assert_called_once()
        mock_session.refresh.assert_called_once()

    @pytest.mark.asyncio
    async def test_update_responsible_no_id(self, repository, mock_session):
        """Тест обновления ответственного лица без ID."""
        # Arrange
        responsible = ResponsiblePerson(
            id=None,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Менеджер",
        )

        # Act & Assert
        with pytest.raises(ValueError, match="Responsible ID is required"):
            await repository.update(responsible)

    @pytest.mark.asyncio
    async def test_update_responsible_not_found(self, repository, mock_session):
        """Тест обновления несуществующего ответственного лица."""
        # Arrange
        responsible = ResponsiblePerson(
            id=999,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Менеджер",
        )
        
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_session.execute.return_value = mock_result

        # Act & Assert
        with pytest.raises(ValueError, match="Responsible with id 999 not found"):
            await repository.update(responsible)

    @pytest.mark.asyncio
    async def test_delete_responsible(self, repository, mock_session):
        """Тест удаления ответственного лица."""
        # Arrange
        mock_model = ResponsiblePersonModel(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Менеджер",
        )
        
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_model
        mock_session.execute.return_value = mock_result

        # Act
        await repository.delete(1)

        # Assert
        mock_session.delete.assert_called_once_with(mock_model)
        mock_session.flush.assert_called_once()

    @pytest.mark.asyncio
    async def test_delete_responsible_not_exists(self, repository, mock_session):
        """Тест удаления несуществующего ответственного лица."""
        # Arrange
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_session.execute.return_value = mock_result

        # Act
        await repository.delete(999)

        # Assert
        mock_session.delete.assert_not_called()

    @pytest.mark.asyncio
    async def test_get_all(self, repository, mock_session):
        """Тест получения всех ответственных лиц."""
        # Arrange
        mock_models = [
            ResponsiblePersonModel(
                id=1,
                full_name="Иван Иванов",
                company="ООО Тест",
                position="Менеджер",
            ),
            ResponsiblePersonModel(
                id=2,
                full_name="Петр Петров",
                company="ООО Другой",
                position="Директор",
            ),
        ]
        
        mock_result = MagicMock()
        mock_result.scalars.return_value.all.return_value = mock_models
        mock_session.execute.return_value = mock_result

        # Act
        result = await repository.get_all()

        # Assert
        assert len(result) == 2
        assert result[0].id == 1
        assert result[1].id == 2

