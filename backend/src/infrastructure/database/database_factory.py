import os
from src.infrastructure.database.database import Database

# Singleton Database instance
_database: Database | None = None


def get_database() -> Database:
    """Получить singleton экземпляр Database."""
    global _database
    if _database is None:
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            raise ValueError("DATABASE_URL environment variable is required")
        _database = Database(database_url)
    return _database

