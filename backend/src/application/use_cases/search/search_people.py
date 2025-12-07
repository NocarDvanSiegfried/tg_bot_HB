from typing import List, Union

from src.application.ports.birthday_repository import BirthdayRepository
from src.application.ports.responsible_repository import ResponsibleRepository
from src.domain.entities.birthday import Birthday
from src.domain.entities.responsible_person import ResponsiblePerson


class SearchPeopleUseCase:
    def __init__(
        self,
        birthday_repository: BirthdayRepository,
        responsible_repository: ResponsibleRepository,
    ):
        self.birthday_repository = birthday_repository
        self.responsible_repository = responsible_repository

    async def execute(
        self,
        query: str,
        search_birthdays: bool = True,
        search_responsible: bool = True,
    ) -> List[Union[Birthday, ResponsiblePerson]]:
        """Поиск людей по ФИО, компании, должности."""
        results = []

        if search_birthdays:
            birthdays = await self.birthday_repository.search(query)
            results.extend(birthdays)

        if search_responsible:
            responsible = await self.responsible_repository.search(query)
            results.extend(responsible)

        return results

