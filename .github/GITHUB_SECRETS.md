# GitHub Secrets Configuration

Данный документ описывает необходимые секреты для GitHub Actions workflows.

## Обязательные секреты

### Для сборки и публикации Docker образов

Эти секреты используются в workflow `build.yml`:

- **Не требуются** - GitHub Actions автоматически использует `GITHUB_TOKEN` для публикации в GitHub Container Registry (ghcr.io)

Если вы хотите использовать Docker Hub вместо GHCR:

- `DOCKER_USERNAME` - ваш логин в Docker Hub
- `DOCKER_PASSWORD` - ваш пароль или токен доступа Docker Hub

### Для тестирования (опционально)

Эти секреты могут использоваться для интеграционных тестов:

- `TELEGRAM_BOT_TOKEN` - токен Telegram бота (для тестов с реальным API)
- `OPENROUTER_API_KEY` - API ключ OpenRouter (для тестов генерации поздравлений)

**Примечание:** В большинстве случаев тесты используют моки, поэтому эти секреты не обязательны.

## Секреты для деплоя

Эти секреты используются в workflow `deploy.yml`:

### Обязательные для деплоя:

- `DEPLOY_HOST` - IP адрес или домен сервера (например: `192.168.1.100` или `example.com`)
- `DEPLOY_USER` - имя пользователя для SSH подключения (например: `deploy` или `ubuntu`)
- `DEPLOY_SSH_KEY` - приватный SSH ключ для подключения к серверу
- `DEPLOY_PATH` - путь на сервере, где находится проект (например: `/var/www/birthday-calendar`)

## Как добавить секреты в GitHub

1. Перейдите в ваш репозиторий на GitHub
2. Откройте **Settings** → **Secrets and variables** → **Actions**
3. Нажмите **New repository secret**
4. Введите имя секрета (например: `DEPLOY_HOST`)
5. Введите значение секрета
6. Нажмите **Add secret**

## Создание SSH ключа для деплоя

Если у вас еще нет SSH ключа для деплоя:

```bash
# Генерация нового SSH ключа
ssh-keygen -t ed25519 -C "github-actions-deploy" -f ~/.ssh/github_deploy

# Скопируйте публичный ключ на сервер
ssh-copy-id -i ~/.ssh/github_deploy.pub user@your-server.com

# Скопируйте приватный ключ в GitHub Secrets как DEPLOY_SSH_KEY
cat ~/.ssh/github_deploy
```

## Настройка окружений (Environments)

Для разделения staging и production:

1. Перейдите в **Settings** → **Environments**
2. Создайте окружения: `staging` и `production`
3. Добавьте секреты для каждого окружения отдельно
4. Настройте правила защиты (protection rules) для production

## Пример конфигурации

### Минимальная конфигурация (без деплоя)

Никаких секретов не требуется - все workflows будут работать с публичными действиями.

### Конфигурация с деплоем

```yaml
# Secrets для деплоя
DEPLOY_HOST: "example.com"
DEPLOY_USER: "deploy"
DEPLOY_SSH_KEY: "-----BEGIN OPENSSH PRIVATE KEY-----\n..."
DEPLOY_PATH: "/var/www/birthday-calendar"
```

### Конфигурация с Docker Hub

```yaml
DOCKER_USERNAME: "your-dockerhub-username"
DOCKER_PASSWORD: "your-dockerhub-token"
```

## Безопасность

- **Никогда** не коммитьте секреты в репозиторий
- Используйте разные ключи для разных окружений
- Регулярно ротируйте (меняйте) секреты
- Используйте минимальные права доступа для токенов
- Для production используйте защищенные окружения с required reviewers

## Проверка секретов

После добавления секретов, проверьте что workflows могут их использовать:

1. Запустите workflow вручную через **Actions** → **Run workflow**
2. Проверьте логи выполнения
3. Убедитесь, что секреты правильно подставляются (значения не отображаются в логах)

## Troubleshooting

### Ошибка: "Secret not found"

- Убедитесь, что секрет добавлен в правильный scope (repository или environment)
- Проверьте правильность написания имени секрета (чувствительно к регистру)

### Ошибка SSH подключения

- Проверьте, что `DEPLOY_SSH_KEY` содержит полный приватный ключ включая заголовки
- Убедитесь, что публичный ключ добавлен в `~/.ssh/authorized_keys` на сервере
- Проверьте права доступа на сервере

### Ошибка доступа к Docker Registry

- Проверьте правильность `DOCKER_USERNAME` и `DOCKER_PASSWORD`
- Убедитесь, что токен имеет права на push в репозиторий

