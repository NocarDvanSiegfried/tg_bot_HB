"""Валидация и санитизация входных данных для поиска."""

import re
from typing import Tuple


# Максимальная длина поискового запроса
MAX_SEARCH_QUERY_LENGTH = 200

# Минимальная длина поискового запроса
MIN_SEARCH_QUERY_LENGTH = 1

# Паттерн для удаления потенциально опасных символов
# Разрешаем буквы, цифры, пробелы, дефисы, апострофы, точки, запятые
SAFE_SEARCH_PATTERN = re.compile(r"[^a-zA-Zа-яА-ЯёЁ0-9\s\-'.,]", re.UNICODE)


def validate_and_sanitize_search_query(query: str) -> Tuple[str, bool]:
    """
    Валидирует и санитизирует поисковый запрос.
    
    Args:
        query: Исходный поисковый запрос
        
    Returns:
        Tuple[str, bool]: (санитизированный запрос, валидность)
        - Если запрос валиден, возвращается санитизированная версия
        - Если запрос невалиден, возвращается пустая строка и False
        
    Raises:
        ValueError: Если query не является строкой
    """
    if not isinstance(query, str):
        raise ValueError("Search query must be a string")
    
    # Удаляем лишние пробелы
    query = query.strip()
    
    # Проверяем длину
    if len(query) < MIN_SEARCH_QUERY_LENGTH:
        return "", False
    
    if len(query) > MAX_SEARCH_QUERY_LENGTH:
        # Обрезаем до максимальной длины
        query = query[:MAX_SEARCH_QUERY_LENGTH]
    
    # Удаляем потенциально опасные символы
    sanitized = SAFE_SEARCH_PATTERN.sub("", query)
    
    # Проверяем, что после санитизации остался хотя бы один символ
    if not sanitized.strip():
        return "", False
    
    return sanitized.strip(), True

