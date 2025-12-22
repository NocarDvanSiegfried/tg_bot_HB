# План исправления критических проблем из analyze.md

## Анализ проблем

Из `analyze.md` выявлены две критические проблемы:

1. **CORS ошибка**: Preflight OPTIONS запросы не получают заголовки `Access-Control-Allow-Origin`
2. **SolidJS TDZ ошибка**: Переменная `m` используется до инициализации в `peerProfile.tsx:749`

---

## Проблема 1: CORS для preflight OPTIONS запросов

### Текущая ситуация
- Ошибка: `Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present`
- Запросы: `https://api.micro-tab.ru:9443/api/calendar/month/2025/12` и `/api/calendar/2025-12-24`
- Origin: `https://miniapp.micro-tab.ru:4443`

### Причина
В nginx использование `if` с `add_header` имеет известные ограничения. Директива `if` в nginx может не работать корректно с `add_header` из-за особенностей обработки контекстов.

### Решение
Использовать отдельный `location` блок для OPTIONS запросов вместо `if`:

**Файл:** `nginx/conf.d/backend.conf`

**Изменения:**
1. Создать отдельный `location = /` для OPTIONS запросов
2. Или использовать `map` для определения метода запроса
3. Убедиться, что CORS заголовки добавляются на уровне `server`, а не только в `location`

**Альтернативное решение:**
Использовать отдельный `location` блок для всех OPTIONS запросов:

```nginx
# Обработка OPTIONS запросов (CORS preflight)
location ~ ^/api/ {
    if ($request_method = 'OPTIONS') {
        add_header 'Access-Control-Allow-Origin' 'https://miniapp.micro-tab.ru:4443' always;
        add_header 'Access-Control-Allow-Methods' 'GET, POST, PUT, DELETE, PATCH, OPTIONS' always;
        add_header 'Access-Control-Allow-Headers' 'Authorization, Content-Type, X-Init-Data, Accept' always;
        add_header 'Access-Control-Allow-Credentials' 'true' always;
        add_header 'Access-Control-Max-Age' '3600' always;
        add_header 'Content-Length' '0' always;
        return 204;
    }
    
    # CORS заголовки для всех остальных запросов
    add_header 'Access-Control-Allow-Origin' 'https://miniapp.micro-tab.ru:4443' always;
    add_header 'Access-Control-Allow-Credentials' 'true' always;
    
    # Проксирование
    proxy_pass http://127.0.0.1:8000;
    # ... остальные настройки прокси
}
```

**Проверка:**
- Убедиться, что FastAPI CORS middleware также настроен правильно
- Проверить, что `backend/src/infrastructure/config/cors.py` включает origin `https://miniapp.micro-tab.ru:4443`

---

## Проблема 2: SolidJS TDZ ошибка в peerProfile.tsx

### Текущая ситуация
- Ошибка: `ReferenceError: Cannot access 'm' before initialization`
- Файл: `peerProfile.tsx:749`
- Компонент: `Birthday` (строка 736)
- Stack trace указывает на использование переменной `m` до её объявления

### Причина
Temporal Dead Zone (TDZ) - переменная `m` используется (в createEffect, JSX или callback) до того, как она объявлена через `createSignal`, `createStore` или `createMemo`.

### Решение
**Шаг 1: Найти файл peerProfile.tsx**
- Файл не найден в исходниках проекта
- Возможные места:
  - `frontend/src/components/` (проверить все подкаталоги)
  - `frontend/src/` (проверить все файлы)
  - Возможно, файл был переименован или удален
  - Может быть в скомпилированном коде (`frontend/dist/`)

**Шаг 2: Исправить порядок инициализации**
После нахождения файла:
1. Найти объявление переменной `m` (строка ~749 или позже)
2. Найти все места использования `m` (строки 736-760)
3. Переместить объявление `m` ПЕРЕД всеми использованиями:

```typescript
// ПРАВИЛЬНО:
const m = createSignal(...) // или createStore/createMemo
// Теперь можно использовать m
createEffect(() => { 
  const value = m() // OK
})
return <div>{m()}</div> // OK

// НЕПРАВИЛЬНО:
createEffect(() => { 
  const value = m() // TDZ ERROR - m еще не объявлена
})
const m = createSignal(...) // Объявление после использования
```

**Шаг 3: Проверить зависимости**
- Убедиться, что все `createSignal`, `createStore`, `createMemo` объявлены до использования
- Проверить, что `createEffect` не обращается к переменным до их объявления

---

## Порядок выполнения

### Приоритет 1: CORS (критично)
1. Исправить обработку OPTIONS в `nginx/conf.d/backend.conf`
   - Использовать отдельный `location` блок для OPTIONS
   - Убедиться, что заголовки добавляются с `always`
2. Проверить FastAPI CORS middleware
   - Убедиться, что `backend/src/infrastructure/config/cors.py` включает нужный origin
3. Перезапустить nginx для применения изменений
4. Протестировать preflight запросы

### Приоритет 2: TDZ ошибка
1. Найти файл `peerProfile.tsx`
   - Поиск в исходниках
   - Проверка скомпилированного кода
   - Проверка node_modules (если это библиотека)
2. Исправить порядок инициализации переменной `m`
3. Пересобрать frontend
4. Протестировать компонент Birthday

---

## Ожидаемый результат

- ✅ CORS preflight запросы возвращают 204 с правильными заголовками
- ✅ API запросы от `https://miniapp.micro-tab.ru:4443` проходят успешно
- ✅ TDZ ошибка исправлена, компонент Birthday инициализируется корректно
- ✅ Нет ошибок в консоли браузера

---

## Файлы для изменения

1. `nginx/conf.d/backend.conf` - исправить обработку OPTIONS запросов
2. `backend/src/infrastructure/config/cors.py` - проверить список разрешенных origins (уже исправлен)
3. `peerProfile.tsx` - исправить порядок инициализации (файл нужно найти)

---

## Примечания

- Nginx может требовать перезапуска после изменения конфигурации
- Если файл `peerProfile.tsx` не найден, возможно, это ошибка из другого контекста или библиотеки
- Проверить, не используется ли SolidJS в проекте (судя по package.json, используется React)

