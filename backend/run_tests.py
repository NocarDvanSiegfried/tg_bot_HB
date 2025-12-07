#!/usr/bin/env python
"""Скрипт для запуска тестов."""
import sys
import os

# Добавляем backend в PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "tests/"])

