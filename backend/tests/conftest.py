import sys
import os
from pathlib import Path

# Add project root to Python path to ensure src is importable
# This ensures paths are set up BEFORE any imports that might need them
# Priority: PYTHONPATH (CI) > explicit path addition (local)
project_root = Path(__file__).parent.parent
project_root_str = str(project_root.resolve())

# Check PYTHONPATH first (used in CI)
pythonpath = os.environ.get("PYTHONPATH", "")
pythonpath_paths = pythonpath.split(os.pathsep) if pythonpath else []

# Normalize paths for cross-platform compatibility
normalized_project_root = os.path.normpath(project_root_str)

# Check if project root is already in PYTHONPATH or sys.path
in_pythonpath = any(
    os.path.normpath(p) == normalized_project_root 
    for p in pythonpath_paths
    if p
) if pythonpath_paths else False

in_sys_path = any(
    os.path.normpath(p) == normalized_project_root
    for p in sys.path
    if p
)

# Only add to sys.path if not already present
# This must happen BEFORE any imports that use src.* modules
if not in_sys_path and not in_pythonpath:
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
