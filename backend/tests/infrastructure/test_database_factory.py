import pytest
import os
from unittest.mock import patch, MagicMock

from src.infrastructure.database import database_factory


class TestDatabaseFactory:
    """Тесты для фабрики Database."""

    def setup_method(self):
        """Очистить singleton перед каждым тестом."""
        database_factory._database = None

    def test_singleton_pattern(self):
        """Тест singleton паттерна."""
        with patch.dict(os.environ, {"DATABASE_URL": "sqlite+aiosqlite:///:memory:"}):
            db1 = database_factory.get_database()
            db2 = database_factory.get_database()
            
            # Должен возвращаться один и тот же экземпляр
            assert db1 is db2

    def test_create_database_with_env(self):
        """Тест создания Database с переменными окружения."""
        with patch.dict(os.environ, {"DATABASE_URL": "sqlite+aiosqlite:///:memory:"}):
            db = database_factory.get_database()
            assert db is not None
            assert db.engine is not None

    def test_missing_database_url(self):
        """Тест обработки отсутствующих переменных."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError, match="DATABASE_URL"):
                database_factory.get_database()

    def test_database_url_empty_string(self):
        """Тест обработки пустой строки DATABASE_URL."""
        with patch.dict(os.environ, {"DATABASE_URL": ""}):
            with pytest.raises(ValueError, match="DATABASE_URL"):
                database_factory.get_database()

