"""Исключения для ошибок "не найдено"."""

from src.domain.exceptions.base import DomainException


class NotFoundError(DomainException):
    """Базовое исключение для ошибок "не найдено"."""

    pass


class BirthdayNotFoundError(NotFoundError):
    """День рождения не найден."""

    pass


class ResponsibleNotFoundError(NotFoundError):
    """Ответственный не найден."""

    pass










