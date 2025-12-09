"""Тесты для BaseRepositoryImpl."""

import pytest
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.birthday import Birthday
from src.infrastructure.database.models import BirthdayModel
from src.infrastructure.database.repositories.base_repository import BaseRepositoryImpl


class TestBaseRepositoryImpl:
    """Тесты для базового репозитория."""

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
        """Тестовый репозиторий, наследующийся от BaseRepositoryImpl."""

        class TestRepository(BaseRepositoryImpl[Birthday, BirthdayModel]):
            def _to_entity(self, model: BirthdayModel) -> Birthday:
                return Birthday(
                    id=model.id,
                    full_name=model.full_name,
                    company=model.company,
                    position=model.position,
                    birth_date=model.birth_date,
                    comment=model.comment,
                )

            def _to_model(self, entity: Birthday) -> BirthdayModel:
                return BirthdayModel(
                    id=entity.id if entity.id else None,
                    full_name=entity.full_name,
                    company=entity.company,
                    position=entity.position,
                    birth_date=entity.birth_date,
                    comment=entity.comment,
                )

        return TestRepository(mock_session, BirthdayModel)

    @pytest.mark.asyncio
    async def test_create(self, repository, mock_session):
        """Тест создания записи."""
        # Arrange
        birthday = Birthday(
            id=None,
            full_name="Test Name",
            company="Test Company",
            position="Test Position",
            birth_date=None,
            comment=None,
        )

        # Настраиваем мок для refresh
        mock_model = BirthdayModel(id=1, full_name="Test Name", company="Test Company", position="Test Position")
        mock_session.refresh.side_effect = lambda m: setattr(m, "id", 1)

        # Act
        result = await repository.create(birthday)

        # Assert
        mock_session.add.assert_called_once()
        mock_session.flush.assert_called_once()
        mock_session.refresh.assert_called_once()
        assert result.full_name == birthday.full_name

    @pytest.mark.asyncio
    async def test_get_by_id_found(self, repository, mock_session):
        """Тест получения по ID (найдено)."""
        # Arrange
        entity_id = 1
        mock_model = BirthdayModel(
            id=1, full_name="Test", company="Test", position="Test", birth_date=None, comment=None
        )
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_model
        mock_session.execute.return_value = mock_result

        # Act
        result = await repository.get_by_id(entity_id)

        # Assert
        assert result is not None
        assert result.id == 1

    @pytest.mark.asyncio
    async def test_get_by_id_not_found(self, repository, mock_session):
        """Тест получения по ID (не найдено)."""
        # Arrange
        entity_id = 999
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_session.execute.return_value = mock_result

        # Act
        result = await repository.get_by_id(entity_id)

        # Assert
        assert result is None

    @pytest.mark.asyncio
    async def test_get_all(self, repository, mock_session):
        """Тест получения всех записей."""
        # Arrange
        mock_models = [
            BirthdayModel(id=1, full_name="Test1", company="Test", position="Test", birth_date=None, comment=None),
            BirthdayModel(id=2, full_name="Test2", company="Test", position="Test", birth_date=None, comment=None),
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

    @pytest.mark.asyncio
    async def test_get_all_empty(self, repository, mock_session):
        """Тест получения всех записей (пустой результат)."""
        # Arrange
        mock_result = MagicMock()
        mock_result.scalars.return_value.all.return_value = []
        mock_session.execute.return_value = mock_result

        # Act
        result = await repository.get_all()

        # Assert
        assert len(result) == 0

    @pytest.mark.asyncio
    async def test_delete_found(self, repository, mock_session):
        """Тест удаления записи (найдено)."""
        # Arrange
        entity_id = 1
        mock_model = BirthdayModel(id=1, full_name="Test", company="Test", position="Test")
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_model
        mock_session.execute.return_value = mock_result

        # Act
        await repository.delete(entity_id)

        # Assert
        mock_session.delete.assert_called_once_with(mock_model)
        mock_session.flush.assert_called_once()

    @pytest.mark.asyncio
    async def test_delete_not_found(self, repository, mock_session):
        """Тест удаления записи (не найдено)."""
        # Arrange
        entity_id = 999
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_session.execute.return_value = mock_result

        # Act
        await repository.delete(entity_id)

        # Assert
        mock_session.delete.assert_not_called()
        mock_session.flush.assert_not_called()

    @pytest.mark.asyncio
    async def test_update_not_implemented(self, repository):
        """Тест что update требует переопределения."""
        # Arrange
        from datetime import date
        birthday = Birthday(
            id=1, full_name="Test", company="Test", position="Test", birth_date=date(1990, 1, 1), comment=None
        )

        # Act & Assert
        with pytest.raises(NotImplementedError):
            await repository.update(birthday)

