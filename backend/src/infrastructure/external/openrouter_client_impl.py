import asyncio
import logging

import httpx

from src.application.ports.openrouter_client import OpenRouterClient
from src.domain.exceptions.api_exceptions import (
    OpenRouterAPIError,
    OpenRouterHTTPError,
    OpenRouterInvalidResponseError,
    OpenRouterTimeoutError,
)
from src.infrastructure.config.openrouter_config import OpenRouterConfig

logger = logging.getLogger(__name__)


class OpenRouterClientImpl(OpenRouterClient):
    def __init__(self, config: OpenRouterConfig):
        self.config = config
        self.api_key = config.api_key
        self.base_url = config.base_url
        self.timeout = config.timeout
        self.max_retries = config.max_retries
        
        # Логирование конфигурации (без sensitive данных)
        logger.info(
            f"[OpenRouterClientImpl] Initialized with config: "
            f"base_url={config.base_url}, model={config.model}, "
            f"timeout={config.timeout}s, max_retries={config.max_retries}, "
            f"api_key_present={'yes' if config.api_key else 'no'}"
        )

    async def generate_greeting(
        self,
        person_name: str,
        person_company: str,
        person_position: str,
        style: str,
        length: str,
        theme: str | None = None,
    ) -> str:
        """Сгенерировать поздравление через DeepSeek."""
        prompt = self._build_prompt(
            person_name, person_company, person_position, style, length, theme
        )

        payload = {
            "model": self.config.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens,
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": self.config.referer,
        }

        logger.info(
            f"[OpenRouterClientImpl] Starting request to OpenRouter API",
            extra={
                "url": f"{self.base_url}/chat/completions",
                "model": self.config.model,
                "person_name": person_name,
                "style": style,
                "length": length,
                "theme": theme,
            },
        )

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            for attempt in range(self.max_retries):
                try:
                    if attempt > 0:
                        logger.warning(
                            f"[OpenRouterClientImpl] Retry attempt {attempt + 1}/{self.max_retries}"
                        )
                    
                    logger.debug(
                        f"[OpenRouterClientImpl] Sending POST request to {self.base_url}/chat/completions"
                    )
                    response = await client.post(
                        f"{self.base_url}/chat/completions",
                        json=payload,
                        headers=headers,
                    )
                    
                    logger.debug(
                        f"[OpenRouterClientImpl] Received response: status={response.status_code}, "
                        f"headers={dict(response.headers)}"
                    )
                    
                    response.raise_for_status()
                    data = response.json()

                    # Валидация структуры ответа
                    if not isinstance(data, dict):
                        logger.error("[OpenRouterClientImpl] Response is not a dictionary")
                        raise OpenRouterInvalidResponseError("Response is not a dictionary")

                    if "choices" not in data:
                        logger.error("[OpenRouterClientImpl] Missing 'choices' field in response")
                        raise OpenRouterInvalidResponseError("Missing 'choices' field in response")

                    if not isinstance(data["choices"], list) or len(data["choices"]) == 0:
                        logger.error("[OpenRouterClientImpl] Invalid or empty 'choices' array")
                        raise OpenRouterInvalidResponseError("Invalid or empty 'choices' array")

                    if "message" not in data["choices"][0]:
                        logger.error("[OpenRouterClientImpl] Missing 'message' field in choice")
                        raise OpenRouterInvalidResponseError("Missing 'message' field in choice")

                    if "content" not in data["choices"][0]["message"]:
                        logger.error("[OpenRouterClientImpl] Missing 'content' field in message")
                        raise OpenRouterInvalidResponseError("Missing 'content' field in message")

                    content = data["choices"][0]["message"]["content"]
                    if not isinstance(content, str):
                        logger.error("[OpenRouterClientImpl] Content is not a string")
                        raise OpenRouterInvalidResponseError("Content is not a string")

                    logger.info(
                        f"[OpenRouterClientImpl] Greeting generated successfully, "
                        f"length={len(content)} characters"
                    )
                    return content.strip()
                    
                except httpx.HTTPStatusError as e:
                    logger.warning(
                        f"[OpenRouterClientImpl] HTTP error {e.response.status_code}: {e.response.text[:200]}"
                    )
                    if attempt == self.max_retries - 1:
                        logger.error(
                            f"[OpenRouterClientImpl] All retry attempts exhausted, "
                            f"HTTP status: {e.response.status_code}"
                        )
                        raise OpenRouterHTTPError(e.response.status_code) from e
                    await asyncio.sleep(2**attempt)
                except httpx.TimeoutException as e:
                    logger.warning(
                        f"[OpenRouterClientImpl] Request timeout (attempt {attempt + 1}/{self.max_retries})"
                    )
                    if attempt == self.max_retries - 1:
                        logger.error("[OpenRouterClientImpl] All retry attempts exhausted, timeout")
                        raise OpenRouterTimeoutError() from e
                    await asyncio.sleep(2**attempt)
                except OpenRouterAPIError:
                    # Если это уже наше доменное исключение, пробрасываем дальше
                    raise
                except Exception as e:
                    logger.error(
                        f"[OpenRouterClientImpl] Unexpected error: {type(e).__name__}: {e}",
                        exc_info=True,
                    )
                    # Иначе оборачиваем в базовое исключение
                    raise OpenRouterAPIError(f"OpenRouter API error: {str(e)}") from e

    def _build_prompt(
        self,
        person_name: str,
        person_company: str,
        person_position: str,
        style: str,
        length: str,
        theme: str | None = None,
    ) -> str:
        """Построить промпт для генерации поздравления."""
        length_map = {
            "short": "короткое (2-3 предложения)",
            "medium": "среднее (4-6 предложений)",
            "long": "длинное (7-10 предложений)",
        }
        length_desc = length_map.get(length, "среднее")

        style_map = {
            "formal": "официальный",
            "friendly": "дружелюбный",
            "humorous": "юмористический",
            "warm": "теплый",
        }
        style_desc = style_map.get(style, "дружелюбный")

        theme_part = f"Тема: {theme}. " if theme else ""

        prompt = f"""Напиши поздравительный текст на день рождения.

Получатель:
- Имя: {person_name}
- Компания: {person_company}
- Должность: {person_position}

Требования:
- Стиль: {style_desc}
- Длина: {length_desc}
{theme_part}
- Текст должен быть искренним и персонализированным
- Упоминай компанию и должность естественным образом
- Не используй шаблонные фразы

Напиши только текст поздравления, без дополнительных комментариев."""

        return prompt
