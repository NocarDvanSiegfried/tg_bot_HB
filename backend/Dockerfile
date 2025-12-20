# Если возникают проблемы с загрузкой образа python:3.11-slim (TLS handshake timeout):
#
# Вариант 1: Использовать альтернативный тег (раскомментируйте нужную строку)
#   FROM python:3.11          # Полный образ (больше размер, но может быть доступен)
#   FROM python:slim          # Последняя версия slim
#
# Вариант 2: Использовать локальный образ (если уже загружен)
#   Запустите: docker compose build --pull=never
#
# Вариант 3: Предварительно загрузить образ
#   Windows: .\scripts\download-all-images.ps1
#   Linux/macOS: ./scripts/download-all-images.sh

# Используем последнюю версию python:3.11-slim для получения обновлений безопасности
FROM python:3.11-slim-bookworm

# Build arguments for metadata
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

# Labels for metadata
LABEL org.opencontainers.image.created="$BUILD_DATE" \
      org.opencontainers.image.revision="$VCS_REF" \
      org.opencontainers.image.version="$VERSION" \
      org.opencontainers.image.title="Telegram Birthday Calendar Backend" \
      org.opencontainers.image.description="Backend service for Telegram Birthday Calendar Mini App"

WORKDIR /app

# Install system dependencies with BuildKit cache mounts for faster rebuilds
# Обновляем системные пакеты для устранения уязвимостей безопасности
# Критичные пакеты (CRITICAL): libsqlite3-0 (CVE-2025-7458), zlib1g (CVE-2023-45853)
# Высокие уязвимости (HIGH): libpam-* (CVE-2025-6020) - обновляются через apt-get upgrade
# Средние уязвимости (MEDIUM): util-linux (CVE-2025-14104), gpgv (CVE-2025-30258),
#   ncurses (CVE-2023-50495), libsqlite3-0 (CVE-2025-7709) - обновляются через apt-get upgrade
# Неизвестные уязвимости (UNKNOWN): libgnutls30 (CVE-2025-9820) - обновляются через apt-get upgrade
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copy and install Python dependencies first (for better caching)
# Using production requirements only to reduce image size and build time
# BuildKit cache mount ускоряет повторные сборки на 30-50%
COPY requirements-prod.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements-prod.txt

# Copy application code
COPY . .

# Copy entrypoint script before user creation
COPY docker-entrypoint.sh /usr/local/bin/

# Create non-root user and set permissions in single layer
# This reduces image layers and improves build performance
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app && \
    chmod +x /usr/local/bin/docker-entrypoint.sh

# Используем entrypoint для создания пользователя при запуске
# Это необходимо при использовании volume монтирования
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

CMD ["python", "main.py"]

