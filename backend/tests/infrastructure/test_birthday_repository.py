import pytest
from datetime import date
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.repositories.birthday_repository_impl import BirthdayRepositoryImpl
from src.infrastructure.database.models import BirthdayModel
from src.domain.entities.birthday import Birthday


class TestBirthdayRepositoryImpl:
    """Тесты для репозитория дней рождения."""

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
        return BirthdayRepositoryImpl(mock_session)

    @pytest.mark.asyncio
    async def test_create_birthday(self, repository, mock_session):
        """Тест создания дня рождения."""
        # Arrange
        birthday = Birthday(
            id=None,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment="Комментарий",
        )

        # Мокируем результат flush и refresh
        created_model = BirthdayModel(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment="Комментарий",
        )
        
        # Мокируем refresh, чтобы он обновлял модель
        def refresh_side_effect(model):
            model.id = 1
        
        mock_session.refresh.side_effect = refresh_side_effect

        # Act
        result = await repository.create(birthday)

        # Assert
        assert result.id == 1
        assert result.full_name == "Иван Иванов"
        mock_session.add.assert_called_once()
        mock_session.flush.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_by_id_found(self, repository, mock_session):
        """Тест получения дня рождения по ID (найден)."""
        # Arrange
        model = BirthdayModel(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment="Комментарий",
        )
        result_mock = MagicMock()
        result_mock.scalar_one_or_none.return_value = model
        mock_session.execute.return_value = result_mock

        # Act
        result = await repository.get_by_id(1)

        # Assert
        assert result is not None
        assert result.id == 1
        assert result.full_name == "Иван Иванов"

    @pytest.mark.asyncio
    async def test_get_by_id_not_found(self, repository, mock_session):
        """Тест получения дня рождения по ID (не найден)."""
        # Arrange
        result_mock = MagicMock()
        result_mock.scalar_one_or_none.return_value = None
        mock_session.execute.return_value = result_mock

        # Act
        result = await repository.get_by_id(999)

        # Assert
        assert result is None

    @pytest.mark.asyncio
    async def test_get_by_date(self, repository, mock_session):
        """Тест получения дней рождения по дате."""
        # Arrange
        check_date = date(1990, 5, 15)
        models = [
            BirthdayModel(
                id=1,
                full_name="Иван Иванов",
                company="ООО Тест",
                position="Разработчик",
                birth_date=check_date,
                comment=None,
            )
        ]
        result_mock = MagicMock()
        result_mock.scalars.return_value.all.return_value = models
        mock_session.execute.return_value = result_mock

        # Act
        result = await repository.get_by_date(check_date)

        # Assert
        assert len(result) == 1
        assert result[0].id == 1
        assert result[0].birth_date == check_date

    @pytest.mark.asyncio
    async def test_delete_birthday(self, repository, mock_session):
        """Тест удаления дня рождения."""
        # Arrange
        model = BirthdayModel(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )
        result_mock = MagicMock()
        result_mock.scalar_one_or_none.return_value = model
        mock_session.execute.return_value = result_mock

        # Act
        await repository.delete(1)

        # Assert
        mock_session.delete.assert_called_once()
        mock_session.flush.assert_called_once()

