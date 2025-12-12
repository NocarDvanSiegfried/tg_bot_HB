import logging
import os

logger = logging.getLogger(__name__)

# Default values for OpenRouter API configuration (used as fallbacks)
DEFAULT_BASE_URL = "https://openrouter.ai/api/v1"
DEFAULT_TIMEOUT = 30.0
DEFAULT_MAX_RETRIES = 3
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 500
DEFAULT_MODEL = "tng/deepseek-r1t2-chimera"
DEFAULT_REFERER = ""


class OpenRouterConfig:
    """Конфигурация для OpenRouter API клиента."""

    def __init__(
        self,
        api_key: str,
        base_url: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        temperature: float | None = None,
        max_tokens: int | None = None,
        model: str | None = None,
        referer: str | None = None,
    ):
        # Валидация обязательных параметров
        if not api_key or not api_key.strip():
            raise ValueError("OPENROUTER_API_KEY is required and cannot be empty")
        
        if not api_key.startswith("sk-or-v1-") and not api_key.startswith("sk-"):
            logger.warning(
                f"[OpenRouterConfig] API key does not start with 'sk-or-v1-' or 'sk-'. "
                f"This may indicate an invalid API key format."
            )

        self.api_key = api_key.strip()
        self.base_url = base_url or os.getenv("OPENROUTER_BASE_URL", DEFAULT_BASE_URL)
        self.timeout = timeout or float(os.getenv("OPENROUTER_TIMEOUT", str(DEFAULT_TIMEOUT)))
        self.max_retries = max_retries or int(
            os.getenv("OPENROUTER_MAX_RETRIES", str(DEFAULT_MAX_RETRIES))
        )
        self.temperature = temperature or float(
            os.getenv("OPENROUTER_TEMPERATURE", str(DEFAULT_TEMPERATURE))
        )
        self.max_tokens = max_tokens or int(
            os.getenv("OPENROUTER_MAX_TOKENS", str(DEFAULT_MAX_TOKENS))
        )
        self.model = model or os.getenv("OPENROUTER_MODEL", DEFAULT_MODEL)
        self.referer = referer or os.getenv("OPENROUTER_REFERER", DEFAULT_REFERER)

        # Валидация значений
        if self.timeout <= 0:
            raise ValueError(f"OPENROUTER_TIMEOUT must be positive, got {self.timeout}")
        if self.max_retries < 0:
            raise ValueError(f"OPENROUTER_MAX_RETRIES must be non-negative, got {self.max_retries}")
        if not (0.0 <= self.temperature <= 2.0):
            raise ValueError(f"OPENROUTER_TEMPERATURE must be between 0.0 and 2.0, got {self.temperature}")
        if self.max_tokens <= 0:
            raise ValueError(f"OPENROUTER_MAX_TOKENS must be positive, got {self.max_tokens}")
        if not self.model or not self.model.strip():
            raise ValueError("OPENROUTER_MODEL is required and cannot be empty")
        if not self.base_url or not self.base_url.strip():
            raise ValueError("OPENROUTER_BASE_URL is required and cannot be empty")

        logger.info(
            f"[OpenRouterConfig] Configuration validated successfully: "
            f"base_url={self.base_url}, model={self.model}, "
            f"timeout={self.timeout}s, max_retries={self.max_retries}, "
            f"temperature={self.temperature}, max_tokens={self.max_tokens}"
        )
