import os

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
        self.api_key = api_key
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
