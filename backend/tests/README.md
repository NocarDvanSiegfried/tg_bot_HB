# Тесты проекта Telegram Birthday Calendar

## Запуск тестов

### Из корня проекта:
```bash
cd backend
python run_tests.py
```

### Или через pytest:
```bash
cd backend
python -m pytest tests/ -v
```

### Конкретный файл:
```bash
python -m pytest tests/domain/test_birthday_entity.py -v
```

### С покрытием:
```bash
pip install pytest-cov
python -m pytest tests/ --cov=src --cov-report=html
```

## Структура тестов

```
tests/
├── conftest.py                    # Общие фикстуры
├── domain/                        # Тесты domain layer
│   └── test_birthday_entity.py
├── application/                   # Тесты application layer
│   ├── test_create_birthday_use_case.py
│   ├── test_update_birthday_use_case.py
│   └── test_delete_birthday_use_case.py
└── infrastructure/               # Тесты infrastructure layer
    └── test_birthday_repository.py
```

## Принципы тестирования

1. **Изоляция** - каждый тест независим
2. **Моки** - используются для изоляции зависимостей
3. **Быстрота** - unit тесты выполняются быстро
4. **Детерминированность** - результаты предсказуемы

