Backend Coverage
failed 1 minute ago in 26s
Search logs
2s
Current runner version: '2.329.0'
Runner Image Provisioner
Operating System
Runner Image
GITHUB_TOKEN Permissions
Secret source: Actions
Prepare workflow directory
Prepare all required actions
Getting action download info
Download action repository 'actions/checkout@v4' (SHA:34e114876b0b11c390a56381ad16ebd13914f8d5)
Download action repository 'actions/setup-python@v5' (SHA:a26af69be951a213d495a4c3e4e4022e16d87065)
Download action repository 'actions/upload-artifact@v4' (SHA:ea165f8d65b6e75b540449e92b4886f43607fa02)
Download action repository 'py-cov-action/python-coverage-comment-action@v3' (SHA:1ac153f97397005ebcbec0c3caefa58f56ae5a26)
Complete job name: Backend Coverage
5s
Build container for action use: '/home/runner/work/_actions/py-cov-action/python-coverage-comment-action/v3/Dockerfile'.
0s
Run actions/checkout@v4
Syncing repository: NocarDvanSiegfried/tg_bot_HB
Getting Git version info
Temporarily overriding HOME='/home/runner/work/_temp/86f8721b-4605-4b04-b1a5-45c1a61e5c37' before making global git config changes
Adding repository directory to the temporary git global config as a safe directory
/usr/bin/git config --global --add safe.directory /home/runner/work/tg_bot_HB/tg_bot_HB
Deleting the contents of '/home/runner/work/tg_bot_HB/tg_bot_HB'
Initializing the repository
Disabling automatic garbage collection
Setting up auth
Fetching the repository
Determining the checkout info
/usr/bin/git sparse-checkout disable
/usr/bin/git config --local --unset-all extensions.worktreeConfig
Checking out the ref
/usr/bin/git log -1 --format=%H
016f7ba73d72fd44a99157bc70eb174bf51a72c7
2s
Run actions/setup-python@v5
Installed versions
/opt/hostedtoolcache/Python/3.11.14/x64/bin/pip cache dir
/home/runner/.cache/pip
Cache hit for: setup-python-Linux-x64-24.04-Ubuntu-python-3.11.14-pip-ace0314700279b625eba2398b4c3061ed26f0e958e6e00272a98aef6c543a4cf
Received 44286820 of 44286820 (100.0%), 146.7 MBs/sec
Cache Size: ~42 MB (44286820 B)
/usr/bin/tar -xf /home/runner/work/_temp/1c01a2a4-5a52-42d7-9ef5-46490160d96b/cache.tzst -P -C /home/runner/work/tg_bot_HB/tg_bot_HB --use-compress-program unzstd
Cache restored successfully
Cache restored from key: setup-python-Linux-x64-24.04-Ubuntu-python-3.11.14-pip-ace0314700279b625eba2398b4c3061ed26f0e958e6e00272a98aef6c543a4cf
10s
Run python -m pip install --upgrade pip
Requirement already satisfied: pip in /opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages (25.3)
Collecting fastapi==0.104.1 (from -r requirements.txt (line 1))
  Using cached fastapi-0.104.1-py3-none-any.whl.metadata (24 kB)
Collecting uvicorn==0.24.0 (from uvicorn[standard]==0.24.0->-r requirements.txt (line 2))
  Using cached uvicorn-0.24.0-py3-none-any.whl.metadata (6.4 kB)
Collecting aiogram==3.23.0 (from -r requirements.txt (line 3))
  Using cached aiogram-3.23.0-py3-none-any.whl.metadata (7.6 kB)
Collecting sqlalchemy==2.0.23 (from -r requirements.txt (line 4))
  Using cached SQLAlchemy-2.0.23-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.6 kB)
Collecting asyncpg==0.29.0 (from -r requirements.txt (line 5))
  Using cached asyncpg-0.29.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.4 kB)
Collecting aiosqlite==0.19.0 (from -r requirements.txt (line 6))
  Using cached aiosqlite-0.19.0-py3-none-any.whl.metadata (4.3 kB)
Collecting alembic==1.12.1 (from -r requirements.txt (line 7))
  Using cached alembic-1.12.1-py3-none-any.whl.metadata (7.3 kB)
Collecting pydantic==2.5.0 (from -r requirements.txt (line 8))
  Using cached pydantic-2.5.0-py3-none-any.whl.metadata (174 kB)
Collecting httpx==0.25.1 (from -r requirements.txt (line 9))
  Using cached httpx-0.25.1-py3-none-any.whl.metadata (7.1 kB)
Collecting pillow==10.1.0 (from -r requirements.txt (line 10))
  Using cached Pillow-10.1.0-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (9.5 kB)
Collecting qrcode==7.4.2 (from qrcode[pil]==7.4.2->-r requirements.txt (line 11))
  Using cached qrcode-7.4.2-py3-none-any.whl.metadata (17 kB)
Collecting apscheduler==3.10.4 (from -r requirements.txt (line 12))
  Using cached APScheduler-3.10.4-py3-none-any.whl.metadata (5.7 kB)
Collecting python-dotenv==1.0.0 (from -r requirements.txt (line 13))
  Using cached python_dotenv-1.0.0-py3-none-any.whl.metadata (21 kB)
Collecting pytest==7.4.3 (from -r requirements.txt (line 14))
  Using cached pytest-7.4.3-py3-none-any.whl.metadata (7.9 kB)
Collecting pytest-asyncio==0.21.1 (from -r requirements.txt (line 15))
  Using cached pytest_asyncio-0.21.1-py3-none-any.whl.metadata (4.0 kB)
Collecting pytest-mock==3.12.0 (from -r requirements.txt (line 16))
  Using cached pytest_mock-3.12.0-py3-none-any.whl.metadata (3.8 kB)
Collecting pytest-cov==4.1.0 (from -r requirements.txt (line 17))
  Using cached pytest_cov-4.1.0-py3-none-any.whl.metadata (26 kB)
Collecting ruff==0.5.0 (from -r requirements.txt (line 18))
  Using cached ruff-0.5.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (24 kB)
Collecting black==24.1.1 (from -r requirements.txt (line 19))
  Using cached black-24.1.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (73 kB)
Collecting anyio<4.0.0,>=3.7.1 (from fastapi==0.104.1->-r requirements.txt (line 1))
  Using cached anyio-3.7.1-py3-none-any.whl.metadata (4.7 kB)
Collecting starlette<0.28.0,>=0.27.0 (from fastapi==0.104.1->-r requirements.txt (line 1))
  Using cached starlette-0.27.0-py3-none-any.whl.metadata (5.8 kB)
Collecting typing-extensions>=4.8.0 (from fastapi==0.104.1->-r requirements.txt (line 1))
  Using cached typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting annotated-types>=0.4.0 (from pydantic==2.5.0->-r requirements.txt (line 8))
  Using cached annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.14.1 (from pydantic==2.5.0->-r requirements.txt (line 8))
  Using cached pydantic_core-2.14.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.5 kB)
Collecting click>=7.0 (from uvicorn==0.24.0->uvicorn[standard]==0.24.0->-r requirements.txt (line 2))
  Using cached click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
Collecting h11>=0.8 (from uvicorn==0.24.0->uvicorn[standard]==0.24.0->-r requirements.txt (line 2))
  Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting aiofiles<26.0,>=23.2.1 (from aiogram==3.23.0->-r requirements.txt (line 3))
  Using cached aiofiles-25.1.0-py3-none-any.whl.metadata (6.3 kB)
Collecting aiohttp<3.14,>=3.9.0 (from aiogram==3.23.0->-r requirements.txt (line 3))
  Using cached aiohttp-3.13.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (8.1 kB)
Collecting certifi>=2023.7.22 (from aiogram==3.23.0->-r requirements.txt (line 3))
  Using cached certifi-2025.11.12-py3-none-any.whl.metadata (2.5 kB)
Collecting magic-filter<1.1,>=1.0.12 (from aiogram==3.23.0->-r requirements.txt (line 3))
  Using cached magic_filter-1.0.12-py3-none-any.whl.metadata (1.5 kB)
Collecting greenlet!=0.4.17 (from sqlalchemy==2.0.23->-r requirements.txt (line 4))
  Using cached greenlet-3.3.0-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (4.1 kB)
Collecting async-timeout>=4.0.3 (from asyncpg==0.29.0->-r requirements.txt (line 5))
  Using cached async_timeout-5.0.1-py3-none-any.whl.metadata (5.1 kB)
Collecting Mako (from alembic==1.12.1->-r requirements.txt (line 7))
  Using cached mako-1.3.10-py3-none-any.whl.metadata (2.9 kB)
Collecting httpcore (from httpx==0.25.1->-r requirements.txt (line 9))
  Using cached httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Collecting idna (from httpx==0.25.1->-r requirements.txt (line 9))
  Using cached idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting sniffio (from httpx==0.25.1->-r requirements.txt (line 9))
  Using cached sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Collecting pypng (from qrcode==7.4.2->qrcode[pil]==7.4.2->-r requirements.txt (line 11))
  Using cached pypng-0.20220715.0-py3-none-any.whl.metadata (13 kB)
Collecting six>=1.4.0 (from apscheduler==3.10.4->-r requirements.txt (line 12))
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting pytz (from apscheduler==3.10.4->-r requirements.txt (line 12))
  Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzlocal!=3.*,>=2.0 (from apscheduler==3.10.4->-r requirements.txt (line 12))
  Using cached tzlocal-5.3.1-py3-none-any.whl.metadata (7.6 kB)
Collecting iniconfig (from pytest==7.4.3->-r requirements.txt (line 14))
  Using cached iniconfig-2.3.0-py3-none-any.whl.metadata (2.5 kB)
Collecting packaging (from pytest==7.4.3->-r requirements.txt (line 14))
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pluggy<2.0,>=0.12 (from pytest==7.4.3->-r requirements.txt (line 14))
  Using cached pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Collecting coverage>=5.2.1 (from coverage[toml]>=5.2.1->pytest-cov==4.1.0->-r requirements.txt (line 17))
  Downloading coverage-7.13.0-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (8.5 kB)
Collecting mypy-extensions>=0.4.3 (from black==24.1.1->-r requirements.txt (line 19))
  Using cached mypy_extensions-1.1.0-py3-none-any.whl.metadata (1.1 kB)
Collecting pathspec>=0.9.0 (from black==24.1.1->-r requirements.txt (line 19))
  Using cached pathspec-0.12.1-py3-none-any.whl.metadata (21 kB)
Collecting platformdirs>=2 (from black==24.1.1->-r requirements.txt (line 19))
  Using cached platformdirs-4.5.1-py3-none-any.whl.metadata (12 kB)
Collecting httptools>=0.5.0 (from uvicorn[standard]==0.24.0->-r requirements.txt (line 2))
  Using cached httptools-0.7.1-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (3.5 kB)
Collecting pyyaml>=5.1 (from uvicorn[standard]==0.24.0->-r requirements.txt (line 2))
  Using cached pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
Collecting uvloop!=0.15.0,!=0.15.1,>=0.14.0 (from uvicorn[standard]==0.24.0->-r requirements.txt (line 2))
  Using cached uvloop-0.22.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.9 kB)
Collecting watchfiles>=0.13 (from uvicorn[standard]==0.24.0->-r requirements.txt (line 2))
  Using cached watchfiles-1.1.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
Collecting websockets>=10.4 (from uvicorn[standard]==0.24.0->-r requirements.txt (line 2))
  Using cached websockets-15.0.1-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
Collecting aiohappyeyeballs>=2.5.0 (from aiohttp<3.14,>=3.9.0->aiogram==3.23.0->-r requirements.txt (line 3))
  Using cached aiohappyeyeballs-2.6.1-py3-none-any.whl.metadata (5.9 kB)
Collecting aiosignal>=1.4.0 (from aiohttp<3.14,>=3.9.0->aiogram==3.23.0->-r requirements.txt (line 3))
  Using cached aiosignal-1.4.0-py3-none-any.whl.metadata (3.7 kB)
Collecting attrs>=17.3.0 (from aiohttp<3.14,>=3.9.0->aiogram==3.23.0->-r requirements.txt (line 3))
  Using cached attrs-25.4.0-py3-none-any.whl.metadata (10 kB)
Collecting frozenlist>=1.1.1 (from aiohttp<3.14,>=3.9.0->aiogram==3.23.0->-r requirements.txt (line 3))
  Using cached frozenlist-1.8.0-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (20 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp<3.14,>=3.9.0->aiogram==3.23.0->-r requirements.txt (line 3))
  Using cached multidict-6.7.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (5.3 kB)
Collecting propcache>=0.2.0 (from aiohttp<3.14,>=3.9.0->aiogram==3.23.0->-r requirements.txt (line 3))
  Using cached propcache-0.4.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (13 kB)
Collecting yarl<2.0,>=1.17.0 (from aiohttp<3.14,>=3.9.0->aiogram==3.23.0->-r requirements.txt (line 3))
  Using cached yarl-1.22.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (75 kB)
Collecting MarkupSafe>=0.9.2 (from Mako->alembic==1.12.1->-r requirements.txt (line 7))
  Using cached markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
Using cached fastapi-0.104.1-py3-none-any.whl (92 kB)
Using cached pydantic-2.5.0-py3-none-any.whl (407 kB)
Using cached uvicorn-0.24.0-py3-none-any.whl (59 kB)
Using cached aiogram-3.23.0-py3-none-any.whl (698 kB)
Using cached SQLAlchemy-2.0.23-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.2 MB)
Using cached asyncpg-0.29.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.8 MB)
Using cached aiosqlite-0.19.0-py3-none-any.whl (15 kB)
Using cached alembic-1.12.1-py3-none-any.whl (226 kB)
Using cached httpx-0.25.1-py3-none-any.whl (75 kB)
Using cached Pillow-10.1.0-cp311-cp311-manylinux_2_28_x86_64.whl (3.6 MB)
Using cached qrcode-7.4.2-py3-none-any.whl (46 kB)
Using cached APScheduler-3.10.4-py3-none-any.whl (59 kB)
Using cached python_dotenv-1.0.0-py3-none-any.whl (19 kB)
Using cached pytest-7.4.3-py3-none-any.whl (325 kB)
Using cached pytest_asyncio-0.21.1-py3-none-any.whl (13 kB)
Using cached pytest_mock-3.12.0-py3-none-any.whl (9.8 kB)
Using cached pytest_cov-4.1.0-py3-none-any.whl (21 kB)
Using cached ruff-0.5.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (10.1 MB)
Using cached black-24.1.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.7 MB)
Using cached pydantic_core-2.14.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
Using cached aiofiles-25.1.0-py3-none-any.whl (14 kB)
Using cached aiohttp-3.13.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (1.7 MB)
Using cached anyio-3.7.1-py3-none-any.whl (80 kB)
Using cached magic_filter-1.0.12-py3-none-any.whl (11 kB)
Using cached multidict-6.7.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (246 kB)
Using cached pluggy-1.6.0-py3-none-any.whl (20 kB)
Using cached starlette-0.27.0-py3-none-any.whl (66 kB)
Using cached typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Using cached yarl-1.22.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (365 kB)
Using cached aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
Using cached aiosignal-1.4.0-py3-none-any.whl (7.5 kB)
Using cached annotated_types-0.7.0-py3-none-any.whl (13 kB)
Using cached async_timeout-5.0.1-py3-none-any.whl (6.2 kB)
Using cached attrs-25.4.0-py3-none-any.whl (67 kB)
Using cached certifi-2025.11.12-py3-none-any.whl (159 kB)
Using cached click-8.3.1-py3-none-any.whl (108 kB)
Downloading coverage-7.13.0-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (250 kB)
Using cached frozenlist-1.8.0-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (231 kB)
Using cached greenlet-3.3.0-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (590 kB)
Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Using cached httptools-0.7.1-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (456 kB)
Using cached idna-3.11-py3-none-any.whl (71 kB)
Using cached mypy_extensions-1.1.0-py3-none-any.whl (5.0 kB)
Using cached packaging-25.0-py3-none-any.whl (66 kB)
Using cached pathspec-0.12.1-py3-none-any.whl (31 kB)
Using cached platformdirs-4.5.1-py3-none-any.whl (18 kB)
Using cached propcache-0.4.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (210 kB)
Using cached pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (806 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
Using cached tzlocal-5.3.1-py3-none-any.whl (18 kB)
Using cached uvloop-0.22.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.8 MB)
Using cached watchfiles-1.1.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (456 kB)
Using cached websockets-15.0.1-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (182 kB)
Using cached httpcore-1.0.9-py3-none-any.whl (78 kB)
Using cached iniconfig-2.3.0-py3-none-any.whl (7.5 kB)
Using cached mako-1.3.10-py3-none-any.whl (78 kB)
Using cached markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
Using cached pypng-0.20220715.0-py3-none-any.whl (58 kB)
Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Installing collected packages: pytz, pypng, websockets, uvloop, tzlocal, typing-extensions, sniffio, six, ruff, pyyaml, python-dotenv, propcache, pluggy, platformdirs, pillow, pathspec, packaging, mypy-extensions, multidict, MarkupSafe, magic-filter, iniconfig, idna, httptools, h11, greenlet, frozenlist, coverage, click, certifi, attrs, async-timeout, annotated-types, aiosqlite, aiohappyeyeballs, aiofiles, yarl, uvicorn, sqlalchemy, qrcode, pytest, pydantic-core, Mako, httpcore, black, asyncpg, apscheduler, anyio, aiosignal, watchfiles, starlette, pytest-mock, pytest-cov, pytest-asyncio, pydantic, httpx, alembic, aiohttp, fastapi, aiogram

Successfully installed Mako-1.3.10 MarkupSafe-3.0.3 aiofiles-25.1.0 aiogram-3.23.0 aiohappyeyeballs-2.6.1 aiohttp-3.13.2 aiosignal-1.4.0 aiosqlite-0.19.0 alembic-1.12.1 annotated-types-0.7.0 anyio-3.7.1 apscheduler-3.10.4 async-timeout-5.0.1 asyncpg-0.29.0 attrs-25.4.0 black-24.1.1 certifi-2025.11.12 click-8.3.1 coverage-7.13.0 fastapi-0.104.1 frozenlist-1.8.0 greenlet-3.3.0 h11-0.16.0 httpcore-1.0.9 httptools-0.7.1 httpx-0.25.1 idna-3.11 iniconfig-2.3.0 magic-filter-1.0.12 multidict-6.7.0 mypy-extensions-1.1.0 packaging-25.0 pathspec-0.12.1 pillow-10.1.0 platformdirs-4.5.1 pluggy-1.6.0 propcache-0.4.1 pydantic-2.5.0 pydantic-core-2.14.1 pypng-0.20220715.0 pytest-7.4.3 pytest-asyncio-0.21.1 pytest-cov-4.1.0 pytest-mock-3.12.0 python-dotenv-1.0.0 pytz-2025.2 pyyaml-6.0.3 qrcode-7.4.2 ruff-0.5.0 six-1.17.0 sniffio-1.3.1 sqlalchemy-2.0.23 starlette-0.27.0 typing-extensions-4.15.0 tzlocal-5.3.1 uvicorn-0.24.0 uvloop-0.22.1 watchfiles-1.1.1 websockets-15.0.1 yarl-1.22.0
6s
Run pytest tests/ --cov=src --cov-report=xml --cov-report=term --cov-report=html -v --import-mode=importlib
  pytest tests/ --cov=src --cov-report=xml --cov-report=term --cov-report=html -v --import-mode=importlib
  shell: /usr/bin/bash -e {0}
  env:
    pythonLocation: /opt/hostedtoolcache/Python/3.11.14/x64
    PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.14/x64/lib/pkgconfig
    Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.14/x64
    Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.14/x64
    Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.14/x64
    LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.14/x64/lib
    PYTHONPATH: /home/runner/work/tg_bot_HB/tg_bot_HB/backend
    DATABASE_URL: sqlite+aiosqlite:///:memory:
    TELEGRAM_BOT_TOKEN: test_token
    OPENROUTER_API_KEY: test_key
============================= test session starts ==============================
platform linux -- Python 3.11.14, pytest-7.4.3, pluggy-1.6.0 -- /opt/hostedtoolcache/Python/3.11.14/x64/bin/python
cachedir: .pytest_cache
rootdir: /home/runner/work/tg_bot_HB/tg_bot_HB/backend
configfile: pytest.ini
plugins: anyio-3.7.1, asyncio-0.21.1, mock-3.12.0, cov-4.1.0
asyncio: mode=Mode.AUTO
collecting ... collected 179 items / 8 errors

==================================== ERRORS ====================================
___________ ERROR collecting tests/presentation/telegram/test_bot.py ___________
ImportError while importing test module '/home/runner/work/tg_bot_HB/tg_bot_HB/backend/tests/presentation/telegram/test_bot.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/python.py:617: in _importtestmodule
    mod = import_path(self.path, mode=importmode, root=self.config.rootpath)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/pathlib.py:540: in import_path
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:186: in exec_module
    exec(co, module.__dict__)
tests/presentation/telegram/test_bot.py:5: in <module>
    from src.presentation.telegram.bot import main
src/presentation/telegram/bot.py:5: in <module>
    from aiogram.fsm.storage.memory import MemoryStorage
E   ModuleNotFoundError: No module named 'aiogram.fsm'; 'aiogram' is not a package
________ ERROR collecting tests/presentation/telegram/test_keyboards.py ________
ImportError while importing test module '/home/runner/work/tg_bot_HB/tg_bot_HB/backend/tests/presentation/telegram/test_keyboards.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/python.py:617: in _importtestmodule
    mod = import_path(self.path, mode=importmode, root=self.config.rootpath)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/pathlib.py:540: in import_path
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:186: in exec_module
    exec(co, module.__dict__)
tests/presentation/telegram/test_keyboards.py:3: in <module>
    from src.presentation.telegram.keyboards import (
src/presentation/telegram/keyboards.py:1: in <module>
    from aiogram.types import (
E   ModuleNotFoundError: No module named 'aiogram.types'; 'aiogram' is not a package
_ ERROR collecting tests/presentation/telegram/handlers/test_birthday_handlers.py _
ImportError while importing test module '/home/runner/work/tg_bot_HB/tg_bot_HB/backend/tests/presentation/telegram/handlers/test_birthday_handlers.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/python.py:617: in _importtestmodule
    mod = import_path(self.path, mode=importmode, root=self.config.rootpath)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/pathlib.py:540: in import_path
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:186: in exec_module
    exec(co, module.__dict__)
tests/presentation/telegram/handlers/test_birthday_handlers.py:5: in <module>
    from src.presentation.telegram.handlers.birthday_handlers import (
src/presentation/telegram/handlers/__init__.py:1: in <module>
    from . import (
src/presentation/telegram/handlers/birthday_handlers.py:4: in <module>
    from aiogram.fsm.context import FSMContext
E   ModuleNotFoundError: No module named 'aiogram.fsm'; 'aiogram' is not a package
_ ERROR collecting tests/presentation/telegram/handlers/test_calendar_handler.py _
ImportError while importing test module '/home/runner/work/tg_bot_HB/tg_bot_HB/backend/tests/presentation/telegram/handlers/test_calendar_handler.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/python.py:617: in _importtestmodule
    mod = import_path(self.path, mode=importmode, root=self.config.rootpath)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/pathlib.py:540: in import_path
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:186: in exec_module
    exec(co, module.__dict__)
tests/presentation/telegram/handlers/test_calendar_handler.py:5: in <module>
    from src.presentation.telegram.handlers.calendar_handler import (
src/presentation/telegram/handlers/__init__.py:1: in <module>
    from . import (
src/presentation/telegram/handlers/birthday_handlers.py:4: in <module>
    from aiogram.fsm.context import FSMContext
E   ModuleNotFoundError: No module named 'aiogram.fsm'; 'aiogram' is not a package
_ ERROR collecting tests/presentation/telegram/handlers/test_greeting_handlers.py _
ImportError while importing test module '/home/runner/work/tg_bot_HB/tg_bot_HB/backend/tests/presentation/telegram/handlers/test_greeting_handlers.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/python.py:617: in _importtestmodule
    mod = import_path(self.path, mode=importmode, root=self.config.rootpath)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/pathlib.py:540: in import_path
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:186: in exec_module
    exec(co, module.__dict__)
tests/presentation/telegram/handlers/test_greeting_handlers.py:4: in <module>
    from src.presentation.telegram.handlers.greeting_handlers import (
src/presentation/telegram/handlers/__init__.py:1: in <module>
    from . import (
src/presentation/telegram/handlers/birthday_handlers.py:4: in <module>
    from aiogram.fsm.context import FSMContext
E   ModuleNotFoundError: No module named 'aiogram.fsm'; 'aiogram' is not a package
_ ERROR collecting tests/presentation/telegram/handlers/test_panel_handler.py __
ImportError while importing test module '/home/runner/work/tg_bot_HB/tg_bot_HB/backend/tests/presentation/telegram/handlers/test_panel_handler.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/python.py:617: in _importtestmodule
    mod = import_path(self.path, mode=importmode, root=self.config.rootpath)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/pathlib.py:540: in import_path
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:186: in exec_module
    exec(co, module.__dict__)
tests/presentation/telegram/handlers/test_panel_handler.py:4: in <module>
    from src.presentation.telegram.handlers.panel_handler import cmd_panel, panel_main_callback
src/presentation/telegram/handlers/__init__.py:1: in <module>
    from . import (
src/presentation/telegram/handlers/birthday_handlers.py:4: in <module>
    from aiogram.fsm.context import FSMContext
E   ModuleNotFoundError: No module named 'aiogram.fsm'; 'aiogram' is not a package
_ ERROR collecting tests/presentation/telegram/handlers/test_responsible_handlers.py _
ImportError while importing test module '/home/runner/work/tg_bot_HB/tg_bot_HB/backend/tests/presentation/telegram/handlers/test_responsible_handlers.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/python.py:617: in _importtestmodule
    mod = import_path(self.path, mode=importmode, root=self.config.rootpath)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/pathlib.py:540: in import_path
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:186: in exec_module
    exec(co, module.__dict__)
tests/presentation/telegram/handlers/test_responsible_handlers.py:4: in <module>
    from src.presentation.telegram.handlers.responsible_handlers import (
src/presentation/telegram/handlers/__init__.py:1: in <module>
    from . import (
src/presentation/telegram/handlers/birthday_handlers.py:4: in <module>
    from aiogram.fsm.context import FSMContext
E   ModuleNotFoundError: No module named 'aiogram.fsm'; 'aiogram' is not a package
_ ERROR collecting tests/presentation/telegram/handlers/test_start_handler.py __
ImportError while importing test module '/home/runner/work/tg_bot_HB/tg_bot_HB/backend/tests/presentation/telegram/handlers/test_start_handler.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/python.py:617: in _importtestmodule
    mod = import_path(self.path, mode=importmode, root=self.config.rootpath)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/pathlib.py:540: in import_path
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:186: in exec_module
    exec(co, module.__dict__)
tests/presentation/telegram/handlers/test_start_handler.py:4: in <module>
    from src.presentation.telegram.handlers.start_handler import cmd_start
src/presentation/telegram/handlers/__init__.py:1: in <module>
    from . import (
src/presentation/telegram/handlers/birthday_handlers.py:4: in <module>
    from aiogram.fsm.context import FSMContext
E   ModuleNotFoundError: No module named 'aiogram.fsm'; 'aiogram' is not a package

---------- coverage: platform linux, python 3.11.14-final-0 ----------
Name                                                                       Stmts   Miss  Cover
----------------------------------------------------------------------------------------------
src/__init__.py                                                                0      0   100%
src/application/__init__.py                                                    0      0   100%
src/application/factories/__init__.py                                          0      0   100%
src/application/factories/use_case_factory.py                                 94     45    52%
src/application/ports/__init__.py                                              0      0   100%
src/application/ports/birthday_repository.py                                   4      0   100%
src/application/ports/card_generator.py                                        2      0   100%
src/application/ports/holiday_repository.py                                    4      0   100%
src/application/ports/openrouter_client.py                                     2      0   100%
src/application/ports/panel_access_repository.py                               2      0   100%
src/application/ports/responsible_repository.py                                4      0   100%
src/application/ports/telegram_auth_service.py                                 2      0   100%
src/application/use_cases/__init__.py                                          0      0   100%
src/application/use_cases/auth/__init__.py                                     0      0   100%
src/application/use_cases/auth/verify_telegram_auth.py                        10      6    40%
src/application/use_cases/birthday/__init__.py                                 0      0   100%
src/application/use_cases/birthday/create_birthday.py                          9      3    67%
src/application/use_cases/birthday/delete_birthday.py                          9      5    44%
src/application/use_cases/birthday/get_all_birthdays.py                        7      2    71%
src/application/use_cases/birthday/get_birthdays_by_date.py                    8      2    75%
src/application/use_cases/birthday/update_birthday.py                         12      6    50%
src/application/use_cases/calendar/__init__.py                                 0      0   100%
src/application/use_cases/calendar/get_calendar_data.py                       14      7    50%
src/application/use_cases/greeting/__init__.py                                 0      0   100%
src/application/use_cases/greeting/create_card.py                             12      6    50%
src/application/use_cases/greeting/generate_greeting.py                       11      6    45%
src/application/use_cases/holiday/__init__.py                                  0      0   100%
src/application/use_cases/holiday/create_holiday.py                            9      3    67%
src/application/use_cases/holiday/delete_holiday.py                            9      5    44%
src/application/use_cases/holiday/update_holiday.py                           12      6    50%
src/application/use_cases/panel/__init__.py                                    0      0   100%
src/application/use_cases/panel/check_panel_access.py                          6      2    67%
src/application/use_cases/panel/record_panel_access.py                         6      2    67%
src/application/use_cases/responsible/__init__.py                              0      0   100%
src/application/use_cases/responsible/assign_responsible_to_date.py           10      5    50%
src/application/use_cases/responsible/create_responsible.py                    8      3    62%
src/application/use_cases/responsible/delete_responsible.py                    9      5    44%
src/application/use_cases/responsible/get_all_responsible.py                   7      2    71%
src/application/use_cases/responsible/update_responsible.py                   11      6    45%
src/application/use_cases/search/__init__.py                                   0      0   100%
src/application/use_cases/search/search_people.py                             17     10    41%
src/domain/entities/__init__.py                                                0      0   100%
src/domain/entities/birthday.py                                               15      4    73%
src/domain/entities/professional_holiday.py                                    8      0   100%
src/domain/entities/responsible_person.py                                      7      0   100%
src/domain/exceptions/__init__.py                                              5      0   100%
src/domain/exceptions/api_exceptions.py                                       12      4    67%
src/domain/exceptions/base.py                                                  2      0   100%
src/domain/exceptions/business.py                                              3      0   100%
src/domain/exceptions/not_found.py                                             7      0   100%
src/domain/exceptions/validation.py                                            5      0   100%
src/infrastructure/__init__.py                                                 0      0   100%
src/infrastructure/config/__init__.py                                          0      0   100%
src/infrastructure/config/openrouter_config.py                                18      8    56%
src/infrastructure/database/__init__.py                                        0      0   100%
src/infrastructure/database/database.py                                       12      6    50%
src/infrastructure/database/database_factory.py                               10      6    40%
src/infrastructure/database/models.py                                         47      0   100%
src/infrastructure/database/repositories/__init__.py                           0      0   100%
src/infrastructure/database/repositories/birthday_repository_impl.py          61     43    30%
src/infrastructure/database/repositories/holiday_repository_impl.py           48     33    31%
src/infrastructure/database/repositories/panel_access_repository_impl.py      15      7    53%
src/infrastructure/database/repositories/responsible_repository_impl.py       65     48    26%
src/infrastructure/external/__init__.py                                        0      0   100%
src/infrastructure/external/openrouter_client_impl.py                         56     47    16%
src/infrastructure/external/telegram_auth.py                                  43     32    26%
src/infrastructure/image/__init__.py                                           0      0   100%
src/infrastructure/image/card_generator.py                                    79     67    15%
src/infrastructure/services/__init__.py                                        0      0   100%
src/infrastructure/services/notification_service_impl.py                      87     69    21%
src/infrastructure/services/notifications_scheduler.py                        30     24    20%
src/presentation/__init__.py                                                   0      0   100%
src/presentation/telegram/__init__.py                                          0      0   100%
src/presentation/telegram/bot.py                                              26     22    15%
src/presentation/telegram/handlers/__init__.py                                 2      1    50%
src/presentation/telegram/handlers/birthday_handlers.py                       64     61     5%
src/presentation/telegram/handlers/calendar_handler.py                        72     72     0%
src/presentation/telegram/handlers/greeting_handlers.py                       87     87     0%
src/presentation/telegram/handlers/panel_handler.py                           17     17     0%
src/presentation/telegram/handlers/responsible_handlers.py                    45     45     0%
src/presentation/telegram/handlers/start_handler.py                            8      8     0%
src/presentation/telegram/keyboards.py                                        19     18     5%
src/presentation/web/__init__.py                                               0      0   100%
src/presentation/web/app.py                                                   15      2    87%
src/presentation/web/routes/__init__.py                                        0      0   100%
src/presentation/web/routes/api.py                                           248    170    31%
----------------------------------------------------------------------------------------------
TOTAL                                                                       1548   1038    33%
Coverage HTML written to dir htmlcov
Coverage XML written to file coverage.xml

=========================== short test summary info ============================
ERROR tests/presentation/telegram/test_bot.py
ERROR tests/presentation/telegram/test_keyboards.py
ERROR tests/presentation/telegram/handlers/test_birthday_handlers.py
ERROR tests/presentation/telegram/handlers/test_calendar_handler.py
ERROR tests/presentation/telegram/handlers/test_greeting_handlers.py
ERROR tests/presentation/telegram/handlers/test_panel_handler.py
ERROR tests/presentation/telegram/handlers/test_responsible_handlers.py
ERROR tests/presentation/telegram/handlers/test_start_handler.py
!!!!!!!!!!!!!!!!!!! Interrupted: 8 errors during collection !!!!!!!!!!!!!!!!!!!!
======================== 2 warnings, 8 errors in 3.87s =========================
Error: Process completed with exit code 2.
0s
0s
0s
0s
0s
Post job cleanup.
/usr/bin/git version
git version 2.52.0
Temporarily overriding HOME='/home/runner/work/_temp/81061409-a2d3-48b2-a676-b1f4626e712e' before making global git config changes
Adding repository directory to the temporary git global config as a safe directory
/usr/bin/git config --global --add safe.directory /home/runner/work/tg_bot_HB/tg_bot_HB
/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
http.https://github.com/.extraheader
/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
0s
Cleaning up orphan processes