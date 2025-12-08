import sys
import os
from pathlib import Path


def _setup_python_path_unified(project_root_str=None):
    """Unified function to setup Python path.
    
    In CI with importlib mode and PYTHONPATH set, don't modify sys.path to avoid conflicts.
    In local development or without importlib, add project root to sys.path.
    Adding to end ensures installed packages (like aiogram) are found first.
    """
    if project_root_str is None:
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
    
    # Check if we're in importlib mode (check sys.argv for pytest arguments)
    is_importlib_mode = any("--import-mode=importlib" in arg for arg in sys.argv)
    
    # In CI with importlib mode and PYTHONPATH set, don't modify sys.path
    # This avoids conflicts where Python might find local files instead of installed packages
    if is_importlib_mode and pythonpath and in_pythonpath:
        # Rely on PYTHONPATH in CI with importlib mode
        return
    
    # Otherwise, add to sys.path if not present
    # Adding to end ensures installed packages (like aiogram) are found first
    if not in_sys_path:
        sys.path.append(project_root_str)


# Setup path IMMEDIATELY when conftest.py is imported, before any other imports
# This ensures sys.path is configured before Python starts importing modules,
# which is critical for importlib mode compatibility
_setup_python_path_unified()

# Verify that aiogram can be imported correctly after path setup
# This helps detect conflicts where local files might shadow installed packages
try:
    import aiogram
    # Verify aiogram is a package, not a module
    if not hasattr(aiogram, '__path__'):
        raise ImportError("aiogram is not a package - possible name conflict")
except ImportError as e:
    # Log warning but don't fail - this is just a diagnostic check
    import warnings
    warnings.warn(f"Could not verify aiogram import: {e}", ImportWarning)


def pytest_load_initial_conftests(early_config, parser, args):
    """Load initial conftests - ensure path is set up (additional guarantee).
    
    This hook runs before pytest_configure and before any test collection,
    ensuring sys.path is set up correctly even with --import-mode=importlib.
    
    Note: Path setup already happens at module import time (see top of file),
    but this hook provides an additional guarantee in case the module import
    path setup didn't work correctly.
    """
    # Path should already be set up at module import time, but verify and add if needed
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
    
    # Use unified function to setup path (will check if already present)
    _setup_python_path_unified(project_root_str)


# Path setup happens at module import time (see _setup_python_path_unified() call above)
# pytest_load_initial_conftests hook provides additional guarantee if needed

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
