import asyncio
from typing import Optional

import httpx

from src.application.ports.openrouter_client import OpenRouterClient
from src.domain.exceptions.api_exceptions import (
    OpenRouterAPIError,
    OpenRouterHTTPError,
    OpenRouterInvalidResponseError,
    OpenRouterTimeoutError,
)
from src.infrastructure.config.openrouter_config import OpenRouterConfig


class OpenRouterClientImpl(OpenRouterClient):
    def __init__(self, config: OpenRouterConfig):
        self.config = config
        self.api_key = config.api_key
        self.base_url = config.base_url
        self.timeout = config.timeout
        self.max_retries = config.max_retries

    async def generate_greeting(
        self,
        person_name: str,
        person_company: str,
        person_position: str,
        style: str,
        length: str,
        theme: Optional[str] = None,
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

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            for attempt in range(self.max_retries):
                try:
                    response = await client.post(
                        f"{self.base_url}/chat/completions",
                        json=payload,
                        headers=headers,
                    )
                    response.raise_for_status()
                    data = response.json()
                    
                    # Валидация структуры ответа
                    if not isinstance(data, dict):
                        raise OpenRouterInvalidResponseError("Response is not a dictionary")
                    
                    if "choices" not in data:
                        raise OpenRouterInvalidResponseError("Missing 'choices' field in response")
                    
                    if not isinstance(data["choices"], list) or len(data["choices"]) == 0:
                        raise OpenRouterInvalidResponseError("Invalid or empty 'choices' array")
                    
                    if "message" not in data["choices"][0]:
                        raise OpenRouterInvalidResponseError("Missing 'message' field in choice")
                    
                    if "content" not in data["choices"][0]["message"]:
                        raise OpenRouterInvalidResponseError("Missing 'content' field in message")
                    
                    content = data["choices"][0]["message"]["content"]
                    if not isinstance(content, str):
                        raise OpenRouterInvalidResponseError("Content is not a string")
                    
                    return content.strip()
                except httpx.HTTPStatusError as e:
                    if attempt == self.max_retries - 1:
                        raise OpenRouterHTTPError(e.response.status_code)
                    await asyncio.sleep(2 ** attempt)
                except httpx.TimeoutException:
                    if attempt == self.max_retries - 1:
                        raise OpenRouterTimeoutError()
                    await asyncio.sleep(2 ** attempt)
                except OpenRouterAPIError:
                    # Если это уже наше доменное исключение, пробрасываем дальше
                    raise
                except Exception as e:
                    # Иначе оборачиваем в базовое исключение
                    raise OpenRouterAPIError(f"OpenRouter API error: {str(e)}")

    def _build_prompt(
        self,
        person_name: str,
        person_company: str,
        person_position: str,
        style: str,
        length: str,
        theme: Optional[str] = None,
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

