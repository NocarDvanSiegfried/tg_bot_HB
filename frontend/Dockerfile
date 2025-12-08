FROM node:20-alpine AS base

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

WORKDIR /app

# Copy package files first (for better caching)
COPY package.json package-lock.json* ./

# Install dependencies (including devDependencies for dev mode)
RUN npm ci && npm cache clean --force

# Copy application code
COPY . .

# Create non-root user for security
RUN addgroup -g 1000 appuser 2>/dev/null || true && \
    adduser -D -u 1000 -G appuser appuser 2>/dev/null || true && \
    chown -R appuser:appuser /app 2>/dev/null || true
USER appuser

EXPOSE 3000

CMD ["npm", "run", "dev"]

