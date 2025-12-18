"""Исключения для ошибок валидации."""

from src.domain.exceptions.base import DomainException


class ValidationError(DomainException):
    """Ошибка валидации данных."""

    pass


class InvalidDateError(ValidationError):
    """Ошибка невалидной даты."""

    pass









