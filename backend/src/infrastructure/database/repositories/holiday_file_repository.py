"""
Файловый репозиторий для профессиональных праздников.

Читает данные из JSON файла вместо БД.
"""

import json
import logging
from datetime import date
from functools import lru_cache
from pathlib import Path

from src.application.ports.holiday_repository import HolidayRepository
from src.domain.entities.professional_holiday import ProfessionalHoliday

logger = logging.getLogger(__name__)


class HolidayFileRepository(HolidayRepository):
    """Реализация репозитория праздников на основе JSON файла."""

    def __init__(self, data_file: Path | None = None):
        """
        Инициализация репозитория.

        Args:
            data_file: Путь к JSON файлу с данными. Если не указан, используется
                       стандартный путь backend/data/professional_holidays.json
        """
        if data_file is None:
            # Определяем путь к файлу относительно корня проекта
            # backend/src/infrastructure/database/repositories/ -> backend/data/
            repo_dir = Path(__file__).parent.parent.parent.parent.parent
            data_file = repo_dir / "data" / "professional_holidays.json"
        
        self.data_file = Path(data_file)
        self._data_cache = None

    def _load_data(self) -> dict:
        """Загрузить данные из JSON файла с кэшированием."""
        if self._data_cache is not None:
            return self._data_cache

        if not self.data_file.exists():
            logger.warning(f"Файл с данными о праздниках не найден: {self.data_file}")
            self._data_cache = {}
            return self._data_cache

        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self._data_cache = data
                return data
        except json.JSONDecodeError as e:
            logger.error(f"Ошибка парсинга JSON файла {self.data_file}: {e}")
            self._data_cache = {}
            return self._data_cache
        except Exception as e:
            logger.error(f"Ошибка загрузки данных из {self.data_file}: {e}")
            self._data_cache = {}
            return self._data_cache

    def _normalize_date(self, check_date: date) -> str:
        """Нормализовать дату в формат MM-DD."""
        return f"{check_date.month:02d}-{check_date.day:02d}"

    async def get_by_date(self, check_date: date) -> list[ProfessionalHoliday]:
        """
        Получить праздники на указанную дату.

        Args:
            check_date: Дата для поиска праздников

        Returns:
            Список профессиональных праздников на эту дату
        """
        data = self._load_data()
        date_key = self._normalize_date(check_date)
        
        holidays_data = data.get(date_key, [])
        
        holidays = []
        for idx, holiday_data in enumerate(holidays_data):
            holiday = ProfessionalHoliday(
                id=None,  # Файловый репозиторий не генерирует ID
                name=holiday_data.get("name", ""),
                description=holiday_data.get("description"),
                date=check_date,  # Используем переданную дату
            )
            holidays.append(holiday)
        
        return holidays

    async def get_by_day_and_month(self, day: int, month: int) -> list[ProfessionalHoliday]:
        """Получить праздники в указанный день и месяц (любой год)."""
        data = self._load_data()
        date_key = f"{month:02d}-{day:02d}"
        
        holidays_data = data.get(date_key, [])
        
        holidays = []
        for holiday_data in holidays_data:
            # Используем текущий год для создания даты
            holiday_date = date(date.today().year, month, day)
            holiday = ProfessionalHoliday(
                id=None,
                name=holiday_data.get("name", ""),
                description=holiday_data.get("description"),
                date=holiday_date,
            )
            holidays.append(holiday)
        
        return holidays

    async def get_all(self) -> list[ProfessionalHoliday]:
        """
        Получить все праздники.

        Returns:
            Список всех профессиональных праздников
        """
        data = self._load_data()
        all_holidays = []
        
        for date_key, holidays_data in data.items():
            # Парсим дату из ключа MM-DD
            try:
                month, day = map(int, date_key.split("-"))
                # Используем текущий год для создания даты
                holiday_date = date(date.today().year, month, day)
            except (ValueError, IndexError) as e:
                logger.warning(f"Неверный формат ключа даты '{date_key}': {e}")
                continue
            
            for holiday_data in holidays_data:
                holiday = ProfessionalHoliday(
                    id=None,
                    name=holiday_data.get("name", ""),
                    description=holiday_data.get("description"),
                    date=holiday_date,
                )
                all_holidays.append(holiday)
        
        return all_holidays

    # Stub методы - не используются, но требуются интерфейсом
    async def create(self, holiday: ProfessionalHoliday) -> ProfessionalHoliday:
        """Создать новый праздник (не поддерживается в файловом репозитории)."""
        raise NotImplementedError("Файловый репозиторий не поддерживает создание праздников")

    async def get_by_id(self, holiday_id: int) -> ProfessionalHoliday | None:
        """Получить праздник по ID (не поддерживается в файловом репозитории)."""
        raise NotImplementedError("Файловый репозиторий не поддерживает поиск по ID")

    async def update(self, holiday: ProfessionalHoliday) -> ProfessionalHoliday:
        """Обновить праздник (не поддерживается в файловом репозитории)."""
        raise NotImplementedError("Файловый репозиторий не поддерживает обновление праздников")

    async def delete(self, holiday_id: int) -> None:
        """Удалить праздник (не поддерживается в файловом репозитории)."""
        raise NotImplementedError("Файловый репозиторий не поддерживает удаление праздников")

