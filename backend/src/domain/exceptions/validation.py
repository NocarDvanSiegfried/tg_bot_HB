"""Исключения для ошибок валидации."""

from src.domain.exceptions.base import DomainException


class ValidationError(DomainException):
    """Ошибка валидации данных."""

    pass


class InvalidDateError(ValidationError):
    """Ошибка невалидной даты."""

    pass


class InvalidGreetingTextError(ValidationError):
    """Ошибка невалидного текста поздравления."""

    pass


class TextTooLongError(ValidationError):
    """Текст поздравления слишком длинный для генерации открытки."""

    pass


class EmptyGreetingTextError(ValidationError):
    """Текст поздравления пустой."""

    pass











