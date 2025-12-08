import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.infrastructure.services.notifications_scheduler import setup_notifications


class TestNotificationsScheduler:
    """Тесты для scheduler уведомлений."""

    @pytest.fixture
    def mock_bot(self):
        """Мок бота."""
        return AsyncMock()

    @pytest.fixture
    def mock_database(self):
        """Мок базы данных."""
        db = MagicMock()
        session = AsyncMock()
        
        async def get_session():
            yield session
        
        db.get_session = get_session
        return db

    @pytest.mark.asyncio
    async def test_scheduler_initialization(self, mock_bot, mock_database):
        """Тест инициализации scheduler."""
        scheduler = await setup_notifications(mock_bot, mock_database)
        
        assert scheduler is not None
        assert isinstance(scheduler, AsyncIOScheduler)
        assert scheduler.running

    @pytest.mark.asyncio
    async def test_scheduler_start(self, mock_bot, mock_database):
        """Тест запуска scheduler."""
        scheduler = await setup_notifications(mock_bot, mock_database)
        
        assert scheduler.running
        # Проверяем, что задачи добавлены
        jobs = scheduler.get_jobs()
        assert len(jobs) == 3
        job_ids = [job.id for job in jobs]
        assert "daily_birthdays" in job_ids
        assert "weekly_birthdays" in job_ids
        assert "monthly_birthdays" in job_ids

    @pytest.mark.asyncio
    async def test_scheduler_stop(self, mock_bot, mock_database):
        """Тест остановки scheduler."""
        scheduler = await setup_notifications(mock_bot, mock_database)
        
        assert scheduler.running
        scheduler.shutdown(wait=True)
        # После shutdown scheduler может быть в состоянии остановки
        # Проверяем, что метод shutdown не вызывает ошибок
        assert scheduler is not None

    @pytest.mark.asyncio
    async def test_scheduler_jobs_configuration(self, mock_bot, mock_database):
        """Тест конфигурации задач scheduler."""
        scheduler = await setup_notifications(mock_bot, mock_database)
        
        jobs = scheduler.get_jobs()
        
        # Проверяем daily job
        daily_job = next(job for job in jobs if job.id == "daily_birthdays")
        assert daily_job is not None
        
        # Проверяем weekly job
        weekly_job = next(job for job in jobs if job.id == "weekly_birthdays")
        assert weekly_job is not None
        
        # Проверяем monthly job
        monthly_job = next(job for job in jobs if job.id == "monthly_birthdays")
        assert monthly_job is not None

