# Mini App Static Deployment Guide

## Обзор

Этот документ описывает процесс перевода Telegram Mini App в полноценный production-static режим, полностью исключающий dev-серверы, порт 3000 и любые runtime-зависимости от Node.js на сервере.

## Архитектура

**До:**
```
Telegram WebView → Nginx (proxy_pass) → Docker Container (Vite dev server:3000)
```

**После:**
```
Telegram WebView → Nginx (static files) → /var/www/miniapp (статические файлы)
```

## Шаги развертывания

### 1. Production-сборка фронтенда

#### На локальной машине или CI/CD:

**Linux/macOS:**
```bash
export VITE_API_URL=https://api.micro-tab.ru:9443
./scripts/build-frontend-static.sh
```

**Windows:**
```powershell
$env:VITE_API_URL="https://api.micro-tab.ru:9443"
.\scripts\build-frontend-static.ps1
```

**Или вручную:**
```bash
cd frontend
export VITE_API_URL=https://api.micro-tab.ru:9443
npm ci
npm run build
```

Результат: статические файлы в `frontend/dist/`

### 2. Подготовка сервера

#### Создайте каталог для статики:

```bash
sudo mkdir -p /var/www/miniapp
sudo chown -R www-data:www-data /var/www/miniapp
sudo chmod -R 755 /var/www/miniapp
```

### 3. Копирование статических файлов на сервер

#### Вариант A: Через SCP

```bash
# С локальной машины
scp -r frontend/dist/* user@server:/var/www/miniapp/
```

#### Вариант B: Через rsync

```bash
rsync -avz --delete frontend/dist/ user@server:/var/www/miniapp/
```

#### Вариант C: Через Git (если dist в .gitignore)

```bash
# На сервере
cd /var/www/miniapp
git pull
cd /path/to/project
npm run build
cp -r frontend/dist/* /var/www/miniapp/
```

### 4. Настройка Nginx

#### Установите конфигурацию:

```bash
# Скопируйте конфигурацию на сервер
sudo cp nginx/conf.d/miniapp-static.conf /etc/nginx/conf.d/

# Или создайте вручную на сервере
sudo nano /etc/nginx/conf.d/miniapp-static.conf
```

#### Убедитесь, что путь к статике правильный:

```nginx
root /var/www/miniapp;
```

#### Проверьте конфигурацию:

```bash
sudo nginx -t
```

#### Перезапустите Nginx:

```bash
sudo systemctl reload nginx
```

### 5. Обновление docker-compose.yml

**ВАЖНО:** Frontend контейнер больше не нужен для production!

#### Вариант A: Закомментировать frontend сервис

В `docker-compose.yml` закомментируйте весь блок `frontend:`:

```yaml
# frontend:
#   build:
#     ...
```

#### Вариант B: Удалить frontend сервис

Удалите весь блок `frontend:` из `docker-compose.yml`.

### 6. Проверка

#### Проверьте доступность:

```bash
curl -I https://miniapp.micro-tab.ru:4443
```

Должен вернуться `200 OK` с `Content-Type: text/html`.

#### Проверьте в браузере:

Откройте `https://miniapp.micro-tab.ru:4443` в браузере - должна загрузиться страница.

#### Проверьте в Telegram:

Откройте Mini App в Telegram - должно работать без ошибок.

## Структура файлов на сервере

```
/var/www/miniapp/
├── index.html
├── assets/
│   ├── index.[hash].js
│   ├── index.[hash].css
│   └── ...
└── ...
```

## Обновление статики

При обновлении фронтенда:

1. Выполните сборку локально или в CI/CD
2. Скопируйте новые файлы на сервер
3. Перезапустите Nginx (если нужно)

```bash
# На сервере
sudo systemctl reload nginx
```

## Устранение проблем

### 502 Bad Gateway

**Причина:** Nginx пытается проксировать на несуществующий порт 3000.

**Решение:** Убедитесь, что используется `miniapp-static.conf`, а не `frontend.conf` с `proxy_pass`.

### 404 Not Found

**Причина:** Неправильный путь к статике или файлы не скопированы.

**Решение:**
1. Проверьте `root /var/www/miniapp;` в nginx конфигурации
2. Убедитесь, что файлы скопированы: `ls -la /var/www/miniapp/`
3. Проверьте права доступа: `sudo chown -R www-data:www-data /var/www/miniapp`

### Белый экран в Telegram

**Причина:** Ошибки JavaScript или неправильные пути к ассетам.

**Решение:**
1. Откройте консоль разработчика в браузере (если возможно)
2. Проверьте логи nginx: `sudo tail -f /var/log/nginx/miniapp_error.log`
3. Убедитесь, что `base: '/'` в `vite.config.js`

## Преимущества статического хостинга

1. ✅ Нет зависимости от Node.js на сервере
2. ✅ Нет dev-серверов и порта 3000
3. ✅ Быстрая загрузка (статический контент)
4. ✅ Меньше потребление ресурсов
5. ✅ Нет 502 ошибок от недоступного dev-сервера
6. ✅ Проще масштабирование (CDN, кеширование)

## Откат к dev-режиму

Если нужно вернуться к dev-режиму:

1. Раскомментируйте `frontend:` в `docker-compose.yml`
2. Используйте `frontend.conf` вместо `miniapp-static.conf`
3. Запустите: `docker compose up -d frontend`

