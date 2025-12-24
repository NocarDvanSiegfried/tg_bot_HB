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
                    # Очищаем сгенерированный текст от рассуждений и служебных фраз
                    cleaned_content = self._clean_generated_text(content)
                    return cleaned_content
                    
                except httpx.HTTPStatusError as e:
                    # Логируем полную информацию об ошибке
                    response_text = ""
                    try:
                        response_text = e.response.text[:500]  # Первые 500 символов для диагностики
                    except Exception:
                        response_text = "Unable to read response text"
                    
                    error_message = f"HTTP {e.response.status_code}"
                    if response_text:
                        error_message += f": {response_text}"
                    
                    logger.warning(
                        f"[OpenRouterClientImpl] HTTP error {e.response.status_code}: {response_text}",
                        extra={
                            "status_code": e.response.status_code,
                            "response_preview": response_text,
                            "attempt": attempt + 1,
                            "max_retries": self.max_retries,
                        }
                    )
                    
                    if attempt == self.max_retries - 1:
                        logger.error(
                            f"[OpenRouterClientImpl] All retry attempts exhausted, "
                            f"HTTP status: {e.response.status_code}, response: {response_text[:200]}"
                        )
                        # Передаем сообщение об ошибке в исключение
                        raise OpenRouterHTTPError(e.response.status_code, error_message) from e
                    await asyncio.sleep(2**attempt)
                except httpx.TimeoutException as e:
                    timeout_message = f"Request timeout after {self.timeout}s (attempt {attempt + 1}/{self.max_retries})"
                    logger.warning(
                        f"[OpenRouterClientImpl] {timeout_message}",
                        extra={
                            "timeout": self.timeout,
                            "attempt": attempt + 1,
                            "max_retries": self.max_retries,
                        }
                    )
                    if attempt == self.max_retries - 1:
                        logger.error(f"[OpenRouterClientImpl] All retry attempts exhausted, timeout: {self.timeout}s")
                        raise OpenRouterTimeoutError(timeout_message) from e
                    await asyncio.sleep(2**attempt)
                except OpenRouterAPIError:
                    # Если это уже наше доменное исключение, пробрасываем дальше
                    raise
                except httpx.RequestError as e:
                    # Ошибки сети (не HTTP статус, а проблемы с подключением)
                    error_message = f"Network error: {str(e)}"
                    logger.error(
                        f"[OpenRouterClientImpl] Network error (attempt {attempt + 1}/{self.max_retries}): {error_message}",
                        exc_info=True,
                        extra={
                            "error_type": type(e).__name__,
                            "attempt": attempt + 1,
                            "max_retries": self.max_retries,
                        }
                    )
                    if attempt == self.max_retries - 1:
                        raise OpenRouterAPIError(error_message) from e
                    await asyncio.sleep(2**attempt)
                except Exception as e:
                    error_message = f"Unexpected error: {type(e).__name__}: {str(e)}"
                    logger.error(
                        f"[OpenRouterClientImpl] {error_message}",
                        exc_info=True,
                        extra={
                            "error_type": type(e).__name__,
                            "attempt": attempt + 1,
                            "max_retries": self.max_retries,
                        }
                    )
                    # Иначе оборачиваем в базовое исключение
                    raise OpenRouterAPIError(error_message) from e

    def _clean_generated_text(self, text: str) -> str:
        """Очистить сгенерированный текст от рассуждений, вопросов и служебных фраз."""
        import re
        
        # Удаляем markdown-разметку
        text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # **bold**
        text = re.sub(r'\*([^*]+)\*', r'\1', text)  # *italic*
        text = re.sub(r'#+\s*', '', text)  # заголовки
        text = re.sub(r'`([^`]+)`', r'\1', text)  # inline code
        text = re.sub(r'```[\s\S]*?```', '', text)  # code blocks
        
        # Удаляем служебные фразы в начале текста
        service_phrases = [
            r'^[^\w]*давайте\s+разберёмся[^\w]*',
            r'^[^\w]*мне\s+нужно[^\w]*',
            r'^[^\w]*я\s+хочу[^\w]*',
            r'^[^\w]*позвольте\s+мне[^\w]*',
            r'^[^\w]*позволь\s+мне[^\w]*',
            r'^[^\w]*хочу\s+поздравить[^\w]*',
            r'^[^\w]*с\s+удовольствием[^\w]*',
            r'^[^\w]*хотел\s+бы[^\w]*',
            r'^[^\w]*хотела\s+бы[^\w]*',
        ]
        
        for phrase in service_phrases:
            text = re.sub(phrase, '', text, flags=re.IGNORECASE)
        
        # Удаляем вопросы в начале текста
        text = re.sub(r'^[^\w]*как\s+лучше[^\w]*\?[^\w]*', '', text, flags=re.IGNORECASE)
        text = re.sub(r'^[^\w]*что\s+пожелать[^\w]*\?[^\w]*', '', text, flags=re.IGNORECASE)
        text = re.sub(r'^[^\w]*как\s+поздравить[^\w]*\?[^\w]*', '', text, flags=re.IGNORECASE)
        
        # Удаляем объяснения в скобках в начале текста
        text = re.sub(r'^[^\w]*\([^)]*объяснени[^)]*\)[^\w]*', '', text, flags=re.IGNORECASE)
        
        # Нормализуем пробелы и переносы строк
        text = re.sub(r'\s+', ' ', text)  # множественные пробелы -> один
        text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)  # множественные переносы -> два
        text = text.strip()
        
        # Удаляем пустые строки в начале
        text = re.sub(r'^\s*\n+', '', text)
        
        # Если текст начинается с маленькой буквы после очистки, делаем первую букву заглавной
        if text and text[0].islower():
            text = text[0].upper() + text[1:]
        
        return text

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
        # Жёсткие требования к длине
        length_requirements = {
            "short": "РОВНО 2-3 предложения. Не больше, не меньше.",
            "medium": "РОВНО 4-6 предложений. Не больше, не меньше.",
            "long": "РОВНО 8-10 предложений. Не больше, не меньше.",
        }
        length_requirement = length_requirements.get(length, "РОВНО 4-6 предложений. Не больше, не меньше.")

        # Детальное описание стилей
        style_descriptions = {
            "formal": """ОФИЦИАЛЬНЫЙ стиль:
- Сдержанный, корпоративный тон
- БЕЗ эмодзи
- Деловая лексика
- Уважительное обращение
- Пример начала: "Уважаемый/ая {person_name}!" или "Дорогой/ая {person_name}!" """,
            "friendly": """ДРУЖЕЛЮБНЫЙ стиль:
- Тёплый, живой тон
- Допустимы 1-2 эмодзи (не больше)
- Неформальное, но уважительное обращение
- Пример начала: "Дорогой/ая {person_name}! 🎉" или "{person_name}, с днём рождения!" """,
            "humorous": """ЮМОРИСТИЧЕСКИЙ стиль:
- Лёгкий, позитивный юмор
- БЕЗ сарказма и иронии
- Дружелюбный тон с шутками
- Пример начала: "{person_name}, поздравляю! 🎂" или "Дорогой/ая {person_name}, с праздником!" """,
            "warm": """ТЁПЛЫЙ стиль:
- Душевный, личный, эмоциональный тон
- Мягкие, искренние слова
- Эмоциональная окраска
- Пример начала: "Дорогой/ая {person_name}!" или "Милый/ая {person_name}!" """,
        }
        style_desc = style_descriptions.get(style, style_descriptions["friendly"]).format(person_name=person_name)

        theme_part = f"\n- Тема поздравления: {theme}" if theme else ""

        prompt = f"""Ты пишешь поздравительный текст на день рождения. 

КРИТИЧЕСКИ ВАЖНО:
- НАЧИНАЙ СРАЗУ С ОБРАЩЕНИЯ. Никаких предисловий, рассуждений, вопросов.
- НЕ пиши: "давайте разберёмся", "мне нужно", "я хочу", "позвольте мне"
- НЕ задавай вопросы: "как лучше поздравить?", "что пожелать?"
- НЕ объясняй, что ты делаешь
- НЕ используй markdown-разметку
- Пиши ТОЛЬКО финальный текст поздравления, как будто он уже готов к использованию

Получатель:
- Имя: {person_name}
- Компания: {person_company}
- Должность: {person_position}

СТИЛЬ (соблюдай строго):
{style_desc}

ДЛИНА (соблюдай строго):
{length_requirement}

ТРЕБОВАНИЯ К ТЕКСТУ:
- Текст должен быть искренним и персонализированным
- Упоминай компанию "{person_company}" и должность "{person_position}" естественным образом
- Не используй шаблонные фразы
- Начинай сразу с обращения к {person_name}{theme_part}

ФОРМАТ ОТВЕТА:
Напиши ТОЛЬКО текст поздравления. Никаких комментариев, объяснений, предисловий. Начинай сразу с обращения."""

        return prompt
