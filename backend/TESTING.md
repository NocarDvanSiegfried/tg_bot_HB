# Инструкции по запуску тестов

## Запуск тестов в Docker (Рекомендуется)

### Windows (PowerShell)

```powershell
# Из корневой директории проекта
cd backend
.\run_tests_docker.ps1

# С дополнительными опциями pytest
.\run_tests_docker.ps1 -PytestArgs @("-v", "--cov=src", "--cov-report=html")
```

### Linux/macOS

```bash
# Сделать скрипт исполняемым (первый раз)
chmod +x backend/run_tests_docker.sh

# Из корневой директории проекта
cd backend
./run_tests_docker.sh

# С дополнительными опциями pytest
./run_tests_docker.sh -v --cov=src --cov-report=html
```

### Требования

- Docker и Docker Compose должны быть установлены и запущены
- Backend контейнер должен быть запущен (скрипт автоматически запустит его, если он не запущен)

## Запуск тестов в локальном окружении

### Создание виртуального окружения

#### Windows

```powershell
# Создать виртуальное окружение
python -m venv venv

# Активировать виртуальное окружение
.\venv\Scripts\Activate.ps1

# Установить зависимости
pip install -r requirements.txt

# Запустить тесты
pytest tests/ -v
```

#### Linux/macOS

```bash
# Создать виртуальное окружение
python3 -m venv venv

# Активировать виртуальное окружение
source venv/bin/activate

# Установить зависимости
pip install -r requirements.txt

# Запустить тесты
pytest tests/ -v
```

## Опции pytest

### Базовые опции

- `-v` или `--verbose` - подробный вывод
- `--tb=short` - короткий traceback при ошибках
- `--tb=long` - полный traceback при ошибках
- `-k "test_name"` - запустить только тесты, соответствующие паттерну

### Покрытие кода

```bash
# С покрытием кода
pytest tests/ -v --cov=src --cov-report=html

# Минимальный порог покрытия
pytest tests/ -v --cov=src --cov-report=html --cov-fail-under=70
```

### Запуск конкретных тестов

```bash
# Запустить тесты в конкретном файле
pytest tests/presentation/web/test_api.py -v

# Запустить конкретный тест
pytest tests/presentation/web/test_api.py::test_specific_test -v

# Запустить тесты по паттерну
pytest tests/ -k "birthday" -v
```

## Структура тестов

```
tests/
├── application/          # Тесты для use cases
├── domain/               # Тесты для domain entities
├── infrastructure/       # Тесты для репозиториев и внешних сервисов
└── presentation/         # Тесты для handlers и API endpoints
    ├── telegram/        # Тесты для Telegram handlers
    └── web/             # Тесты для Web API endpoints
```

## Устранение проблем

### Ошибка: ModuleNotFoundError

**Проблема:** Отсутствуют зависимости

**Решение:**
1. Убедитесь, что виртуальное окружение активировано
2. Установите зависимости: `pip install -r requirements.txt`
3. Или используйте Docker: `.\run_tests_docker.ps1` (Windows) / `./run_tests_docker.sh` (Linux/macOS)

### Ошибка: Database connection failed

**Проблема:** База данных недоступна

**Решение:**
1. Убедитесь, что Docker Compose запущен: `docker compose up -d`
2. Проверьте, что PostgreSQL контейнер запущен: `docker compose ps postgres`
3. Проверьте переменные окружения в `.env` файле

### Ошибка: Docker container not running

**Проблема:** Backend контейнер не запущен

**Решение:**
1. Запустите Docker Compose: `docker compose up -d`
2. Дождитесь готовности контейнеров: `docker compose ps`
3. Скрипт `run_tests_docker` автоматически запустит контейнер, если он не запущен

## CI/CD

Для автоматического запуска тестов в CI/CD используйте:

```yaml
# Пример для GitHub Actions
- name: Run tests
  run: |
    docker compose up -d
    docker compose exec -T backend pytest tests/ -v
```

## Дополнительная информация

- Всего тестов: ~225
- Категории: Domain, Application, Infrastructure, Presentation
- Используемый фреймворк: pytest с pytest-asyncio для async тестов

