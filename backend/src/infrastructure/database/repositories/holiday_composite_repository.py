"""
Композитный репозиторий для профессиональных праздников.

Объединяет данные из файлового репозитория (автоматические праздники)
и БД репозитория (ручные праздники).
"""

import logging
from datetime import date

from src.application.ports.holiday_repository import HolidayRepository
from src.domain.entities.professional_holiday import ProfessionalHoliday

logger = logging.getLogger(__name__)


class HolidayCompositeRepository(HolidayRepository):
    """Реализация репозитория, объединяющая файловый и БД источники."""

    def __init__(
        self,
        file_repository: HolidayRepository,
        db_repository: HolidayRepository,
    ):
        """
        Инициализация композитного репозитория.

        Args:
            file_repository: Репозиторий для автоматических праздников (файл)
            db_repository: Репозиторий для ручных праздников (БД)
        """
        self.file_repository = file_repository
        self.db_repository = db_repository

    async def get_by_date(self, check_date: date) -> list[ProfessionalHoliday]:
        """
        Получить праздники на указанную дату.

        Объединяет автоматические (файл) и ручные (БД) праздники.

        Args:
            check_date: Дата для поиска праздников

        Returns:
            Объединенный список праздников
        """
        # Получаем автоматические праздники из файла
        file_holidays = await self.file_repository.get_by_date(check_date)
        
        # Получаем ручные праздники из БД (по дню и месяцу)
        db_holidays = await self.db_repository.get_by_day_and_month(
            check_date.day, check_date.month
        )
        
        # Объединяем списки
        # Автоматические праздники имеют id=None, ручные - id из БД
        # Сохраняем оба типа, даже если названия совпадают
        all_holidays = list(file_holidays) + list(db_holidays)
        
        return all_holidays

    async def get_by_day_and_month(self, day: int, month: int) -> list[ProfessionalHoliday]:
        """
        Получить праздники в указанный день и месяц (любой год).

        Объединяет автоматические (файл) и ручные (БД) праздники.

        Args:
            day: День месяца
            month: Месяц (1-12)

        Returns:
            Объединенный список праздников
        """
        # Получаем автоматические праздники из файла
        file_holidays = await self.file_repository.get_by_day_and_month(day, month)
        
        # Получаем ручные праздники из БД
        db_holidays = await self.db_repository.get_by_day_and_month(day, month)
        
        # Объединяем списки
        all_holidays = list(file_holidays) + list(db_holidays)
        
        return all_holidays

    async def get_all(self) -> list[ProfessionalHoliday]:
        """
        Получить все праздники.

        Объединяет автоматические (файл) и ручные (БД) праздники.

        Returns:
            Объединенный список всех праздников
        """
        file_holidays = await self.file_repository.get_all()
        db_holidays = await self.db_repository.get_all()
        
        # Объединяем списки
        all_holidays = list(file_holidays) + list(db_holidays)
        
        return all_holidays

    # CRUD операции делегируются в БД репозиторий
    async def create(self, holiday: ProfessionalHoliday) -> ProfessionalHoliday:
        """Создать новый праздник (сохраняется в БД)."""
        return await self.db_repository.create(holiday)

    async def get_by_id(self, holiday_id: int) -> ProfessionalHoliday | None:
        """Получить праздник по ID (только из БД, файловые праздники не имеют ID)."""
        return await self.db_repository.get_by_id(holiday_id)

    async def update(self, holiday: ProfessionalHoliday) -> ProfessionalHoliday:
        """Обновить праздник (только в БД)."""
        return await self.db_repository.update(holiday)

    async def delete(self, holiday_id: int) -> None:
        """Удалить праздник (только из БД)."""
        return await self.db_repository.delete(holiday_id)

