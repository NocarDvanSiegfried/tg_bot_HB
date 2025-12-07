from abc import ABC, abstractmethod
from datetime import date
from typing import List, Optional

from src.domain.entities.birthday import Birthday


class BirthdayRepository(ABC):
    @abstractmethod
    async def create(self, birthday: Birthday) -> Birthday:
        """Создать новый день рождения."""
        pass

    @abstractmethod
    async def get_by_id(self, birthday_id: int) -> Optional[Birthday]:
        """Получить день рождения по ID."""
        pass

    @abstractmethod
    async def get_by_date(self, check_date: date) -> List[Birthday]:
        """Получить дни рождения на указанную дату."""
        pass

    @abstractmethod
    async def get_by_date_range(self, start_date: date, end_date: date) -> List[Birthday]:
        """Получить дни рождения в диапазоне дат."""
        pass

    @abstractmethod
    async def update(self, birthday: Birthday) -> Birthday:
        """Обновить день рождения."""
        pass

    @abstractmethod
    async def delete(self, birthday_id: int) -> None:
        """Удалить день рождения."""
        pass

    @abstractmethod
    async def search(self, query: str) -> List[Birthday]:
        """Поиск по ФИО, компании, должности."""
        pass

    @abstractmethod
    async def get_all(self) -> List[Birthday]:
        """Получить все дни рождения."""
        pass

