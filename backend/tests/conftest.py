import sys
import os
from pathlib import Path

# Add project root to Python path to ensure src is importable
# This ensures paths are set up BEFORE any imports that might need them
# Check PYTHONPATH first to avoid conflicts
project_root = Path(__file__).parent.parent
project_root_str = str(project_root.resolve())

# Only add to sys.path if not already in PYTHONPATH or sys.path
# This must happen BEFORE any imports that use src.* modules
pythonpath = os.environ.get("PYTHONPATH", "")
if project_root_str not in sys.path:
    # Check if it's in PYTHONPATH (can be colon/semicolon separated)
    if project_root_str not in pythonpath.split(os.pathsep):
        # Insert at position 1 (after current directory, before site-packages)
        # This ensures installed packages are still found first
        sys.path.insert(1, project_root_str)

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
