import pytest
from datetime import date

from src.domain.entities.birthday import Birthday


class TestBirthdayEntity:
    """Тесты для сущности Birthday."""

    def test_birthday_creation(self):
        """Тест создания дня рождения."""
        birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment="Комментарий",
        )

        assert birthday.id == 1
        assert birthday.full_name == "Иван Иванов"
        assert birthday.company == "ООО Тест"
        assert birthday.position == "Разработчик"
        assert birthday.birth_date == date(1990, 5, 15)
        assert birthday.comment == "Комментарий"

    def test_birthday_without_comment(self):
        """Тест создания дня рождения без комментария."""
        birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )

        assert birthday.comment is None

    def test_calculate_age_same_year(self):
        """Тест расчета возраста в год рождения."""
        birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )

        age = birthday.calculate_age(date(1990, 6, 1))
        assert age == 0

    def test_calculate_age_next_year(self):
        """Тест расчета возраста в следующем году."""
        birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )

        age = birthday.calculate_age(date(1991, 6, 1))
        assert age == 1

    def test_calculate_age_before_birthday(self):
        """Тест расчета возраста до дня рождения в году."""
        birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )

        # 1 мая 1991 - еще не исполнилось 1 год
        age = birthday.calculate_age(date(1991, 5, 1))
        assert age == 0

        # 15 мая 1991 - исполнилось 1 год
        age = birthday.calculate_age(date(1991, 5, 15))
        assert age == 1

    def test_calculate_age_after_birthday(self):
        """Тест расчета возраста после дня рождения."""
        birthday = Birthday(
            id=1,
            full_name="Иван Иванов",
            company="ООО Тест",
            position="Разработчик",
            birth_date=date(1990, 5, 15),
            comment=None,
        )

        age = birthday.calculate_age(date(2024, 6, 1))
        assert age == 34

