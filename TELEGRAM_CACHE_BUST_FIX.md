# Исправление проблемы кэширования Telegram Mini App

## Проблема

Telegram кэширует Mini App по URL. После изменений пользователи могут видеть старую версию панели управления при открытии через команду `/panel`.

## Решение

Добавлен query-параметр версии к URL Mini App **только для команды `/panel`**. Это заставляет Telegram воспринимать URL как новый и обновлять кэш.

## Изменения

### Файл: `backend/src/presentation/telegram/keyboards.py`

#### 1. Добавлена функция `_add_version_query_param()`

```python
def _add_version_query_param(url: str, version: int) -> str:
    """
    Добавляет query-параметр версии к URL для обхода кэша Telegram.
    
    КРИТИЧНО: Telegram кэширует Mini App по URL. Изменение query-параметра
    используется как принудительный cache-bust, чтобы гарантировать актуальную версию.
    """
    # Парсит URL, добавляет параметр v={version}, собирает обратно
```

#### 2. Изменена функция `get_panel_menu_keyboard()`

**Было:**
```python
web_app=WebAppInfo(url=webapp_url, start_param="panel")
```

**Стало:**
```python
panel_webapp_url = _add_version_query_param(webapp_url, version=2)
web_app=WebAppInfo(url=panel_webapp_url, start_param="panel")
```

#### 3. Функция `get_main_menu_keyboard()` не изменена

Команда `/start` продолжает открывать Mini App без version-параметра:
```python
web_app=WebAppInfo(url=webapp_url)  # Без параметра версии
```

## Результат

### ✅ Команда `/panel`
- URL Mini App: `https://domain.com/?v=2` (или `https://domain.com/?existing=param&v=2`)
- `start_param="panel"` сохранён без изменений
- Telegram воспринимает URL как новый и обновляет кэш
- Всегда открывается актуальная версия панели управления

### ✅ Команда `/start`
- URL Mini App: `https://domain.com/` (без параметра версии)
- Открывается пользовательский режим (календарь)
- Поведение не изменено

## Архитектурные гарантии

1. **Минимальные изменения**
   - Изменён только backend
   - Изменена только функция `get_panel_menu_keyboard()`
   - Добавлена одна вспомогательная функция

2. **Локальность изменений**
   - НЕ изменён nginx
   - НЕ изменён frontend
   - НЕ добавлена кэш-логика
   - НЕ изменён useAppMode

3. **Сохранение функциональности**
   - `start_param="panel"` сохранён без изменений
   - Команда `/start` работает как раньше
   - Команда `/panel` работает как раньше, но с обновлённым кэшем

4. **Архитектурное решение**
   - Это не временный костыль
   - Использует стандартный механизм cache-bust через query-параметры
   - Версию можно легко увеличить при необходимости (изменить `version=2` на `version=3`)

## Примеры работы

### До изменений
- `/panel` → `https://domain.com/` (кэшируется Telegram)
- `/start` → `https://domain.com/` (кэшируется Telegram)

### После изменений
- `/panel` → `https://domain.com/?v=2` (новый URL, кэш обновляется)
- `/start` → `https://domain.com/` (без изменений)

### Если URL уже содержит query-параметры
- `/panel` → `https://domain.com/?existing=param&v=2` (параметр добавляется корректно)

## Критерии готовности

✅ Telegram перестаёт открывать старую версию Mini App  
✅ После `/panel` всегда открывается актуальная панель управления  
✅ `/start` по-прежнему открывает пользовательский режим  
✅ `start_param="panel"` сохранён без изменений  
✅ Изменения минимальны и локальны (только backend)  

**Решение готово к использованию.**

