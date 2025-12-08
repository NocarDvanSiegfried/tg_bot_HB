import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from datetime import date

from src.presentation.telegram.handlers.birthday_handlers import (
    panel_birthdays_callback,
    birthday_add_start,
    process_full_name,
    process_company,
    process_position,
    process_birth_date,
    process_comment,
)
from aiogram.types import CallbackQuery, Message, User, Chat
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession


class TestBirthdayHandlers:
    """Тесты для обработчиков дней рождения."""

    @pytest.fixture
    def mock_callback(self):
        """Мок callback query."""
        callback = MagicMock(spec=CallbackQuery)
        callback.data = "panel_birthdays"
        callback.message = MagicMock()
        callback.message.edit_text = AsyncMock()
        callback.message.answer = AsyncMock()
        callback.answer = AsyncMock()
        return callback

    @pytest.fixture
    def mock_message(self):
        """Мок сообщения."""
        message = MagicMock(spec=Message)
        message.from_user = MagicMock(spec=User)
        message.chat = MagicMock(spec=Chat)
        message.text = "Test Text"
        message.answer = AsyncMock()
        return message

    @pytest.fixture
    def mock_state(self):
        """Мок FSM context."""
        state = MagicMock(spec=FSMContext)
        state.set_state = AsyncMock()
        state.update_data = AsyncMock()
        state.get_data = AsyncMock(return_value={
            "full_name": "Test Name",
            "company": "Test Company",
            "position": "Test Position",
            "birth_date": date(1990, 5, 15)
        })
        state.get_state = AsyncMock(return_value="BirthdayForm:waiting_for_comment")
        state.clear = AsyncMock()
        return state

    @pytest.fixture
    def mock_session(self):
        """Мок сессии БД."""
        session = AsyncMock(spec=AsyncSession)
        session.commit = AsyncMock()
        session.rollback = AsyncMock()
        return session

    @pytest.mark.asyncio
    async def test_panel_birthdays_callback(self, mock_callback):
        """Тест callback для меню управления ДР."""
        # Act
        await panel_birthdays_callback(mock_callback)

        # Assert
        mock_callback.message.edit_text.assert_called_once()
        call_args = mock_callback.message.edit_text.call_args
        assert "Управление днями рождения" in call_args[0][0]
        assert call_args[1]["reply_markup"] is not None
        mock_callback.answer.assert_called_once()

    @pytest.mark.asyncio
    async def test_birthday_add_start(self, mock_callback, mock_state):
        """Тест начала добавления ДР."""
        # Act
        await birthday_add_start(mock_callback, mock_state)

        # Assert
        mock_state.set_state.assert_called_once()
        mock_callback.message.answer.assert_called_once_with("Введите ФИО:")
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
    async def test_process_position(self, mock_message, mock_state):
        """Тест обработки должности."""
        # Act
        await process_position(mock_message, mock_state)

        # Assert
        mock_state.update_data.assert_called_once_with(position="Test Text")
        mock_state.set_state.assert_called_once()
        mock_message.answer.assert_called_once_with("Введите дату рождения (формат: ДД.ММ.ГГГГ):")

    @pytest.mark.asyncio
    async def test_process_birth_date_valid(self, mock_message, mock_state, mock_session):
        """Тест обработки валидной даты рождения."""
        mock_message.text = "15.05.1990"
        
        # Act
        await process_birth_date(mock_message, mock_state, mock_session)

        # Assert
        mock_state.update_data.assert_called_once()
        mock_state.set_state.assert_called_once()
        mock_message.answer.assert_called_once_with("Введите комментарий (или отправьте '-' для пропуска):")

    @pytest.mark.asyncio
    async def test_process_birth_date_invalid(self, mock_message, mock_state, mock_session):
        """Тест обработки невалидной даты рождения."""
        mock_message.text = "invalid date"
        
        # Act
        await process_birth_date(mock_message, mock_state, mock_session)

        # Assert
        mock_state.update_data.assert_not_called()
        mock_message.answer.assert_called_once_with("Неверный формат даты. Используйте ДД.ММ.ГГГГ")

    @pytest.mark.asyncio
    async def test_process_comment_success(self, mock_message, mock_state, mock_session):
        """Тест успешной обработки комментария и создания ДР."""
        from src.domain.entities.birthday import Birthday
        
        mock_message.text = "Test comment"
        mock_birthday = Birthday(
            id=1,
            full_name="Test Name",
            company="Test Company",
            position="Test Position",
            birth_date=date(1990, 5, 15),
            comment="Test comment"
        )
        
        with patch("src.presentation.telegram.handlers.birthday_handlers.UseCaseFactory") as mock_factory:
            mock_use_cases = {
                "create": AsyncMock(return_value=mock_birthday)
            }
            mock_factory_instance = MagicMock()
            mock_factory_instance.create_birthday_use_cases.return_value = mock_use_cases
            mock_factory.return_value = mock_factory_instance
            
            # Act
            await process_comment(mock_message, mock_state, mock_session)

            # Assert
            mock_state.get_data.assert_called_once()
            mock_use_cases["create"].execute.assert_called_once()
            mock_session.commit.assert_called_once()
            mock_message.answer.assert_called()
            mock_state.clear.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_comment_with_dash(self, mock_message, mock_state, mock_session):
        """Тест обработки комментария с пропуском (отправка '-')."""
        from src.domain.entities.birthday import Birthday
        
        mock_message.text = "-"
        mock_birthday = Birthday(
            id=1,
            full_name="Test Name",
            company="Test Company",
            position="Test Position",
            birth_date=date(1990, 5, 15),
            comment=None
        )
        
        with patch("src.presentation.telegram.handlers.birthday_handlers.UseCaseFactory") as mock_factory:
            mock_use_cases = {
                "create": AsyncMock(return_value=mock_birthday)
            }
            mock_factory_instance = MagicMock()
            mock_factory_instance.create_birthday_use_cases.return_value = mock_use_cases
            mock_factory.return_value = mock_factory_instance
            
            # Act
            await process_comment(mock_message, mock_state, mock_session)

            # Assert
            mock_use_cases["create"].execute.assert_called_once()
            call_args = mock_use_cases["create"].execute.call_args
            assert call_args[1]["comment"] is None
            mock_session.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_comment_error(self, mock_message, mock_state, mock_session):
        """Тест обработки ошибки при создании ДР."""
        mock_message.text = "Test comment"
        
        with patch("src.presentation.telegram.handlers.birthday_handlers.UseCaseFactory") as mock_factory:
            mock_create_use_case = AsyncMock()
            mock_create_use_case.execute = AsyncMock(side_effect=ValueError("Test error"))
            mock_use_cases = {
                "create": mock_create_use_case
            }
            mock_factory_instance = MagicMock()
            mock_factory_instance.create_birthday_use_cases.return_value = mock_use_cases
            mock_factory.return_value = mock_factory_instance
            
            # Act
            await process_comment(mock_message, mock_state, mock_session)

            # Assert
            # rollback вызывается в except блоке
            mock_session.rollback.assert_called_once()
            mock_message.answer.assert_called()
            # Проверяем, что сообщение об ошибке отправлено
            answer_text = mock_message.answer.call_args[0][0]
            assert "Ошибка" in answer_text
            mock_state.clear.assert_called_once()

