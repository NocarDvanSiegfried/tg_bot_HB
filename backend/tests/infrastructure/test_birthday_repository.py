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

    @pytest.mark.asyncio
    async def test_get_by_date_range(self, repository, mock_session):
        """Тест получения дней рождения по диапазону дат."""
        # Arrange
        start_date = date(1990, 5, 1)
        end_date = date(1990, 5, 31)
        models = [
            BirthdayModel(
                id=1,
                full_name="Иван Иванов",
                company="ООО Тест",
                position="Разработчик",
                birth_date=date(1990, 5, 15),
                comment=None,
            ),
            BirthdayModel(
                id=2,
                full_name="Петр Петров",
                company="ООО Тест",
                position="Менеджер",
                birth_date=date(1990, 5, 20),
                comment="Комментарий",
            ),
        ]
        result_mock = MagicMock()
        result_mock.scalars.return_value.all.return_value = models
        mock_session.execute.return_value = result_mock

        # Act
        result = await repository.get_by_date_range(start_date, end_date)

        # Assert
        assert len(result) == 2
        assert result[0].id == 1
        assert result[1].id == 2

    @pytest.mark.asyncio
    async def test_get_by_date_range_empty(self, repository, mock_session):
        """Тест получения дней рождения по диапазону дат (пустой результат)."""
        # Arrange
        start_date = date(2000, 1, 1)
        end_date = date(2000, 1, 31)
        result_mock = MagicMock()
        result_mock.scalars.return_value.all.return_value = []
        mock_session.execute.return_value = result_mock

        # Act
        result = await repository.get_by_date_range(start_date, end_date)

        # Assert
        assert len(result) == 0

    @pytest.mark.asyncio
    async def test_update_birthday(self, repository, mock_session):
        """Тест обновления дня рождения."""
        # Arrange
        existing_model = BirthdayModel(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment="Старый комментарий",
        )
        result_mock = MagicMock()
        result_mock.scalar_one_or_none.return_value = existing_model
        mock_session.execute.return_value = result_mock

        updated_birthday = Birthday(
            id=1,
            full_name="Иван Иванов Обновленный",
            company="ООО Новая Компания",
            position="Старший Разработчик",
            birth_date=date(1990, 5, 15),
            comment="Новый комментарий",
        )

        # Act
        result = await repository.update(updated_birthday)

        # Assert
        assert result.id == 1
        assert result.full_name == "Иван Иванов Обновленный"
        assert result.company == "ООО Новая Компания"
        assert result.position == "Старший Разработчик"
        assert result.comment == "Новый комментарий"
        mock_session.flush.assert_called_once()
        mock_session.refresh.assert_called_once()

    @pytest.mark.asyncio
    async def test_update_birthday_no_id(self, repository, mock_session):
        """Тест обновления дня рождения без ID (должна быть ошибка)."""
        # Arrange
        birthday = Birthday(
            id=None,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )

        # Act & Assert
        with pytest.raises(ValueError, match="Birthday ID is required"):
            await repository.update(birthday)

    @pytest.mark.asyncio
    async def test_update_birthday_not_found(self, repository, mock_session):
        """Тест обновления несуществующего дня рождения."""
        # Arrange
        result_mock = MagicMock()
        result_mock.scalar_one_or_none.return_value = None
        mock_session.execute.return_value = result_mock

        birthday = Birthday(
            id=999,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )

        # Act & Assert
        with pytest.raises(ValueError, match="Birthday with id 999 not found"):
            await repository.update(birthday)

    @pytest.mark.asyncio
    async def test_search(self, repository, mock_session):
        """Тест поиска дней рождения."""
        # Arrange
        query = "Иван"
        models = [
            BirthdayModel(
                id=1,
                full_name="Иван Иванов",
                company="ООО Тест",
                position="Разработчик",
                birth_date=date(1990, 5, 15),
                comment=None,
            )
        ]
        result_mock = MagicMock()
        result_mock.scalars.return_value.all.return_value = models
        mock_session.execute.return_value = result_mock

        # Act
        result = await repository.search(query)

        # Assert
        assert len(result) == 1
        assert result[0].id == 1
        assert "Иван" in result[0].full_name

    @pytest.mark.asyncio
    async def test_search_empty(self, repository, mock_session):
        """Тест поиска дней рождения (пустой результат)."""
        # Arrange
        query = "Несуществующий"
        result_mock = MagicMock()
        result_mock.scalars.return_value.all.return_value = []
        mock_session.execute.return_value = result_mock

        # Act
        result = await repository.search(query)

        # Assert
        assert len(result) == 0

    @pytest.mark.asyncio
    async def test_search_by_company(self, repository, mock_session):
        """Тест поиска по компании."""
        # Arrange
        query = "Тест"
        models = [
            BirthdayModel(
                id=1,
                full_name="Иван Иванов",
                company="ООО Тест",
                position="Разработчик",
                birth_date=date(1990, 5, 15),
                comment=None,
            )
        ]
        result_mock = MagicMock()
        result_mock.scalars.return_value.all.return_value = models
        mock_session.execute.return_value = result_mock

        # Act
        result = await repository.search(query)

        # Assert
        assert len(result) == 1
        assert "Тест" in result[0].company

    @pytest.mark.asyncio
    async def test_get_all(self, repository, mock_session):
        """Тест получения всех дней рождения."""
        # Arrange
        models = [
            BirthdayModel(
                id=1,
                full_name="Иван Иванов",
                company="ООО Тест",
                position="Разработчик",
                birth_date=date(1990, 5, 15),
                comment=None,
            ),
            BirthdayModel(
                id=2,
                full_name="Петр Петров",
                company="ООО Тест",
                position="Менеджер",
                birth_date=date(1991, 6, 20),
                comment="Комментарий",
            ),
        ]
        result_mock = MagicMock()
        result_mock.scalars.return_value.all.return_value = models
        mock_session.execute.return_value = result_mock

        # Act
        result = await repository.get_all()

        # Assert
        assert len(result) == 2
        assert result[0].id == 1
        assert result[1].id == 2

    @pytest.mark.asyncio
    async def test_get_all_empty(self, repository, mock_session):
        """Тест получения всех дней рождения (пустой результат)."""
        # Arrange
        result_mock = MagicMock()
        result_mock.scalars.return_value.all.return_value = []
        mock_session.execute.return_value = result_mock

        # Act
        result = await repository.get_all()

        # Assert
        assert len(result) == 0

    @pytest.mark.asyncio
    async def test_to_model_conversion(self, repository):
        """Тест преобразования entity в модель (покрытие _to_model)."""
        # Arrange
        birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment="Комментарий",
        )

        # Act
        model = repository._to_model(birthday)

        # Assert
        assert isinstance(model, BirthdayModel)
        assert model.id == 1
        assert model.full_name == "Иван Иванов"
        assert model.company == "ООО Тест"
        assert model.position == "Разработчик"
        assert model.birth_date == date(1990, 5, 15)
        assert model.comment == "Комментарий"

