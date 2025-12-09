"""Доменные исключения для API ошибок."""


class OpenRouterAPIError(Exception):
    """Базовое исключение для ошибок OpenRouter API."""

    pass


class OpenRouterHTTPError(OpenRouterAPIError):
    """Ошибка HTTP запроса к OpenRouter API."""

    def __init__(self, status_code: int, message: str = ""):
        self.status_code = status_code
        super().__init__(f"OpenRouter API HTTP error: {status_code}. {message}")


class OpenRouterTimeoutError(OpenRouterAPIError):
    """Таймаут запроса к OpenRouter API."""

    def __init__(self, message: str = "Request timeout"):
        super().__init__(f"OpenRouter API timeout: {message}")


class OpenRouterRateLimitError(OpenRouterAPIError):
    """Превышен лимит запросов к OpenRouter API."""

    def __init__(self, message: str = "Rate limit exceeded"):
        super().__init__(f"OpenRouter API rate limit: {message}")


class OpenRouterInvalidResponseError(OpenRouterAPIError):
    """Невалидный ответ от OpenRouter API."""

    def __init__(self, message: str = "Invalid response structure"):
        super().__init__(f"OpenRouter API invalid response: {message}")
