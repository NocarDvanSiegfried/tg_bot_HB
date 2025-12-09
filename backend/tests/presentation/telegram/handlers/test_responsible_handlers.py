import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from src.presentation.telegram.handlers.responsible_handlers import (
    panel_responsible_callback,
    responsible_add_start,
    process_full_name,
    process_company,
    process_position,
)
from aiogram.types import CallbackQuery, Message, User, Chat
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession


class TestResponsibleHandlers:
    """Тесты для обработчиков ответственных лиц."""

    @pytest.fixture
    def mock_callback(self):
        """Мок callback query."""
        callback = MagicMock()
        callback.data = "panel_responsible"
        callback.message = MagicMock()
        callback.message.edit_text = AsyncMock()
        callback.message.answer = AsyncMock()
        callback.answer = AsyncMock()
        return callback

    @pytest.fixture
    def mock_message(self):
        """Мок сообщения."""
        message = MagicMock()
        message.from_user = MagicMock()
        message.chat = MagicMock()
        message.text = "Test Text"
        message.answer = AsyncMock()
        return message

    @pytest.fixture
    def mock_state(self):
        """Мок FSM context."""
        state = MagicMock()
        state.set_state = AsyncMock()
        state.update_data = AsyncMock()
        state.get_data = AsyncMock(return_value={"full_name": "Test Name", "company": "Test Company"})
        state.get_state = AsyncMock(return_value="ResponsibleForm:waiting_for_position")
        state.clear = AsyncMock()
        return state

    @pytest.fixture
    def mock_session(self):
        """Мок сессии БД."""
        session = AsyncMock()
        session.commit = AsyncMock()
        session.rollback = AsyncMock()
        return session

    @pytest.mark.asyncio
    async def test_panel_responsible_callback(self, mock_callback):
        """Тест callback для меню управления ответственными."""
        # Act
        await panel_responsible_callback(mock_callback)

        # Assert
        mock_callback.message.edit_text.assert_called_once()
        call_args = mock_callback.message.edit_text.call_args
        assert "Управление ответственными" in call_args[0][0]
        assert call_args[1]["reply_markup"] is not None
        mock_callback.answer.assert_called_once()

    @pytest.mark.asyncio
    async def test_responsible_add_start(self, mock_callback, mock_state):
        """Тест начала добавления ответственного."""
        # Act
        await responsible_add_start(mock_callback, mock_state)

        # Assert
        mock_state.set_state.assert_called_once()
        mock_callback.message.answer.assert_called_once()
        assert "ФИО" in mock_callback.message.answer.call_args[0][0]
        mock_callback.answer.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_full_name(self, mock_message, mock_state):
        """Тест обработки ФИО."""
        # Act
        await process_full_name(mock_message, mock_state)

        # Assert
        mock_state.update_data.assert_called_once_with(full_name="Test Text")
        mock_state.set_state.assert_called_once()
        mock_message.answer.assert_called_once_with("Введите компанию:")

    @pytest.mark.asyncio
    async def test_process_company(self, mock_message, mock_state):
        """Тест обработки компании."""
        # Act
        await process_company(mock_message, mock_state)

        # Assert
        mock_state.update_data.assert_called_once_with(company="Test Text")
        mock_state.set_state.assert_called_once()
        mock_message.answer.assert_called_once_with("Введите должность:")

    @pytest.mark.asyncio
    async def test_process_position_success(self, mock_message, mock_state, mock_session):
        """Тест успешной обработки должности и создания ответственного."""
        from src.domain.entities.responsible_person import ResponsiblePerson
        
        mock_responsible = ResponsiblePerson(
            id=1,
            full_name="Test Name",
            company="Test Company",
            position="Test Position"
        )
        
        with patch("src.presentation.telegram.handlers.responsible_handlers.UseCaseFactory") as mock_factory:
            mock_use_cases = {
                "create": AsyncMock(return_value=mock_responsible)
            }
            mock_factory_instance = MagicMock()
            mock_factory_instance.create_responsible_use_cases.return_value = mock_use_cases
            mock_factory.return_value = mock_factory_instance
            
            # Act
            await process_position(mock_message, mock_state, mock_session)

            # Assert
            mock_state.get_data.assert_called_once()
            mock_use_cases["create"].execute.assert_called_once()
            # Управление транзакциями теперь в middleware, не проверяем commit/rollback
            mock_message.answer.assert_called()
            mock_state.clear.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_position_error(self, mock_message, mock_state, mock_session):
        """Тест обработки ошибки при создании ответственного."""
        mock_message.text = "Test Position"
        with patch("src.presentation.telegram.handlers.responsible_handlers.UseCaseFactory") as mock_factory:
            mock_create_use_case = AsyncMock()
            mock_create_use_case.execute = AsyncMock(side_effect=ValueError("Test error"))
            mock_use_cases = {
                "create": mock_create_use_case
            }
            mock_factory_instance = MagicMock()
            mock_factory_instance.create_responsible_use_cases.return_value = mock_use_cases
            mock_factory.return_value = mock_factory_instance
            
            # Act
            await process_position(mock_message, mock_state, mock_session)

            # Assert
            # Управление транзакциями теперь в middleware, не проверяем rollback
            mock_message.answer.assert_called()
            assert "Ошибка" in mock_message.answer.call_args[0][0]
            mock_state.clear.assert_called_once()

