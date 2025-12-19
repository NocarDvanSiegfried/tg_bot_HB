 trivy image tg_bot_hb-backend
2025-12-19T16:45:35Z    INFO    [vuln] Vulnerability scanning is enabled
2025-12-19T16:45:35Z    INFO    [secret] Secret scanning is enabled
2025-12-19T16:45:35Z    INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-12-19T16:45:35Z    INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2025-12-19T16:45:35Z    INFO    Detected OS     family="debian" version="13.2"
2025-12-19T16:45:35Z    INFO    [debian] Detecting vulnerabilities...   os_version="13" pkg_num=118
2025-12-19T16:45:35Z    INFO    Number of language-specific files       num=1
2025-12-19T16:45:35Z    INFO    [python-pkg] Detecting vulnerabilities...
2025-12-19T16:45:35Z    WARN    Using severities from other vendors for some vulnerabilities. Read https://trivy.dev/docs/v0.68/guide/scanner/vulnerability#severity-selection for details.
2025-12-19T16:45:36Z    INFO    Table result includes only package filenames. Use '--format json' option to get the full path to the package file.

Report Summary

┌──────────────────────────────────────────────────────────────────────────────────┬────────────┬─────────────────┬─────────┐
│                                      Target                                      │    Type    │ Vulnerabilities │ Secrets │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ tg_bot_hb-backend (debian 13.2)                                                  │   debian   │       326       │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/APScheduler-3.10.4.dist-info/METADATA     │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/Pillow-10.1.0.dist-info/METADATA          │ python-pkg │        2        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/SQLAlchemy-2.0.23.dist-info/METADATA      │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/aiofiles-25.1.0.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/aiogram-3.23.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/aiohappyeyeballs-2.6.1.dist-info/METADATA │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/aiohttp-3.13.2.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/aiosignal-1.4.0.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/alembic-1.12.1.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/annotated_types-0.7.0.dist-info/METADATA  │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/anyio-3.7.1.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/async_timeout-5.0.1.dist-info/METADATA    │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/asyncpg-0.29.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/attrs-25.4.0.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/certifi-2025.11.12.dist-info/METADATA     │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/click-8.3.1.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/deprecated-1.3.1.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/fastapi-0.104.1.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/frozenlist-1.8.0.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/greenlet-3.3.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/h11-0.16.0.dist-info/METADATA             │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/httpcore-1.0.9.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/httptools-0.7.1.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/httpx-0.25.1.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/idna-3.11.dist-info/METADATA              │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/limits-5.6.0.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/magic_filter-1.0.12.dist-info/METADATA    │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/mako-1.3.10.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/markupsafe-3.0.3.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/multidict-6.7.0.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/packaging-25.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pip-25.3.dist-info/METADATA               │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/propcache-0.4.1.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pydantic-2.5.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pydantic_core-2.14.1.dist-info/METADATA   │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pypng-0.20220715.0.dist-info/METADATA     │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/python_dotenv-1.0.0.dist-info/METADATA    │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pytz-2025.2.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pyyaml-6.0.3.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/qrcode-7.4.2.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools-79.0.1.dist-info/METADATA      │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/autocommand-2.2.2.dis- │ python-pkg │        0        │    -    │
│ t-info/METADATA                                                                  │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/backports.tarfile-1.2- │ python-pkg │        0        │    -    │
│ .0.dist-info/METADATA                                                            │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata-8.- │ python-pkg │        0        │    -    │
│ 0.0.dist-info/METADATA                                                           │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/inflect-7.3.1.dist-in- │ python-pkg │        0        │    -    │
│ fo/METADATA                                                                      │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/jaraco.collections-5.- │ python-pkg │        0        │    -    │
│ 1.0.dist-info/METADATA                                                           │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/jaraco.context-5.3.0.- │ python-pkg │        0        │    -    │
│ dist-info/METADATA                                                               │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/jaraco.functools-4.0.- │ python-pkg │        0        │    -    │
│ 1.dist-info/METADATA                                                             │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/jaraco.text-3.12.1.di- │ python-pkg │        0        │    -    │
│ st-info/METADATA                                                                 │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/more_itertools-10.3.0- │ python-pkg │        0        │    -    │
│ .dist-info/METADATA                                                              │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/packaging-24.2.dist-i- │ python-pkg │        0        │    -    │
│ nfo/METADATA                                                                     │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/platformdirs-4.2.2.di- │ python-pkg │        0        │    -    │
│ st-info/METADATA                                                                 │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/tomli-2.0.1.dist-info- │ python-pkg │        0        │    -    │
│ /METADATA                                                                        │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/typeguard-4.3.0.dist-- │ python-pkg │        0        │    -    │
│ info/METADATA                                                                    │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/typing_extensions-4.1- │ python-pkg │        0        │    -    │
│ 2.2.dist-info/METADATA                                                           │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/wheel-0.45.1.dist-inf- │ python-pkg │        0        │    -    │
│ o/METADATA                                                                       │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/zipp-3.19.2.dist-info- │ python-pkg │        0        │    -    │
│ /METADATA                                                                        │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/six-1.17.0.dist-info/METADATA             │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/slowapi-0.1.9.dist-info/METADATA          │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/sniffio-1.3.1.dist-info/METADATA          │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/starlette-0.27.0.dist-info/METADATA       │ python-pkg │        2        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/typing_extensions-4.15.0.dist-info/METAD- │ python-pkg │        0        │    -    │
│ ATA                                                                              │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/tzlocal-5.3.1.dist-info/METADATA          │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/uvicorn-0.24.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/uvloop-0.22.1.dist-info/METADATA          │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/watchfiles-1.1.1.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/websockets-15.0.1.dist-info/METADATA      │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/wheel-0.45.1.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/wrapt-2.0.1.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/yarl-1.22.0.dist-info/METADATA            │ python-pkg │        0        │    -    │
└──────────────────────────────────────────────────────────────────────────────────┴────────────┴─────────────────┴─────────┘
Legend:
- '-': Not scanned
- '0': Clean (no security findings detected)


tg_bot_hb-backend (debian 13.2)

Total: 326 (UNKNOWN: 0, LOW: 316, MEDIUM: 10, HIGH: 0, CRITICAL: 0)

┌───────────────────────────┬─────────────────────┬──────────┬──────────┬─────────────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│          Library          │    Vulnerability    │ Severity │  Status  │    Installed Version    │ Fixed Version │                            Title                             │
├───────────────────────────┼─────────────────────┼──────────┼──────────┼─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ apt                       │ CVE-2011-3374       │ LOW      │ affected │ 3.0.3                   │               │ It was found that apt-key in apt, all versions, do not       │
│                           │                     │          │          │                         │               │ correctly...                                                 │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2011-3374                    │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ bash                      │ TEMP-0841856-B18BAF │          │          │ 5.2.37-2+b5             │               │ [Privilege escalation possible to other user than root]      │
│                           │                     │          │          │                         │               │ https://security-tracker.debian.org/tracker/TEMP-0841856-B1- │
│                           │                     │          │          │                         │               │ 8BAF                                                         │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ binutils                  │ CVE-2017-13716      │          │          │ 2.44-3                  │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │          │                         │               │ in libiberty                                                 │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │          │                         │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │          │                         │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │          │                         │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │          │                         │               │ crash                                                        │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │          │                         │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │          │                         │               │ rust-demangle.c.                                             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11081      │          │          │                         │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11081                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11082      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11082                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11083      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11083                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11412      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │          │                         │               │ bfd_elf_gc_record_vtentry out-of-bounds                      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11412                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11413      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │          │                         │               │ elf_link_add_object_symbols out-of-bounds                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11413                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11414      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c get_link_hash_entry  │
│                           │                     │          │          │                         │               │ out-of-bounds                                                │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11414                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │          │                         │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │          │                         │               │ overflow                                                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │          │                         │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │          │                         │               │ leak                                                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │          │                         │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11494      │          │          │                         │               │ binutils: GNU Binutils Linker out-of-bounds read             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11494                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11495      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11495                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │          │                         │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │          │                         │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │          │                         │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │          │                         │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │          │                         │               │ heap-based overflow                                          │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │          │                         │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │          │                         │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │          │                         │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │          │                         │               │ memory corruption                                            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │          │                         │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11839      │          │          │                         │               │ binutils: GNU Binutils prdbg.c tg_tag_type return value      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11839                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11840      │          │          │                         │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11840                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │          │                         │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │          │                         │               │ leak                                                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │          │                         │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │          │                         │               │ memory corruption                                            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7545       │          │          │                         │               │ binutils: Binutils: Heap Buffer Overflow                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7545                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7546       │          │          │                         │               │ binutils: Binutils: Out-of-bounds Write Vulnerability        │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7546                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8225       │          │          │                         │               │ binutils: Binutils DWARF Section Handler Memory Leak         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-8225                    │
├───────────────────────────┼─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│ binutils-common           │ CVE-2017-13716      │          │          │                         │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │          │                         │               │ in libiberty                                                 │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │          │                         │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │          │                         │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │          │                         │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │          │                         │               │ crash                                                        │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │          │                         │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │          │                         │               │ rust-demangle.c.                                             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11081      │          │          │                         │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11081                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11082      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11082                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11083      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11083                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11412      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │          │                         │               │ bfd_elf_gc_record_vtentry out-of-bounds                      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11412                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11413      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │          │                         │               │ elf_link_add_object_symbols out-of-bounds                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11413                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11414      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c get_link_hash_entry  │
│                           │                     │          │          │                         │               │ out-of-bounds                                                │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11414                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │          │                         │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │          │                         │               │ overflow                                                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │          │                         │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │          │                         │               │ leak                                                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │          │                         │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11494      │          │          │                         │               │ binutils: GNU Binutils Linker out-of-bounds read             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11494                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11495      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11495                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │          │                         │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │          │                         │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │          │                         │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │          │                         │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │          │                         │               │ heap-based overflow                                          │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │          │                         │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │          │                         │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │          │                         │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │          │                         │               │ memory corruption                                            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │          │                         │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11839      │          │          │                         │               │ binutils: GNU Binutils prdbg.c tg_tag_type return value      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11839                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11840      │          │          │                         │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11840                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │          │                         │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │          │                         │               │ leak                                                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │          │                         │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │          │                         │               │ memory corruption                                            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7545       │          │          │                         │               │ binutils: Binutils: Heap Buffer Overflow                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7545                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7546       │          │          │                         │               │ binutils: Binutils: Out-of-bounds Write Vulnerability        │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7546                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8225       │          │          │                         │               │ binutils: Binutils DWARF Section Handler Memory Leak         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-8225                    │
├───────────────────────────┼─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│ binutils-x86-64-linux-gnu │ CVE-2017-13716      │          │          │                         │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │          │                         │               │ in libiberty                                                 │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │          │                         │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │          │                         │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │          │                         │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │          │                         │               │ crash                                                        │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │          │                         │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │          │                         │               │ rust-demangle.c.                                             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11081      │          │          │                         │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11081                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11082      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11082                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11083      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11083                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11412      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │          │                         │               │ bfd_elf_gc_record_vtentry out-of-bounds                      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11412                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11413      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │          │                         │               │ elf_link_add_object_symbols out-of-bounds                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11413                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11414      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c get_link_hash_entry  │
│                           │                     │          │          │                         │               │ out-of-bounds                                                │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11414                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │          │                         │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │          │                         │               │ overflow                                                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │          │                         │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │          │                         │               │ leak                                                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │          │                         │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11494      │          │          │                         │               │ binutils: GNU Binutils Linker out-of-bounds read             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11494                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11495      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11495                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │          │                         │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │          │                         │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │          │                         │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │          │                         │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │          │                         │               │ heap-based overflow                                          │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │          │                         │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │          │                         │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │          │                         │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │          │                         │               │ memory corruption                                            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │          │                         │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11839      │          │          │                         │               │ binutils: GNU Binutils prdbg.c tg_tag_type return value      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11839                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11840      │          │          │                         │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11840                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │          │                         │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │          │                         │               │ leak                                                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │          │                         │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │          │                         │               │ memory corruption                                            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7545       │          │          │                         │               │ binutils: Binutils: Heap Buffer Overflow                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7545                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7546       │          │          │                         │               │ binutils: Binutils: Out-of-bounds Write Vulnerability        │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7546                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8225       │          │          │                         │               │ binutils: Binutils DWARF Section Handler Memory Leak         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-8225                    │
├───────────────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ bsdutils                  │ CVE-2025-14104      │ MEDIUM   │          │ 1:2.41-5                │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                           │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                           ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ coreutils                 │ CVE-2017-18018      │          │          │ 9.7-3                   │               │ coreutils: race condition vulnerability in chown and chgrp   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2017-18018                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5278       │          │          │                         │               │ coreutils: Heap Buffer Under-Read in GNU Coreutils sort via  │
│                           │                     │          │          │                         │               │ Key Specification                                            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5278                    │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libapt-pkg7.0             │ CVE-2011-3374       │          │          │ 3.0.3                   │               │ It was found that apt-key in apt, all versions, do not       │
│                           │                     │          │          │                         │               │ correctly...                                                 │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2011-3374                    │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libbinutils               │ CVE-2017-13716      │          │          │ 2.44-3                  │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │          │                         │               │ in libiberty                                                 │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │          │                         │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │          │                         │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │          │                         │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │          │                         │               │ crash                                                        │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │          │                         │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │          │                         │               │ rust-demangle.c.                                             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11081      │          │          │                         │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11081                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11082      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11082                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11083      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11083                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11412      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │          │                         │               │ bfd_elf_gc_record_vtentry out-of-bounds                      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11412                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11413      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │          │                         │               │ elf_link_add_object_symbols out-of-bounds                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11413                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11414      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c get_link_hash_entry  │
│                           │                     │          │          │                         │               │ out-of-bounds                                                │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11414                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │          │                         │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │          │                         │               │ overflow                                                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │          │                         │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │          │                         │               │ leak                                                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │          │                         │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11494      │          │          │                         │               │ binutils: GNU Binutils Linker out-of-bounds read             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11494                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11495      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11495                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │          │                         │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │          │                         │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │          │                         │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │          │                         │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │          │                         │               │ heap-based overflow                                          │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │          │                         │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │          │                         │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │          │                         │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │          │                         │               │ memory corruption                                            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │          │                         │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11839      │          │          │                         │               │ binutils: GNU Binutils prdbg.c tg_tag_type return value      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11839                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11840      │          │          │                         │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11840                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │          │                         │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │          │                         │               │ leak                                                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │          │                         │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │          │                         │               │ memory corruption                                            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7545       │          │          │                         │               │ binutils: Binutils: Heap Buffer Overflow                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7545                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7546       │          │          │                         │               │ binutils: Binutils: Out-of-bounds Write Vulnerability        │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7546                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8225       │          │          │                         │               │ binutils: Binutils DWARF Section Handler Memory Leak         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-8225                    │
├───────────────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libblkid1                 │ CVE-2025-14104      │ MEDIUM   │          │ 2.41-5                  │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                           │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                           ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libc-bin                  │ CVE-2010-4756       │          │          │ 2.41-12                 │               │ glibc: glob implementation can cause excessive CPU and       │
│                           │                     │          │          │                         │               │ memory consumption due to...                                 │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2010-4756                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20796      │          │          │                         │               │ glibc: uncontrolled recursion in function                    │
│                           │                     │          │          │                         │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20796                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010022    │          │          │                         │               │ glibc: stack guard protection bypass                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-1010022                 │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010023    │          │          │                         │               │ glibc: running ldd on malicious ELF leads to code execution  │
│                           │                     │          │          │                         │               │ because of...                                                │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-1010023                 │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010024    │          │          │                         │               │ glibc: ASLR bypass using cache of thread stack and heap      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-1010024                 │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010025    │          │          │                         │               │ glibc: information disclosure of heap addresses of           │
│                           │                     │          │          │                         │               │ pthread_created thread                                       │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-1010025                 │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-9192       │          │          │                         │               │ glibc: uncontrolled recursion in function                    │
│                           │                     │          │          │                         │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-9192                    │
├───────────────────────────┼─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libc6                     │ CVE-2010-4756       │          │          │                         │               │ glibc: glob implementation can cause excessive CPU and       │
│                           │                     │          │          │                         │               │ memory consumption due to...                                 │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2010-4756                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20796      │          │          │                         │               │ glibc: uncontrolled recursion in function                    │
│                           │                     │          │          │                         │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20796                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010022    │          │          │                         │               │ glibc: stack guard protection bypass                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-1010022                 │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010023    │          │          │                         │               │ glibc: running ldd on malicious ELF leads to code execution  │
│                           │                     │          │          │                         │               │ because of...                                                │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-1010023                 │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010024    │          │          │                         │               │ glibc: ASLR bypass using cache of thread stack and heap      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-1010024                 │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010025    │          │          │                         │               │ glibc: information disclosure of heap addresses of           │
│                           │                     │          │          │                         │               │ pthread_created thread                                       │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-1010025                 │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-9192       │          │          │                         │               │ glibc: uncontrolled recursion in function                    │
│                           │                     │          │          │                         │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-9192                    │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libctf-nobfd0             │ CVE-2017-13716      │          │          │ 2.44-3                  │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │          │                         │               │ in libiberty                                                 │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │          │                         │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │          │                         │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │          │                         │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │          │                         │               │ crash                                                        │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │          │                         │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │          │                         │               │ rust-demangle.c.                                             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11081      │          │          │                         │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11081                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11082      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11082                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11083      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11083                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11412      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │          │                         │               │ bfd_elf_gc_record_vtentry out-of-bounds                      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11412                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11413      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │          │                         │               │ elf_link_add_object_symbols out-of-bounds                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11413                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11414      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c get_link_hash_entry  │
│                           │                     │          │          │                         │               │ out-of-bounds                                                │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11414                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │          │                         │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │          │                         │               │ overflow                                                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │          │                         │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │          │                         │               │ leak                                                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │          │                         │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11494      │          │          │                         │               │ binutils: GNU Binutils Linker out-of-bounds read             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11494                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11495      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11495                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │          │                         │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │          │                         │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │          │                         │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │          │                         │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │          │                         │               │ heap-based overflow                                          │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │          │                         │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │          │                         │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │          │                         │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │          │                         │               │ memory corruption                                            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │          │                         │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11839      │          │          │                         │               │ binutils: GNU Binutils prdbg.c tg_tag_type return value      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11839                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11840      │          │          │                         │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11840                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │          │                         │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │          │                         │               │ leak                                                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │          │                         │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │          │                         │               │ memory corruption                                            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7545       │          │          │                         │               │ binutils: Binutils: Heap Buffer Overflow                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7545                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7546       │          │          │                         │               │ binutils: Binutils: Out-of-bounds Write Vulnerability        │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7546                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8225       │          │          │                         │               │ binutils: Binutils DWARF Section Handler Memory Leak         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-8225                    │
├───────────────────────────┼─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libctf0                   │ CVE-2017-13716      │          │          │                         │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │          │                         │               │ in libiberty                                                 │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │          │                         │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │          │                         │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │          │                         │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │          │                         │               │ crash                                                        │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │          │                         │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │          │                         │               │ rust-demangle.c.                                             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11081      │          │          │                         │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11081                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11082      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11082                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11083      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11083                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11412      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │          │                         │               │ bfd_elf_gc_record_vtentry out-of-bounds                      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11412                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11413      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │          │                         │               │ elf_link_add_object_symbols out-of-bounds                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11413                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11414      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c get_link_hash_entry  │
│                           │                     │          │          │                         │               │ out-of-bounds                                                │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11414                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │          │                         │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │          │                         │               │ overflow                                                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │          │                         │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │          │                         │               │ leak                                                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │          │                         │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11494      │          │          │                         │               │ binutils: GNU Binutils Linker out-of-bounds read             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11494                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11495      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11495                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │          │                         │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │          │                         │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │          │                         │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │          │                         │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │          │                         │               │ heap-based overflow                                          │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │          │                         │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │          │                         │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │          │                         │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │          │                         │               │ memory corruption                                            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │          │                         │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11839      │          │          │                         │               │ binutils: GNU Binutils prdbg.c tg_tag_type return value      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11839                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11840      │          │          │                         │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11840                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │          │                         │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │          │                         │               │ leak                                                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │          │                         │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │          │                         │               │ memory corruption                                            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7545       │          │          │                         │               │ binutils: Binutils: Heap Buffer Overflow                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7545                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7546       │          │          │                         │               │ binutils: Binutils: Out-of-bounds Write Vulnerability        │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7546                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8225       │          │          │                         │               │ binutils: Binutils DWARF Section Handler Memory Leak         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-8225                    │
├───────────────────────────┼─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libgprofng0               │ CVE-2017-13716      │          │          │                         │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │          │                         │               │ in libiberty                                                 │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │          │                         │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │          │                         │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │          │                         │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │          │                         │               │ crash                                                        │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │          │                         │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │          │                         │               │ rust-demangle.c.                                             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11081      │          │          │                         │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11081                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11082      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11082                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11083      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11083                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11412      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │          │                         │               │ bfd_elf_gc_record_vtentry out-of-bounds                      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11412                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11413      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │          │                         │               │ elf_link_add_object_symbols out-of-bounds                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11413                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11414      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c get_link_hash_entry  │
│                           │                     │          │          │                         │               │ out-of-bounds                                                │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11414                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │          │                         │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │          │                         │               │ overflow                                                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │          │                         │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │          │                         │               │ leak                                                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │          │                         │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11494      │          │          │                         │               │ binutils: GNU Binutils Linker out-of-bounds read             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11494                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11495      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11495                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │          │                         │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │          │                         │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │          │                         │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │          │                         │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │          │                         │               │ heap-based overflow                                          │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │          │                         │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │          │                         │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │          │                         │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │          │                         │               │ memory corruption                                            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │          │                         │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11839      │          │          │                         │               │ binutils: GNU Binutils prdbg.c tg_tag_type return value      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11839                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11840      │          │          │                         │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11840                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │          │                         │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │          │                         │               │ leak                                                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │          │                         │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │          │                         │               │ memory corruption                                            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7545       │          │          │                         │               │ binutils: Binutils: Heap Buffer Overflow                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7545                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7546       │          │          │                         │               │ binutils: Binutils: Out-of-bounds Write Vulnerability        │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7546                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8225       │          │          │                         │               │ binutils: Binutils DWARF Section Handler Memory Leak         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-8225                    │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libjansson4               │ CVE-2020-36325      │          │          │ 2.14-2+b3               │               │ jansson: out-of-bounds read in json_loads() due to a parsing │
│                           │                     │          │          │                         │               │ error                                                        │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2020-36325                   │
├───────────────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ liblastlog2-2             │ CVE-2025-14104      │ MEDIUM   │          │ 2.41-5                  │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                           │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                           ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libmount1                 │ CVE-2025-14104      │ MEDIUM   │          │                         │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                           │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                           ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libncursesw6              │ CVE-2025-6141       │          │          │ 6.5+20250216-2          │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libsframe1                │ CVE-2017-13716      │          │          │ 2.44-3                  │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │          │                         │               │ in libiberty                                                 │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │          │                         │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │          │                         │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │          │                         │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │          │                         │               │ crash                                                        │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │          │                         │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │          │                         │               │ rust-demangle.c.                                             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11081      │          │          │                         │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11081                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11082      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11082                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11083      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11083                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11412      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │          │                         │               │ bfd_elf_gc_record_vtentry out-of-bounds                      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11412                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11413      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │          │                         │               │ elf_link_add_object_symbols out-of-bounds                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11413                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11414      │          │          │                         │               │ binutils: GNU Binutils Linker elflink.c get_link_hash_entry  │
│                           │                     │          │          │                         │               │ out-of-bounds                                                │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11414                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │          │                         │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │          │                         │               │ overflow                                                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │          │                         │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │          │                         │               │ leak                                                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │          │                         │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11494      │          │          │                         │               │ binutils: GNU Binutils Linker out-of-bounds read             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11494                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11495      │          │          │                         │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11495                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │          │                         │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │          │                         │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │          │                         │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │          │                         │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │          │                         │               │ heap-based overflow                                          │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │          │                         │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │          │                         │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │          │                         │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │          │                         │               │ memory corruption                                            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │          │                         │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11839      │          │          │                         │               │ binutils: GNU Binutils prdbg.c tg_tag_type return value      │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11839                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11840      │          │          │                         │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-11840                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │          │                         │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │          │                         │               │ leak                                                         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │          │                         │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │          │                         │               │ corruption                                                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │          │                         │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │          │                         │               │ memory corruption                                            │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7545       │          │          │                         │               │ binutils: Binutils: Heap Buffer Overflow                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7545                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7546       │          │          │                         │               │ binutils: Binutils: Out-of-bounds Write Vulnerability        │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7546                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8225       │          │          │                         │               │ binutils: Binutils DWARF Section Handler Memory Leak         │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-8225                    │
├───────────────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libsmartcols1             │ CVE-2025-14104      │ MEDIUM   │          │ 2.41-5                  │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                           │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                           ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libsqlite3-0              │ CVE-2025-7709       │ MEDIUM   │          │ 3.46.1-7                │               │ An integer overflow exists in the FTS5                       │
│                           │                     │          │          │                         │               │ https://sqlite.org/fts5.html e ...                           │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7709                    │
│                           ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-45346      │ LOW      │          │                         │               │ sqlite: crafted SQL query allows a malicious user to obtain  │
│                           │                     │          │          │                         │               │ sensitive information...                                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2021-45346                   │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libsystemd0               │ CVE-2013-4392       │          │          │ 257.9-1~deb13u1         │               │ systemd: TOCTOU race condition when updating file            │
│                           │                     │          │          │                         │               │ permissions and SELinux security contexts...                 │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2013-4392                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31437      │          │          │                         │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │          │                         │               │ modify a...                                                  │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2023-31437                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31438      │          │          │                         │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │          │                         │               │ truncate a...                                                │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2023-31438                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31439      │          │          │                         │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │          │                         │               │ modify the...                                                │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2023-31439                   │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libtinfo6                 │ CVE-2025-6141       │          │          │ 6.5+20250216-2          │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libudev1                  │ CVE-2013-4392       │          │          │ 257.9-1~deb13u1         │               │ systemd: TOCTOU race condition when updating file            │
│                           │                     │          │          │                         │               │ permissions and SELinux security contexts...                 │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2013-4392                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31437      │          │          │                         │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │          │                         │               │ modify a...                                                  │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2023-31437                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31438      │          │          │                         │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │          │                         │               │ truncate a...                                                │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2023-31438                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31439      │          │          │                         │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │          │                         │               │ modify the...                                                │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2023-31439                   │
├───────────────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libuuid1                  │ CVE-2025-14104      │ MEDIUM   │          │ 2.41-5                  │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                           │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                           ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ login                     │ CVE-2025-14104      │ MEDIUM   │          │ 1:4.16.0-2+really2.41-5 │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                           │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                           ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ login.defs                │ CVE-2007-5686       │          │          │ 1:4.17.4-2              │               │ initscripts in rPath Linux 1 sets insecure permissions for   │
│                           │                     │          │          │                         │               │ the /var/lo ......                                           │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2007-5686                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-56433      │          │          │                         │               │ shadow-utils: Default subordinate ID configuration in        │
│                           │                     │          │          │                         │               │ /etc/login.defs could lead to compromise                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2024-56433                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ TEMP-0628843-DBAD28 │          │          │                         │               │ [more related to CVE-2005-4890]                              │
│                           │                     │          │          │                         │               │ https://security-tracker.debian.org/tracker/TEMP-0628843-DB- │
│                           │                     │          │          │                         │               │ AD28                                                         │
├───────────────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ mount                     │ CVE-2025-14104      │ MEDIUM   │          │ 2.41-5                  │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                           │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                           ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ ncurses-base              │ CVE-2025-6141       │          │          │ 6.5+20250216-2          │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├───────────────────────────┤                     │          │          │                         ├───────────────┤                                                              │
│ ncurses-bin               │                     │          │          │                         │               │                                                              │
│                           │                     │          │          │                         │               │                                                              │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ passwd                    │ CVE-2007-5686       │          │          │ 1:4.17.4-2              │               │ initscripts in rPath Linux 1 sets insecure permissions for   │
│                           │                     │          │          │                         │               │ the /var/lo ......                                           │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2007-5686                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-56433      │          │          │                         │               │ shadow-utils: Default subordinate ID configuration in        │
│                           │                     │          │          │                         │               │ /etc/login.defs could lead to compromise                     │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2024-56433                   │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ TEMP-0628843-DBAD28 │          │          │                         │               │ [more related to CVE-2005-4890]                              │
│                           │                     │          │          │                         │               │ https://security-tracker.debian.org/tracker/TEMP-0628843-DB- │
│                           │                     │          │          │                         │               │ AD28                                                         │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ perl-base                 │ CVE-2011-4116       │          │          │ 5.40.1-6                │               │ perl: File:: Temp insecure temporary file handling           │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2011-4116                    │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ sysvinit-utils            │ TEMP-0517018-A83CE6 │          │          │ 3.14-4                  │               │ [sysvinit: no-root option in expert installer exposes        │
│                           │                     │          │          │                         │               │ locally exploitable security flaw]                           │
│                           │                     │          │          │                         │               │ https://security-tracker.debian.org/tracker/TEMP-0517018-A8- │
│                           │                     │          │          │                         │               │ 3CE6                                                         │
├───────────────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ tar                       │ CVE-2005-2541       │          │          │ 1.35+dfsg-3.1           │               │ tar: does not properly warn the user when extracting setuid  │
│                           │                     │          │          │                         │               │ or setgid...                                                 │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2005-2541                    │
│                           ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ TEMP-0290435-0B57B5 │          │          │                         │               │ [tar's rmt command may have undesired side effects]          │
│                           │                     │          │          │                         │               │ https://security-tracker.debian.org/tracker/TEMP-0290435-0B- │
│                           │                     │          │          │                         │               │ 57B5                                                         │
├───────────────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ util-linux                │ CVE-2025-14104      │ MEDIUM   │          │ 2.41-5                  │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                           │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                           ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                           │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
└───────────────────────────┴─────────────────────┴──────────┴──────────┴─────────────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘

Python (python-pkg)

Total: 4 (UNKNOWN: 0, LOW: 0, MEDIUM: 1, HIGH: 2, CRITICAL: 1)

┌──────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────┐
│       Library        │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                        Title                         │
├──────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────┤
│ Pillow (METADATA)    │ CVE-2023-50447 │ CRITICAL │ fixed  │ 10.1.0            │ 10.2.0        │ pillow: Arbitrary Code Execution via the environment │
│                      │                │          │        │                   │               │ parameter                                            │
│                      │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2023-50447           │
│                      ├────────────────┼──────────┤        │                   ├───────────────┼──────────────────────────────────────────────────────┤
│                      │ CVE-2024-28219 │ HIGH     │        │                   │ 10.3.0        │ python-pillow: buffer overflow in _imagingcms.c      │
│                      │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2024-28219           │
├──────────────────────┼────────────────┤          │        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────┤
│ starlette (METADATA) │ CVE-2024-47874 │          │        │ 0.27.0            │ 0.40.0        │ starlette: Starlette Denial of service (DoS) via     │
│                      │                │          │        │                   │               │ multipart/form-data                                  │
│                      │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2024-47874           │
│                      ├────────────────┼──────────┤        │                   ├───────────────┼──────────────────────────────────────────────────────┤
│                      │ CVE-2025-54121 │ MEDIUM   │        │                   │ 0.47.2        │ starlette: Starlette denial-of-service               │
│                      │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2025-54121           │
└──────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴───────────────────────────────────────────────────

trivy image --severity HIGH,CRITICAL tg_bot_hb-backend
2025-12-19T16:51:23Z    INFO    [vuln] Vulnerability scanning is enabled
2025-12-19T16:51:23Z    INFO    [secret] Secret scanning is enabled
2025-12-19T16:51:23Z    INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-12-19T16:51:23Z    INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2025-12-19T16:51:23Z    INFO    Detected OS     family="debian" version="13.2"
2025-12-19T16:51:23Z    INFO    [debian] Detecting vulnerabilities...   os_version="13" pkg_num=118
2025-12-19T16:51:23Z    INFO    Number of language-specific files       num=1
2025-12-19T16:51:23Z    INFO    [python-pkg] Detecting vulnerabilities...
2025-12-19T16:51:23Z    WARN    Using severities from other vendors for some vulnerabilities. Read https://trivy.dev/docs/v0.68/guide/scanner/vulnerability#severity-selection for details.
2025-12-19T16:51:23Z    INFO    Table result includes only package filenames. Use '--format json' option to get the full path to the package file.

Report Summary

┌──────────────────────────────────────────────────────────────────────────────────┬────────────┬─────────────────┬─────────┐
│                                      Target                                      │    Type    │ Vulnerabilities │ Secrets │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ tg_bot_hb-backend (debian 13.2)                                                  │   debian   │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/APScheduler-3.10.4.dist-info/METADATA     │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/Pillow-10.1.0.dist-info/METADATA          │ python-pkg │        2        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/SQLAlchemy-2.0.23.dist-info/METADATA      │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/aiofiles-25.1.0.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/aiogram-3.23.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/aiohappyeyeballs-2.6.1.dist-info/METADATA │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/aiohttp-3.13.2.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/aiosignal-1.4.0.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/alembic-1.12.1.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/annotated_types-0.7.0.dist-info/METADATA  │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/anyio-3.7.1.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/async_timeout-5.0.1.dist-info/METADATA    │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/asyncpg-0.29.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/attrs-25.4.0.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/certifi-2025.11.12.dist-info/METADATA     │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/click-8.3.1.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/deprecated-1.3.1.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/fastapi-0.104.1.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/frozenlist-1.8.0.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/greenlet-3.3.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/h11-0.16.0.dist-info/METADATA             │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/httpcore-1.0.9.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/httptools-0.7.1.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/httpx-0.25.1.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/idna-3.11.dist-info/METADATA              │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/limits-5.6.0.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/magic_filter-1.0.12.dist-info/METADATA    │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/mako-1.3.10.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/markupsafe-3.0.3.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/multidict-6.7.0.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/packaging-25.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pip-25.3.dist-info/METADATA               │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/propcache-0.4.1.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pydantic-2.5.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pydantic_core-2.14.1.dist-info/METADATA   │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pypng-0.20220715.0.dist-info/METADATA     │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/python_dotenv-1.0.0.dist-info/METADATA    │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pytz-2025.2.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pyyaml-6.0.3.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/qrcode-7.4.2.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools-79.0.1.dist-info/METADATA      │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/autocommand-2.2.2.dis- │ python-pkg │        0        │    -    │
│ t-info/METADATA                                                                  │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/backports.tarfile-1.2- │ python-pkg │        0        │    -    │
│ .0.dist-info/METADATA                                                            │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata-8.- │ python-pkg │        0        │    -    │
│ 0.0.dist-info/METADATA                                                           │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/inflect-7.3.1.dist-in- │ python-pkg │        0        │    -    │
│ fo/METADATA                                                                      │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/jaraco.collections-5.- │ python-pkg │        0        │    -    │
│ 1.0.dist-info/METADATA                                                           │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/jaraco.context-5.3.0.- │ python-pkg │        0        │    -    │
│ dist-info/METADATA                                                               │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/jaraco.functools-4.0.- │ python-pkg │        0        │    -    │
│ 1.dist-info/METADATA                                                             │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/jaraco.text-3.12.1.di- │ python-pkg │        0        │    -    │
│ st-info/METADATA                                                                 │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/more_itertools-10.3.0- │ python-pkg │        0        │    -    │
│ .dist-info/METADATA                                                              │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/packaging-24.2.dist-i- │ python-pkg │        0        │    -    │
│ nfo/METADATA                                                                     │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/platformdirs-4.2.2.di- │ python-pkg │        0        │    -    │
│ st-info/METADATA                                                                 │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/tomli-2.0.1.dist-info- │ python-pkg │        0        │    -    │
│ /METADATA                                                                        │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/typeguard-4.3.0.dist-- │ python-pkg │        0        │    -    │
│ info/METADATA                                                                    │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/typing_extensions-4.1- │ python-pkg │        0        │    -    │
│ 2.2.dist-info/METADATA                                                           │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/wheel-0.45.1.dist-inf- │ python-pkg │        0        │    -    │
│ o/METADATA                                                                       │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/zipp-3.19.2.dist-info- │ python-pkg │        0        │    -    │
│ /METADATA                                                                        │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/six-1.17.0.dist-info/METADATA             │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/slowapi-0.1.9.dist-info/METADATA          │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/sniffio-1.3.1.dist-info/METADATA          │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/starlette-0.27.0.dist-info/METADATA       │ python-pkg │        1        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/typing_extensions-4.15.0.dist-info/METAD- │ python-pkg │        0        │    -    │
│ ATA                                                                              │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/tzlocal-5.3.1.dist-info/METADATA          │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/uvicorn-0.24.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/uvloop-0.22.1.dist-info/METADATA          │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/watchfiles-1.1.1.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/websockets-15.0.1.dist-info/METADATA      │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/wheel-0.45.1.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/wrapt-2.0.1.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/yarl-1.22.0.dist-info/METADATA            │ python-pkg │        0        │    -    │
└──────────────────────────────────────────────────────────────────────────────────┴────────────┴─────────────────┴─────────┘
Legend:
- '-': Not scanned
- '0': Clean (no security findings detected)


Python (python-pkg)

Total: 3 (HIGH: 2, CRITICAL: 1)

┌──────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────┐
│       Library        │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                        Title                         │
├──────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────┤
│ Pillow (METADATA)    │ CVE-2023-50447 │ CRITICAL │ fixed  │ 10.1.0            │ 10.2.0        │ pillow: Arbitrary Code Execution via the environment │
│                      │                │          │        │                   │               │ parameter                                            │
│                      │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2023-50447           │
│                      ├────────────────┼──────────┤        │                   ├───────────────┼──────────────────────────────────────────────────────┤
│                      │ CVE-2024-28219 │ HIGH     │        │                   │ 10.3.0        │ python-pillow: buffer overflow in _imagingcms.c      │
│                      │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2024-28219           │
├──────────────────────┼────────────────┤          │        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────┤
│ starlette (METADATA) │ CVE-2024-47874 │          │        │ 0.27.0            │ 0.40.0        │ starlette: Starlette Denial of service (DoS) via     │
│                      │                │          │        │                   │               │ multipart/form-data                                  │
│                      │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2024-47874           │
└──────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────┘
root@server-cqfsqu:~/tg_bot_HB# trivy image --ignore-unfixed tg_bot_hb-backend
2025-12-19T16:51:31Z    INFO    [vuln] Vulnerability scanning is enabled
2025-12-19T16:51:31Z    INFO    [secret] Secret scanning is enabled
2025-12-19T16:51:31Z    INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-12-19T16:51:31Z    INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2025-12-19T16:51:31Z    INFO    Detected OS     family="debian" version="13.2"
2025-12-19T16:51:31Z    INFO    [debian] Detecting vulnerabilities...   os_version="13" pkg_num=118
2025-12-19T16:51:31Z    INFO    Number of language-specific files       num=1
2025-12-19T16:51:31Z    INFO    [python-pkg] Detecting vulnerabilities...
2025-12-19T16:51:31Z    WARN    Using severities from other vendors for some vulnerabilities. Read https://trivy.dev/docs/v0.68/guide/scanner/vulnerability#severity-selection for details.
2025-12-19T16:51:31Z    INFO    Table result includes only package filenames. Use '--format json' option to get the full path to the package file.

Report Summary

┌──────────────────────────────────────────────────────────────────────────────────┬────────────┬─────────────────┬─────────┐
│                                      Target                                      │    Type    │ Vulnerabilities │ Secrets │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ tg_bot_hb-backend (debian 13.2)                                                  │   debian   │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/APScheduler-3.10.4.dist-info/METADATA     │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/Pillow-10.1.0.dist-info/METADATA          │ python-pkg │        2        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/SQLAlchemy-2.0.23.dist-info/METADATA      │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/aiofiles-25.1.0.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/aiogram-3.23.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/aiohappyeyeballs-2.6.1.dist-info/METADATA │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/aiohttp-3.13.2.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/aiosignal-1.4.0.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/alembic-1.12.1.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/annotated_types-0.7.0.dist-info/METADATA  │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/anyio-3.7.1.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/async_timeout-5.0.1.dist-info/METADATA    │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/asyncpg-0.29.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/attrs-25.4.0.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/certifi-2025.11.12.dist-info/METADATA     │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/click-8.3.1.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/deprecated-1.3.1.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/fastapi-0.104.1.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/frozenlist-1.8.0.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/greenlet-3.3.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/h11-0.16.0.dist-info/METADATA             │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/httpcore-1.0.9.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/httptools-0.7.1.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/httpx-0.25.1.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/idna-3.11.dist-info/METADATA              │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/limits-5.6.0.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/magic_filter-1.0.12.dist-info/METADATA    │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/mako-1.3.10.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/markupsafe-3.0.3.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/multidict-6.7.0.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/packaging-25.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pip-25.3.dist-info/METADATA               │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/propcache-0.4.1.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pydantic-2.5.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pydantic_core-2.14.1.dist-info/METADATA   │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pypng-0.20220715.0.dist-info/METADATA     │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/python_dotenv-1.0.0.dist-info/METADATA    │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pytz-2025.2.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/pyyaml-6.0.3.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/qrcode-7.4.2.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools-79.0.1.dist-info/METADATA      │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/autocommand-2.2.2.dis- │ python-pkg │        0        │    -    │
│ t-info/METADATA                                                                  │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/backports.tarfile-1.2- │ python-pkg │        0        │    -    │
│ .0.dist-info/METADATA                                                            │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/importlib_metadata-8.- │ python-pkg │        0        │    -    │
│ 0.0.dist-info/METADATA                                                           │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/inflect-7.3.1.dist-in- │ python-pkg │        0        │    -    │
│ fo/METADATA                                                                      │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/jaraco.collections-5.- │ python-pkg │        0        │    -    │
│ 1.0.dist-info/METADATA                                                           │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/jaraco.context-5.3.0.- │ python-pkg │        0        │    -    │
│ dist-info/METADATA                                                               │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/jaraco.functools-4.0.- │ python-pkg │        0        │    -    │
│ 1.dist-info/METADATA                                                             │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/jaraco.text-3.12.1.di- │ python-pkg │        0        │    -    │
│ st-info/METADATA                                                                 │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/more_itertools-10.3.0- │ python-pkg │        0        │    -    │
│ .dist-info/METADATA                                                              │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/packaging-24.2.dist-i- │ python-pkg │        0        │    -    │
│ nfo/METADATA                                                                     │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/platformdirs-4.2.2.di- │ python-pkg │        0        │    -    │
│ st-info/METADATA                                                                 │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/tomli-2.0.1.dist-info- │ python-pkg │        0        │    -    │
│ /METADATA                                                                        │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/typeguard-4.3.0.dist-- │ python-pkg │        0        │    -    │
│ info/METADATA                                                                    │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/typing_extensions-4.1- │ python-pkg │        0        │    -    │
│ 2.2.dist-info/METADATA                                                           │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/wheel-0.45.1.dist-inf- │ python-pkg │        0        │    -    │
│ o/METADATA                                                                       │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/setuptools/_vendor/zipp-3.19.2.dist-info- │ python-pkg │        0        │    -    │
│ /METADATA                                                                        │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/six-1.17.0.dist-info/METADATA             │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/slowapi-0.1.9.dist-info/METADATA          │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/sniffio-1.3.1.dist-info/METADATA          │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/starlette-0.27.0.dist-info/METADATA       │ python-pkg │        2        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/typing_extensions-4.15.0.dist-info/METAD- │ python-pkg │        0        │    -    │
│ ATA                                                                              │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/tzlocal-5.3.1.dist-info/METADATA          │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/uvicorn-0.24.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/uvloop-0.22.1.dist-info/METADATA          │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/watchfiles-1.1.1.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/websockets-15.0.1.dist-info/METADATA      │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/wheel-0.45.1.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/wrapt-2.0.1.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/yarl-1.22.0.dist-info/METADATA            │ python-pkg │        0        │    -    │
└──────────────────────────────────────────────────────────────────────────────────┴────────────┴─────────────────┴─────────┘
Legend:
- '-': Not scanned
- '0': Clean (no security findings detected)


Python (python-pkg)

Total: 4 (UNKNOWN: 0, LOW: 0, MEDIUM: 1, HIGH: 2, CRITICAL: 1)

┌──────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────┐
│       Library        │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                        Title                         │
├──────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────┤
│ Pillow (METADATA)    │ CVE-2023-50447 │ CRITICAL │ fixed  │ 10.1.0            │ 10.2.0        │ pillow: Arbitrary Code Execution via the environment │
│                      │                │          │        │                   │               │ parameter                                            │
│                      │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2023-50447           │
│                      ├────────────────┼──────────┤        │                   ├───────────────┼──────────────────────────────────────────────────────┤
│                      │ CVE-2024-28219 │ HIGH     │        │                   │ 10.3.0        │ python-pillow: buffer overflow in _imagingcms.c      │
│                      │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2024-28219           │
├──────────────────────┼────────────────┤          │        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────┤
│ starlette (METADATA) │ CVE-2024-47874 │          │        │ 0.27.0            │ 0.40.0        │ starlette: Starlette Denial of service (DoS) via     │
│                      │                │          │        │                   │               │ multipart/form-data                                  │
│                      │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2024-47874           │
│                      ├────────────────┼──────────┤        │                   ├───────────────┼──────────────────────────────────────────────────────┤
│                      │ CVE-2025-54121 │ MEDIUM   │        │                   │ 0.47.2        │ starlette: Starlette denial-of-service               │
│                      │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2025-54121           │
└──────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────┘