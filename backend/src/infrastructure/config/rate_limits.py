"""Константы для rate limiting."""

# Rate limits для различных типов endpoints
PUBLIC_ENDPOINT_LIMIT = "30/minute"  # Публичные endpoints (календарь)
READ_LIMIT = "60/minute"  # Чтение данных (списки, поиск)
WRITE_LIMIT = "20/minute"  # Создание, обновление, удаление
HEAVY_OPERATION_LIMIT = "10/minute"  # Тяжелые операции (генерация, создание карточек)
ACCESS_CHECK_LIMIT = "10/minute"  # Проверка доступа
