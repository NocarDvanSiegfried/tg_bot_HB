"""Исключения для бизнес-правил."""

from src.domain.exceptions.base import DomainException


class BusinessRuleError(DomainException):
    """Ошибка нарушения бизнес-правила."""
    pass

