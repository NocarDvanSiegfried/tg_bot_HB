#!/usr/bin/env python3
"""
Диагностический скрипт для проверки подключения к PostgreSQL.

Проверяет:
- Доступность PostgreSQL
- Корректность credentials
- Существование базы данных
- Сетевую связность между контейнерами

Использование:
    python scripts/check_database_connection.py
    или
    python -m scripts.check_database_connection
"""

import asyncio
import os
import sys
from pathlib import Path

# Добавляем корневую директорию backend в путь
backend_root = Path(__file__).parent.parent
sys.path.insert(0, str(backend_root))

# Загружаем переменные окружения из .env файла
from dotenv import load_dotenv

# Загружаем .env из корня проекта (на уровень выше backend)
project_root = backend_root.parent
env_path = project_root / ".env"
if env_path.exists():
    load_dotenv(env_path)
    print(f"✅ Загружен .env файл: {env_path}")
else:
    print(f"⚠️  .env файл не найден: {env_path}")
    print("   Переменные окружения будут загружены из системных переменных")

from src.infrastructure.config.env_validator import (
    get_database_name_from_url,
    mask_database_url,
    validate_database_env_sync,
    validate_database_url,
)


async def check_database_connection():
    """Проверка подключения к базе данных."""
    print("=" * 70)
    print("Проверка подключения к PostgreSQL")
    print("=" * 70)
    print()

    # Шаг 1: Проверка переменных окружения
    print("Шаг 1: Проверка переменных окружения...")
    is_sync, messages = validate_database_env_sync()
    if not is_sync:
        print("❌ ОШИБКИ:")
        for msg in messages:
            if "не установлен" in msg.lower() or "несовпадение" in msg.lower():
                print(f"   - {msg}")
        if any("предупреждение" not in msg.lower() for msg in messages if "warning" not in msg.lower()):
            print()
            print("⚠️  ПРЕДУПРЕЖДЕНИЯ:")
            for msg in messages:
                if "warning" in msg.lower() or "предупреждение" in msg.lower():
                    print(f"   - {msg}")
        print()
        print("Исправьте ошибки перед продолжением.")
        return False
    else:
        print("✅ Все переменные окружения установлены и синхронизированы")
        if messages:
            print("⚠️  Предупреждения:")
            for msg in messages:
                print(f"   - {msg}")
    print()

    # Шаг 2: Валидация формата DATABASE_URL
    print("Шаг 2: Валидация формата DATABASE_URL...")
    database_url = os.getenv("DATABASE_URL")
    is_valid, db_name, error_msg = validate_database_url(database_url)
    if not is_valid:
        print(f"❌ Ошибка валидации: {error_msg}")
        print(f"   DATABASE_URL (замаскирован): {mask_database_url(database_url)}")
        return False
    else:
        print(f"✅ Формат DATABASE_URL корректен")
        print(f"   Имя базы данных: {db_name}")
        print(f"   DATABASE_URL (замаскирован): {mask_database_url(database_url)}")
    print()

    # Шаг 3: Попытка подключения
    print("Шаг 3: Попытка подключения к PostgreSQL...")
    try:
        from sqlalchemy import text
        from sqlalchemy.ext.asyncio import create_async_engine

        engine = create_async_engine(database_url, echo=False)
        async with engine.begin() as conn:
            # Простой запрос для проверки подключения
            result = await conn.execute(text("SELECT version();"))
            version = result.scalar()
            print(f"✅ Подключение успешно!")
            print(f"   Версия PostgreSQL: {version.split(',')[0]}")
    except Exception as e:
        error_msg = str(e).lower()
        print(f"❌ Ошибка подключения: {type(e).__name__}: {e}")
        print()

        # Детальная диагностика
        if "password authentication failed" in error_msg:
            print("   Проблема: Неверное имя пользователя или пароль")
            print("   Решение:")
            print("     1. Проверьте POSTGRES_USER и POSTGRES_PASSWORD в .env")
            print("     2. Убедитесь, что они совпадают с значениями в DATABASE_URL")
            print("     3. Проверьте, что пользователь существует в PostgreSQL")
        elif "could not translate host name" in error_msg or "could not resolve" in error_msg:
            print("   Проблема: Неверный hostname")
            print("   Решение:")
            print("     1. Для Docker Compose используйте 'postgres' как hostname")
            print("     2. Для локального запуска используйте 'localhost'")
            print("     3. Проверьте, что контейнер postgres запущен (docker compose ps)")
        elif "connection refused" in error_msg or "connection timed out" in error_msg:
            print("   Проблема: PostgreSQL недоступен")
            print("   Решение:")
            print("     1. Убедитесь, что PostgreSQL запущен")
            print("     2. Для Docker Compose: docker compose up postgres")
            print("     3. Проверьте порт (обычно 5432)")
            print("     4. Проверьте сетевые настройки контейнеров")
        elif "database" in error_msg and "does not exist" in error_msg:
            print("   Проблема: База данных не существует")
            print("   Решение:")
            print("     1. Проверьте POSTGRES_DB в .env")
            print("     2. Убедитесь, что POSTGRES_DB совпадает с именем БД в DATABASE_URL")
            print("     3. PostgreSQL создаст БД автоматически при первом запуске")
        else:
            print("   Проблема: Неизвестная ошибка подключения")
            print("   Решение:")
            print("     1. Проверьте все настройки в .env")
            print("     2. Убедитесь, что PostgreSQL запущен и доступен")
            print("     3. Проверьте логи PostgreSQL для деталей")

        return False
    finally:
        await engine.dispose()
    print()

    # Шаг 4: Проверка существования базы данных
    print("Шаг 4: Проверка существования базы данных...")
    try:
        from sqlalchemy import text
        from sqlalchemy.ext.asyncio import create_async_engine

        engine = create_async_engine(database_url, echo=False)
        async with engine.begin() as conn:
            result = await conn.execute(text("SELECT current_database();"))
            current_db = result.scalar()
            if current_db == db_name:
                print(f"✅ База данных '{db_name}' существует и доступна")
            else:
                print(f"⚠️  Текущая база данных: '{current_db}', ожидалась: '{db_name}'")
    except Exception as e:
        print(f"❌ Ошибка при проверке базы данных: {e}")
        return False
    finally:
        await engine.dispose()
    print()

    print("=" * 70)
    print("✅ Все проверки пройдены успешно!")
    print("=" * 70)
    return True


if __name__ == "__main__":
    try:
        result = asyncio.run(check_database_connection())
        sys.exit(0 if result else 1)
    except KeyboardInterrupt:
        print("\n\nПрервано пользователем")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Критическая ошибка: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)

