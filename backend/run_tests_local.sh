#!/bin/bash
# Bash script for running tests locally with correct PYTHONPATH
# Usage: ./run_tests_local.sh

export PYTHONPATH=$(pwd)
pytest tests/ --cov=src --cov-report=term-missing -v

