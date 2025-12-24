"""Доменные исключения."""

from src.domain.exceptions.base import DomainException
from src.domain.exceptions.business import BusinessRuleError
from src.domain.exceptions.not_found import (
    BirthdayNotFoundError,
    NotFoundError,
    ResponsibleNotFoundError,
)
from src.domain.exceptions.validation import (
    EmptyGreetingTextError,
    InvalidDateError,
    InvalidGreetingTextError,
    TextTooLongError,
    ValidationError,
)

__all__ = [
    "DomainException",
    "ValidationError",
    "InvalidGreetingTextError",
    "TextTooLongError",
    "EmptyGreetingTextError",
    "InvalidDateError",
    "NotFoundError",
    "BirthdayNotFoundError",
    "ResponsibleNotFoundError",
    "BusinessRuleError",
]
