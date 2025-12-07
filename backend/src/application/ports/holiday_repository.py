from abc import ABC, abstractmethod
from datetime import date
from typing import List, Optional

from src.domain.entities.professional_holiday import ProfessionalHoliday


class HolidayRepository(ABC):
    @abstractmethod
    async def create(self, holiday: ProfessionalHoliday) -> ProfessionalHoliday:
        """Создать новый профессиональный праздник."""
        pass

    @abstractmethod
    async def get_by_id(self, holiday_id: int) -> Optional[ProfessionalHoliday]:
        """Получить праздник по ID."""
        pass

    @abstractmethod
    async def get_by_date(self, check_date: date) -> List[ProfessionalHoliday]:
        """Получить праздники на указанную дату."""
        pass

    @abstractmethod
    async def update(self, holiday: ProfessionalHoliday) -> ProfessionalHoliday:
        """Обновить праздник."""
        pass

    @abstractmethod
    async def delete(self, holiday_id: int) -> None:
        """Удалить праздник."""
        pass

    @abstractmethod
    async def get_all(self) -> List[ProfessionalHoliday]:
        """Получить все праздники."""
        pass

