import pytest
from datetime import date
from unittest.mock import AsyncMock, Mock

from src.application.use_cases.greeting.create_card import CreateCardUseCase
from src.application.ports.card_generator import CardGeneratorPort
from src.domain.entities.birthday import Birthday


class TestCreateCardUseCase:
    """Тесты для use-case создания открытки."""

    @pytest.mark.asyncio
    async def test_create_card_success(self):
        """Тест успешного создания открытки."""
        # Arrange
        mock_birthday_repo = AsyncMock()
        mock_card_generator = Mock(spec=CardGeneratorPort)
        
        birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment="Комментарий",
        )
        mock_birthday_repo.get_by_id.return_value = birthday
        mock_card_generator.generate_card.return_value = b"fake_image_bytes"
        
        use_case = CreateCardUseCase(mock_birthday_repo, mock_card_generator)

        # Act
        result = await use_case.execute(
            birthday_id=1,
            greeting_text="Поздравляем!",
            qr_url="https://example.com/qr",
        )

        # Assert
        assert result == b"fake_image_bytes"
        mock_birthday_repo.get_by_id.assert_called_once_with(1)
        mock_card_generator.generate_card.assert_called_once_with(
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            greeting_text="Поздравляем!",
            comment="Комментарий",
            qr_url="https://example.com/qr",
        )

    @pytest.mark.asyncio
    async def test_create_card_without_qr(self):
        """Тест создания открытки без QR кода."""
        # Arrange
        mock_birthday_repo = AsyncMock()
        mock_card_generator = Mock(spec=CardGeneratorPort)
        
        birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )
        mock_birthday_repo.get_by_id.return_value = birthday
        mock_card_generator.generate_card.return_value = b"fake_image_bytes"
        
        use_case = CreateCardUseCase(mock_birthday_repo, mock_card_generator)

        # Act
        result = await use_case.execute(
            birthday_id=1,
            greeting_text="Поздравляем!",
            qr_url=None,
        )

        # Assert
        assert result == b"fake_image_bytes"
        mock_card_generator.generate_card.assert_called_once_with(
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            greeting_text="Поздравляем!",
            comment=None,
            qr_url=None,
        )

    @pytest.mark.asyncio
    async def test_create_card_birthday_not_found(self):
        """Тест создания открытки для несуществующего дня рождения."""
        # Arrange
        mock_birthday_repo = AsyncMock()
        mock_card_generator = Mock(spec=CardGeneratorPort)
        
        mock_birthday_repo.get_by_id.return_value = None
        
        use_case = CreateCardUseCase(mock_birthday_repo, mock_card_generator)

        # Act & Assert
        from src.domain.exceptions.not_found import BirthdayNotFoundError
        with pytest.raises(BirthdayNotFoundError, match="Birthday with id 999 not found"):
            await use_case.execute(
                birthday_id=999,
                greeting_text="Поздравляем!",
            )
        
        mock_birthday_repo.get_by_id.assert_called_once_with(999)
        mock_card_generator.generate_card.assert_not_called()

