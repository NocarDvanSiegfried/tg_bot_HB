import logging

from sqlalchemy.exc import (
    InterfaceError,
    OperationalError,
    ProgrammingError,
)
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.infrastructure.config.env_validator import mask_database_url
from src.infrastructure.database.models import Base

logger = logging.getLogger(__name__)


class Database:
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.engine = create_async_engine(
            database_url,
            echo=False,
            future=True,
        )
        self.async_session_maker = async_sessionmaker(
            self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    def _handle_connection_error(self, error: Exception, operation: str) -> Exception:
        """
        Обрабатывает ошибки подключения к базе данных и возвращает понятное сообщение.

        Args:
            error: Исключение, возникшее при подключении
            operation: Операция, во время которой произошла ошибка

        Returns:
            Exception: Исключение с понятным сообщением об ошибке
        """
        masked_url = mask_database_url(self.database_url)
        error_msg = str(error).lower()

        # OperationalError - проблемы с подключением, credentials, недоступный хост
        if isinstance(error, OperationalError):
            if "password authentication failed" in error_msg or "authentication failed" in error_msg:
                logger.error(
                    f"Ошибка аутентификации при {operation}. "
                    f"Проверьте POSTGRES_USER и POSTGRES_PASSWORD. "
                    f"DATABASE_URL (замаскирован): {masked_url}"
                )
                return ValueError(
                    "Ошибка аутентификации PostgreSQL: неверное имя пользователя или пароль. "
                    "Убедитесь, что POSTGRES_USER и POSTGRES_PASSWORD в .env совпадают с "
                    "значениями в DATABASE_URL."
                )
            elif "could not translate host name" in error_msg or "could not resolve" in error_msg:
                logger.error(
                    f"Ошибка разрешения hostname при {operation}. "
                    f"Проверьте hostname в DATABASE_URL. "
                    f"DATABASE_URL (замаскирован): {masked_url}"
                )
                return ValueError(
                    f"Не удалось подключиться к PostgreSQL: неверный hostname. "
                    f"Для Docker Compose используйте 'postgres' как hostname, "
                    f"для локального запуска - 'localhost'. "
                    f"DATABASE_URL (замаскирован): {masked_url}"
                )
            elif "connection refused" in error_msg or "connection timed out" in error_msg:
                logger.error(
                    f"Ошибка подключения при {operation}. "
                    f"PostgreSQL недоступен. Проверьте, что сервис запущен. "
                    f"DATABASE_URL (замаскирован): {masked_url}"
                )
                return ValueError(
                    "PostgreSQL недоступен: соединение отклонено или истекло время ожидания. "
                    "Убедитесь, что PostgreSQL запущен и доступен. "
                    "Для Docker Compose проверьте, что контейнер postgres запущен и здоров."
                )
            else:
                logger.error(
                    f"Операционная ошибка при {operation}: {type(error).__name__}: {error}. "
                    f"DATABASE_URL (замаскирован): {masked_url}"
                )
                return ValueError(
                    f"Ошибка подключения к PostgreSQL: {error}. "
                    f"Проверьте настройки подключения. "
                    f"DATABASE_URL (замаскирован): {masked_url}"
                )

        # ProgrammingError - проблемы с SQL, неверное имя БД
        elif isinstance(error, ProgrammingError):
            if "database" in error_msg and "does not exist" in error_msg:
                logger.error(
                    f"База данных не существует при {operation}. "
                    f"Проверьте POSTGRES_DB. "
                    f"DATABASE_URL (замаскирован): {masked_url}"
                )
                return ValueError(
                    "База данных не существует. "
                    "Убедитесь, что POSTGRES_DB установлен и совпадает с именем базы данных в DATABASE_URL. "
                    "PostgreSQL создаст базу данных автоматически при первом запуске, если она указана в POSTGRES_DB."
                )
            else:
                logger.error(
                    f"Ошибка программирования при {operation}: {type(error).__name__}: {error}. "
                    f"DATABASE_URL (замаскирован): {masked_url}"
                )
                return ValueError(
                    f"Ошибка SQL при {operation}: {error}. "
                    f"Проверьте настройки базы данных."
                )

        # InterfaceError - проблемы с сетью, драйвером
        elif isinstance(error, InterfaceError):
            logger.error(
                f"Ошибка интерфейса при {operation}: {type(error).__name__}: {error}. "
                f"DATABASE_URL (замаскирован): {masked_url}"
            )
            return ValueError(
                f"Ошибка сетевого подключения к PostgreSQL: {error}. "
                f"Проверьте сетевые настройки и доступность PostgreSQL. "
                f"Для Docker Compose убедитесь, что контейнеры находятся в одной сети."
            )

        # Другие ошибки
        else:
            logger.error(
                f"Неожиданная ошибка при {operation}: {type(error).__name__}: {error}. "
                f"DATABASE_URL (замаскирован): {masked_url}",
                exc_info=True,
            )
            return ValueError(
                f"Неожиданная ошибка при подключении к PostgreSQL: {error}. "
                f"Проверьте настройки подключения."
            )

    async def create_tables(self):
        """Создать все таблицы."""
        try:
            async with self.engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
        except (OperationalError, ProgrammingError, InterfaceError) as e:
            raise self._handle_connection_error(e, "создании таблиц") from e
        except Exception as e:
            logger.error(f"Неожиданная ошибка при создании таблиц: {type(e).__name__}: {e}", exc_info=True)
            raise

    async def get_session(self) -> AsyncSession:
        """Получить сессию БД."""
        try:
            async with self.async_session_maker() as session:
                yield session
        except (OperationalError, ProgrammingError, InterfaceError) as e:
            raise self._handle_connection_error(e, "получении сессии") from e
        except Exception as e:
            logger.error(f"Неожиданная ошибка при получении сессии: {type(e).__name__}: {e}", exc_info=True)
            raise
