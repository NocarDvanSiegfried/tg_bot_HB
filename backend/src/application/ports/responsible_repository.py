from abc import ABC, abstractmethod
from datetime import date
from typing import List, Optional

from src.domain.entities.responsible_person import ResponsiblePerson


class ResponsibleRepository(ABC):
    @abstractmethod
    async def create(self, responsible: ResponsiblePerson) -> ResponsiblePerson:
        """Создать нового ответственного."""
        pass

    @abstractmethod
    async def get_by_id(self, responsible_id: int) -> Optional[ResponsiblePerson]:
        """Получить ответственного по ID."""
        pass

    @abstractmethod
    async def get_by_date(self, check_date: date) -> Optional[ResponsiblePerson]:
        """Получить ответственного на указанную дату."""
        pass

    @abstractmethod
    async def update(self, responsible: ResponsiblePerson) -> ResponsiblePerson:
        """Обновить ответственного."""
        pass

    @abstractmethod
    async def delete(self, responsible_id: int) -> None:
        """Удалить ответственного."""
        pass

    @abstractmethod
    async def assign_to_date(self, responsible_id: int, assignment_date: date) -> None:
        """Назначить ответственного на дату."""
        pass

    @abstractmethod
    async def search(self, query: str) -> List[ResponsiblePerson]:
        """Поиск по ФИО, компании, должности."""
        pass

    @abstractmethod
    async def get_all(self) -> List[ResponsiblePerson]:
        """Получить всех ответственных."""
        pass

