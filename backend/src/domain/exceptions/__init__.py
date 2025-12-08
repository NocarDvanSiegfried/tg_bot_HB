"""Доменные исключения."""

from src.domain.exceptions.base import DomainException
from src.domain.exceptions.business import BusinessRuleError
from src.domain.exceptions.not_found import (
    BirthdayNotFoundError,
    NotFoundError,
    ResponsibleNotFoundError,
)
from src.domain.exceptions.validation import InvalidDateError, ValidationError

__all__ = [
    "DomainException",
    "ValidationError",
    "InvalidDateError",
    "NotFoundError",
    "BirthdayNotFoundError",
    "ResponsibleNotFoundError",
    "BusinessRuleError",
]
