import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from datetime import date, datetime

from src.presentation.telegram.handlers.calendar_handler import (
    show_calendar,
    calendar_callback,
    date_selected_callback,
)
from aiogram.types import Message, User, Chat, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession


class TestCalendarHandler:
    """Тесты для обработчика календаря."""

    @pytest.fixture
    def mock_message(self):
        """Мок сообщения."""
        message = MagicMock()
        message.from_user = MagicMock()
        message.chat = MagicMock()
        message.text = "📅 Календарь"
        message.answer = AsyncMock()
        return message

    @pytest.fixture
    def mock_callback(self):
        """Мок callback query."""
        callback = MagicMock()
        callback.data = "cal_prev_2024_5"
        callback.message = MagicMock()
        callback.message.edit_text = AsyncMock()
        callback.message.answer = AsyncMock()
        callback.answer = AsyncMock()
        return callback

    @pytest.fixture
    def mock_session(self):
        """Мок сессии БД."""
        session = AsyncMock()
        return session

    @pytest.mark.asyncio
    async def test_show_calendar(self, mock_message):
        """Тест показа календаря."""
        # Act
        await show_calendar(mock_message)

        # Assert
        mock_message.answer.assert_called_once()
        call_args = mock_message.answer.call_args
        assert "Календарь" in call_args[0][0]
        assert call_args[1]["reply_markup"] is not None

    @pytest.mark.asyncio
    async def test_calendar_callback_info(self, mock_callback, mock_session):
        """Тест callback для информации о календаре."""
        mock_callback.data = "cal_info"
        
        # Act
        await calendar_callback(mock_callback, mock_session)

        # Assert
        mock_callback.answer.assert_called_once_with("Информация о календаре")
        mock_callback.message.edit_text.assert_not_called()

    @pytest.mark.asyncio
    async def test_calendar_callback_prev(self, mock_callback, mock_session):
        """Тест callback для предыдущего месяца."""
        mock_callback.data = "cal_prev_2024_1"
        
        # Act
        await calendar_callback(mock_callback, mock_session)

        # Assert
        mock_callback.message.edit_text.assert_called_once()
        call_args = mock_callback.message.edit_text.call_args
        assert "2023-12" in call_args[0][0] or "Календарь" in call_args[0][0]
        mock_callback.answer.assert_called_once()

    @pytest.mark.asyncio
    async def test_calendar_callback_next(self, mock_callback, mock_session):
        """Тест callback для следующего месяца."""
        mock_callback.data = "cal_next_2024_12"
        
        # Act
        await calendar_callback(mock_callback, mock_session)

        # Assert
        mock_callback.message.edit_text.assert_called_once()
        call_args = mock_callback.message.edit_text.call_args
        assert "2025-01" in call_args[0][0] or "Календарь" in call_args[0][0]
        mock_callback.answer.assert_called_once()

    @pytest.mark.asyncio
    async def test_date_selected_callback_with_data(self, mock_callback, mock_session):
        """Тест callback для выбранной даты с данными."""
        mock_callback.data = "date_2024-05-15"
        
        mock_calendar_data = {
            "birthdays": [{
                "full_name": "Test Person",
                "company": "Test Company",
                "position": "Test Position",
                "age": 34,
                "comment": "Test comment"
            }],
            "holidays": [{
                "name": "Test Holiday",
                "description": "Test Description"
            }],
            "responsible": {
                "full_name": "Test Responsible",
                "company": "Test Company",
                "position": "Test Position"
            }
        }
        
        with patch("src.presentation.telegram.handlers.calendar_handler.UseCaseFactory") as mock_factory:
            mock_use_case = AsyncMock()
            mock_use_case.execute = AsyncMock(return_value=mock_calendar_data)
            mock_factory_instance = MagicMock()
            mock_factory_instance.create_calendar_use_case.return_value = mock_use_case
            mock_factory.return_value = mock_factory_instance
            
            # Act
            await date_selected_callback(mock_callback, mock_session)

            # Assert
            mock_callback.message.answer.assert_called_once()
            call_args = mock_callback.message.answer.call_args
            text = call_args[0][0]
            assert "15.05.2024" in text
            assert "Test Person" in text
            assert "Test Holiday" in text
            assert "Test Responsible" in text
            mock_callback.answer.assert_called_once()

    @pytest.mark.asyncio
    async def test_date_selected_callback_empty(self, mock_callback, mock_session):
        """Тест callback для выбранной даты без данных."""
        mock_callback.data = "date_2024-05-15"
        
        mock_calendar_data = {
            "birthdays": [],
            "holidays": [],
            "responsible": None
        }
        
        with patch("src.presentation.telegram.handlers.calendar_handler.UseCaseFactory") as mock_factory:
            mock_use_case = AsyncMock()
            mock_use_case.execute = AsyncMock(return_value=mock_calendar_data)
            mock_factory_instance = MagicMock()
            mock_factory_instance.create_calendar_use_case.return_value = mock_use_case
            mock_factory.return_value = mock_factory_instance
            
            # Act
            await date_selected_callback(mock_callback, mock_session)

            # Assert
            mock_callback.message.answer.assert_called_once()
            call_args = mock_callback.message.answer.call_args
            text = call_args[0][0]
            assert "15.05.2024" in text
            # Проверяем наличие текста о пустых данных
            assert "Дни рождения: нет" in text or "нет" in text
            assert "не назначено" in text
            mock_callback.answer.assert_called_once()

