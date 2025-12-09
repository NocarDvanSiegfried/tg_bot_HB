C:\Users\admin\Desktop\проекты\tg_bot_HB>docker compose up --build
[+] Building 5.4s (27/27) FINISHED
 => [internal] load local bake definitions                                                                         0.0s
 => => reading from stdin 1.21kB                                                                                   0.0s
 => [frontend internal] load build definition from Dockerfile                                                      0.0s
 => => transferring dockerfile: 3.18kB                                                                             0.0s
 => [backend internal] load build definition from Dockerfile                                                       0.0s
 => => transferring dockerfile: 2.77kB                                                                             0.0s
 => [frontend internal] load metadata for docker.io/library/node:20-alpine                                         3.8s
 => [backend internal] load metadata for docker.io/library/python:3.11-slim                                        3.8s
 => [frontend internal] load .dockerignore                                                                         0.0s
 => => transferring context: 545B                                                                                  0.0s
 => [backend internal] load .dockerignore                                                                          0.0s
 => => transferring context: 665B                                                                                  0.0s
 => [frontend builder 1/5] FROM docker.io/library/node:20-alpine@sha256:643e7036aa985317ebfee460005e322aa550c6b68  0.0s
 => => resolve docker.io/library/node:20-alpine@sha256:643e7036aa985317ebfee460005e322aa550c6b6883000d01daefb5868  0.0s
 => [frontend internal] load build context                                                                         0.0s
 => => transferring context: 3.15kB                                                                                0.0s
 => [backend stage-0 1/8] FROM docker.io/library/python:3.11-slim@sha256:7cd0079a9bd8800c81632d65251048fc2848bf9a  0.0s
 => => resolve docker.io/library/python:3.11-slim@sha256:7cd0079a9bd8800c81632d65251048fc2848bf9afda542224b1b10e0  0.0s
 => [backend internal] load build context                                                                          0.1s
 => => transferring context: 46.49kB                                                                               0.0s
 => CACHED [frontend builder 2/5] WORKDIR /app                                                                     0.0s
 => CACHED [frontend builder 3/5] COPY package.json package-lock.json* ./                                          0.0s
 => CACHED [frontend builder 4/5] RUN --mount=type=cache,target=/root/.npm     npm ci --prefer-offline && npm cac  0.0s
 => CACHED [frontend builder 5/5] COPY . .                                                                         0.0s
 => CACHED [frontend runtime 1/1] RUN addgroup -g 1000 appuser 2>/dev/null || true &&     adduser -D -u 1000 -G a  0.0s
 => [frontend] exporting to image                                                                                  0.2s
 => => exporting layers                                                                                            0.0s
 => => preparing layers for inline cache                                                                           0.1s
 => => exporting manifest sha256:f5f674901d8d20a186e124df2cf5e5ca233c6cbea2bfb1e28423efbf27fa6411                  0.0s
 => => exporting config sha256:9319bda5384e465466d9c2f9759a02170027131ea9faf2e4a9f718250fe0c7a3                    0.0s
 => => exporting attestation manifest sha256:51492b2897b014cb0ee24c5b69696a1e5fab3972b6a8aec78210f8f9eea0ce04      0.0s
 => => exporting manifest list sha256:f16407a57a8c0e34b74b52147baf48f0a16baa656c5b9c5a5aad9d8c9f467361             0.0s
 => => naming to docker.io/library/tg_bot_hb-frontend:latest                                                       0.0s
 => => unpacking to docker.io/library/tg_bot_hb-frontend:latest                                                    0.0s
 => CACHED [backend stage-0 2/8] WORKDIR /app                                                                      0.0s
 => CACHED [backend stage-0 3/8] RUN --mount=type=cache,target=/var/cache/apt,sharing=locked     --mount=type=cac  0.0s
 => CACHED [backend stage-0 4/8] COPY requirements-prod.txt .                                                      0.0s
 => CACHED [backend stage-0 5/8] RUN --mount=type=cache,target=/root/.cache/pip     pip install --no-cache-dir --  0.0s
 => [backend stage-0 6/8] COPY . .                                                                                 0.1s
 => [backend stage-0 7/8] COPY docker-entrypoint.sh /usr/local/bin/                                                0.1s
 => [backend stage-0 8/8] RUN useradd -m -u 1000 appuser &&     chown -R appuser:appuser /app &&     chmod +x /us  0.7s
 => [frontend] resolving provenance for metadata file                                                              0.0s
 => [backend] exporting to image                                                                                   0.4s
 => => exporting layers                                                                                            0.1s
 => => preparing layers for inline cache                                                                           0.1s
 => => exporting manifest sha256:c38e58a8b25caafc566d4a382a0e65eeb5d0e556009264a97f07cb3ae8e25387                  0.0s
 => => exporting config sha256:d3755d34a991ad67a686aded688c03b9e44ccc1b843629d0b3d6e40387ade480                    0.0s
 => => exporting attestation manifest sha256:e3fcb9c853111e58ebd9ee256d82704da20daeaa2c3a1c7774a4330a1d807caf      0.0s
 => => exporting manifest list sha256:7d8532d4c78224afdd82e482cb12072e31488b5547adee88bc4b964bf1fbb301             0.0s
 => => naming to docker.io/library/tg_bot_hb-backend:latest                                                        0.0s
 => => unpacking to docker.io/library/tg_bot_hb-backend:latest                                                     0.1s
 => [backend] resolving provenance for metadata file                                                               0.0s
[+] Running 6/6
 ✔ tg_bot_hb-backend               Built                                                                           0.0s
 ✔ tg_bot_hb-frontend              Built                                                                           0.0s
 ✔ Network tg_bot_hb_default       Created                                                                         0.0s
 ✔ Container tg_bot_hb-frontend-1  Created                                                                         1.7s
 ✔ Container tg_bot_hb-postgres-1  Created                                                                         0.1s
 ✔ Container tg_bot_hb-backend-1   Created                                                                         0.1s
Attaching to backend-1, frontend-1, postgres-1
postgres-1  |
postgres-1  | PostgreSQL Database directory appears to contain a database; Skipping initialization
postgres-1  |
postgres-1  | 2025-12-09 18:33:41.013 UTC [1] LOG:  starting PostgreSQL 15.15 (Debian 15.15-1.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
postgres-1  | 2025-12-09 18:33:41.028 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
postgres-1  | 2025-12-09 18:33:41.028 UTC [1] LOG:  listening on IPv6 address "::", port 5432
postgres-1  | 2025-12-09 18:33:41.032 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
postgres-1  | 2025-12-09 18:33:41.038 UTC [30] LOG:  database system was shut down at 2025-12-09 18:31:18 UTC
postgres-1  | 2025-12-09 18:33:41.045 UTC [1] LOG:  database system is ready to accept connections
frontend-1  |
frontend-1  | > telegram-birthday-calendar-frontend@1.0.0 dev
frontend-1  | > vite
frontend-1  |
frontend-1  |
frontend-1  |   VITE v4.5.14  ready in 359 ms
frontend-1  |
frontend-1  |   ➜  Local:   http://localhost:3000/
frontend-1  |   ➜  Network: http://172.18.0.3:3000/
backend-1   | Traceback (most recent call last):
backend-1   |   File "/app/main.py", line 24, in <module>
backend-1   |     from src.presentation.web.app import app as web_app
backend-1   |   File "/app/src/presentation/web/app.py", line 10, in <module>
backend-1   |     from src.presentation.web.routes.api import router
backend-1   |   File "/app/src/presentation/web/routes/api.py", line 20, in <module>
backend-1   |     from src.presentation.web.decorators import handle_api_errors
backend-1   |   File "/app/src/presentation/web/decorators.py", line 10, in <module>
backend-1   |     from src.domain.exceptions.api_exceptions import (
backend-1   | ImportError: cannot import name 'OpenRouterRateLimitError' from 'src.domain.exceptions.api_exceptions' (/app/src/domain/exceptions/api_exceptions.py)
backend-1 exited with code 1