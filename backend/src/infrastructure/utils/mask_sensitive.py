"""
Mask Sensitive Data - утилиты для маскировки чувствительных данных в логах

Предотвращает утечку чувствительных данных (токены, пароли, API ключи)
в логи приложения.
"""

from typing import Dict, Any, Union

# Список полей, которые содержат чувствительные данные
SENSITIVE_FIELDS = [
    'X-Init-Data',
    'Authorization',
    'X-Api-Key',
    'X-Auth-Token',
    'password',
    'token',
    'secret',
    'api_key',
    'apiKey',
]


def mask_value(value: str, visible_chars: int = 20) -> str:
    """
    Маскировать значение чувствительного поля
    
    Args:
        value: исходное значение
        visible_chars: количество видимых символов в начале (по умолчанию 20)
    
    Returns:
        замаскированное значение (первые N символов + "...")
    """
    if not value or len(value) <= visible_chars:
        return '***'
    return f"{value[:visible_chars]}..."


def is_sensitive_field(field_name: str) -> bool:
    """
    Проверить, является ли поле чувствительным
    
    Args:
        field_name: имя поля
    
    Returns:
        True, если поле содержит чувствительные данные
    """
    lower_field_name = field_name.lower()
    return any(field.lower() in lower_field_name for field in SENSITIVE_FIELDS)


def mask_sensitive_headers(headers: Dict[str, str]) -> Dict[str, str]:
    """
    Маскировать чувствительные данные в headers
    
    Args:
        headers: словарь с headers
    
    Returns:
        новый словарь с замаскированными чувствительными полями
    """
    masked: Dict[str, str] = {}
    
    for key, value in headers.items():
        if is_sensitive_field(key):
            masked[key] = mask_value(value)
        else:
            masked[key] = value
    
    return masked


def mask_sensitive_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Маскировать чувствительные данные в объекте
    
    Args:
        data: словарь с данными
    
    Returns:
        новый словарь с замаскированными чувствительными полями
    """
    masked: Dict[str, Any] = {}
    
    for key, value in data.items():
        if is_sensitive_field(key):
            if isinstance(value, str):
                masked[key] = mask_value(value)
            else:
                masked[key] = '***'
        elif isinstance(value, dict):
            # Рекурсивно маскируем вложенные словари
            masked[key] = mask_sensitive_data(value)
        else:
            masked[key] = value
    
    return masked

