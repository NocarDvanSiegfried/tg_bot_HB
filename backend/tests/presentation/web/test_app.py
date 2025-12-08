import pytest
import os
from unittest.mock import patch
from fastapi.testclient import TestClient

from src.presentation.web.app import app


class TestWebApp:
    """Тесты для FastAPI приложения."""

    @pytest.fixture
    def client(self):
        """Тестовый клиент FastAPI."""
        return TestClient(app)

    def test_app_creation(self):
        """Тест создания FastAPI приложения."""
        assert app is not None
        assert app.title == "Telegram Birthday Calendar API"

    def test_root_endpoint(self, client):
        """Тест root endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Telegram Birthday Calendar API"}

    def test_cors_middleware_configured(self, client):
        """Тест, что CORS middleware настроен."""
        # Проверяем, что middleware добавлен
        assert len(app.user_middleware) > 0
        # Проверяем наличие CORS middleware через имя класса
        middleware_names = [str(middleware.cls) for middleware in app.user_middleware]
        assert any("CORS" in name for name in middleware_names)

    def test_router_included(self, client):
        """Тест, что API router включен в приложение."""
        # Проверяем, что router зарегистрирован
        assert len(app.routes) > 1  # Должен быть root endpoint и API routes

