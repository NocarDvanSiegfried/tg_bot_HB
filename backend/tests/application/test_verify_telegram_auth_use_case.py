import pytest
from unittest.mock import Mock

from src.application.use_cases.auth.verify_telegram_auth import VerifyTelegramAuthUseCase


class TestVerifyTelegramAuthUseCase:
    """Тесты для use-case верификации Telegram auth."""

    @pytest.mark.asyncio
    async def test_verify_telegram_auth_success(self):
        """Тест успешной верификации initData."""
        # Arrange
        mock_auth_service = Mock()
        mock_auth_service.verify_init_data.return_value = True
        mock_auth_service.parse_init_data.return_value = {"id": 123, "first_name": "Test"}
        
        bot_token = "test_token"
        init_data = "test_init_data"
        
        use_case = VerifyTelegramAuthUseCase(mock_auth_service, bot_token)

        # Act
        result = await use_case.execute(init_data)

        # Assert
        assert result == {"id": 123, "first_name": "Test"}
        mock_auth_service.verify_init_data.assert_called_once_with(init_data, bot_token)
        mock_auth_service.parse_init_data.assert_called_once_with(init_data)

    @pytest.mark.asyncio
    async def test_verify_telegram_auth_invalid(self):
        """Тест невалидного initData."""
        # Arrange
        mock_auth_service = Mock()
        mock_auth_service.verify_init_data.return_value = False
        
        bot_token = "test_token"
        init_data = "invalid_init_data"
        
        use_case = VerifyTelegramAuthUseCase(mock_auth_service, bot_token)

        # Act & Assert
        with pytest.raises(ValueError, match="Invalid initData"):
            await use_case.execute(init_data)
        
        mock_auth_service.verify_init_data.assert_called_once_with(init_data, bot_token)
        mock_auth_service.parse_init_data.assert_not_called()

    @pytest.mark.asyncio
    async def test_verify_telegram_auth_empty_user_data(self):
        """Тест верификации с пустыми данными пользователя."""
        # Arrange
        mock_auth_service = Mock()
        mock_auth_service.verify_init_data.return_value = True
        mock_auth_service.parse_init_data.return_value = None
        
        bot_token = "test_token"
        init_data = "test_init_data"
        
        use_case = VerifyTelegramAuthUseCase(mock_auth_service, bot_token)

        # Act
        result = await use_case.execute(init_data)

        # Assert
        assert result == {}





