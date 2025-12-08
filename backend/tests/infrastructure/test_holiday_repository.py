import pytest
from datetime import date
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.repositories.holiday_repository_impl import HolidayRepositoryImpl
from src.infrastructure.database.models import ProfessionalHolidayModel
from src.domain.entities.professional_holiday import ProfessionalHoliday


class TestHolidayRepositoryImpl:
    """Тесты для репозитория праздников."""

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
        return HolidayRepositoryImpl(mock_session)

    @pytest.mark.asyncio
    async def test_create_holiday(self, repository, mock_session):
        """Тест создания праздника."""
        # Arrange
        holiday = ProfessionalHoliday(
            id=None,
            name="День программиста",
            description="Профессиональный праздник",
            date=date(2024, 9, 13),
        )
        
        # Создаем реальную модель, которая будет добавлена в сессию
        # После flush и refresh модель получит ID
        added_model = None
        
        def add_side_effect(model):
            nonlocal added_model
            added_model = model
            model.id = 1  # ID устанавливается после flush
        
        def refresh_side_effect(model):
            # После refresh модель уже имеет ID
            pass
        
        mock_session.add.side_effect = add_side_effect
        mock_session.refresh.side_effect = refresh_side_effect

        # Act
        result = await repository.create(holiday)

        # Assert
        assert result.id == 1
        assert result.name == "День программиста"
        assert result.description == "Профессиональный праздник"
        assert result.date == date(2024, 9, 13)
        mock_session.add.assert_called_once()
        mock_session.flush.assert_called_once()
        mock_session.refresh.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_by_id_exists(self, repository, mock_session):
        """Тест получения праздника по ID (существует)."""
        # Arrange
        mock_model = ProfessionalHolidayModel(
            id=1,
            name="День программиста",
            description="Профессиональный праздник",
            holiday_date=date(2024, 9, 13),
        )
        
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_model
        mock_session.execute.return_value = mock_result

        # Act
        result = await repository.get_by_id(1)

        # Assert
        assert result is not None
        assert result.id == 1
        assert result.name == "День программиста"
        assert result.date == date(2024, 9, 13)

    @pytest.mark.asyncio
    async def test_get_by_id_not_exists(self, repository, mock_session):
        """Тест получения праздника по ID (не существует)."""
        # Arrange
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_session.execute.return_value = mock_result

        # Act
        result = await repository.get_by_id(999)

        # Assert
        assert result is None

    @pytest.mark.asyncio
    async def test_get_by_date(self, repository, mock_session):
        """Тест получения праздников по дате."""
        # Arrange
        check_date = date(2024, 9, 13)
        mock_models = [
            ProfessionalHolidayModel(
                id=1,
                name="День программиста",
                description="Профессиональный праздник",
                holiday_date=check_date,
            ),
            ProfessionalHolidayModel(
                id=2,
                name="День тестировщика",
                description="Еще один праздник",
                holiday_date=check_date,
            ),
        ]
        
        mock_result = MagicMock()
        mock_result.scalars.return_value.all.return_value = mock_models
        mock_session.execute.return_value = mock_result

        # Act
        result = await repository.get_by_date(check_date)

        # Assert
        assert len(result) == 2
        assert result[0].id == 1
        assert result[1].id == 2

    @pytest.mark.asyncio
    async def test_update_holiday(self, repository, mock_session):
        """Тест обновления праздника."""
        # Arrange
        existing_holiday = ProfessionalHoliday(
            id=1,
            name="День программиста",
            description="Старое описание",
            date=date(2024, 9, 13),
        )
        
        mock_model = ProfessionalHolidayModel(
            id=1,
            name="День программиста",
            description="Новое описание",
            holiday_date=date(2024, 9, 13),
        )
        
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_model
        mock_session.execute.return_value = mock_result
        mock_session.refresh.return_value = None

        # Act
        result = await repository.update(existing_holiday)

        # Assert
        assert result.id == 1
        mock_session.flush.assert_called_once()
        mock_session.refresh.assert_called_once()

    @pytest.mark.asyncio
    async def test_update_holiday_no_id(self, repository, mock_session):
        """Тест обновления праздника без ID."""
        # Arrange
        holiday = ProfessionalHoliday(
            id=None,
            name="День программиста",
            description="Описание",
            date=date(2024, 9, 13),
        )

        # Act & Assert
        with pytest.raises(ValueError, match="Holiday ID is required"):
            await repository.update(holiday)

    @pytest.mark.asyncio
    async def test_update_holiday_not_found(self, repository, mock_session):
        """Тест обновления несуществующего праздника."""
        # Arrange
        holiday = ProfessionalHoliday(
            id=999,
            name="День программиста",
            description="Описание",
            date=date(2024, 9, 13),
        )
        
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_session.execute.return_value = mock_result

        # Act & Assert
        with pytest.raises(ValueError, match="Holiday with id 999 not found"):
            await repository.update(holiday)

    @pytest.mark.asyncio
    async def test_delete_holiday(self, repository, mock_session):
        """Тест удаления праздника."""
        # Arrange
        mock_model = ProfessionalHolidayModel(
            id=1,
            name="День программиста",
            description="Описание",
            holiday_date=date(2024, 9, 13),
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
    async def test_delete_holiday_not_exists(self, repository, mock_session):
        """Тест удаления несуществующего праздника."""
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
        """Тест получения всех праздников."""
        # Arrange
        mock_models = [
            ProfessionalHolidayModel(
                id=1,
                name="День программиста",
                description="Описание 1",
                holiday_date=date(2024, 9, 13),
            ),
            ProfessionalHolidayModel(
                id=2,
                name="День тестировщика",
                description="Описание 2",
                holiday_date=date(2024, 10, 1),
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

