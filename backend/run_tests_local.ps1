# PowerShell script for running tests locally with correct PYTHONPATH
# Usage: .\run_tests_local.ps1

$env:PYTHONPATH = $PWD
pytest tests/ --cov=src --cov-report=term-missing -v

