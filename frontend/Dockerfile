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
# Build mode: dev or production (default: dev)
ARG FRONTEND_MODE=dev

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

# Build stage
# 
# DEVELOPMENT MODE (FRONTEND_MODE=dev):
#   - Uses Vite dev server directly
#   - Hot module replacement enabled
#   - All devDependencies included
#   - Command: npm run dev
#
# PRODUCTION MODE (FRONTEND_MODE=production):
#   - Builds static assets
#   - Uses nginx to serve static files
#   - Smaller image size, better performance
#
RUN if [ "$FRONTEND_MODE" = "production" ]; then \
        npm run build; \
    fi

# Stage 2: Production runtime (nginx)
FROM nginx:alpine AS runtime-prod
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]

# Stage 3: Development runtime (Vite dev server)
FROM builder AS runtime-dev
EXPOSE 3000
CMD ["npm", "run", "dev"]

# Stage 4: Default runtime (dev mode for backward compatibility)
# Docker Compose will use --target to select the correct stage:
#   - For production: target: runtime-prod
#   - For dev: target: runtime-dev (default)
FROM runtime-dev AS runtime
