# Multi-stage build for optimized production image
#
# Если возникают проблемы с загрузкой образа node:20-alpine (TLS handshake timeout):
# 
# Вариант 1: Использовать альтернативный тег (раскомментируйте нужную строку)
#   FROM node:20 AS builder          # Полный образ (больше размер, но может быть доступен)
#   FROM node:alpine AS builder       # Последняя версия alpine
#
# Вариант 2: Использовать локальный образ (если уже загружен)
#   Запустите: docker compose build --pull=never
#
# Вариант 3: Предварительно загрузить образ
#   Windows: .\scripts\download-all-images.ps1
#   Linux/macOS: ./scripts/download-all-images.sh

# Stage 1: Builder - install all dependencies and build
FROM node:20-alpine AS builder

# Build arguments for metadata
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

# Labels for metadata
LABEL org.opencontainers.image.created="$BUILD_DATE" \
      org.opencontainers.image.revision="$VCS_REF" \
      org.opencontainers.image.version="$VERSION" \
      org.opencontainers.image.title="Telegram Birthday Calendar Frontend Builder" \
      org.opencontainers.image.description="Builder stage for Frontend service"

WORKDIR /app

# Copy package files first (for better caching)
COPY package.json package-lock.json* ./

# Install all dependencies (including devDependencies for build)
# BuildKit cache mount ускоряет повторные сборки на 30-50%
RUN --mount=type=cache,target=/root/.npm \
    npm ci --prefer-offline && npm cache clean --force

# Copy application code
COPY . .

# Note: For dev mode, we use vite dev server directly
# For production build, uncomment: RUN npm run build

# Stage 2: Runtime - use builder for dev mode (needs devDependencies for vite dev server)
# For production, this would use --only=production, but for dev mode we need all deps
FROM builder AS runtime

# Build arguments for metadata
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

# Labels for metadata
LABEL org.opencontainers.image.created="$BUILD_DATE" \
      org.opencontainers.image.revision="$VCS_REF" \
      org.opencontainers.image.version="$VERSION" \
      org.opencontainers.image.title="Telegram Birthday Calendar Frontend" \
      org.opencontainers.image.description="Frontend service for Telegram Birthday Calendar Mini App"

# Create non-root user for security (for production builds)
# For dev mode with volume mounts, we skip USER directive to avoid permission issues
# Volume mounts can overwrite permissions, so running as root in dev is acceptable
RUN addgroup -g 1000 appuser 2>/dev/null || true && \
    adduser -D -u 1000 -G appuser appuser 2>/dev/null || true

# For development mode: run as root to avoid volume mount permission issues
# For production: uncomment the line below and ensure proper file permissions
# USER appuser

EXPOSE 3000

CMD ["npm", "run", "dev"]
