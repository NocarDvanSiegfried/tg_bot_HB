import sys
import os
from pathlib import Path


def pytest_load_initial_conftests(early_config, parser, args):
    """Load initial conftests - setup path before any imports.
    
    This hook runs before pytest_configure and before any test collection,
    ensuring sys.path is set up correctly even with --import-mode=importlib.
    """
    # Setup path immediately, before any test collection
    # Try to get path from early_config.rootpath first, fallback to __file__
    try:
        if hasattr(early_config, 'rootpath') and early_config.rootpath:
            project_root = early_config.rootpath
        else:
            # Fallback to __file__ if rootpath is not available
            project_root = Path(__file__).parent.parent
        project_root_str = str(project_root.resolve())
    except (NameError, AttributeError):
        # If __file__ is not available, try to use current working directory
        # This should work in CI where PYTHONPATH is set
        project_root_str = os.getcwd()
    
    # Check PYTHONPATH first (used in CI)
    pythonpath = os.environ.get("PYTHONPATH", "")
    pythonpath_paths = pythonpath.split(os.pathsep) if pythonpath else []
    
    normalized_project_root = os.path.normpath(project_root_str)
    
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
    
    # Add to sys.path if not already present
    # Append to end to ensure installed packages (like aiogram) are found first
    if not in_sys_path and not in_pythonpath:
        sys.path.append(project_root_str)


def _setup_python_path():
    """Setup Python path before any imports."""
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
    # Insert at position 1 (after current directory, before site-packages)
    # This ensures installed packages like aiogram are still found first
    if not in_sys_path and not in_pythonpath:
        sys.path.insert(1, project_root_str)

# Setup path immediately when conftest is imported
# This runs before pytest collects tests, even with --import-mode=importlib
_setup_python_path()

# Also set up path in pytest_configure hook as a fallback
# This ensures path is set even if conftest imports happen in unexpected order
def pytest_configure(config):
    """Configure pytest - ensure Python path is set up."""
    _setup_python_path()

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
