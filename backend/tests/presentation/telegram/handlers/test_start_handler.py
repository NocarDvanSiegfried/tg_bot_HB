import pytest
from unittest.mock import AsyncMock, MagicMock

from src.presentation.telegram.handlers.start_handler import cmd_start
from aiogram.types import Message, User, Chat


class TestStartHandler:
    """Тесты для обработчика команды /start."""

    @pytest.fixture
    def mock_message(self):
        """Мок сообщения."""
        message = MagicMock(spec=Message)
        message.from_user = MagicMock(spec=User)
        message.chat = MagicMock(spec=Chat)
        message.answer = AsyncMock()
        return message

    @pytest.mark.asyncio
    async def test_cmd_start(self, mock_message):
        """Тест команды /start."""
        # Act
        await cmd_start(mock_message)

        # Assert
        mock_message.answer.assert_called_once()
        call_args = mock_message.answer.call_args
        assert "Добро пожаловать" in call_args[0][0]
        assert call_args[1]["reply_markup"] is not None

