import os

from sqlalchemy.ext.asyncio import AsyncSession

from src.application.use_cases.auth.verify_telegram_auth import VerifyTelegramAuthUseCase
from src.application.use_cases.birthday.create_birthday import CreateBirthdayUseCase
from src.application.use_cases.birthday.delete_birthday import DeleteBirthdayUseCase
from src.application.use_cases.birthday.get_all_birthdays import GetAllBirthdaysUseCase
from src.application.use_cases.birthday.update_birthday import UpdateBirthdayUseCase
from src.application.use_cases.calendar.get_calendar_data import GetCalendarDataUseCase
from src.application.use_cases.greeting.create_card import CreateCardUseCase
from src.application.use_cases.greeting.generate_greeting import GenerateGreetingUseCase
from src.application.use_cases.panel.check_panel_access import CheckPanelAccessUseCase
from src.application.use_cases.panel.record_panel_access import RecordPanelAccessUseCase
from src.application.use_cases.responsible.assign_responsible_to_date import (
    AssignResponsibleToDateUseCase,
)
from src.application.use_cases.responsible.create_responsible import CreateResponsibleUseCase
from src.application.use_cases.responsible.delete_responsible import DeleteResponsibleUseCase
from src.application.use_cases.responsible.get_all_responsible import GetAllResponsibleUseCase
from src.application.use_cases.responsible.update_responsible import UpdateResponsibleUseCase
from src.application.use_cases.search.search_people import SearchPeopleUseCase
from src.infrastructure.database.repositories.birthday_repository_impl import BirthdayRepositoryImpl
from src.infrastructure.database.repositories.holiday_file_repository import HolidayFileRepository
from src.infrastructure.database.repositories.panel_access_repository_impl import (
    PanelAccessRepositoryImpl,
)
from src.infrastructure.database.repositories.responsible_repository_impl import (
    ResponsibleRepositoryImpl,
)
from src.infrastructure.external.openrouter_client_impl import OpenRouterClientImpl
from src.infrastructure.external.telegram_auth import TelegramAuthServiceImpl
from src.infrastructure.image.card_generator import CardGeneratorImpl


class UseCaseFactory:
    """Фабрика для создания use-cases с зависимостями."""

    def __init__(self, session: AsyncSession | None = None):
        self.session = session
        self._birthday_repo = None
        self._holiday_repo = None
        self._responsible_repo = None
        self._panel_access_repo = None
        self._openrouter_client = None
        self._card_generator = None
        self._telegram_auth_service = None

    @property
    def birthday_repo(self):
        if self._birthday_repo is None:
            self._birthday_repo = BirthdayRepositoryImpl(self.session)
        return self._birthday_repo

    @property
    def holiday_repo(self):
        if self._holiday_repo is None:
            self._holiday_repo = HolidayFileRepository()
        return self._holiday_repo

    @property
    def responsible_repo(self):
        if self._responsible_repo is None:
            self._responsible_repo = ResponsibleRepositoryImpl(self.session)
        return self._responsible_repo

    @property
    def panel_access_repo(self):
        if self._panel_access_repo is None:
            self._panel_access_repo = PanelAccessRepositoryImpl(self.session)
        return self._panel_access_repo

    @property
    def openrouter_client(self):
        if self._openrouter_client is None:
            from src.infrastructure.config.openrouter_config import OpenRouterConfig

            api_key = os.getenv("OPENROUTER_API_KEY")
            if not api_key:
                raise ValueError("OPENROUTER_API_KEY environment variable is required")
            config = OpenRouterConfig(api_key=api_key)
            self._openrouter_client = OpenRouterClientImpl(config)
        return self._openrouter_client

    @property
    def card_generator(self):
        if self._card_generator is None:
            self._card_generator = CardGeneratorImpl()
        return self._card_generator

    @property
    def telegram_auth_service(self):
        if self._telegram_auth_service is None:
            self._telegram_auth_service = TelegramAuthServiceImpl()
        return self._telegram_auth_service

    def create_birthday_use_cases(self):
        """Создать use-cases для работы с днями рождения."""
        return {
            "create": CreateBirthdayUseCase(self.birthday_repo),
            "update": UpdateBirthdayUseCase(self.birthday_repo),
            "delete": DeleteBirthdayUseCase(self.birthday_repo),
            "get_all": GetAllBirthdaysUseCase(self.birthday_repo),
        }

    def create_calendar_use_case(self):
        """Создать use-case для получения данных календаря."""
        return GetCalendarDataUseCase(
            self.birthday_repo,
            self.holiday_repo,
            self.responsible_repo,
        )

    def create_responsible_use_cases(self):
        """Создать use-cases для работы с ответственными."""
        return {
            "create": CreateResponsibleUseCase(self.responsible_repo),
            "update": UpdateResponsibleUseCase(self.responsible_repo),
            "delete": DeleteResponsibleUseCase(self.responsible_repo),
            "assign_to_date": AssignResponsibleToDateUseCase(self.responsible_repo),
            "get_all": GetAllResponsibleUseCase(self.responsible_repo),
        }

    def create_search_use_case(self):
        """Создать use-case для поиска."""
        return SearchPeopleUseCase(self.birthday_repo, self.responsible_repo)

    def create_greeting_use_cases(self):
        """Создать use-cases для генерации поздравлений."""
        return {
            "generate": GenerateGreetingUseCase(self.birthday_repo, self.openrouter_client),
            "create_card": CreateCardUseCase(self.birthday_repo, self.card_generator),
        }

    def create_panel_access_use_case(self):
        """Создать use-case для проверки доступа к панели."""
        return CheckPanelAccessUseCase(self.panel_access_repo)

    def create_record_panel_access_use_case(self):
        """Создать use-case для записи доступа к панели."""
        return RecordPanelAccessUseCase(self.panel_access_repo)

    def create_auth_use_case(self):
        """Создать use-case для верификации Telegram auth."""
        bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        if not bot_token:
            raise ValueError("TELEGRAM_BOT_TOKEN environment variable is required")
        return VerifyTelegramAuthUseCase(self.telegram_auth_service, bot_token)
