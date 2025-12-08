import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from src.presentation.telegram.handlers.greeting_handlers import (
    panel_greetings_callback,
    greeting_manual_start,
    greeting_generate_start,
    greeting_card_start,
    process_birthday_id,
    process_style,
    process_length,
    process_theme,
    process_text,
    process_qr_url,
)
from aiogram.types import CallbackQuery, Message, User, Chat
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession


class TestGreetingHandlers:
    """Тесты для обработчиков генерации поздравлений."""

    @pytest.fixture
    def mock_callback(self):
        """Мок callback query."""
        callback = MagicMock()
        callback.data = "panel_greetings"
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
        message.text = "123"
        message.answer = AsyncMock()
        message.answer_photo = AsyncMock()
        return message

    @pytest.fixture
    def mock_state(self):
        """Мок FSM context."""
        state = MagicMock()
        state.set_state = AsyncMock()
        state.update_data = AsyncMock()
        state.get_data = AsyncMock(return_value={
            "birthday_id": 1,
            "style": "formal",
            "length": "medium",
            "greeting_text": "Test greeting"
        })
        state.get_state = AsyncMock(return_value="GreetingForm:waiting_for_birthday_id")
        state.clear = AsyncMock()
        return state

    @pytest.fixture
    def mock_session(self):
        """Мок сессии БД."""
        session = AsyncMock()
        return session

    @pytest.mark.asyncio
    async def test_panel_greetings_callback(self, mock_callback):
        """Тест callback для меню генерации поздравлений."""
        # Act
        await panel_greetings_callback(mock_callback)

        # Assert
        mock_callback.message.edit_text.assert_called_once()
        call_args = mock_callback.message.edit_text.call_args
        assert "Генерация поздравлений" in call_args[0][0]
        assert call_args[1]["reply_markup"] is not None
        mock_callback.answer.assert_called_once()

    @pytest.mark.asyncio
    async def test_greeting_manual_start(self, mock_callback, mock_state):
        """Тест начала ручного ввода текста."""
        # Act
        await greeting_manual_start(mock_callback, mock_state)

        # Assert
        mock_state.set_state.assert_called_once()
        mock_callback.message.answer.assert_called_once()
        assert "ID сотрудника" in mock_callback.message.answer.call_args[0][0]
        mock_callback.answer.assert_called_once()

    @pytest.mark.asyncio
    async def test_greeting_generate_start(self, mock_callback, mock_state):
        """Тест начала генерации через DeepSeek."""
        # Act
        await greeting_generate_start(mock_callback, mock_state)

        # Assert
        mock_state.set_state.assert_called_once()
        mock_callback.message.answer.assert_called_once()
        assert "ID сотрудника" in mock_callback.message.answer.call_args[0][0]
        mock_callback.answer.assert_called_once()

    @pytest.mark.asyncio
    async def test_greeting_card_start(self, mock_callback, mock_state):
        """Тест начала создания открытки."""
        # Act
        await greeting_card_start(mock_callback, mock_state)

        # Assert
        mock_state.set_state.assert_called_once()
        mock_callback.message.answer.assert_called_once()
        assert "ID сотрудника" in mock_callback.message.answer.call_args[0][0]
        mock_callback.answer.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_birthday_id_valid(self, mock_message, mock_state):
        """Тест обработки валидного ID сотрудника."""
        mock_message.text = "123"
        
        # Act
        await process_birthday_id(mock_message, mock_state)

        # Assert
        mock_state.update_data.assert_called_once_with(birthday_id=123)
        mock_state.set_state.assert_called_once()
        mock_message.answer.assert_called_once()
        assert "стиль" in mock_message.answer.call_args[0][0].lower()

    @pytest.mark.asyncio
    async def test_process_birthday_id_invalid(self, mock_message, mock_state):
        """Тест обработки невалидного ID сотрудника."""
        mock_message.text = "invalid"
        
        # Act
        await process_birthday_id(mock_message, mock_state)

        # Assert
        mock_state.update_data.assert_not_called()
        mock_message.answer.assert_called_once()
        assert "Неверный формат" in mock_message.answer.call_args[0][0]

    @pytest.mark.asyncio
    async def test_process_style(self, mock_message, mock_state):
        """Тест обработки стиля."""
        mock_message.text = "formal"
        
        # Act
        await process_style(mock_message, mock_state)

        # Assert
        mock_state.update_data.assert_called_once_with(style="formal")
        mock_state.set_state.assert_called_once()
        mock_message.answer.assert_called_once()
        answer_text = mock_message.answer.call_args[0][0].lower()
        assert "длину" in answer_text or "длина" in answer_text or "length" in answer_text

    @pytest.mark.asyncio
    async def test_process_length(self, mock_message, mock_state):
        """Тест обработки длины."""
        mock_message.text = "medium"
        
        # Act
        await process_length(mock_message, mock_state)

        # Assert
        mock_state.update_data.assert_called_once_with(length="medium")
        mock_state.set_state.assert_called_once()
        mock_message.answer.assert_called_once()
        answer_text = mock_message.answer.call_args[0][0].lower()
        assert "тему" in answer_text or "тема" in answer_text or "theme" in answer_text

    @pytest.mark.asyncio
    async def test_process_theme_success(self, mock_message, mock_state, mock_session):
        """Тест успешной обработки темы и генерации поздравления."""
        mock_message.text = "birthday"
        
        with patch("src.presentation.telegram.handlers.greeting_handlers.UseCaseFactory") as mock_factory:
            mock_generate = AsyncMock()
            mock_generate.execute = AsyncMock(return_value="Test greeting text")
            mock_use_cases = {
                "generate": mock_generate
            }
            mock_factory_instance = MagicMock()
            mock_factory_instance.create_greeting_use_cases.return_value = mock_use_cases
            mock_factory.return_value = mock_factory_instance
            
            # Act
            await process_theme(mock_message, mock_state, mock_session)

            # Assert
            mock_generate.execute.assert_called_once()
            mock_message.answer.assert_called_once()
            assert "Сгенерированное поздравление" in mock_message.answer.call_args[0][0]
            mock_state.clear.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_theme_with_dash(self, mock_message, mock_state, mock_session):
        """Тест обработки темы с пропуском (отправка '-')."""
        mock_message.text = "-"
        
        with patch("src.presentation.telegram.handlers.greeting_handlers.UseCaseFactory") as mock_factory:
            mock_generate = AsyncMock()
            mock_generate.execute = AsyncMock(return_value="Test greeting text")
            mock_use_cases = {
                "generate": mock_generate
            }
            mock_factory_instance = MagicMock()
            mock_factory_instance.create_greeting_use_cases.return_value = mock_use_cases
            mock_factory.return_value = mock_factory_instance
            
            # Act
            await process_theme(mock_message, mock_state, mock_session)

            # Assert
            call_args = mock_generate.execute.call_args
            assert call_args[1]["theme"] is None

    @pytest.mark.asyncio
    async def test_process_theme_error(self, mock_message, mock_state, mock_session):
        """Тест обработки ошибки при генерации поздравления."""
        mock_message.text = "birthday"
        
        with patch("src.presentation.telegram.handlers.greeting_handlers.UseCaseFactory") as mock_factory:
            mock_generate = AsyncMock()
            mock_generate.execute = AsyncMock(side_effect=ValueError("Test error"))
            mock_use_cases = {
                "generate": mock_generate
            }
            mock_factory_instance = MagicMock()
            mock_factory_instance.create_greeting_use_cases.return_value = mock_use_cases
            mock_factory.return_value = mock_factory_instance
            
            # Act
            await process_theme(mock_message, mock_state, mock_session)

            # Assert
            mock_message.answer.assert_called_once()
            answer_text = mock_message.answer.call_args[0][0]
            # Проверяем, что сообщение об ошибке отправлено
            assert "Ошибка" in answer_text or "error" in answer_text.lower()
            mock_state.clear.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_text(self, mock_message, mock_state):
        """Тест обработки текста для открытки."""
        mock_message.text = "Test greeting text"
        
        # Act
        await process_text(mock_message, mock_state)

        # Assert
        mock_state.update_data.assert_called_once_with(greeting_text="Test greeting text")
        mock_state.set_state.assert_called_once()
        mock_message.answer.assert_called_once()
        assert "QR" in mock_message.answer.call_args[0][0] or "qr" in mock_message.answer.call_args[0][0].lower()

    @pytest.mark.asyncio
    async def test_process_qr_url_success(self, mock_message, mock_state, mock_session):
        """Тест успешной обработки QR URL и создания открытки."""
        mock_message.text = "https://example.com"
        
        with patch("src.presentation.telegram.handlers.greeting_handlers.UseCaseFactory") as mock_factory, \
             patch("aiogram.types.BufferedInputFile") as mock_buffered:
            mock_use_cases = {
                "create_card": AsyncMock(return_value=b"fake_image_bytes")
            }
            mock_factory_instance = MagicMock()
            mock_factory_instance.create_greeting_use_cases.return_value = mock_use_cases
            mock_factory.return_value = mock_factory_instance
            
            # Act
            await process_qr_url(mock_message, mock_state, mock_session)

            # Assert
            mock_use_cases["create_card"].execute.assert_called_once()
            mock_message.answer_photo.assert_called_once()
            mock_state.clear.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_qr_url_with_dash(self, mock_message, mock_state, mock_session):
        """Тест обработки QR URL с пропуском (отправка '-')."""
        mock_message.text = "-"
        
        with patch("src.presentation.telegram.handlers.greeting_handlers.UseCaseFactory") as mock_factory, \
             patch("aiogram.types.BufferedInputFile") as mock_buffered:
            mock_create_card = AsyncMock()
            mock_create_card.execute = AsyncMock(return_value=b"fake_image_bytes")
            mock_use_cases = {
                "create_card": mock_create_card
            }
            mock_factory_instance = MagicMock()
            mock_factory_instance.create_greeting_use_cases.return_value = mock_use_cases
            mock_factory.return_value = mock_factory_instance
            
            # Act
            await process_qr_url(mock_message, mock_state, mock_session)

            # Assert
            call_args = mock_create_card.execute.call_args
            assert call_args[1]["qr_url"] is None

    @pytest.mark.asyncio
    async def test_process_qr_url_error(self, mock_message, mock_state, mock_session):
        """Тест обработки ошибки при создании открытки."""
        mock_message.text = "https://example.com"
        
        with patch("src.presentation.telegram.handlers.greeting_handlers.UseCaseFactory") as mock_factory:
            mock_create_card = AsyncMock()
            mock_create_card.execute = AsyncMock(side_effect=ValueError("Test error"))
            mock_use_cases = {
                "create_card": mock_create_card
            }
            mock_factory_instance = MagicMock()
            mock_factory_instance.create_greeting_use_cases.return_value = mock_use_cases
            mock_factory.return_value = mock_factory_instance
            
            # Act
            await process_qr_url(mock_message, mock_state, mock_session)

            # Assert
            mock_message.answer.assert_called_once()
            assert "Ошибка" in mock_message.answer.call_args[0][0]
            mock_state.clear.assert_called_once()

