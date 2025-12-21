# Анализ проблемы 502 Bad Gateway

**Дата:** 2025-01-19  
**Проблема:** 502 Bad Gateway при обращении к API через nginx

---

## Описание проблемы

```
502 Bad Gateway
nginx/1.24.0 (Ubuntu)
Failed to load resource: the server responded with a status of 502 (Bad Gateway)
```

**Симптомы:**
- Nginx возвращает 502 Bad Gateway
- Запросы к API не проходят
- Frontend не может получить данные от backend

---

## Анализ конфигурации

### 1. Nginx конфигурация (backend.conf)

**Текущая конфигурация:**
```nginx
location / {
    proxy_pass http://127.0.0.1:8000;
    ...
}
```

**Проблема:**
- Nginx пытается подключиться к `127.0.0.1:8000`
- Если nginx работает в отдельном контейнере или на хосте, а backend в Docker, это может не работать
- `127.0.0.1` в контексте nginx - это localhost самого nginx, а не хоста

### 2. Docker Compose конфигурация

**Текущая конфигурация:**
- Backend слушает на порту 8000 внутри контейнера
- Порт проброшен на хост: `8000:8000`
- Backend доступен на `localhost:8000` на хосте

**Проблема:**
- Если nginx работает на хосте (не в Docker), то `127.0.0.1:8000` должен работать
- Если nginx работает в Docker контейнере, нужно использовать имя сервиса `backend:8000` или `host.docker.internal:8000`

### 3. Возможные причины 502

1. **Backend не запущен**
   - Контейнер backend не запущен
   - Backend упал при старте
   - Backend не слушает на порту 8000

2. **Проблемы с сетью**
   - Nginx не может достучаться до backend
   - Неправильная конфигурация proxy_pass
   - Firewall блокирует соединение

3. **Проблемы с конфигурацией nginx**
   - Неправильный URL в proxy_pass
   - Проблемы с заголовками
   - Таймауты слишком короткие

4. **Проблемы с backend**
   - Backend падает при обработке запросов
   - Backend не отвечает на запросы
   - Проблемы с базой данных

---

## Диагностика

### Шаг 1: Проверить статус контейнеров

```bash
docker compose ps
```

**Ожидаемый результат:**
- Backend контейнер должен быть в статусе `Up`
- Postgres контейнер должен быть в статусе `Up (healthy)`

### Шаг 2: Проверить логи backend

```bash
docker compose logs backend --tail 100
```

**Что искать:**
- Ошибки при запуске
- Сообщения о том, что сервер запущен
- Ошибки подключения к базе данных
- Ошибки при обработке запросов

### Шаг 3: Проверить доступность backend напрямую

```bash
curl http://localhost:8000/health
```

**Ожидаемый результат:**
- Должен вернуться JSON с `{"status": "ok"}`

### Шаг 4: Проверить логи nginx

```bash
# Если nginx в Docker
docker compose logs nginx --tail 100

# Если nginx на хосте
tail -f /var/log/nginx/backend_error.log
```

**Что искать:**
- Ошибки подключения к upstream
- Таймауты
- Ошибки проксирования

### Шаг 5: Проверить конфигурацию nginx

```bash
# Если nginx в Docker
docker compose exec nginx nginx -t

# Если nginx на хосте
nginx -t
```

---

## Решения

### Решение 1: Исправить proxy_pass для Docker сети

**Если nginx работает в Docker контейнере:**

Изменить `nginx/conf.d/backend.conf`:
```nginx
location / {
    proxy_pass http://backend:8000;  # Использовать имя сервиса вместо 127.0.0.1
    ...
}
```

**Если nginx работает на хосте:**

Оставить как есть (`127.0.0.1:8000`), но убедиться, что:
- Backend контейнер запущен
- Порт 8000 проброшен на хост
- Backend слушает на `0.0.0.0:8000` (не на `127.0.0.1:8000`)

### Решение 2: Проверить, что backend слушает на правильном интерфейсе

**В backend коде (main.py или app.py):**

Убедиться, что uvicorn запускается с `host="0.0.0.0"`:
```python
uvicorn.run(app, host="0.0.0.0", port=8000)
```

Если используется `host="127.0.0.1"`, backend будет доступен только внутри контейнера.

### Решение 3: Добавить nginx в docker-compose (если его нет)

Если nginx не в docker-compose, добавить:

```yaml
nginx:
  image: nginx:alpine
  ports:
    - "8001:8001"
    - "3001:3001"
  volumes:
    - ./nginx/conf.d:/etc/nginx/conf.d
    - ./nginx/ssl:/etc/nginx/ssl
  depends_on:
    - backend
    - frontend
```

И изменить proxy_pass на имена сервисов.

### Решение 4: Увеличить таймауты в nginx

Если backend медленно отвечает, увеличить таймауты:

```nginx
proxy_connect_timeout 120s;
proxy_send_timeout 120s;
proxy_read_timeout 120s;
```

---

## Рекомендуемые действия

1. **Немедленно:**
   - Проверить статус контейнеров: `docker compose ps`
   - Проверить логи backend: `docker compose logs backend --tail 100`
   - Проверить доступность backend: `curl http://localhost:8000/health`

2. **Если backend не запущен:**
   - Запустить контейнеры: `docker compose up -d`
   - Проверить ошибки в логах
   - Исправить проблемы с конфигурацией или кодом

3. **Если backend запущен, но nginx не может подключиться:**
   - Проверить конфигурацию proxy_pass
   - Убедиться, что backend слушает на `0.0.0.0:8000`
   - Проверить сеть Docker (если nginx в Docker)

4. **Если все работает локально, но не работает на сервере:**
   - Проверить firewall
   - Проверить, что порты открыты
   - Проверить логи nginx на сервере

---

## Чеклист диагностики

- [ ] Backend контейнер запущен (`docker compose ps`)
- [ ] Backend отвечает на `http://localhost:8000/health`
- [ ] Backend слушает на `0.0.0.0:8000` (не `127.0.0.1:8000`)
- [ ] Nginx конфигурация правильная (proxy_pass указывает на правильный адрес)
- [ ] Нет ошибок в логах backend
- [ ] Нет ошибок в логах nginx
- [ ] Порты не заблокированы firewall
- [ ] Если nginx в Docker, используется правильное имя сервиса в proxy_pass

---

---

## Выводы из анализа кода

### Проверено:

1. **Backend конфигурация (main.py:189):**
   - ✅ Backend слушает на `host="0.0.0.0"` - правильно
   - ✅ Порт берется из `WEB_PORT` или по умолчанию 8000
   - ✅ Backend должен быть доступен на `localhost:8000` на хосте

2. **Docker Compose конфигурация:**
   - ✅ Backend порт проброшен: `8000:8000`
   - ✅ Backend должен быть доступен на хосте через `localhost:8000`
   - ❓ Nginx не найден в docker-compose.yml - вероятно, работает на хосте

3. **Nginx конфигурация (backend.conf:26):**
   - ⚠️ Использует `proxy_pass http://127.0.0.1:8000`
   - ✅ Это правильно, если nginx работает на хосте (не в Docker)
   - ❌ Это неправильно, если nginx работает в Docker контейнере

### Наиболее вероятные причины:

1. **Backend не запущен или упал при старте**
   - Проверить: `docker compose ps`
   - Проверить логи: `docker compose logs backend --tail 100`

2. **Backend не отвечает на запросы**
   - Проверить: `curl http://localhost:8000/health`
   - Проверить логи на ошибки

3. **Nginx работает в Docker, но использует 127.0.0.1**
   - Если nginx в Docker, нужно использовать имя сервиса `backend:8000`
   - Или использовать `host.docker.internal:8000` для доступа к хосту

4. **Проблемы с сетью или firewall**
   - Проверить, что порт 8000 не заблокирован
   - Проверить, что backend действительно слушает на порту

---

## Рекомендуемые действия для диагностики

### 1. Проверить статус контейнеров

```bash
docker compose ps
```

**Ожидаемый результат:**
```
NAME                STATUS
tg_bot_hb-backend   Up (healthy)
tg_bot_hb-postgres  Up (healthy)
```

### 2. Проверить логи backend

```bash
docker compose logs backend --tail 100
```

**Что искать:**
- Сообщение "Application startup complete" или "Uvicorn running on"
- Ошибки при запуске
- Ошибки подключения к базе данных
- Ошибки при обработке запросов

### 3. Проверить доступность backend напрямую

```bash
curl http://localhost:8000/health
```

**Ожидаемый результат:**
```json
{"status":"ok","service":"Telegram Birthday Calendar API","message":"API is running"}
```

### 4. Проверить, слушает ли backend на порту 8000

```bash
# Linux/macOS
netstat -tuln | grep 8000
# или
ss -tuln | grep 8000

# Windows
netstat -an | findstr 8000
```

**Ожидаемый результат:**
```
tcp  0.0.0.0:8000  LISTEN
```

### 5. Проверить логи nginx (если доступны)

```bash
# Если nginx в Docker
docker compose logs nginx --tail 100

# Если nginx на хосте
tail -f /var/log/nginx/backend_error.log
```

**Что искать:**
- "connect() failed (111: Connection refused)"
- "upstream timed out"
- "no live upstreams"

---

## Быстрое решение

Если backend не запущен:

```bash
# Перезапустить все сервисы
docker compose down
docker compose up -d

# Проверить статус
docker compose ps

# Проверить логи
docker compose logs backend --tail 50
```

Если backend запущен, но nginx не может подключиться:

1. **Если nginx в Docker контейнере:**
   - Изменить `proxy_pass http://127.0.0.1:8000` на `proxy_pass http://backend:8000`
   - Или добавить nginx в docker-compose.yml с правильной сетью

2. **Если nginx на хосте:**
   - Убедиться, что backend контейнер запущен
   - Проверить, что порт 8000 проброшен: `docker compose ps`
   - Проверить доступность: `curl http://localhost:8000/health`

---

**Статус:** Требуется диагностика для определения точной причины  
**Приоритет:** Высокий (блокирует работу приложения)  
**Следующий шаг:** Выполнить диагностические команды выше

