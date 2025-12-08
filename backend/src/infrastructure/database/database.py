from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.infrastructure.database.models import Base


class Database:
    def __init__(self, database_url: str):
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

    async def create_tables(self):
        """Создать все таблицы."""
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def get_session(self) -> AsyncSession:
        """Получить сессию БД."""
        async with self.async_session_maker() as session:
            yield session
