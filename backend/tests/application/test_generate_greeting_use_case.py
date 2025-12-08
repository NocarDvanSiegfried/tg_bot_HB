import pytest
from datetime import date
from unittest.mock import AsyncMock

from src.application.use_cases.greeting.generate_greeting import GenerateGreetingUseCase
from src.domain.entities.birthday import Birthday


class TestGenerateGreetingUseCase:
    """Тесты для use-case генерации поздравления."""

    @pytest.mark.asyncio
    async def test_generate_greeting_success(self):
        """Тест успешной генерации поздравления."""
        # Arrange
        mock_birthday_repo = AsyncMock()
        mock_openrouter_client = AsyncMock()
        
        birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )
        mock_birthday_repo.get_by_id.return_value = birthday
        mock_openrouter_client.generate_greeting.return_value = "Поздравляем с днем рождения!"
        
        use_case = GenerateGreetingUseCase(mock_birthday_repo, mock_openrouter_client)

        # Act
        result = await use_case.execute(
            birthday_id=1,
            style="formal",
            length="short",
            theme=None,
        )

        # Assert
        assert result == "Поздравляем с днем рождения!"
        mock_birthday_repo.get_by_id.assert_called_once_with(1)
        mock_openrouter_client.generate_greeting.assert_called_once_with(
            person_name="Иван Иванов",
            person_company="ООО Тест",
            person_position="Разработчик",
            style="formal",
            length="short",
            theme=None,
        )

    @pytest.mark.asyncio
    async def test_generate_greeting_with_theme(self):
        """Тест генерации поздравления с темой."""
        # Arrange
        mock_birthday_repo = AsyncMock()
        mock_openrouter_client = AsyncMock()
        
        birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )
        mock_birthday_repo.get_by_id.return_value = birthday
        mock_openrouter_client.generate_greeting.return_value = "Поздравляем!"
        
        use_case = GenerateGreetingUseCase(mock_birthday_repo, mock_openrouter_client)

        # Act
        result = await use_case.execute(
            birthday_id=1,
            style="casual",
            length="long",
            theme="work",
        )

        # Assert
        assert result == "Поздравляем!"
        mock_openrouter_client.generate_greeting.assert_called_once_with(
            person_name="Иван Иванов",
            person_company="ООО Тест",
            person_position="Разработчик",
            style="casual",
            length="long",
            theme="work",
        )

    @pytest.mark.asyncio
    async def test_generate_greeting_birthday_not_found(self):
        """Тест генерации поздравления для несуществующего дня рождения."""
        # Arrange
        mock_birthday_repo = AsyncMock()
        mock_openrouter_client = AsyncMock()
        
        mock_birthday_repo.get_by_id.return_value = None
        
        use_case = GenerateGreetingUseCase(mock_birthday_repo, mock_openrouter_client)

        # Act & Assert
        with pytest.raises(ValueError, match="Birthday with id 999 not found"):
            await use_case.execute(
                birthday_id=999,
                style="formal",
                length="short",
            )
        
        mock_birthday_repo.get_by_id.assert_called_once_with(999)
        mock_openrouter_client.generate_greeting.assert_not_called()





