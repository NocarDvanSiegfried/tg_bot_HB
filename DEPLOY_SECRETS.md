# Документация по настройке секретов для деплоя

## Обзор

Этот документ описывает, какие секреты необходимы для деплоя проекта и как их настроить в GitHub Secrets.

## Необходимые секреты

### 1. DEPLOY_HOST
- **Описание**: IP-адрес или доменное имя сервера для деплоя
- **Пример**: `192.168.1.100` или `deploy.example.com`
- **Где получить**: У вашего хостинг-провайдера или в настройках сервера

### 2. DEPLOY_USER
- **Описание**: Имя пользователя для SSH-подключения к серверу
- **Пример**: `deploy` или `ubuntu`
- **Где получить**: Создайте пользователя на сервере или используйте существующего

### 3. DEPLOY_PATH
- **Описание**: Путь на сервере, куда будет развернут проект
- **Пример**: `/var/www/tg_bot_HB` или `/home/deploy/app`
- **Где получить**: Выберите подходящий путь на сервере

### 4. DEPLOY_SSH_KEY
- **Описание**: Приватный SSH-ключ для подключения к серверу
- **Пример**: Содержимое файла `~/.ssh/id_rsa` или `~/.ssh/id_ed25519`
- **Где получить**: 
  1. Сгенерируйте SSH-ключ на вашем локальном компьютере:
     ```bash
     ssh-keygen -t ed25519 -C "github-actions"
     ```
  2. Скопируйте публичный ключ на сервер:
     ```bash
     ssh-copy-id -i ~/.ssh/id_ed25519.pub deploy@your-server
     ```
  3. Скопируйте приватный ключ (содержимое `~/.ssh/id_ed25519`) в GitHub Secrets

## Как добавить секреты в GitHub Secrets

1. Перейдите в репозиторий на GitHub
2. Откройте **Settings** → **Secrets and variables** → **Actions**
3. Нажмите **New repository secret**
4. Введите имя секрета (например, `DEPLOY_HOST`)
5. Введите значение секрета
6. Нажмите **Add secret**
7. Повторите для всех необходимых секретов

## Примеры конфигурации

### Для одного сервера

```
DEPLOY_HOST=192.168.1.100
DEPLOY_USER=deploy
DEPLOY_PATH=/var/www/tg_bot_HB
DEPLOY_SSH_KEY=<содержимое приватного ключа>
```

### Для нескольких серверов (staging и production)

Для staging:
```
DEPLOY_HOST_STAGING=staging.example.com
DEPLOY_USER_STAGING=deploy
DEPLOY_PATH_STAGING=/var/www/tg_bot_HB_staging
DEPLOY_SSH_KEY_STAGING=<содержимое приватного ключа для staging>
```

Для production:
```
DEPLOY_HOST_PRODUCTION=production.example.com
DEPLOY_USER_PRODUCTION=deploy
DEPLOY_PATH_PRODUCTION=/var/www/tg_bot_HB_production
DEPLOY_SSH_KEY_PRODUCTION=<содержимое приватного ключа для production>
```

## Безопасность

- **Никогда не коммитьте секреты в репозиторий**
- Используйте разные SSH-ключи для разных серверов
- Регулярно ротируйте SSH-ключи
- Ограничьте права доступа SSH-ключей на сервере
- Используйте отдельные пользователи для деплоя (не root)

## Проверка подключения

Перед добавлением секретов в GitHub, проверьте подключение:

```bash
ssh -i ~/.ssh/id_ed25519 deploy@your-server
```

Если подключение успешно, секреты настроены правильно.

## Troubleshooting

### Ошибка "Permission denied (publickey)"
- Убедитесь, что публичный ключ добавлен на сервер
- Проверьте права доступа к приватному ключу: `chmod 600 ~/.ssh/id_ed25519`

### Ошибка "Host key verification failed"
- Добавьте сервер в known_hosts: `ssh-keyscan your-server >> ~/.ssh/known_hosts`

### Ошибка "Connection refused"
- Проверьте, что SSH-сервер запущен на сервере
- Проверьте firewall настройки

