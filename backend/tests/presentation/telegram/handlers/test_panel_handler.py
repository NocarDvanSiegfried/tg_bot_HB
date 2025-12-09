import pytest
from unittest.mock import AsyncMock, MagicMock

from src.presentation.telegram.handlers.panel_handler import cmd_panel, panel_main_callback
from aiogram.types import Message, User, Chat, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession


class TestPanelHandler:
    """Тесты для обработчика панели управления."""

    @pytest.fixture
    def mock_message(self):
        """Мок сообщения."""
        message = MagicMock()
        message.from_user = MagicMock()
        message.from_user.id = 12345
        message.chat = MagicMock()
        message.answer = AsyncMock()
        return message

    @pytest.fixture
    def mock_session(self):
        """Мок сессии БД."""
        session = AsyncMock()
        session.add = MagicMock()
        session.flush = AsyncMock()  # Изменено: flush вместо commit
        return session

    @pytest.fixture
    def mock_callback(self):
        """Мок callback query."""
        callback = MagicMock()
        callback.data = "panel_main"
        callback.message = MagicMock()
        callback.message.edit_text = AsyncMock()
        callback.answer = AsyncMock()
        return callback

    @pytest.mark.asyncio
    async def test_cmd_panel(self, mock_message, mock_session):
        """Тест команды /panel."""
        # Arrange - настраиваем моки для use case factory
        from unittest.mock import patch
        from src.application.use_cases.panel.record_panel_access import RecordPanelAccessUseCase
        
        mock_record_use_case = AsyncMock(spec=RecordPanelAccessUseCase)
        mock_record_use_case.execute = AsyncMock()
        
        with patch('src.presentation.telegram.handlers.panel_handler.UseCaseFactory') as mock_factory:
            mock_factory_instance = mock_factory.return_value
            mock_factory_instance.create_record_panel_access_use_case.return_value = mock_record_use_case
            
            # Act
            await cmd_panel(mock_message, mock_session)

        # Assert
        mock_record_use_case.execute.assert_called_once_with(mock_message.from_user.id)
        mock_message.answer.assert_called_once()
        call_args = mock_message.answer.call_args
        assert "Панель управления" in call_args[0][0]
        assert call_args[1]["reply_markup"] is not None

    @pytest.mark.asyncio
    async def test_panel_main_callback(self, mock_callback):
        """Тест callback для возврата в главное меню панели."""
        # Act
        await panel_main_callback(mock_callback)

        # Assert
        mock_callback.message.edit_text.assert_called_once()
        call_args = mock_callback.message.edit_text.call_args
        assert "Панель управления" in call_args[0][0]
        assert call_args[1]["reply_markup"] is not None
        mock_callback.answer.assert_called_once()

