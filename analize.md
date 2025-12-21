.env
TELEGRAM_BOT_TOKEN=84665**************************
POSTGRES_USER=birthday_user
POSTGRES_PASSWORD=secure_password_2024
POSTGRES_DB=birthday_calendar_db
DATABASE_URL=postgresql+asyncpg://birthday_user:secure_password_2024@postgres:5432/birthday_calendar_db
OPENROUTER_API_KEY=sk-or-v1-8e8c2***************************
OPENROUTER_REFERER=https://micro-tab.ru
OPENROUTER_MODEL=tng/deepseek-r1t2-chimera
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_TIMEOUT=30.0
WEB_PORT=8000
API_HOST=0.0.0.0
VITE_API_URL=https://api.micro-tab.ru:9443
TELEGRAM_WEBAPP_URL=https://miniapp.micro-tab.ru:4443
TIMEZONE=Asia/Tokyo
NOTIFICATION_HOUR=9
NOTIFICATION_MINUTE=0
ENVIRONMENT=production
DEBUG=false
ALLOWED_ORIGINS=https://micro-tab.ru,https://web.telegram.org,https://telegram.org,https://miniapp.micro-tab.ru:4443

CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS                   PORTS                                         NAMES
bda732965c7c   tg_bot_hb-backend    "/usr/local/bin/dock…"   5 minutes ago   Up 5 minutes             0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   tg_bot_hb-backend-1
fbac77b7c2ec   postgres:15          "docker-entrypoint.s…"   5 minutes ago   Up 5 minutes (healthy)   0.0.0.0:5432->5432/tcp, [::]:5432->5432/tcp   tg_bot_hb-postgres-1
fb24e93aff27   d1befb6295d5         "gunicorn --config g…"   2 weeks ago     Up 2 weeks (healthy)     127.0.0.1:5000->5000/tcp                      workflowgenius-backend
fefbbfd09f92   postgres:15-alpine   "docker-entrypoint.s…"   2 weeks ago     Up 2 weeks (healthy)     5432/tcp                                      workflowgenius-postgres

root@server-cqfsqu:~/tg_bot_HB#    docker compose logs backend --tail 100
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 1.305342 seconds and try again... (tryings = 1, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 1.699399 seconds and try again... (tryings = 2, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 2.286007 seconds and try again... (tryings = 3, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 3.165626 seconds and try again... (tryings = 4, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.141736 seconds and try again... (tryings = 5, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.040496 seconds and try again... (tryings = 6, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.065852 seconds and try again... (tryings = 7, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.947325 seconds and try again... (tryings = 8, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.115690 seconds and try again... (tryings = 9, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.169757 seconds and try again... (tryings = 10, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.993618 seconds and try again... (tryings = 11, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.020946 seconds and try again... (tryings = 12, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.059103 seconds and try again... (tryings = 13, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.946079 seconds and try again... (tryings = 14, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.005024 seconds and try again... (tryings = 15, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.987617 seconds and try again... (tryings = 16, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.870407 seconds and try again... (tryings = 17, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.112717 seconds and try again... (tryings = 18, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.898537 seconds and try again... (tryings = 19, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.048135 seconds and try again... (tryings = 20, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.050844 seconds and try again... (tryings = 21, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.043585 seconds and try again... (tryings = 22, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.627458 seconds and try again... (tryings = 23, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.969688 seconds and try again... (tryings = 24, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.862819 seconds and try again... (tryings = 25, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.041034 seconds and try again... (tryings = 26, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.079916 seconds and try again... (tryings = 27, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.003744 seconds and try again... (tryings = 28, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.082285 seconds and try again... (tryings = 29, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.993575 seconds and try again... (tryings = 30, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.907644 seconds and try again... (tryings = 31, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.080079 seconds and try again... (tryings = 32, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.959694 seconds and try again... (tryings = 33, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.902405 seconds and try again... (tryings = 34, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.956418 seconds and try again... (tryings = 35, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.112730 seconds and try again... (tryings = 36, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.034993 seconds and try again... (tryings = 37, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.000420 seconds and try again... (tryings = 38, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.808700 seconds and try again... (tryings = 39, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.144321 seconds and try again... (tryings = 40, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.127913 seconds and try again... (tryings = 41, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.144692 seconds and try again... (tryings = 42, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.114505 seconds and try again... (tryings = 43, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.826315 seconds and try again... (tryings = 44, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.849748 seconds and try again... (tryings = 45, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.884563 seconds and try again... (tryings = 46, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.985367 seconds and try again... (tryings = 47, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 5.104372 seconds and try again... (tryings = 48, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.986499 seconds and try again... (tryings = 49, bot id = 8466582536)
backend-1  | ERROR:aiogram.dispatcher:Failed to fetch updates - TelegramConflictError: Telegram server says - Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
backend-1  | WARNING:aiogram.dispatcher:Sleep for 4.879279 seconds and try again... (tryings = 50, bot id = 8466582536)
root@server-cqfsqu:~/tg_bot_HB#    curl http://localhost:8000/health
root@server-cqfsqu:~/tg_bot_HB#    # Linux/macOSndar API","message":"API is running"}root@server-cqfsqu:~/tg_bot_HB#    # Linux/macOS
   netstat -tuln | grep 8000
   
   # Windows
   netstat -an | findstr 8000
tcp        0      0 0.0.0.0:8000            0.0.0.0:*               LISTEN     
tcp6       0      0 :::8000                 :::*                    LISTEN     
-bash: findstr: command not found
root@server-cqfsqu:~/tg_bot_HB#    # Linux/macOS
   netstat -tuln | grep 8000
   
   # Windows
   netstat -an | findstr 8000
tcp        0      0 0.0.0.0:8000            0.0.0.0:*               LISTEN     
tcp6       0      0 :::8000                 :::*                    LISTEN     
-bash: findstr: command not found

 docker ps | grep nginx
   systemctl status nginx
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled; preset: 
enabled)
     Active: active (running) since Fri 2025-12-12 00:57:33 UTC; 1 week 2 days ago
       Docs: man:nginx(8)
   Main PID: 3388584 (nginx)
      Tasks: 2 (limit: 2287)
     Memory: 7.6M (peak: 13.4M)
        CPU: 26.405s
     CGroup: /system.slice/nginx.service
             ├─3388584 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             └─3392344 "nginx: worker process"

Dec 12 00:57:33 server-cqfsqu systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Dec 12 00:57:33 server-cqfsqu systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
root@server-cqfsqu:~/tg_bot_HB#    tail -50 /var/log/nginx/backend_error.log
   tail -50 /var/log/nginx/error.log
2025/12/10 21:03:27 [error] 2862462#2862462: *4343 connect() failed (111: Connection refused) while connecting to upstream, client: 160.224.51.11, server: api.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:8000/", host: "api.micro-tab.ru:3001"
2025/12/10 21:03:27 [error] 2862462#2862462: *4346 connect() failed (111: Connection refused) while connecting to upstream, client: 160.224.51.11, server: api.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:8000/", host: "api.micro-tab.ru:3001"
2025/12/10 21:44:42 [error] 2886856#2886856: *4385 connect() failed (111: Connection refused) while connecting to upstream, client: 193.142.147.209, server: api.micro-tab.ru, request: "GET /cgi-bin/luci/;stok=/locale HTTP/1.1", upstream: "http://127.0.0.1:8000/cgi-bin/luci/;stok=/locale", host: "31.56.28.232:3001", referrer: "http://31.56.28.232:80/cgi-bin/luci/;stok=/locale"
2025/12/10 21:51:47 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:8000/", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:48 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:8000//wp-includes/wlwmanifest.xml", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:48 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //xmlrpc.php?rsd HTTP/1.1", upstream: "http://127.0.0.1:8000//xmlrpc.php?rsd", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:48 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:8000/", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:48 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //blog/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:8000//blog/wp-includes/wlwmanifest.xml", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:48 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //web/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:8000//web/wp-includes/wlwmanifest.xml", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:48 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //wordpress/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:8000//wordpress/wp-includes/wlwmanifest.xml", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:48 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //website/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:8000//website/wp-includes/wlwmanifest.xml", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:48 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //wp/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:8000//wp/wp-includes/wlwmanifest.xml", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:49 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //news/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:8000//news/wp-includes/wlwmanifest.xml", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:49 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //2018/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:8000//2018/wp-includes/wlwmanifest.xml", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:49 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //2019/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:8000//2019/wp-includes/wlwmanifest.xml", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:49 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //shop/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:8000//shop/wp-includes/wlwmanifest.xml", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:49 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //wp1/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:8000//wp1/wp-includes/wlwmanifest.xml", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:49 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //test/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:8000//test/wp-includes/wlwmanifest.xml", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:49 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //media/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:8000//media/wp-includes/wlwmanifest.xml", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:50 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //wp2/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:8000//wp2/wp-includes/wlwmanifest.xml", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:50 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //site/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:8000//site/wp-includes/wlwmanifest.xml", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:50 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //cms/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:8000//cms/wp-includes/wlwmanifest.xml", host: "api.micro-tab.ru:3001"
2025/12/10 21:51:50 [error] 2886856#2886856: *4452 connect() failed (111: Connection refused) while connecting to upstream, client: 208.84.102.244, server: api.micro-tab.ru, request: "GET //sito/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:8000//sito/wp-includes/wlwmanifest.xml", host: "api.micro-tab.ru:3001"
2025/12/10 22:58:11 [error] 2886856#2886856: *4489 connect() failed (111: Connection refused) while connecting to upstream, client: 35.203.210.144, server: api.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:8000/", host: "31.56.28.232:3001", referrer: "http://31.56.28.232:80/"
2025/12/10 23:07:53 [error] 2886856#2886856: *4507 connect() failed (111: Connection refused) while connecting to upstream, client: 199.45.155.101, server: api.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:8000/", host: "31.56.28.232:3001"
2025/12/10 23:08:05 [error] 2886856#2886856: *4509 connect() failed (111: Connection refused) while connecting to upstream, client: 199.45.155.101, server: api.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:8000/", host: "31.56.28.232:3001"
2025/12/10 23:08:23 [error] 2886856#2886856: *4516 connect() failed (111: Connection refused) while connecting to upstream, client: 199.45.155.101, server: api.micro-tab.ru, request: "GET /.well-known/security.txt HTTP/1.1", upstream: "http://127.0.0.1:8000/.well-known/security.txt", host: "31.56.28.232:3001"
2025/12/10 23:51:07 [error] 2886856#2886856: *4536 connect() failed (111: Connection refused) while connecting to upstream, client: 193.142.147.209, server: api.micro-tab.ru, request: "GET /cgi-bin/luci/;stok=/locale HTTP/1.1", upstream: "http://127.0.0.1:8000/cgi-bin/luci/;stok=/locale", host: "31.56.28.232:3001", referrer: "http://31.56.28.232:80/cgi-bin/luci/;stok=/locale"
2025/12/12 02:27:14 [error] 3392344#3392344: *1199 connect() failed (111: Connection refused) while connecting to upstream, client: 65.87.7.112, server: micro-tab.ru, request: "HEAD / HTTP/1.1", upstream: "http://127.0.0.1:3000/", host: "micro-tab.ru:8001", referrer: "http://micro-tab.ru"
2025/12/12 02:27:14 [error] 3392344#3392344: *1199 connect() failed (111: Connection refused) while connecting to upstream, client: 65.87.7.112, server: micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:3000/", host: "micro-tab.ru:8001", referrer: "http://micro-tab.ru"
2025/12/12 02:27:15 [error] 3392344#3392344: *1199 connect() failed (111: Connection refused) while connecting to upstream, client: 65.87.7.112, server: micro-tab.ru, request: "HEAD /_next HTTP/1.1", upstream: "http://127.0.0.1:3000/_next", host: "micro-tab.ru:8001", referrer: "http://micro-tab.ru/_next"
2025/12/12 02:27:16 [error] 3392344#3392344: *1199 connect() failed (111: Connection refused) while connecting to upstream, client: 65.87.7.112, server: micro-tab.ru, request: "HEAD /__rsc HTTP/1.1", upstream: "http://127.0.0.1:3000/__rsc", host: "micro-tab.ru:8001", referrer: "http://micro-tab.ru/__rsc"
2025/12/12 02:27:16 [error] 3392344#3392344: *1199 connect() failed (111: Connection refused) while connecting to upstream, client: 65.87.7.112, server: micro-tab.ru, request: "HEAD /rsc HTTP/1.1", upstream: "http://127.0.0.1:3000/rsc", host: "micro-tab.ru:8001", referrer: "http://micro-tab.ru/rsc"
2025/12/12 03:03:56 [alert] 3392344#3392344: *1917 write() to "/var/log/nginx/access.log" was incomplete: 19 of 328 while logging request, client: 46.42.144.189, server: miniapp.micro-tab.ru, request: "GET /src/App.tsx HTTP/1.1", upstream: "http://127.0.0.1:3000/src/App.tsx", host: "miniapp.micro-tab.ru:4443", referrer: "https://miniapp.micro-tab.ru:4443/src/main.tsx"
2025/12/12 03:03:57 [crit] 3392344#3392344: *1918 mkdir() "/var/lib/nginx/proxy/7/01" failed (28: No space left on device) while reading upstream, client: 46.42.144.189, server: miniapp.micro-tab.ru, request: "GET /node_modules/.vite/deps/react-router-dom.js?v=77252c1b HTTP/1.1", upstream: "http://127.0.0.1:3000/node_modules/.vite/deps/react-router-dom.js?v=77252c1b", host: "miniapp.micro-tab.ru:4443", referrer: "ht2025/12/12 04:05:56 [error] 3392344#3392344: *2586 connect() failed (111: Connection refused) while connecting to upstream, client: 193.142.147.209, server: api.micro-tab.ru, request: "GET /cgi-bin/luci/;stok=/locale HTTP/1.1", upstream: "http://127.0.0.1:8000/cgi-bin/luci/;stok=/locale", host: "31.56.28.232:9443", referrer: "http://31.56.28.232:80/cgi-bin/luci/;stok=/locale"
2025/12/14 12:41:51 [error] 3392344#3392344: *6733 client intended to send too large body: 10485761 bytes, client: 195.170.172.128, server: api.micro-tab.ru, request: "POST / HTTP/1.1", host: "31.56.28.232:9443"
2025/12/18 19:01:20 [error] 3392344#3392344: *12534 recv() failed (104: Connection reset by peer) while reading response header from upstream, client: 167.94.138.171, server: api.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:8000/", host: "31.56.28.232:9443"
2025/12/19 16:11:14 [error] 3392344#3392344: *14164 connect() failed (111: Connection refused) while connecting to upstream, client: 195.184.76.80, server: miniapp.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:3000/", host: "31.56.28.232:4443"
2025/12/19 18:43:20 [error] 3392344#3392344: *14904 client intended to send too large body: 10485761 bytes, client: 185.91.69.33, server: miniapp.micro-tab.ru, request: "POST / HTTP/1.1", host: "31.56.28.232:4443"
2025/12/21 09:27:54 [error] 3392344#3392344: *19292 connect() failed (111: Connection refused) while connecting to upstream, client: 46.42.147.238, server: miniapp.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:3000/", host: "miniapp.micro-tab.ru:4443"
2025/12/21 09:27:54 [error] 3392344#3392344: *19292 connect() failed (111: Connection refused) while connecting to upstream, client: 46.42.147.238, server: miniapp.micro-tab.ru, request: "GET /favicon.ico HTTP/1.1", upstream: "http://127.0.0.1:3000/favicon.ico", host: "miniapp.micro-tab.ru:4443", referrer: "https://miniapp.micro-tab.ru:4443/"
2025/12/21 10:00:17 [error] 3392344#3392344: *19344 connect() failed (111: Connection refused) while connecting to upstream, client: 31.56.28.232, server: miniapp.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:3000/", host: "miniapp.micro-tab.ru:4443", referrer: "https://web.telegram.org/"
2025/12/21 10:00:23 [error] 3392344#3392344: *19344 connect() failed (111: Connection refused) while connecting to upstream, client: 31.56.28.232, server: miniapp.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:3000/", host: "miniapp.micro-tab.ru:4443", referrer: "https://web.telegram.org/"
2025/12/21 10:02:08 [error] 3392344#3392344: *19347 connect() failed (111: Connection refused) while connecting to upstream, client: 46.42.147.238, server: miniapp.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:3000/", host: "miniapp.micro-tab.ru:4443"
2025/12/21 10:02:08 [error] 3392344#3392344: *19347 connect() failed (111: Connection refused) while connecting to upstream, client: 46.42.147.238, server: miniapp.micro-tab.ru, request: "GET /favicon.ico HTTP/1.1", upstream: "http://127.0.0.1:3000/favicon.ico", host: "miniapp.micro-tab.ru:4443", referrer: "https://miniapp.micro-tab.ru:4443/"
2025/12/21 10:02:25 [error] 3392344#3392344: *19351 connect() failed (111: Connection refused) while connecting to upstream, client: 206.168.34.40, server: api.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:8000/", host: "31.56.28.232:9443"
2025/12/21 10:02:42 [error] 3392344#3392344: *19353 connect() failed (111: Connection refused) while connecting to upstream, client: 31.56.28.232, server: miniapp.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:3000/", host: "miniapp.micro-tab.ru:4443", referrer: "https://web.telegram.org/"
2025/12/21 10:02:51 [error] 3392344#3392344: *19353 connect() failed (111: Connection refused) while connecting to upstream, client: 31.56.28.232, server: miniapp.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:3000/", host: "miniapp.micro-tab.ru:4443", referrer: "https://web.telegram.org/"
2025/12/21 10:02:56 [error] 3392344#3392344: *19355 connect() failed (111: Connection refused) while connecting to upstream, client: 206.168.34.40, server: api.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:8000/", host: "31.56.28.232:9443"
2025/12/21 10:03:35 [error] 3392344#3392344: *19363 connect() failed (111: Connection refused) while connecting to upstream, client: 206.168.34.40, server: api.micro-tab.ru, request: "GET /sitemap.xml HTTP/1.1", upstream: "http://127.0.0.1:8000/sitemap.xml", host: "31.56.28.232:9443"
2025/12/21 10:06:34 [error] 3392344#3392344: *19366 connect() failed (111: Connection refused) while connecting to upstream, client: 43.135.144.126, server: api.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:8000/", host: "31.56.28.232:9443", referrer: "http://31.56.28.232"
2025/12/21 10:08:21 [error] 3392344#3392344: *19368 connect() failed (111: Connection refused) while connecting to upstream, client: 216.218.206.68, server: micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:3000/", host: "31.56.28.232:8001"
2025/12/21 10:08:35 [error] 3392344#3392344: *19372 connect() failed (111: Connection refused) while connecting to upstream, client: 216.218.206.68, server: micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:3000/", host: "31.56.28.232:8001"
2025/12/21 10:08:44 [error] 3392344#3392344: *19374 connect() failed (111: Connection refused) while connecting to upstream, client: 216.218.206.68, server: micro-tab.ru, request: "GET /favicon.ico HTTP/1.1", upstream: "http://127.0.0.1:3000/favicon.ico", host: "31.56.28.232:8001"
2025/12/21 10:11:27 [error] 3392344#3392344: *19376 connect() failed (111: Connection refused) while connecting to upstream, client: 46.42.147.238, server: miniapp.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:3000/", host: "miniapp.micro-tab.ru:4443"
2025/12/21 10:11:28 [error] 3392344#3392344: *19376 connect() failed (111: Connection refused) while connecting to upstream, client: 46.42.147.238, server: miniapp.micro-tab.ru, request: "GET /favicon.ico HTTP/1.1", upstream: "http://127.0.0.1:3000/favicon.ico", host: "miniapp.micro-tab.ru:4443", referrer: "https://miniapp.micro-tab.ru:4443/"
2025/12/21 10:11:36 [error] 3392344#3392344: *19379 connect() failed (111: Connection refused) while connecting to upstream, client: 46.42.147.238, server: miniapp.micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:3000/", host: "miniapp.micro-tab.ru:4443"
2025/12/21 10:11:36 [error] 3392344#3392344: *19379 connect() failed (111: Connection refused) while connecting to upstream, client: 46.42.147.238, server: miniapp.micro-tab.ru, request: "GET /favicon.ico HTTP/1.1", upstream: "http://127.0.0.1:3000/favicon.ico", host: "miniapp.micro-tab.ru:4443", referrer: "https://miniapp.micro-tab.ru:4443/"
2025/12/21 10:23:24 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:3000/", host: "micro-tab.ru:8001"
2025/12/21 10:23:25 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:3000//wp-includes/wlwmanifest.xml", host: "micro-tab.ru:8001"
2025/12/21 10:23:25 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //xmlrpc.php?rsd HTTP/1.1", upstream: "http://127.0.0.1:3000//xmlrpc.php?rsd", host: "micro-tab.ru:8001"
2025/12/21 10:23:25 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:3000/", host: "micro-tab.ru:8001"
2025/12/21 10:23:25 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //blog/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:3000//blog/wp-includes/wlwmanifest.xml", host: "micro-tab.ru:8001"
2025/12/21 10:23:26 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //web/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:3000//web/wp-includes/wlwmanifest.xml", host: "micro-tab.ru:8001"
2025/12/21 10:23:26 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //wordpress/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:3000//wordpress/wp-includes/wlwmanifest.xml", host: "micro-tab.ru:8001"
2025/12/21 10:23:26 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //website/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:3000//website/wp-includes/wlwmanifest.xml", host: "micro-tab.ru:8001"
2025/12/21 10:23:26 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //wp/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:3000//wp/wp-includes/wlwmanifest.xml", host: "micro-tab.ru:8001"
2025/12/21 10:23:27 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //news/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:3000//news/wp-includes/wlwmanifest.xml", host: "micro-tab.ru:8001"
2025/12/21 10:23:27 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //2018/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:3000//2018/wp-includes/wlwmanifest.xml", host: "micro-tab.ru:8001"
2025/12/21 10:23:27 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //2019/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:3000//2019/wp-includes/wlwmanifest.xml", host: "micro-tab.ru:8001"
2025/12/21 10:23:27 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //shop/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:3000//shop/wp-includes/wlwmanifest.xml", host: "micro-tab.ru:8001"
2025/12/21 10:23:28 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //wp1/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:3000//wp1/wp-includes/wlwmanifest.xml", host: "micro-tab.ru:8001"
2025/12/21 10:23:28 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //test/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:3000//test/wp-includes/wlwmanifest.xml", host: "micro-tab.ru:8001"
2025/12/21 10:23:28 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //media/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:3000//media/wp-includes/wlwmanifest.xml", host: "micro-tab.ru:8001"
2025/12/21 10:23:28 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //wp2/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:3000//wp2/wp-includes/wlwmanifest.xml", host: "micro-tab.ru:8001"
2025/12/21 10:23:29 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //site/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:3000//site/wp-includes/wlwmanifest.xml", host: "micro-tab.ru:8001"
2025/12/21 10:23:29 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //cms/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:3000//cms/wp-includes/wlwmanifest.xml", host: "micro-tab.ru:8001"
2025/12/21 10:23:29 [error] 3392344#3392344: *19384 connect() failed (111: Connection refused) while connecting to upstream, client: 159.223.92.152, server: micro-tab.ru, request: "GET //sito/wp-includes/wlwmanifest.xml HTTP/1.1", upstream: "http://127.0.0.1:3000//sito/wp-includes/wlwmanifest.xml", host: "micro-tab.ru:8001"
root@server-cqfsqu:~/tg_bot_HB#    # Если nginx в Docker
   docker exec -it <nginx-container> curl http://host.docker.internal:8000/health
   
   # Если nginx на хосте
   curl http://127.0.0.1:8000/health
-bash: nginx-container: No such file or directory
{"status":"ok","service":"Telegram Birthday Calendar API","message":"API is running"}root@server-cqfsqu:~/tg_bot_HB#    nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful