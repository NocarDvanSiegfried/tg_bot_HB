import pytest
from datetime import date
from unittest.mock import AsyncMock, Mock, patch

from src.infrastructure.services.notification_service_impl import NotificationServiceImpl
from src.domain.entities.birthday import Birthday


class TestNotificationServiceImpl:
    """Тесты для NotificationServiceImpl."""

    @pytest.mark.asyncio
    async def test_send_today_notifications_logs_error_on_failure(self):
        """Тест логирования ошибки при отправке уведомления сегодня."""
        # Arrange
        mock_bot = AsyncMock()
        mock_session = AsyncMock()
        mock_birthday_repo = AsyncMock()
        
        birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )
        mock_birthday_repo.get_by_date.return_value = [birthday]
        
        # Мокируем get_active_users
        mock_result = AsyncMock()
        mock_scalars = Mock()
        mock_scalars.return_value.all.return_value = [
            Mock(user_id=123)
        ]
        mock_result.scalars = mock_scalars
        mock_session.execute = AsyncMock(return_value=mock_result)
        
        # Мокируем ошибку отправки
        mock_bot.send_message.side_effect = Exception("Network error")
        
        service = NotificationServiceImpl(
            bot=mock_bot,
            birthday_repository=mock_birthday_repo,
            session=mock_session
        )
        
        # Act
        with patch('src.infrastructure.services.notification_service_impl.logger') as mock_logger:
            await service.send_today_notifications()
            
            # Assert
            mock_logger.error.assert_called_once()
            call_args = mock_logger.error.call_args
            assert "Failed to send notification" in call_args[0][0]
            assert call_args[1]['extra']['user_id'] == 123
            assert 'error_type' in call_args[1]['extra']
            assert 'error_message' in call_args[1]['extra']

    @pytest.mark.asyncio
    async def test_send_week_notifications_logs_error_on_failure(self):
        """Тест логирования ошибки при отправке уведомления на неделе."""
        # Arrange
        mock_bot = AsyncMock()
        mock_session = AsyncMock()
        mock_birthday_repo = AsyncMock()
        
        birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )
        mock_birthday_repo.get_by_date_range.return_value = [birthday]
        
        # Мокируем get_active_users
        mock_result = AsyncMock()
        mock_scalars = Mock()
        mock_scalars.return_value.all.return_value = [
            Mock(user_id=456)
        ]
        mock_result.scalars = mock_scalars
        mock_session.execute = AsyncMock(return_value=mock_result)
        
        mock_bot.send_message.side_effect = Exception("Telegram API error")
        
        service = NotificationServiceImpl(
            bot=mock_bot,
            birthday_repository=mock_birthday_repo,
            session=mock_session
        )
        
        # Act
        with patch('src.infrastructure.services.notification_service_impl.logger') as mock_logger:
            await service.send_week_notifications()
            
            # Assert
            mock_logger.error.assert_called_once()
            call_args = mock_logger.error.call_args
            assert "Failed to send notification" in call_args[0][0]
            assert call_args[1]['extra']['user_id'] == 456

    @pytest.mark.asyncio
    async def test_send_month_notifications_logs_error_on_failure(self):
        """Тест логирования ошибки при отправке уведомления в месяце."""
        # Arrange
        mock_bot = AsyncMock()
        mock_session = AsyncMock()
        mock_birthday_repo = AsyncMock()
        
        birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )
        mock_birthday_repo.get_by_date_range.return_value = [birthday]
        
        # Мокируем get_active_users
        mock_result = AsyncMock()
        mock_scalars = Mock()
        mock_scalars.return_value.all.return_value = [
            Mock(user_id=789)
        ]
        mock_result.scalars = mock_scalars
        mock_session.execute = AsyncMock(return_value=mock_result)
        
        mock_bot.send_message.side_effect = Exception("Timeout error")
        
        service = NotificationServiceImpl(
            bot=mock_bot,
            birthday_repository=mock_birthday_repo,
            session=mock_session
        )
        
        # Act
        with patch('src.infrastructure.services.notification_service_impl.logger') as mock_logger:
            await service.send_month_notifications()
            
            # Assert
            mock_logger.error.assert_called_once()
            call_args = mock_logger.error.call_args
            assert "Failed to send notification" in call_args[0][0]
            assert call_args[1]['extra']['user_id'] == 789

