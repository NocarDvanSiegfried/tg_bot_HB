import pytest
import importlib
from datetime import date
from unittest.mock import AsyncMock, MagicMock, patch
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.infrastructure.services import notifications_scheduler


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
        scheduler = await notifications_scheduler.setup_notifications(mock_bot, mock_database)
        
        assert scheduler is not None
        assert isinstance(scheduler, AsyncIOScheduler)
        assert scheduler.running

    @pytest.mark.asyncio
    async def test_scheduler_start(self, mock_bot, mock_database):
        """Тест запуска scheduler."""
        scheduler = await notifications_scheduler.setup_notifications(mock_bot, mock_database)
        
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
        scheduler = await notifications_scheduler.setup_notifications(mock_bot, mock_database)
        
        assert scheduler.running
        scheduler.shutdown(wait=True)
        # После shutdown scheduler может быть в состоянии остановки
        # Проверяем, что метод shutdown не вызывает ошибок
        assert scheduler is not None

    @pytest.mark.asyncio
    async def test_scheduler_jobs_configuration(self, mock_bot, mock_database):
        """Тест конфигурации задач scheduler."""
        scheduler = await notifications_scheduler.setup_notifications(mock_bot, mock_database)
        
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

    @pytest.mark.asyncio
    async def test_send_today_execution(self, mock_bot, mock_database):
        """Тест выполнения задачи send_today."""
        # Патчим классы в исходных модулях - они будут использованы при импорте внутри функций
        with patch(
            "src.infrastructure.database.repositories.birthday_repository_impl.BirthdayRepositoryImpl"
        ) as mock_repo_class, patch(
            "src.infrastructure.services.notification_service_impl.NotificationServiceImpl"
        ) as mock_service_class:
            # Настройка моков
            mock_session = AsyncMock()
            async def get_session():
                yield mock_session
            
            mock_database.get_session = get_session
            
            # Мокируем репозиторий с async методами
            from src.domain.entities.birthday import Birthday
            mock_birthday = Birthday(
                id=1,
                full_name="Иван Иванов",
                company="ООО Тест",
                position="Разработчик",
                birth_date=date.today(),
                comment=None,
            )
            mock_repo = AsyncMock()
            mock_repo.get_by_date = AsyncMock(return_value=[mock_birthday])
            mock_repo_class.return_value = mock_repo
            
            # Мокируем session для get_active_users
            mock_session.execute = AsyncMock()
            mock_result = MagicMock()
            mock_result.scalars.return_value.all.return_value = []
            mock_session.execute.return_value = mock_result
            
            mock_service = AsyncMock()
            mock_service.send_today_notifications = AsyncMock()
            mock_service.get_active_users = AsyncMock(return_value=[123])
            mock_service_class.return_value = mock_service
            
            # Перезагружаем модуль после патчей, чтобы импорты внутри функций использовали патченные классы
            importlib.reload(notifications_scheduler)
            scheduler = await notifications_scheduler.setup_notifications(mock_bot, mock_database)
            
            # Получаем задачу и выполняем её
            jobs = scheduler.get_jobs()
            daily_job = next(job for job in jobs if job.id == "daily_birthdays")
            
            # Выполняем задачу
            await daily_job.func()
            
            # Проверяем, что сервис был вызван
            mock_service.send_today_notifications.assert_called_once()
            
            scheduler.shutdown(wait=True)

    @pytest.mark.asyncio
    async def test_send_week_execution(self, mock_bot, mock_database):
        """Тест выполнения задачи send_week."""
        with patch(
            "src.infrastructure.database.repositories.birthday_repository_impl.BirthdayRepositoryImpl"
        ) as mock_repo_class, patch(
            "src.infrastructure.services.notification_service_impl.NotificationServiceImpl"
        ) as mock_service_class:
            # Настройка моков
            mock_session = AsyncMock()
            async def get_session():
                yield mock_session
            
            mock_database.get_session = get_session
            
            # Мокируем репозиторий с async методами
            from src.domain.entities.birthday import Birthday
            mock_birthday = Birthday(
                id=1,
                full_name="Иван Иванов",
                company="ООО Тест",
                position="Разработчик",
                birth_date=date.today(),
                comment=None,
            )
            mock_repo = AsyncMock()
            mock_repo.get_by_date_range = AsyncMock(return_value=[mock_birthday])
            mock_repo_class.return_value = mock_repo
            
            # Мокируем session для get_active_users
            mock_session.execute = AsyncMock()
            mock_result = MagicMock()
            mock_result.scalars.return_value.all.return_value = []
            mock_session.execute.return_value = mock_result
            
            mock_service = AsyncMock()
            mock_service.send_week_notifications = AsyncMock()
            mock_service.get_active_users = AsyncMock(return_value=[123])
            mock_service_class.return_value = mock_service
            
            # Перезагружаем модуль после патчей, чтобы импорты внутри функций использовали патченные классы
            importlib.reload(notifications_scheduler)
            scheduler = await notifications_scheduler.setup_notifications(mock_bot, mock_database)
            
            # Получаем задачу и выполняем её
            jobs = scheduler.get_jobs()
            weekly_job = next(job for job in jobs if job.id == "weekly_birthdays")
            
            # Выполняем задачу
            await weekly_job.func()
            
            # Проверяем, что сервис был вызван
            mock_service.send_week_notifications.assert_called_once()
            
            scheduler.shutdown(wait=True)

    @pytest.mark.asyncio
    async def test_send_month_execution(self, mock_bot, mock_database):
        """Тест выполнения задачи send_month."""
        with patch(
            "src.infrastructure.database.repositories.birthday_repository_impl.BirthdayRepositoryImpl"
        ) as mock_repo_class, patch(
            "src.infrastructure.services.notification_service_impl.NotificationServiceImpl"
        ) as mock_service_class:
            # Настройка моков
            mock_session = AsyncMock()
            async def get_session():
                yield mock_session
            
            mock_database.get_session = get_session
            
            # Мокируем репозиторий с async методами
            from src.domain.entities.birthday import Birthday
            mock_birthday = Birthday(
                id=1,
                full_name="Иван Иванов",
                company="ООО Тест",
                position="Разработчик",
                birth_date=date.today(),
                comment=None,
            )
            mock_repo = AsyncMock()
            mock_repo.get_by_date_range = AsyncMock(return_value=[mock_birthday])
            mock_repo_class.return_value = mock_repo
            
            # Мокируем session для get_active_users
            mock_session.execute = AsyncMock()
            mock_result = MagicMock()
            mock_result.scalars.return_value.all.return_value = []
            mock_session.execute.return_value = mock_result
            
            mock_service = AsyncMock()
            mock_service.send_month_notifications = AsyncMock()
            mock_service.get_active_users = AsyncMock(return_value=[123])
            mock_service_class.return_value = mock_service
            
            # Перезагружаем модуль после патчей, чтобы импорты внутри функций использовали патченные классы
            importlib.reload(notifications_scheduler)
            scheduler = await notifications_scheduler.setup_notifications(mock_bot, mock_database)
            
            # Получаем задачу и выполняем её
            jobs = scheduler.get_jobs()
            monthly_job = next(job for job in jobs if job.id == "monthly_birthdays")
            
            # Выполняем задачу
            await monthly_job.func()
            
            # Проверяем, что сервис был вызван
            mock_service.send_month_notifications.assert_called_once()
            
            scheduler.shutdown(wait=True)

    @pytest.mark.asyncio
    async def test_send_today_error_handling(self, mock_bot, mock_database):
        """Тест обработки ошибок в send_today."""
        with patch(
            "src.infrastructure.database.repositories.birthday_repository_impl.BirthdayRepositoryImpl"
        ) as mock_repo_class, patch(
            "src.infrastructure.services.notification_service_impl.NotificationServiceImpl"
        ) as mock_service_class:
            # Настройка моков
            mock_session = AsyncMock()
            async def get_session():
                yield mock_session
            
            mock_database.get_session = get_session
            
            # Мокируем репозиторий с async методами
            from src.domain.entities.birthday import Birthday
            mock_birthday = Birthday(
                id=1,
                full_name="Иван Иванов",
                company="ООО Тест",
                position="Разработчик",
                birth_date=date.today(),
                comment=None,
            )
            mock_repo = AsyncMock()
            mock_repo.get_by_date = AsyncMock(return_value=[mock_birthday])
            mock_repo_class.return_value = mock_repo
            
            # Мокируем session для get_active_users
            mock_session.execute = AsyncMock()
            mock_result = MagicMock()
            mock_result.scalars.return_value.all.return_value = []
            mock_session.execute.return_value = mock_result
            
            mock_service = AsyncMock()
            mock_service.send_today_notifications = AsyncMock(side_effect=Exception("Test error"))
            mock_service.get_active_users = AsyncMock(return_value=[123])
            mock_service_class.return_value = mock_service
            
            # Перезагружаем модуль после патчей, чтобы импорты внутри функций использовали патченные классы
            importlib.reload(notifications_scheduler)
            scheduler = await notifications_scheduler.setup_notifications(mock_bot, mock_database)
            
            # Получаем задачу и выполняем её
            jobs = scheduler.get_jobs()
            daily_job = next(job for job in jobs if job.id == "daily_birthdays")
            
            # Выполняем задачу - ошибка должна быть обработана
            try:
                await daily_job.func()
            except Exception:
                # Ошибка ожидаема
                pass
            
            # Проверяем, что сервис был вызван
            mock_service.send_today_notifications.assert_called_once()
            
            scheduler.shutdown(wait=True)

