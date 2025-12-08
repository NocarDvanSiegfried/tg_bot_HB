import pytest
import httpx
from unittest.mock import AsyncMock, patch, MagicMock

from src.infrastructure.external.openrouter_client_impl import OpenRouterClientImpl
from src.infrastructure.config.openrouter_config import OpenRouterConfig
from src.domain.exceptions.api_exceptions import (
    OpenRouterAPIError,
    OpenRouterHTTPError,
    OpenRouterTimeoutError,
    OpenRouterInvalidResponseError,
)


class TestOpenRouterClientImpl:
    """Тесты для OpenRouterClientImpl."""

    @pytest.fixture
    def config(self):
        """Фикстура для конфигурации OpenRouter."""
        return OpenRouterConfig(
            api_key="test_api_key",
            base_url="https://openrouter.ai/api/v1",
            timeout=30.0,
            max_retries=3,
            temperature=0.7,
            max_tokens=500,
            model="test-model",
        )

    @pytest.fixture
    def client(self, config):
        """Фикстура для OpenRouterClientImpl."""
        return OpenRouterClientImpl(config)

    @pytest.mark.asyncio
    async def test_generate_greeting_success(self, client):
        """Тест успешной генерации поздравления."""
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "choices": [
                {
                    "message": {
                        "content": "Поздравляем с днем рождения!"
                    }
                }
            ]
        }
        mock_response.raise_for_status = MagicMock()
        
        # Act
        with patch('httpx.AsyncClient') as mock_client_class:
            mock_client = AsyncMock()
            mock_client.__aenter__.return_value = mock_client
            mock_client.__aexit__.return_value = None
            mock_client.post = AsyncMock(return_value=mock_response)
            mock_client_class.return_value = mock_client
            
            result = await client.generate_greeting(
                person_name="Иван Иванов",
                person_company="ООО Тест",
                person_position="Разработчик",
                style="friendly",
                length="medium",
            )
        
        # Assert
        assert result == "Поздравляем с днем рождения!"
        mock_client.post.assert_called_once()
        call_args = mock_client.post.call_args
        assert call_args[0][0] == "https://openrouter.ai/api/v1/chat/completions"
        assert "model" in call_args[1]["json"]
        assert call_args[1]["json"]["model"] == "test-model"

    @pytest.mark.asyncio
    async def test_generate_greeting_with_theme(self, client):
        """Тест генерации поздравления с темой."""
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "choices": [
                {
                    "message": {
                        "content": "Поздравление с темой"
                    }
                }
            ]
        }
        mock_response.raise_for_status = MagicMock()
        
        # Act
        with patch('httpx.AsyncClient') as mock_client_class:
            mock_client = AsyncMock()
            mock_client.__aenter__.return_value = mock_client
            mock_client.__aexit__.return_value = None
            mock_client.post = AsyncMock(return_value=mock_response)
            mock_client_class.return_value = mock_client
            
            result = await client.generate_greeting(
                person_name="Иван Иванов",
                person_company="ООО Тест",
                person_position="Разработчик",
                style="friendly",
                length="medium",
                theme="technology",
            )
        
        # Assert
        assert result == "Поздравление с темой"

    @pytest.mark.asyncio
    async def test_generate_greeting_http_error(self, client):
        """Тест обработки HTTP ошибки."""
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 500
        http_error = httpx.HTTPStatusError("Server Error", request=MagicMock(), response=mock_response)
        
        # Act & Assert
        with patch('httpx.AsyncClient') as mock_client_class:
            mock_client = AsyncMock()
            mock_client.__aenter__.return_value = mock_client
            mock_client.__aexit__.return_value = None
            mock_client.post = AsyncMock(side_effect=http_error)
            mock_client_class.return_value = mock_client
            
            with pytest.raises(OpenRouterHTTPError) as exc_info:
                await client.generate_greeting(
                    person_name="Иван Иванов",
                    person_company="ООО Тест",
                    person_position="Разработчик",
                    style="friendly",
                    length="medium",
                )
            
            assert exc_info.value.status_code == 500

    @pytest.mark.asyncio
    async def test_generate_greeting_timeout_error(self, client):
        """Тест обработки timeout ошибки."""
        # Act & Assert
        with patch('httpx.AsyncClient') as mock_client_class:
            mock_client = AsyncMock()
            mock_client.__aenter__.return_value = mock_client
            mock_client.__aexit__.return_value = None
            mock_client.post = AsyncMock(side_effect=httpx.TimeoutException("Timeout"))
            mock_client_class.return_value = mock_client
            
            with pytest.raises(OpenRouterTimeoutError):
                await client.generate_greeting(
                    person_name="Иван Иванов",
                    person_company="ООО Тест",
                    person_position="Разработчик",
                    style="friendly",
                    length="medium",
                )

    @pytest.mark.asyncio
    async def test_generate_greeting_invalid_response_not_dict(self, client):
        """Тест обработки невалидного ответа (не словарь)."""
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = "not a dict"
        mock_response.raise_for_status = MagicMock()
        
        # Act & Assert
        with patch('httpx.AsyncClient') as mock_client_class:
            mock_client = AsyncMock()
            mock_client.__aenter__.return_value = mock_client
            mock_client.__aexit__.return_value = None
            mock_client.post = AsyncMock(return_value=mock_response)
            mock_client_class.return_value = mock_client
            
            with pytest.raises(OpenRouterInvalidResponseError, match="Response is not a dictionary"):
                await client.generate_greeting(
                    person_name="Иван Иванов",
                    person_company="ООО Тест",
                    person_position="Разработчик",
                    style="friendly",
                    length="medium",
                )

    @pytest.mark.asyncio
    async def test_generate_greeting_invalid_response_missing_choices(self, client):
        """Тест обработки невалидного ответа (нет choices)."""
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_response.raise_for_status = MagicMock()
        
        # Act & Assert
        with patch('httpx.AsyncClient') as mock_client_class:
            mock_client = AsyncMock()
            mock_client.__aenter__.return_value = mock_client
            mock_client.__aexit__.return_value = None
            mock_client.post = AsyncMock(return_value=mock_response)
            mock_client_class.return_value = mock_client
            
            with pytest.raises(OpenRouterInvalidResponseError, match="Missing 'choices' field"):
                await client.generate_greeting(
                    person_name="Иван Иванов",
                    person_company="ООО Тест",
                    person_position="Разработчик",
                    style="friendly",
                    length="medium",
                )

    @pytest.mark.asyncio
    async def test_generate_greeting_invalid_response_empty_choices(self, client):
        """Тест обработки невалидного ответа (пустой choices)."""
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {"choices": []}
        mock_response.raise_for_status = MagicMock()
        
        # Act & Assert
        with patch('httpx.AsyncClient') as mock_client_class:
            mock_client = AsyncMock()
            mock_client.__aenter__.return_value = mock_client
            mock_client.__aexit__.return_value = None
            mock_client.post = AsyncMock(return_value=mock_response)
            mock_client_class.return_value = mock_client
            
            with pytest.raises(OpenRouterInvalidResponseError, match="Invalid or empty 'choices' array"):
                await client.generate_greeting(
                    person_name="Иван Иванов",
                    person_company="ООО Тест",
                    person_position="Разработчик",
                    style="friendly",
                    length="medium",
                )

    @pytest.mark.asyncio
    async def test_generate_greeting_invalid_response_missing_message(self, client):
        """Тест обработки невалидного ответа (нет message)."""
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {"choices": [{}]}
        mock_response.raise_for_status = MagicMock()
        
        # Act & Assert
        with patch('httpx.AsyncClient') as mock_client_class:
            mock_client = AsyncMock()
            mock_client.__aenter__.return_value = mock_client
            mock_client.__aexit__.return_value = None
            mock_client.post = AsyncMock(return_value=mock_response)
            mock_client_class.return_value = mock_client
            
            with pytest.raises(OpenRouterInvalidResponseError, match="Missing 'message' field"):
                await client.generate_greeting(
                    person_name="Иван Иванов",
                    person_company="ООО Тест",
                    person_position="Разработчик",
                    style="friendly",
                    length="medium",
                )

    @pytest.mark.asyncio
    async def test_generate_greeting_invalid_response_missing_content(self, client):
        """Тест обработки невалидного ответа (нет content)."""
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {"choices": [{"message": {}}]}
        mock_response.raise_for_status = MagicMock()
        
        # Act & Assert
        with patch('httpx.AsyncClient') as mock_client_class:
            mock_client = AsyncMock()
            mock_client.__aenter__.return_value = mock_client
            mock_client.__aexit__.return_value = None
            mock_client.post = AsyncMock(return_value=mock_response)
            mock_client_class.return_value = mock_client
            
            with pytest.raises(OpenRouterInvalidResponseError, match="Missing 'content' field"):
                await client.generate_greeting(
                    person_name="Иван Иванов",
                    person_company="ООО Тест",
                    person_position="Разработчик",
                    style="friendly",
                    length="medium",
                )

    @pytest.mark.asyncio
    async def test_generate_greeting_invalid_response_content_not_string(self, client):
        """Тест обработки невалидного ответа (content не строка)."""
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "choices": [
                {
                    "message": {
                        "content": 123
                    }
                }
            ]
        }
        mock_response.raise_for_status = MagicMock()
        
        # Act & Assert
        with patch('httpx.AsyncClient') as mock_client_class:
            mock_client = AsyncMock()
            mock_client.__aenter__.return_value = mock_client
            mock_client.__aexit__.return_value = None
            mock_client.post = AsyncMock(return_value=mock_response)
            mock_client_class.return_value = mock_client
            
            with pytest.raises(OpenRouterInvalidResponseError, match="Content is not a string"):
                await client.generate_greeting(
                    person_name="Иван Иванов",
                    person_company="ООО Тест",
                    person_position="Разработчик",
                    style="friendly",
                    length="medium",
                )

    @pytest.mark.asyncio
    async def test_generate_greeting_retry_on_http_error(self, client):
        """Тест повторной попытки при HTTP ошибке."""
        # Arrange
        mock_response_success = MagicMock()
        mock_response_success.json.return_value = {
            "choices": [
                {
                    "message": {
                        "content": "Успешный ответ после retry"
                    }
                }
            ]
        }
        mock_response_success.raise_for_status = MagicMock()
        
        mock_response_error = MagicMock()
        mock_response_error.status_code = 500
        http_error = httpx.HTTPStatusError("Server Error", request=MagicMock(), response=mock_response_error)
        
        # Act
        with patch('httpx.AsyncClient') as mock_client_class, \
             patch('asyncio.sleep', new_callable=AsyncMock) as mock_sleep:
            mock_client = AsyncMock()
            mock_client.__aenter__.return_value = mock_client
            mock_client.__aexit__.return_value = None
            mock_client.post = AsyncMock(side_effect=[http_error, mock_response_success])
            mock_client_class.return_value = mock_client
            
            result = await client.generate_greeting(
                person_name="Иван Иванов",
                person_company="ООО Тест",
                person_position="Разработчик",
                style="friendly",
                length="medium",
            )
        
        # Assert
        assert result == "Успешный ответ после retry"
        assert mock_client.post.call_count == 2
        mock_sleep.assert_called_once()

    def test_build_prompt_without_theme(self, client):
        """Тест построения промпта без темы."""
        # Act
        prompt = client._build_prompt(
            person_name="Иван Иванов",
            person_company="ООО Тест",
            person_position="Разработчик",
            style="friendly",
            length="medium",
        )
        
        # Assert
        assert "Иван Иванов" in prompt
        assert "ООО Тест" in prompt
        assert "Разработчик" in prompt
        assert "дружелюбный" in prompt
        assert "среднее" in prompt
        assert "Тема:" not in prompt

    def test_build_prompt_with_theme(self, client):
        """Тест построения промпта с темой."""
        # Act
        prompt = client._build_prompt(
            person_name="Иван Иванов",
            person_company="ООО Тест",
            person_position="Разработчик",
            style="formal",
            length="long",
            theme="technology",
        )
        
        # Assert
        assert "Иван Иванов" in prompt
        assert "ООО Тест" in prompt
        assert "Разработчик" in prompt
        assert "официальный" in prompt
        assert "длинное" in prompt
        assert "Тема: technology" in prompt

    def test_build_prompt_unknown_style_and_length(self, client):
        """Тест построения промпта с неизвестным стилем и длиной."""
        # Act
        prompt = client._build_prompt(
            person_name="Иван Иванов",
            person_company="ООО Тест",
            person_position="Разработчик",
            style="unknown_style",
            length="unknown_length",
        )
        
        # Assert
        assert "Иван Иванов" in prompt
        assert "дружелюбный" in prompt  # Дефолтный стиль
        assert "среднее" in prompt  # Дефолтная длина

