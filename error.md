
C:\Users\admin\Desktop\проекты\tg_bot_HB>docker compose up --build
[+] Running 14/14
 ✔ postgres Pulled                                                                                                23.1s
   ✔ 2e6036390374 Pull complete                                                                                    2.8s
   ✔ 95bcad39f7ff Pull complete                                                                                    0.7s
   ✔ 5a19b1f63ace Pull complete                                                                                    5.4s
   ✔ e213bd2560e2 Pull complete                                                                                    2.2s
   ✔ fa51353b2c9b Pull complete                                                                                    2.2s
   ✔ 4eb4a683c389 Pull complete                                                                                    2.2s
   ✔ b10108f2d223 Pull complete                                                                                    2.2s
   ✔ 6e6c09f9e058 Pull complete                                                                                    1.9s
   ✔ b475dc4bba47 Pull complete                                                                                   17.2s
   ✔ 304e9b7c93e6 Pull complete                                                                                    2.2s
   ✔ dd23ed782cae Pull complete                                                                                    2.2s
   ✔ 9fcd228516aa Pull complete                                                                                    5.0s
   ✔ 2c64a0db539b Pull complete                                                                                    2.2s
[+] Building 135.5s (29/29) FINISHED
 => [internal] load local bake definitions                                                                         0.0s
 => => reading from stdin 1.34kB                                                                                   0.0s
 => [frontend internal] load build definition from Dockerfile                                                      0.1s
 => => transferring dockerfile: 3.18kB                                                                             0.0s
 => [backend internal] load build definition from Dockerfile                                                       0.0s
 => => transferring dockerfile: 2.77kB                                                                             0.0s
 => [backend internal] load metadata for docker.io/library/python:3.11-slim                                        5.0s
 => [frontend internal] load metadata for docker.io/library/node:20-alpine                                         5.0s
 => [backend internal] load .dockerignore                                                                          0.0s
 => => transferring context: 665B                                                                                  0.0s
 => ERROR [backend] importing cache manifest from tg_bot_hb-backend:latest                                         2.0s
 => [backend stage-0 1/8] FROM docker.io/library/python:3.11-slim@sha256:193fdd0bbcb3d2ae612bd6cc3548d2f7c78d65b5  7.2s
 => => resolve docker.io/library/python:3.11-slim@sha256:193fdd0bbcb3d2ae612bd6cc3548d2f7c78d65b549fcaa8af75624c4  0.0s
 => => sha256:1771569cc1299abc9cc762fc4419523e721b11a3927ef968ae63ba0a4a88f2da 251B / 251B                         0.7s
 => => extracting sha256:1771569cc1299abc9cc762fc4419523e721b11a3927ef968ae63ba0a4a88f2da                          0.0s
 => => sha256:0e4bc2bd6656e6e004e3c749af70e5650bac2258243eb0949dea51cb8b7863db 29.78MB / 29.78MB                   6.3s
 => [backend internal] load build context                                                                          0.1s
 => => transferring context: 589.47kB                                                                              0.1s
 => [frontend internal] load .dockerignore                                                                         0.1s
 => => transferring context: 545B                                                                                  0.0s
 => ERROR [frontend] importing cache manifest from tg_bot_hb-frontend:latest                                       1.9s
 => [frontend builder 1/5] FROM docker.io/library/node:20-alpine@sha256:643e7036aa985317ebfee460005e322aa550c6b68  2.1s
 => => resolve docker.io/library/node:20-alpine@sha256:643e7036aa985317ebfee460005e322aa550c6b6883000d01daefb5868  0.0s
 => => sha256:34226f5414967f183a8ba2d2a0bf2809b3864182e8f68c07c066fa83f025024a 1.26MB / 1.26MB                     1.9s
 => => extracting sha256:34226f5414967f183a8ba2d2a0bf2809b3864182e8f68c07c066fa83f025024a                          0.0s
 => => extracting sha256:6ac8cc1f0b52065d2132d052abc59bf19e19ac0c65729d4300ab41db30fed855                          0.0s
 => [frontend internal] load build context                                                                         0.1s
 => => transferring context: 158.93kB                                                                              0.0s
 => [backend stage-0 2/8] WORKDIR /app                                                                             0.2s
 => [backend stage-0 3/8] RUN --mount=type=cache,target=/var/cache/apt,sharing=locked     --mount=type=cache,tar  60.6s
 => [frontend builder 2/5] WORKDIR /app                                                                            0.0s
 => [frontend builder 3/5] COPY package.json package-lock.json* ./                                                 0.0s
 => [frontend builder 4/5] RUN --mount=type=cache,target=/root/.npm     npm ci --prefer-offline && npm cache clea  9.0s
 => [frontend builder 5/5] COPY . .                                                                                0.1s
 => [frontend runtime 1/1] RUN addgroup -g 1000 appuser 2>/dev/null || true &&     adduser -D -u 1000 -G appuser   0.3s
 => [frontend] exporting to image                                                                                  5.5s
 => => exporting layers                                                                                            3.8s
 => => preparing layers for inline cache                                                                           0.1s
 => => exporting manifest sha256:2c8de5a0ba20d51c3ddfd10b980d5c35837693825f2f380f528b553dc316ee7f                  0.0s
 => => exporting config sha256:dda47927c42c85beec36daa7e4bb404f24ec948757a512b623ad913a662d6f8a                    0.0s
 => => exporting attestation manifest sha256:ff13f7ceb534fdc539247bfe3684f895be77532bdf062bea94a3f06bc294ca6f      0.0s
 => => exporting manifest list sha256:a42056af33c2e76ce882a15489c4fec0a72c53ff252078387e63de4f20800e79             0.0s
 => => naming to docker.io/library/tg_bot_hb-frontend:latest                                                       0.0s
 => => unpacking to docker.io/library/tg_bot_hb-frontend:latest                                                    1.5s
 => [frontend] resolving provenance for metadata file                                                              0.0s
 => [backend stage-0 4/8] COPY requirements-prod.txt .                                                             0.0s
 => [backend stage-0 5/8] RUN --mount=type=cache,target=/root/.cache/pip     pip install --no-cache-dir --upgrad  49.3s
 => [backend stage-0 6/8] COPY . .                                                                                 0.1s
 => [backend stage-0 7/8] COPY docker-entrypoint.sh /usr/local/bin/                                                0.0s
 => [backend stage-0 8/8] RUN useradd -m -u 1000 appuser &&     chown -R appuser:appuser /app &&     chmod +x /us  0.7s
 => [backend] exporting to image                                                                                  13.7s
 => => exporting layers                                                                                            5.1s
 => => preparing layers for inline cache                                                                           0.1s
 => => exporting manifest sha256:06648e53c4aa3e01715cedb97d3495f2ef8171595a6aa8977ca01eb4fe943978                  0.0s
 => => exporting config sha256:663b8d806e0c0568c2920ba2d982b466a07a65fd3e6f944d482aea12d7b80993                    0.0s
 => => exporting attestation manifest sha256:9f11c6f640fce4d160aef255b3d412763948ee11a2d04c7128549c031595e65c      0.0s
 => => exporting manifest list sha256:57b00475dad7a4d7d193e8fb40e27a3901d271ecbeb1f1a9443c237de36b26d5             0.0s
 => => naming to docker.io/library/tg_bot_hb-backend:latest                                                        0.0s
 => => unpacking to docker.io/library/tg_bot_hb-backend:latest                                                     8.4s
 => [backend] resolving provenance for metadata file                                                               0.0s
------
 > [backend] importing cache manifest from tg_bot_hb-backend:latest:
------
------
 > [frontend] importing cache manifest from tg_bot_hb-frontend:latest:
------
[+] Running 7/7
 ✔ tg_bot_hb-backend               Built                                                                           0.0s
 ✔ tg_bot_hb-frontend              Built                                                                           0.0s
 ✔ Network tg_bot_hb_default       Created                                                                         0.0s
 ✔ Volume tg_bot_hb_postgres_data  Created                                                                         0.0s
 ✔ Container tg_bot_hb-postgres-1  Created                                                                         0.4s
 ✔ Container tg_bot_hb-frontend-1  Created                                                                         1.5s
 ✔ Container tg_bot_hb-backend-1   Created                                                                         0.1s
Attaching to backend-1, frontend-1, postgres-1
postgres-1  | The files belonging to this database system will be owned by user "postgres".
postgres-1  | This user must also own the server process.
postgres-1  |
postgres-1  | The database cluster will be initialized with locale "en_US.utf8".
postgres-1  | The default database encoding has accordingly been set to "UTF8".
postgres-1  | The default text search configuration will be set to "english".
postgres-1  |
postgres-1  | Data page checksums are disabled.
postgres-1  |
postgres-1  | fixing permissions on existing directory /var/lib/postgresql/data ... ok
postgres-1  | creating subdirectories ... ok
postgres-1  | selecting dynamic shared memory implementation ... posix
postgres-1  | selecting default max_connections ... 100
postgres-1  | selecting default shared_buffers ... 128MB
postgres-1  | selecting default time zone ... Etc/UTC
postgres-1  | creating configuration files ... ok
postgres-1  | running bootstrap script ... ok
frontend-1  |
frontend-1  | > telegram-birthday-calendar-frontend@1.0.0 dev
frontend-1  | > vite
frontend-1  |
postgres-1  | performing post-bootstrap initialization ... ok
postgres-1  | initdb: warning: enabling "trust" authentication for local connections
postgres-1  | initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
postgres-1  | syncing data to disk ... ok
postgres-1  |
postgres-1  |
postgres-1  | Success. You can now start the database server using:
postgres-1  |
postgres-1  |     pg_ctl -D /var/lib/postgresql/data -l logfile start
postgres-1  |
postgres-1  | waiting for server to start....2025-12-09 00:01:00.293 UTC [48] LOG:  starting PostgreSQL 15.15 (Debian 15.15-1.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
postgres-1  | 2025-12-09 00:01:00.295 UTC [48] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
postgres-1  | 2025-12-09 00:01:00.300 UTC [51] LOG:  database system was shut down at 2025-12-09 00:01:00 UTC
postgres-1  | 2025-12-09 00:01:00.305 UTC [48] LOG:  database system is ready to accept connections
postgres-1  |  done


postgres-1  | server started
frontend-1  |   VITE v4.5.14  ready in 341 ms

frontend-1  |
frontend-1  |   ➜  Local:   http://localhost:3000/
frontend-1  |   ➜  Network: http://172.18.0.3:3000/
postgres-1  | CREATE DATABASE
postgres-1  |
postgres-1  |
postgres-1  | /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*
postgres-1  |
postgres-1  | waiting for server to shut down....2025-12-09 00:01:00.548 UTC [48] LOG:  received fast shutdown request
postgres-1  | 2025-12-09 00:01:00.550 UTC [48] LOG:  aborting any active transactions
postgres-1  | 2025-12-09 00:01:00.554 UTC [48] LOG:  background worker "logical replication launcher" (PID 54) exited with exit code 1
postgres-1  | 2025-12-09 00:01:00.554 UTC [49] LOG:  shutting down
postgres-1  | 2025-12-09 00:01:00.556 UTC [49] LOG:  checkpoint starting: shutdown immediate
postgres-1  | 2025-12-09 00:01:00.682 UTC [49] LOG:  checkpoint complete: wrote 922 buffers (5.6%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.029 s, sync=0.088 s, total=0.129 s; sync files=301, longest=0.003 s, average=0.001 s; distance=4239 kB, estimate=4239 kB
postgres-1  | 2025-12-09 00:01:00.688 UTC [48] LOG:  database system is shut down
postgres-1  |  done
postgres-1  | server stopped
postgres-1  |
postgres-1  | PostgreSQL init process complete; ready for start up.
postgres-1  |
postgres-1  | 2025-12-09 00:01:00.780 UTC [1] LOG:  starting PostgreSQL 15.15 (Debian 15.15-1.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
postgres-1  | 2025-12-09 00:01:00.781 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
postgres-1  | 2025-12-09 00:01:00.781 UTC [1] LOG:  listening on IPv6 address "::", port 5432
postgres-1  | 2025-12-09 00:01:00.785 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
postgres-1  | 2025-12-09 00:01:00.790 UTC [64] LOG:  database system was shut down at 2025-12-09 00:01:00 UTC
postgres-1  | 2025-12-09 00:01:00.796 UTC [1] LOG:  database system is ready to accept connections
backend-1   | INFO:__main__:DATABASE_URL валиден. База данных: birthday_calendar_db
backend-1   | INFO:__main__:Подключение (замаскировано): postgresql+asyncpg://birthday_user:***@postgres:5432/birthday_calendar_db
backend-1   | INFO:__main__:Подключение к базе данных: postgresql+asyncpg://birthday_user:***@postgres:5432/birthday_calendar_db
backend-1   | INFO:__main__:Имя базы данных: birthday_calendar_db
backend-1   | INFO:     Started server process [16]
backend-1   | INFO:     Waiting for application startup.
backend-1   | INFO:     Application startup complete.
backend-1   | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
backend-1   | INFO:apscheduler.scheduler:Adding job tentatively -- it will be properly scheduled when the scheduler starts
backend-1   | INFO:apscheduler.scheduler:Adding job tentatively -- it will be properly scheduled when the scheduler starts
backend-1   | INFO:apscheduler.scheduler:Adding job tentatively -- it will be properly scheduled when the scheduler starts
backend-1   | INFO:apscheduler.scheduler:Added job "setup_notifications.<locals>.send_today" to job store "default"
backend-1   | INFO:apscheduler.scheduler:Added job "setup_notifications.<locals>.send_week" to job store "default"
backend-1   | INFO:apscheduler.scheduler:Added job "setup_notifications.<locals>.send_month" to job store "default"
backend-1   | INFO:apscheduler.scheduler:Scheduler started
backend-1   | INFO:aiogram.dispatcher:Start polling
backend-1   | INFO:aiogram.dispatcher:Polling stopped
backend-1   | ERROR:    Traceback (most recent call last):
backend-1   |   File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
backend-1   |     return runner.run(main)
backend-1   |            ^^^^^^^^^^^^^^^^
backend-1   |   File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
backend-1   |     return self._loop.run_until_complete(task)
backend-1   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
backend-1   |   File "/usr/local/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
backend-1   |     return future.result()
backend-1   |            ^^^^^^^^^^^^^^^
backend-1   |   File "/app/main.py", line 120, in main
backend-1   |     await asyncio.gather(
backend-1   |   File "/app/main.py", line 86, in start_bot
backend-1   |     await dp.start_polling(bot)
backend-1   |   File "/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/dispatcher.py", line 621, in start_polling
backend-1   |     await asyncio.gather(*done)
backend-1   |   File "/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/dispatcher.py", line 377, in _polling
backend-1   |     user: User = await bot.me()
backend-1   |                  ^^^^^^^^^^^^^^
backend-1   |   File "/usr/local/lib/python3.11/site-packages/aiogram/client/bot.py", line 357, in me
backend-1   |     self._me = await self.get_me()
backend-1   |                ^^^^^^^^^^^^^^^^^^^
backend-1   |   File "/usr/local/lib/python3.11/site-packages/aiogram/client/bot.py", line 1797, in get_me
backend-1   |     return await self(call, request_timeout=request_timeout)
backend-1   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
backend-1   |   File "/usr/local/lib/python3.11/site-packages/aiogram/client/bot.py", line 485, in __call__
backend-1   |     return await self.session(self, method, timeout=request_timeout)
backend-1   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
backend-1   |   File "/usr/local/lib/python3.11/site-packages/aiogram/client/session/base.py", line 259, in __call__
backend-1   |     return cast(TelegramType, await middleware(bot, method))
backend-1   |                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
backend-1   |   File "/usr/local/lib/python3.11/site-packages/aiogram/client/session/aiohttp.py", line 177, in make_request
backend-1   |     response = self.check_response(
backend-1   |                ^^^^^^^^^^^^^^^^^^^^
backend-1   |   File "/usr/local/lib/python3.11/site-packages/aiogram/client/session/base.py", line 127, in check_response
backend-1   |     raise TelegramUnauthorizedError(method=method, message=description)
backend-1   | aiogram.exceptions.TelegramUnauthorizedError: Telegram server says - Unauthorized
backend-1   |
backend-1   | During handling of the above exception, another exception occurred:
backend-1   |
backend-1   | Traceback (most recent call last):
backend-1   |   File "/usr/local/lib/python3.11/site-packages/starlette/routing.py", line 686, in lifespan
backend-1   |     await receive()
backend-1   |   File "/usr/local/lib/python3.11/site-packages/uvicorn/lifespan/on.py", line 137, in receive
backend-1   |     return await self.receive_queue.get()
backend-1   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
backend-1   |   File "/usr/local/lib/python3.11/asyncio/queues.py", line 158, in get
backend-1   |     await getter
backend-1   | asyncio.exceptions.CancelledError
backend-1   |
backend-1   | Traceback (most recent call last):
backend-1   |   File "/app/main.py", line 127, in <module>
backend-1   |     asyncio.run(main())
backend-1   |   File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
backend-1   |     return runner.run(main)
backend-1   |            ^^^^^^^^^^^^^^^^
backend-1   |   File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
backend-1   |     return self._loop.run_until_complete(task)
backend-1   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
backend-1   |   File "/usr/local/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
backend-1   |     return future.result()
backend-1   |            ^^^^^^^^^^^^^^^
backend-1   |   File "/app/main.py", line 120, in main
backend-1   |     await asyncio.gather(
backend-1   |   File "/app/main.py", line 86, in start_bot
backend-1   |     await dp.start_polling(bot)
backend-1   |   File "/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/dispatcher.py", line 621, in start_polling
backend-1   |     await asyncio.gather(*done)
backend-1   |   File "/usr/local/lib/python3.11/site-packages/aiogram/dispatcher/dispatcher.py", line 377, in _polling
backend-1   |     user: User = await bot.me()
backend-1   |                  ^^^^^^^^^^^^^^
backend-1   |   File "/usr/local/lib/python3.11/site-packages/aiogram/client/bot.py", line 357, in me
backend-1   |     self._me = await self.get_me()
backend-1   |                ^^^^^^^^^^^^^^^^^^^
backend-1   |   File "/usr/local/lib/python3.11/site-packages/aiogram/client/bot.py", line 1797, in get_me
backend-1   |     return await self(call, request_timeout=request_timeout)
backend-1   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
backend-1   |   File "/usr/local/lib/python3.11/site-packages/aiogram/client/bot.py", line 485, in __call__
backend-1   |     return await self.session(self, method, timeout=request_timeout)
backend-1   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
backend-1   |   File "/usr/local/lib/python3.11/site-packages/aiogram/client/session/base.py", line 259, in __call__
backend-1   |     return cast(TelegramType, await middleware(bot, method))
backend-1   |                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
backend-1   |   File "/usr/local/lib/python3.11/site-packages/aiogram/client/session/aiohttp.py", line 177, in make_request
backend-1   |     response = self.check_response(
backend-1   |                ^^^^^^^^^^^^^^^^^^^^
backend-1   |   File "/usr/local/lib/python3.11/site-packages/aiogram/client/session/base.py", line 127, in check_response
backend-1   |     raise TelegramUnauthorizedError(method=method, message=description)
backend-1   | aiogram.exceptions.TelegramUnauthorizedError: Telegram server says - Unauthorized
backend-1 exited with code 1