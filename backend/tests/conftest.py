import sys
from pathlib import Path

# Add project root to Python path to ensure src is importable
# This is needed when pytest.ini doesn't have pythonpath set
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

import pytest
from datetime import date
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.birthday import Birthday
from src.domain.entities.responsible_person import ResponsiblePerson
from src.domain.entities.professional_holiday import ProfessionalHoliday


@pytest.fixture
def mock_session():
    """Мок сессии БД."""
    return AsyncMock(spec=AsyncSession)


@pytest.fixture
def sample_birthday():
    """Пример дня рождения."""
    return Birthday(
        id=1,
        full_name="Иван Иванов",
        company="ООО Тест",
        position="Разработчик",
        birth_date=date(1990, 5, 15),
        comment="Тестовый комментарий",
    )


@pytest.fixture
def sample_responsible():
    """Пример ответственного."""
    return ResponsiblePerson(
        id=1,
        full_name="Петр Петров",
        company="ООО Тест",
        position="Менеджер",
    )


@pytest.fixture
def sample_holiday():
    """Пример праздника."""
    return ProfessionalHoliday(
        id=1,
        name="День программиста",
        description="Профессиональный праздник",
        date=date(2024, 9, 13),
    )
