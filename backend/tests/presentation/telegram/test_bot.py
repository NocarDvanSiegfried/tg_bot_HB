import pytest
import os
from unittest.mock import AsyncMock, MagicMock, patch

from src.presentation.telegram.bot import main


class TestTelegramBot:
    """Тесты для Telegram бота."""

    @pytest.mark.asyncio
    async def test_main_with_valid_env(self):
        """Тест инициализации бота с валидными env переменными."""
        with patch.dict(os.environ, {
            "TELEGRAM_BOT_TOKEN": "test_token",
            "DATABASE_URL": "sqlite+aiosqlite:///:memory:"
        }):
            with patch("src.presentation.telegram.bot.Bot") as mock_bot_class, \
                 patch("src.presentation.telegram.bot.Dispatcher") as mock_dp_class, \
                 patch("src.presentation.telegram.bot.Database") as mock_db_class, \
                 patch("src.presentation.telegram.bot.start_handler") as mock_start, \
                 patch("src.presentation.telegram.bot.panel_handler") as mock_panel, \
                 patch("src.presentation.telegram.bot.calendar_handler") as mock_calendar, \
                 patch("src.presentation.telegram.bot.birthday_handlers") as mock_birthday, \
                 patch("src.presentation.telegram.bot.responsible_handlers") as mock_responsible, \
                 patch("src.presentation.telegram.bot.greeting_handlers") as mock_greeting:
                
                mock_bot = MagicMock()
                mock_bot_class.return_value = mock_bot
                
                mock_dp = AsyncMock()
                mock_dp.include_router = MagicMock()
                mock_dp.start_polling = AsyncMock()
                mock_dp_class.return_value = mock_dp
                
                mock_db = AsyncMock()
                mock_db.create_tables = AsyncMock()
                mock_db_class.return_value = mock_db
                
                # Act
                try:
                    await main()
                except Exception:
                    # start_polling может работать бесконечно, это нормально
                    pass
                
                # Assert
                mock_bot_class.assert_called_once_with(token="test_token")
                mock_db_class.assert_called_once_with("sqlite+aiosqlite:///:memory:")
                assert mock_dp.include_router.call_count == 6

    @pytest.mark.asyncio
    async def test_main_missing_bot_token(self):
        """Тест ошибки при отсутствии TELEGRAM_BOT_TOKEN."""
        with patch.dict(os.environ, {"DATABASE_URL": "sqlite+aiosqlite:///:memory:"}, clear=True):
            with pytest.raises(ValueError, match="TELEGRAM_BOT_TOKEN"):
                await main()

    @pytest.mark.asyncio
    async def test_main_missing_database_url(self):
        """Тест ошибки при отсутствии DATABASE_URL."""
        with patch.dict(os.environ, {"TELEGRAM_BOT_TOKEN": "test_token"}, clear=True):
            with pytest.raises(ValueError, match="DATABASE_URL"):
                await main()

    @pytest.mark.asyncio
    async def test_main_registers_all_routers(self):
        """Тест регистрации всех роутеров."""
        with patch.dict(os.environ, {
            "TELEGRAM_BOT_TOKEN": "test_token",
            "DATABASE_URL": "sqlite+aiosqlite:///:memory:"
        }):
            with patch("src.presentation.telegram.bot.Bot") as mock_bot_class, \
                 patch("src.presentation.telegram.bot.Dispatcher") as mock_dp_class, \
                 patch("src.presentation.telegram.bot.Database") as mock_db_class, \
                 patch("src.presentation.telegram.bot.start_handler") as mock_start, \
                 patch("src.presentation.telegram.bot.panel_handler") as mock_panel, \
                 patch("src.presentation.telegram.bot.calendar_handler") as mock_calendar, \
                 patch("src.presentation.telegram.bot.birthday_handlers") as mock_birthday, \
                 patch("src.presentation.telegram.bot.responsible_handlers") as mock_responsible, \
                 patch("src.presentation.telegram.bot.greeting_handlers") as mock_greeting:
                
                mock_bot = MagicMock()
                mock_bot_class.return_value = mock_bot
                
                mock_dp = AsyncMock()
                mock_dp.include_router = MagicMock()
                mock_dp.start_polling = AsyncMock()
                mock_dp_class.return_value = mock_dp
                
                mock_db = AsyncMock()
                mock_db.create_tables = AsyncMock()
                mock_db_class.return_value = mock_db
                
                mock_start.router = MagicMock()
                mock_panel.router = MagicMock()
                mock_calendar.router = MagicMock()
                mock_birthday.router = MagicMock()
                mock_responsible.router = MagicMock()
                mock_greeting.router = MagicMock()
                
                try:
                    await main()
                except Exception:
                    pass
                
                # Проверяем, что все роутеры зарегистрированы
                assert mock_dp.include_router.call_count == 6
                mock_dp.include_router.assert_any_call(mock_start.router)
                mock_dp.include_router.assert_any_call(mock_panel.router)
                mock_dp.include_router.assert_any_call(mock_calendar.router)
                mock_dp.include_router.assert_any_call(mock_birthday.router)
                mock_dp.include_router.assert_any_call(mock_responsible.router)
                mock_dp.include_router.assert_any_call(mock_greeting.router)

