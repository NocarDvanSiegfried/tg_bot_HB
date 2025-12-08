import pytest
import hmac
import hashlib
import urllib.parse
import json
from unittest.mock import patch

from src.infrastructure.external.telegram_auth import (
    TelegramAuthServiceImpl,
    verify_telegram_init_data,
    parse_init_data,
    get_user_id_from_init_data,
)


class TestTelegramAuthServiceImpl:
    """Тесты для TelegramAuthServiceImpl."""

    def test_verify_init_data_success(self):
        """Тест успешной верификации initData."""
        # Arrange
        bot_token = "test_bot_token"
        service = TelegramAuthServiceImpl()
        
        # Создаем валидный initData
        user_data = {"id": 123, "first_name": "Test"}
        user_str = json.dumps(user_data)
        
        # Формируем data_check_string
        data_check_string = f"user={user_str}"
        
        # Вычисляем hash
        secret_key = hmac.new(
            "WebAppData".encode(),
            bot_token.encode(),
            hashlib.sha256
        ).digest()
        calculated_hash = hmac.new(
            secret_key,
            data_check_string.encode(),
            hashlib.sha256
        ).hexdigest()
        
        init_data = f"user={user_str}&hash={calculated_hash}"
        
        # Act
        result = service.verify_init_data(init_data, bot_token)
        
        # Assert
        assert result is True

    def test_verify_init_data_invalid_hash(self):
        """Тест верификации с неверным hash."""
        # Arrange
        bot_token = "test_bot_token"
        service = TelegramAuthServiceImpl()
        init_data = "user={\"id\":123}&hash=invalid_hash"
        
        # Act
        result = service.verify_init_data(init_data, bot_token)
        
        # Assert
        assert result is False

    def test_verify_init_data_missing_hash(self):
        """Тест верификации без hash."""
        # Arrange
        bot_token = "test_bot_token"
        service = TelegramAuthServiceImpl()
        init_data = "user={\"id\":123}"
        
        # Act
        result = service.verify_init_data(init_data, bot_token)
        
        # Assert
        assert result is False

    def test_verify_init_data_invalid_format(self):
        """Тест верификации с невалидным форматом."""
        # Arrange
        bot_token = "test_bot_token"
        service = TelegramAuthServiceImpl()
        init_data = "invalid_format"
        
        # Act
        result = service.verify_init_data(init_data, bot_token)
        
        # Assert
        assert result is False

    def test_parse_init_data_success(self):
        """Тест успешного парсинга initData."""
        # Arrange
        service = TelegramAuthServiceImpl()
        user_data = {"id": 123, "first_name": "Test", "last_name": "User"}
        user_str = json.dumps(user_data)
        init_data = f"user={user_str}"
        
        # Act
        result = service.parse_init_data(init_data)
        
        # Assert
        assert result == user_data

    def test_parse_init_data_without_user(self):
        """Тест парсинга initData без user."""
        # Arrange
        service = TelegramAuthServiceImpl()
        init_data = "auth_date=1234567890"
        
        # Act
        result = service.parse_init_data(init_data)
        
        # Assert
        assert result == {}

    def test_parse_init_data_invalid_json(self):
        """Тест парсинга initData с невалидным JSON."""
        # Arrange
        service = TelegramAuthServiceImpl()
        init_data = "user=invalid_json"
        
        # Act
        result = service.parse_init_data(init_data)
        
        # Assert
        assert result is None

    def test_parse_init_data_invalid_format(self):
        """Тест парсинга initData с невалидным форматом."""
        # Arrange
        service = TelegramAuthServiceImpl()
        init_data = "invalid_format"
        
        # Act
        result = service.parse_init_data(init_data)
        
        # Assert
        # parse_qs может вернуть пустой словарь для невалидного формата
        assert result == {} or result is None


class TestDeprecatedFunctions:
    """Тесты для deprecated функций обратной совместимости."""

    def test_verify_telegram_init_data_function(self):
        """Тест функции verify_telegram_init_data."""
        # Arrange
        bot_token = "test_bot_token"
        user_data = {"id": 123}
        user_str = json.dumps(user_data)
        data_check_string = f"user={user_str}"
        
        secret_key = hmac.new(
            "WebAppData".encode(),
            bot_token.encode(),
            hashlib.sha256
        ).digest()
        calculated_hash = hmac.new(
            secret_key,
            data_check_string.encode(),
            hashlib.sha256
        ).hexdigest()
        
        init_data = f"user={user_str}&hash={calculated_hash}"
        
        # Act
        result = verify_telegram_init_data(init_data, bot_token)
        
        # Assert
        assert result is True

    def test_parse_init_data_function(self):
        """Тест функции parse_init_data."""
        # Arrange
        user_data = {"id": 456, "first_name": "Test"}
        user_str = json.dumps(user_data)
        init_data = f"user={user_str}"
        
        # Act
        result = parse_init_data(init_data)
        
        # Assert
        assert result == user_data

    def test_get_user_id_from_init_data_success(self):
        """Тест функции get_user_id_from_init_data с успешным извлечением."""
        # Arrange
        user_data = {"id": 789, "first_name": "Test"}
        user_str = json.dumps(user_data)
        init_data = f"user={user_str}"
        
        # Act
        result = get_user_id_from_init_data(init_data)
        
        # Assert
        assert result == 789

    def test_get_user_id_from_init_data_no_user(self):
        """Тест функции get_user_id_from_init_data без user."""
        # Arrange
        init_data = "auth_date=1234567890"
        
        # Act
        result = get_user_id_from_init_data(init_data)
        
        # Assert
        assert result is None

    def test_get_user_id_from_init_data_no_id(self):
        """Тест функции get_user_id_from_init_data без id в user."""
        # Arrange
        user_data = {"first_name": "Test"}
        user_str = json.dumps(user_data)
        init_data = f"user={user_str}"
        
        # Act
        result = get_user_id_from_init_data(init_data)
        
        # Assert
        assert result is None

