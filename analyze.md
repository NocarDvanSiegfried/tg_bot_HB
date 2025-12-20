  trivy image tg_bot_hb-backend
   trivy image --severity CRITICAL,HIGH,MEDIUM,UNKNOWN tg_bot_hb-backend
2025-12-20T03:04:00Z    INFO    [vuln] Vulnerability scanning is enabled
2025-12-20T03:04:00Z    INFO    [secret] Secret scanning is enabled
2025-12-20T03:04:00Z    INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-12-20T03:04:00Z    INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2025-12-20T03:04:22Z    INFO    [python] Licenses acquired from one or more METADATA files may be subject to additional terms. Use `--debug` flag to see all affected packages.
2025-12-20T03:04:22Z    INFO    Detected OS     family="debian" version="12.12"
2025-12-20T03:04:22Z    INFO    [debian] Detecting vulnerabilities...   os_version="12" pkg_num=130
2025-12-20T03:04:22Z    INFO    Number of language-specific files       num=1
2025-12-20T03:04:22Z    INFO    [python-pkg] Detecting vulnerabilities...
2025-12-20T03:04:22Z    WARN    Using severities from other vendors for some vulnerabilities. Read https://trivy.dev/docs/v0.68/guide/scanner/vulnerability#severity-selection for details.

Report Summary

┌──────────────────────────────────────────────────────────────────────────────────┬────────────┬─────────────────┬─────────┐
│                                      Target                                      │    Type    │ Vulnerabilities │ Secrets │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ tg_bot_hb-backend (debian 12.12)                                                 │   debian   │       390       │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/APScheduler-3.10.4.dist-info/METADATA     │ python-pkg │        0        │    -    │
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
│ usr/local/lib/python3.11/site-packages/annotated_doc-0.0.4.dist-info/METADATA    │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/annotated_types-0.7.0.dist-info/METADATA  │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/anyio-4.12.0.dist-info/METADATA           │ python-pkg │        0        │    -    │
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
│ usr/local/lib/python3.11/site-packages/fastapi-0.125.0.dist-info/METADATA        │ python-pkg │        0        │    -    │
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
│ usr/local/lib/python3.11/site-packages/pillow-12.0.0.dist-info/METADATA          │ python-pkg │        0        │    -    │
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
│ usr/local/lib/python3.11/site-packages/starlette-0.50.0.dist-info/METADATA       │ python-pkg │        0        │    -    │
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


tg_bot_hb-backend (debian 12.12)

Total: 390 (UNKNOWN: 1, LOW: 361, MEDIUM: 22, HIGH: 4, CRITICAL: 2)

┌───────────────────────────┬─────────────────────┬──────────┬──────────────┬────────────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│          Library          │    Vulnerability    │ Severity │    Status    │   Installed Version    │ Fixed Version │                            Title                             │
├───────────────────────────┼─────────────────────┼──────────┼──────────────┼────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ apt                       │ CVE-2011-3374       │ LOW      │ affected     │ 2.6.1                  │               │ It was found that apt-key in apt, all versions, do not       │
│                           │                     │          │              │                        │               │ correctly...                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2011-3374                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ bash                      │ TEMP-0841856-B18BAF │          │              │ 5.2.15-2+b9            │               │ [Privilege escalation possible to other user than root]      │
│                           │                     │          │              │                        │               │ https://security-tracker.debian.org/tracker/TEMP-0841856-B1- │
│                           │                     │          │              │                        │               │ 8BAF                                                         │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ binutils                  │ CVE-2017-13716      │          │              │ 2.40-2                 │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │              │                        │               │ in libiberty                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │              │                        │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │              │                        │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │              │                        │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │              │                        │               │ crash                                                        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │              │                        │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │              │                        │               │ rust-demangle.c.                                             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-1972       │          │              │                        │               │ binutils: Illegal memory access when accessing a             │
│                           │                     │          │              │                        │               │ zer0-lengthverdef table                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-1972                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-53589      │          │              │                        │               │ binutils: objdump: buffer Overflow in the BFD library's      │
│                           │                     │          │              │                        │               │ handling of tekhex format...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-53589                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-57360      │          │              │                        │               │ binutils: nm: potential segmentation fault when displaying   │
│                           │                     │          │              │                        │               │ symbols without version info                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-57360                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-0840       │          │              │                        │               │ binutils: GNU Binutils objdump.c disassemble_bytes           │
│                           │                     │          │              │                        │               │ stack-based overflow                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-0840                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11081      │          │              │                        │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11081                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11082      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11082                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11083      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11083                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11412      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │              │                        │               │ bfd_elf_gc_record_vtentry out-of-bounds                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11412                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11413      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │              │                        │               │ elf_link_add_object_symbols out-of-bounds                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11413                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11414      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c get_link_hash_entry  │
│                           │                     │          │              │                        │               │ out-of-bounds                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11414                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │              │                        │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │              │                        │               │ overflow                                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │              │                        │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │              │                        │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11494      │          │              │                        │               │ binutils: GNU Binutils Linker out-of-bounds read             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11494                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11495      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11495                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │              │                        │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │              │                        │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │              │                        │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ heap-based overflow                                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1179       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1179                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │              │                        │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │              │                        │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │              │                        │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11839      │          │              │                        │               │ binutils: GNU Binutils prdbg.c tg_tag_type return value      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11839                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11840      │          │              │                        │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11840                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │              │                        │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │              │                        │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7545       │          │              │                        │               │ binutils: Binutils: Heap Buffer Overflow                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-7545                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7546       │          │              │                        │               │ binutils: Binutils: Out-of-bounds Write Vulnerability        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-7546                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8224       │          │              │                        │               │ binutils: Binutils BFD Null Pointer Dereference              │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-8224                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8225       │          │              │                        │               │ binutils: Binutils DWARF Section Handler Memory Leak         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-8225                    │
├───────────────────────────┼─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ binutils-common           │ CVE-2017-13716      │          │              │                        │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │              │                        │               │ in libiberty                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │              │                        │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │              │                        │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │              │                        │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │              │                        │               │ crash                                                        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │              │                        │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │              │                        │               │ rust-demangle.c.                                             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-1972       │          │              │                        │               │ binutils: Illegal memory access when accessing a             │
│                           │                     │          │              │                        │               │ zer0-lengthverdef table                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-1972                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-53589      │          │              │                        │               │ binutils: objdump: buffer Overflow in the BFD library's      │
│                           │                     │          │              │                        │               │ handling of tekhex format...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-53589                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-57360      │          │              │                        │               │ binutils: nm: potential segmentation fault when displaying   │
│                           │                     │          │              │                        │               │ symbols without version info                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-57360                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-0840       │          │              │                        │               │ binutils: GNU Binutils objdump.c disassemble_bytes           │
│                           │                     │          │              │                        │               │ stack-based overflow                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-0840                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11081      │          │              │                        │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11081                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11082      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11082                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11083      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11083                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11412      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │              │                        │               │ bfd_elf_gc_record_vtentry out-of-bounds                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11412                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11413      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │              │                        │               │ elf_link_add_object_symbols out-of-bounds                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11413                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11414      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c get_link_hash_entry  │
│                           │                     │          │              │                        │               │ out-of-bounds                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11414                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │              │                        │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │              │                        │               │ overflow                                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │              │                        │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │              │                        │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11494      │          │              │                        │               │ binutils: GNU Binutils Linker out-of-bounds read             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11494                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11495      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11495                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │              │                        │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │              │                        │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │              │                        │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ heap-based overflow                                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1179       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1179                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │              │                        │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │              │                        │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │              │                        │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11839      │          │              │                        │               │ binutils: GNU Binutils prdbg.c tg_tag_type return value      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11839                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11840      │          │              │                        │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11840                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │              │                        │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │              │                        │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7545       │          │              │                        │               │ binutils: Binutils: Heap Buffer Overflow                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-7545                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7546       │          │              │                        │               │ binutils: Binutils: Out-of-bounds Write Vulnerability        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-7546                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8224       │          │              │                        │               │ binutils: Binutils BFD Null Pointer Dereference              │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-8224                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8225       │          │              │                        │               │ binutils: Binutils DWARF Section Handler Memory Leak         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-8225                    │
├───────────────────────────┼─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ binutils-x86-64-linux-gnu │ CVE-2017-13716      │          │              │                        │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │              │                        │               │ in libiberty                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │              │                        │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │              │                        │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │              │                        │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │              │                        │               │ crash                                                        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │              │                        │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │              │                        │               │ rust-demangle.c.                                             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-1972       │          │              │                        │               │ binutils: Illegal memory access when accessing a             │
│                           │                     │          │              │                        │               │ zer0-lengthverdef table                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-1972                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-53589      │          │              │                        │               │ binutils: objdump: buffer Overflow in the BFD library's      │
│                           │                     │          │              │                        │               │ handling of tekhex format...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-53589                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-57360      │          │              │                        │               │ binutils: nm: potential segmentation fault when displaying   │
│                           │                     │          │              │                        │               │ symbols without version info                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-57360                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-0840       │          │              │                        │               │ binutils: GNU Binutils objdump.c disassemble_bytes           │
│                           │                     │          │              │                        │               │ stack-based overflow                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-0840                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11081      │          │              │                        │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11081                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11082      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11082                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11083      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11083                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11412      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │              │                        │               │ bfd_elf_gc_record_vtentry out-of-bounds                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11412                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11413      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │              │                        │               │ elf_link_add_object_symbols out-of-bounds                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11413                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11414      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c get_link_hash_entry  │
│                           │                     │          │              │                        │               │ out-of-bounds                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11414                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │              │                        │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │              │                        │               │ overflow                                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │              │                        │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │              │                        │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11494      │          │              │                        │               │ binutils: GNU Binutils Linker out-of-bounds read             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11494                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11495      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11495                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │              │                        │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │              │                        │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │              │                        │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ heap-based overflow                                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1179       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1179                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │              │                        │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │              │                        │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │              │                        │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11839      │          │              │                        │               │ binutils: GNU Binutils prdbg.c tg_tag_type return value      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11839                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11840      │          │              │                        │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11840                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │              │                        │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │              │                        │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7545       │          │              │                        │               │ binutils: Binutils: Heap Buffer Overflow                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-7545                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7546       │          │              │                        │               │ binutils: Binutils: Out-of-bounds Write Vulnerability        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-7546                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8224       │          │              │                        │               │ binutils: Binutils BFD Null Pointer Dereference              │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-8224                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8225       │          │              │                        │               │ binutils: Binutils DWARF Section Handler Memory Leak         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-8225                    │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ bsdutils                  │ CVE-2025-14104      │ MEDIUM   │              │ 1:2.38.1-5+deb12u3     │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                           │                     │          │              │                        │               │ when processing 256-byte usernames                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-0563       │ LOW      │              │                        │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │              │                        │               │ and chsh when compiled...                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┤          ├──────────────┼────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ coreutils                 │ CVE-2016-2781       │          │ will_not_fix │ 9.1-1                  │               │ coreutils: Non-privileged session can escape to the parent   │
│                           │                     │          │              │                        │               │ session in chroot                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2016-2781                    │
│                           ├─────────────────────┤          ├──────────────┤                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2017-18018      │          │ affected     │                        │               │ coreutils: race condition vulnerability in chown and chgrp   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-18018                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5278       │          │              │                        │               │ coreutils: Heap Buffer Under-Read in GNU Coreutils sort via  │
│                           │                     │          │              │                        │               │ Key Specification                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5278                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ cpp-12                    │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ dpkg                      │ CVE-2025-6297       │          │              │ 1.21.22                │               │ It was discovered that dpkg-deb does not properly sanitize   │
│                           │                     │          │              │                        │               │ directory p ......                                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-6297                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ gcc-12                    │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┤                     │          │              │                        ├───────────────┤                                                              │
│ gcc-12-base               │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ gpgv                      │ CVE-2025-30258      │ MEDIUM   │              │ 2.2.40-1.1+deb12u1     │               │ gnupg: verification DoS due to a malicious subkey in the     │
│                           │                     │          │              │                        │               │ keyring                                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-30258                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-3219       │ LOW      │              │                        │               │ gnupg: denial of service issue (resource consumption) using  │
│                           │                     │          │              │                        │               │ compressed packets                                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-3219                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libapt-pkg6.0             │ CVE-2011-3374       │          │              │ 2.6.1                  │               │ It was found that apt-key in apt, all versions, do not       │
│                           │                     │          │              │                        │               │ correctly...                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2011-3374                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libasan8                  │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┤                     │          │              │                        ├───────────────┤                                                              │
│ libatomic1                │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libbinutils               │ CVE-2017-13716      │          │              │ 2.40-2                 │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │              │                        │               │ in libiberty                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │              │                        │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │              │                        │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │              │                        │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │              │                        │               │ crash                                                        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │              │                        │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │              │                        │               │ rust-demangle.c.                                             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-1972       │          │              │                        │               │ binutils: Illegal memory access when accessing a             │
│                           │                     │          │              │                        │               │ zer0-lengthverdef table                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-1972                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-53589      │          │              │                        │               │ binutils: objdump: buffer Overflow in the BFD library's      │
│                           │                     │          │              │                        │               │ handling of tekhex format...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-53589                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-57360      │          │              │                        │               │ binutils: nm: potential segmentation fault when displaying   │
│                           │                     │          │              │                        │               │ symbols without version info                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-57360                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-0840       │          │              │                        │               │ binutils: GNU Binutils objdump.c disassemble_bytes           │
│                           │                     │          │              │                        │               │ stack-based overflow                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-0840                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11081      │          │              │                        │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11081                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11082      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11082                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11083      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11083                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11412      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │              │                        │               │ bfd_elf_gc_record_vtentry out-of-bounds                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11412                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11413      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │              │                        │               │ elf_link_add_object_symbols out-of-bounds                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11413                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11414      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c get_link_hash_entry  │
│                           │                     │          │              │                        │               │ out-of-bounds                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11414                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │              │                        │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │              │                        │               │ overflow                                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │              │                        │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │              │                        │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11494      │          │              │                        │               │ binutils: GNU Binutils Linker out-of-bounds read             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11494                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11495      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11495                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │              │                        │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │              │                        │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │              │                        │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ heap-based overflow                                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1179       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1179                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │              │                        │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │              │                        │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │              │                        │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11839      │          │              │                        │               │ binutils: GNU Binutils prdbg.c tg_tag_type return value      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11839                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11840      │          │              │                        │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11840                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │              │                        │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │              │                        │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7545       │          │              │                        │               │ binutils: Binutils: Heap Buffer Overflow                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-7545                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7546       │          │              │                        │               │ binutils: Binutils: Out-of-bounds Write Vulnerability        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-7546                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8224       │          │              │                        │               │ binutils: Binutils BFD Null Pointer Dereference              │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-8224                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8225       │          │              │                        │               │ binutils: Binutils DWARF Section Handler Memory Leak         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-8225                    │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libblkid1                 │ CVE-2025-14104      │ MEDIUM   │              │ 2.38.1-5+deb12u3       │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                           │                     │          │              │                        │               │ when processing 256-byte usernames                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-0563       │ LOW      │              │                        │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │              │                        │               │ and chsh when compiled...                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libc-bin                  │ CVE-2010-4756       │          │              │ 2.36-9+deb12u13        │               │ glibc: glob implementation can cause excessive CPU and       │
│                           │                     │          │              │                        │               │ memory consumption due to...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2010-4756                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20796      │          │              │                        │               │ glibc: uncontrolled recursion in function                    │
│                           │                     │          │              │                        │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20796                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010022    │          │              │                        │               │ glibc: stack guard protection bypass                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-1010022                 │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010023    │          │              │                        │               │ glibc: running ldd on malicious ELF leads to code execution  │
│                           │                     │          │              │                        │               │ because of...                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-1010023                 │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010024    │          │              │                        │               │ glibc: ASLR bypass using cache of thread stack and heap      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-1010024                 │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010025    │          │              │                        │               │ glibc: information disclosure of heap addresses of           │
│                           │                     │          │              │                        │               │ pthread_created thread                                       │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-1010025                 │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-9192       │          │              │                        │               │ glibc: uncontrolled recursion in function                    │
│                           │                     │          │              │                        │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-9192                    │
├───────────────────────────┼─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libc6                     │ CVE-2010-4756       │          │              │                        │               │ glibc: glob implementation can cause excessive CPU and       │
│                           │                     │          │              │                        │               │ memory consumption due to...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2010-4756                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20796      │          │              │                        │               │ glibc: uncontrolled recursion in function                    │
│                           │                     │          │              │                        │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20796                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010022    │          │              │                        │               │ glibc: stack guard protection bypass                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-1010022                 │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010023    │          │              │                        │               │ glibc: running ldd on malicious ELF leads to code execution  │
│                           │                     │          │              │                        │               │ because of...                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-1010023                 │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010024    │          │              │                        │               │ glibc: ASLR bypass using cache of thread stack and heap      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-1010024                 │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-1010025    │          │              │                        │               │ glibc: information disclosure of heap addresses of           │
│                           │                     │          │              │                        │               │ pthread_created thread                                       │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-1010025                 │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2019-9192       │          │              │                        │               │ glibc: uncontrolled recursion in function                    │
│                           │                     │          │              │                        │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2019-9192                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libcc1-0                  │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libctf-nobfd0             │ CVE-2017-13716      │          │              │ 2.40-2                 │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │              │                        │               │ in libiberty                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │              │                        │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │              │                        │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │              │                        │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │              │                        │               │ crash                                                        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │              │                        │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │              │                        │               │ rust-demangle.c.                                             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-1972       │          │              │                        │               │ binutils: Illegal memory access when accessing a             │
│                           │                     │          │              │                        │               │ zer0-lengthverdef table                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-1972                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-53589      │          │              │                        │               │ binutils: objdump: buffer Overflow in the BFD library's      │
│                           │                     │          │              │                        │               │ handling of tekhex format...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-53589                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-57360      │          │              │                        │               │ binutils: nm: potential segmentation fault when displaying   │
│                           │                     │          │              │                        │               │ symbols without version info                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-57360                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-0840       │          │              │                        │               │ binutils: GNU Binutils objdump.c disassemble_bytes           │
│                           │                     │          │              │                        │               │ stack-based overflow                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-0840                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11081      │          │              │                        │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11081                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11082      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11082                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11083      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11083                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11412      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │              │                        │               │ bfd_elf_gc_record_vtentry out-of-bounds                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11412                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11413      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │              │                        │               │ elf_link_add_object_symbols out-of-bounds                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11413                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11414      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c get_link_hash_entry  │
│                           │                     │          │              │                        │               │ out-of-bounds                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11414                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │              │                        │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │              │                        │               │ overflow                                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │              │                        │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │              │                        │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11494      │          │              │                        │               │ binutils: GNU Binutils Linker out-of-bounds read             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11494                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11495      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11495                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │              │                        │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │              │                        │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │              │                        │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ heap-based overflow                                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1179       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1179                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │              │                        │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │              │                        │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │              │                        │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11839      │          │              │                        │               │ binutils: GNU Binutils prdbg.c tg_tag_type return value      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11839                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11840      │          │              │                        │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11840                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │              │                        │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │              │                        │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7545       │          │              │                        │               │ binutils: Binutils: Heap Buffer Overflow                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-7545                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7546       │          │              │                        │               │ binutils: Binutils: Out-of-bounds Write Vulnerability        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-7546                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8224       │          │              │                        │               │ binutils: Binutils BFD Null Pointer Dereference              │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-8224                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8225       │          │              │                        │               │ binutils: Binutils DWARF Section Handler Memory Leak         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-8225                    │
├───────────────────────────┼─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libctf0                   │ CVE-2017-13716      │          │              │                        │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │              │                        │               │ in libiberty                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │              │                        │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │              │                        │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │              │                        │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │              │                        │               │ crash                                                        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │              │                        │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │              │                        │               │ rust-demangle.c.                                             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-1972       │          │              │                        │               │ binutils: Illegal memory access when accessing a             │
│                           │                     │          │              │                        │               │ zer0-lengthverdef table                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-1972                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-53589      │          │              │                        │               │ binutils: objdump: buffer Overflow in the BFD library's      │
│                           │                     │          │              │                        │               │ handling of tekhex format...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-53589                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-57360      │          │              │                        │               │ binutils: nm: potential segmentation fault when displaying   │
│                           │                     │          │              │                        │               │ symbols without version info                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-57360                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-0840       │          │              │                        │               │ binutils: GNU Binutils objdump.c disassemble_bytes           │
│                           │                     │          │              │                        │               │ stack-based overflow                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-0840                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11081      │          │              │                        │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11081                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11082      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11082                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11083      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11083                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11412      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │              │                        │               │ bfd_elf_gc_record_vtentry out-of-bounds                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11412                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11413      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │              │                        │               │ elf_link_add_object_symbols out-of-bounds                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11413                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11414      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c get_link_hash_entry  │
│                           │                     │          │              │                        │               │ out-of-bounds                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11414                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │              │                        │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │              │                        │               │ overflow                                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │              │                        │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │              │                        │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11494      │          │              │                        │               │ binutils: GNU Binutils Linker out-of-bounds read             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11494                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11495      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11495                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │              │                        │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │              │                        │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │              │                        │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ heap-based overflow                                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1179       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1179                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │              │                        │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │              │                        │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │              │                        │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11839      │          │              │                        │               │ binutils: GNU Binutils prdbg.c tg_tag_type return value      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11839                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11840      │          │              │                        │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11840                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │              │                        │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │              │                        │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7545       │          │              │                        │               │ binutils: Binutils: Heap Buffer Overflow                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-7545                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7546       │          │              │                        │               │ binutils: Binutils: Out-of-bounds Write Vulnerability        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-7546                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8224       │          │              │                        │               │ binutils: Binutils BFD Null Pointer Dereference              │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-8224                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8225       │          │              │                        │               │ binutils: Binutils DWARF Section Handler Memory Leak         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-8225                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libgcc-12-dev             │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┤                     │          │              │                        ├───────────────┤                                                              │
│ libgcc-s1                 │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libgcrypt20               │ CVE-2018-6829       │          │              │ 1.10.1-3               │               │ libgcrypt: ElGamal implementation doesn't have semantic      │
│                           │                     │          │              │                        │               │ security due to incorrectly encoded plaintexts...            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-6829                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-2236       │          │              │                        │               │ libgcrypt: vulnerable to Marvin Attack                       │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-2236                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libgnutls30               │ CVE-2011-3389       │          │              │ 3.7.9-2+deb12u5        │               │ HTTPS: block-wise chosen-plaintext attack against SSL/TLS    │
│                           │                     │          │              │                        │               │ (BEAST)                                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2011-3389                    │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-9820       │ UNKNOWN  │              │                        │               │ [GNUTLS-SA-2025-11-18]                                       │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-9820                    │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libgomp1                  │ CVE-2022-27943      │ LOW      │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libgprofng0               │ CVE-2017-13716      │          │              │ 2.40-2                 │               │ binutils: Memory leak with the C++ symbol demangler routine  │
│                           │                     │          │              │                        │               │ in libiberty                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2017-13716                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20673      │          │              │                        │               │ libiberty: Integer overflow in demangle_template() function  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20673                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-20712      │          │              │                        │               │ libiberty: heap-based buffer over-read in d_expression_1     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-20712                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2018-9996       │          │              │                        │               │ binutils: Stack-overflow in libiberty/cplus-dem.c causes     │
│                           │                     │          │              │                        │               │ crash                                                        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-9996                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-32256      │          │              │                        │               │ binutils: stack-overflow issue in demangle_type in           │
│                           │                     │          │              │                        │               │ rust-demangle.c.                                             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2021-32256                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-1972       │          │              │                        │               │ binutils: Illegal memory access when accessing a             │
│                           │                     │          │              │                        │               │ zer0-lengthverdef table                                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-1972                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-53589      │          │              │                        │               │ binutils: objdump: buffer Overflow in the BFD library's      │
│                           │                     │          │              │                        │               │ handling of tekhex format...                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-53589                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-57360      │          │              │                        │               │ binutils: nm: potential segmentation fault when displaying   │
│                           │                     │          │              │                        │               │ symbols without version info                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-57360                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-0840       │          │              │                        │               │ binutils: GNU Binutils objdump.c disassemble_bytes           │
│                           │                     │          │              │                        │               │ stack-based overflow                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-0840                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11081      │          │              │                        │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11081                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11082      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11082                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11083      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11083                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11412      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │              │                        │               │ bfd_elf_gc_record_vtentry out-of-bounds                      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11412                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11413      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c                      │
│                           │                     │          │              │                        │               │ elf_link_add_object_symbols out-of-bounds                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11413                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11414      │          │              │                        │               │ binutils: GNU Binutils Linker elflink.c get_link_hash_entry  │
│                           │                     │          │              │                        │               │ out-of-bounds                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11414                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1147       │          │              │                        │               │ binutils: GNU Binutils nm nm.c internal_strlen buffer        │
│                           │                     │          │              │                        │               │ overflow                                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1147                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1148       │          │              │                        │               │ binutils: GNU Binutils ld ldelfgen.c link_order_scan memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1148                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1149       │          │              │                        │               │ binutils: GNU Binutils ld xmalloc.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1149                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11494      │          │              │                        │               │ binutils: GNU Binutils Linker out-of-bounds read             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11494                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11495      │          │              │                        │               │ binutils: GNU Binutils Linker heap-based overflow            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11495                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1150       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_malloc memory leak    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1150                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1151       │          │              │                        │               │ binutils: GNU Binutils ld xmemdup.c xmemdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1151                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1152       │          │              │                        │               │ binutils: GNU Binutils ld xstrdup.c xstrdup memory leak      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1152                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1153       │          │              │                        │               │ binutils: GNU Binutils format.c bfd_set_format memory        │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1153                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1176       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ heap-based overflow                                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1176                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1178       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1178                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1179       │          │              │                        │               │ binutils: GNU Binutils ld libbfd.c bfd_putl64 memory         │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1179                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1180       │          │              │                        │               │ binutils: GNU Binutils ld elf-eh-frame.c                     │
│                           │                     │          │              │                        │               │ _bfd_elf_write_section_eh_frame memory corruption            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1180                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1181       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c _bfd_elf_gc_mark_rsec    │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1181                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-1182       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c                          │
│                           │                     │          │              │                        │               │ bfd_elf_reloc_symbol_deleted_p memory corruption             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-1182                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11839      │          │              │                        │               │ binutils: GNU Binutils prdbg.c tg_tag_type return value      │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11839                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-11840      │          │              │                        │               │ binutils: GNU Binutils out-of-bounds read                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-11840                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-3198       │          │              │                        │               │ binutils: GNU Binutils objdump bucomm.c display_info memory  │
│                           │                     │          │              │                        │               │ leak                                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-3198                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5244       │          │              │                        │               │ binutils: GNU Binutils ld elflink.c elf_gc_sweep memory      │
│                           │                     │          │              │                        │               │ corruption                                                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5244                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-5245       │          │              │                        │               │ binutils: GNU Binutils objdump debug.c debug_type_samep      │
│                           │                     │          │              │                        │               │ memory corruption                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-5245                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7545       │          │              │                        │               │ binutils: Binutils: Heap Buffer Overflow                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-7545                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7546       │          │              │                        │               │ binutils: Binutils: Out-of-bounds Write Vulnerability        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-7546                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8224       │          │              │                        │               │ binutils: Binutils BFD Null Pointer Dereference              │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-8224                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-8225       │          │              │                        │               │ binutils: Binutils DWARF Section Handler Memory Leak         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-8225                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libgssapi-krb5-2          │ CVE-2018-5709       │          │              │ 1.20.1-2+deb12u4       │               │ krb5: integer overflow in dbentry->n_key_data in             │
│                           │                     │          │              │                        │               │ kadmin/dbutil/dump.c                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-5709                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-26458      │          │              │                        │               │ krb5: Memory leak at /krb5/src/lib/rpc/pmap_rmt.c            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-26458                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-26461      │          │              │                        │               │ krb5: Memory leak at /krb5/src/lib/gssapi/krb5/k5sealv3.c    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-26461                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libitm1                   │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libjansson4               │ CVE-2020-36325      │          │              │ 2.14-2                 │               │ jansson: out-of-bounds read in json_loads() due to a parsing │
│                           │                     │          │              │                        │               │ error                                                        │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2020-36325                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libk5crypto3              │ CVE-2018-5709       │          │              │ 1.20.1-2+deb12u4       │               │ krb5: integer overflow in dbentry->n_key_data in             │
│                           │                     │          │              │                        │               │ kadmin/dbutil/dump.c                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-5709                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-26458      │          │              │                        │               │ krb5: Memory leak at /krb5/src/lib/rpc/pmap_rmt.c            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-26458                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-26461      │          │              │                        │               │ krb5: Memory leak at /krb5/src/lib/gssapi/krb5/k5sealv3.c    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-26461                   │
├───────────────────────────┼─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libkrb5-3                 │ CVE-2018-5709       │          │              │                        │               │ krb5: integer overflow in dbentry->n_key_data in             │
│                           │                     │          │              │                        │               │ kadmin/dbutil/dump.c                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-5709                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-26458      │          │              │                        │               │ krb5: Memory leak at /krb5/src/lib/rpc/pmap_rmt.c            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-26458                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-26461      │          │              │                        │               │ krb5: Memory leak at /krb5/src/lib/gssapi/krb5/k5sealv3.c    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-26461                   │
├───────────────────────────┼─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libkrb5support0           │ CVE-2018-5709       │          │              │                        │               │ krb5: integer overflow in dbentry->n_key_data in             │
│                           │                     │          │              │                        │               │ kadmin/dbutil/dump.c                                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2018-5709                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-26458      │          │              │                        │               │ krb5: Memory leak at /krb5/src/lib/rpc/pmap_rmt.c            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-26458                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-26461      │          │              │                        │               │ krb5: Memory leak at /krb5/src/lib/gssapi/krb5/k5sealv3.c    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-26461                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ liblsan0                  │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libmount1                 │ CVE-2025-14104      │ MEDIUM   │              │ 2.38.1-5+deb12u3       │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                           │                     │          │              │                        │               │ when processing 256-byte usernames                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-0563       │ LOW      │              │                        │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │              │                        │               │ and chsh when compiled...                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libncursesw6              │ CVE-2023-50495      │ MEDIUM   │              │ 6.4-4                  │               │ ncurses: segmentation fault via _nc_wrap_entry()             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-50495                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-6141       │ LOW      │              │                        │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libpam-modules            │ CVE-2025-6020       │ HIGH     │              │ 1.5.2-6+deb12u1        │               │ linux-pam: Linux-pam directory Traversal                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-6020                    │
│                           ├─────────────────────┼──────────┼──────────────┤                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-10041      │ MEDIUM   │ will_not_fix │                        │               │ pam: libpam: Libpam vulnerable to read hashed password       │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-10041                   │
│                           ├─────────────────────┤          ├──────────────┤                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-22365      │          │ affected     │                        │               │ pam: allowing unprivileged user to block another user        │
│                           │                     │          │              │                        │               │ namespace                                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-22365                   │
├───────────────────────────┼─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libpam-modules-bin        │ CVE-2025-6020       │ HIGH     │              │                        │               │ linux-pam: Linux-pam directory Traversal                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-6020                    │
│                           ├─────────────────────┼──────────┼──────────────┤                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-10041      │ MEDIUM   │ will_not_fix │                        │               │ pam: libpam: Libpam vulnerable to read hashed password       │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-10041                   │
│                           ├─────────────────────┤          ├──────────────┤                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-22365      │          │ affected     │                        │               │ pam: allowing unprivileged user to block another user        │
│                           │                     │          │              │                        │               │ namespace                                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-22365                   │
├───────────────────────────┼─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libpam-runtime            │ CVE-2025-6020       │ HIGH     │              │                        │               │ linux-pam: Linux-pam directory Traversal                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-6020                    │
│                           ├─────────────────────┼──────────┼──────────────┤                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-10041      │ MEDIUM   │ will_not_fix │                        │               │ pam: libpam: Libpam vulnerable to read hashed password       │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-10041                   │
│                           ├─────────────────────┤          ├──────────────┤                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-22365      │          │ affected     │                        │               │ pam: allowing unprivileged user to block another user        │
│                           │                     │          │              │                        │               │ namespace                                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-22365                   │
├───────────────────────────┼─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libpam0g                  │ CVE-2025-6020       │ HIGH     │              │                        │               │ linux-pam: Linux-pam directory Traversal                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-6020                    │
│                           ├─────────────────────┼──────────┼──────────────┤                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-10041      │ MEDIUM   │ will_not_fix │                        │               │ pam: libpam: Libpam vulnerable to read hashed password       │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-10041                   │
│                           ├─────────────────────┤          ├──────────────┤                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-22365      │          │ affected     │                        │               │ pam: allowing unprivileged user to block another user        │
│                           │                     │          │              │                        │               │ namespace                                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-22365                   │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libquadmath0              │ CVE-2022-27943      │ LOW      │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libsmartcols1             │ CVE-2025-14104      │ MEDIUM   │              │ 2.38.1-5+deb12u3       │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                           │                     │          │              │                        │               │ when processing 256-byte usernames                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-0563       │ LOW      │              │                        │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │              │                        │               │ and chsh when compiled...                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libsqlite3-0              │ CVE-2025-7458       │ CRITICAL │              │ 3.40.1-2+deb12u2       │               │ sqlite: SQLite integer overflow                              │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-7458                    │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-7709       │ MEDIUM   │              │                        │               │ An integer overflow exists in the FTS5                       │
│                           │                     │          │              │                        │               │ https://sqlite.org/fts5.html e ...                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-7709                    │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2021-45346      │ LOW      │              │                        │               │ sqlite: crafted SQL query allows a malicious user to obtain  │
│                           │                     │          │              │                        │               │ sensitive information...                                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2021-45346                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-29088      │          │              │                        │               │ sqlite: Denial of Service in SQLite                          │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-29088                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libssl3                   │ CVE-2025-27587      │          │              │ 3.0.17-1~deb12u3       │               │ OpenSSL 3.0.0 through 3.3.2 on the PowerPC architecture is   │
│                           │                     │          │              │                        │               │ vulnerable ......                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-27587                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libstdc++6                │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libsystemd0               │ CVE-2013-4392       │          │              │ 252.39-1~deb12u1       │               │ systemd: TOCTOU race condition when updating file            │
│                           │                     │          │              │                        │               │ permissions and SELinux security contexts...                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2013-4392                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31437      │          │              │                        │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │              │                        │               │ modify a...                                                  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-31437                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31438      │          │              │                        │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │              │                        │               │ truncate a...                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-31438                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31439      │          │              │                        │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │              │                        │               │ modify the...                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-31439                   │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libtinfo6                 │ CVE-2023-50495      │ MEDIUM   │              │ 6.4-4                  │               │ ncurses: segmentation fault via _nc_wrap_entry()             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-50495                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-6141       │ LOW      │              │                        │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libtsan2                  │ CVE-2022-27943      │          │              │ 12.2.0-14+deb12u1      │               │ binutils: libiberty/rust-demangle.c in GNU GCC 11.2 allows   │
│                           │                     │          │              │                        │               │ stack exhaustion in demangle_const                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-27943                   │
├───────────────────────────┤                     │          │              │                        ├───────────────┤                                                              │
│ libubsan1                 │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
│                           │                     │          │              │                        │               │                                                              │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libudev1                  │ CVE-2013-4392       │          │              │ 252.39-1~deb12u1       │               │ systemd: TOCTOU race condition when updating file            │
│                           │                     │          │              │                        │               │ permissions and SELinux security contexts...                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2013-4392                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31437      │          │              │                        │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │              │                        │               │ modify a...                                                  │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-31437                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31438      │          │              │                        │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │              │                        │               │ truncate a...                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-31438                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31439      │          │              │                        │               │ An issue was discovered in systemd 253. An attacker can      │
│                           │                     │          │              │                        │               │ modify the...                                                │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-31439                   │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libuuid1                  │ CVE-2025-14104      │ MEDIUM   │              │ 2.38.1-5+deb12u3       │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                           │                     │          │              │                        │               │ when processing 256-byte usernames                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-0563       │ LOW      │              │                        │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │              │                        │               │ and chsh when compiled...                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ login                     │ CVE-2007-5686       │          │              │ 1:4.13+dfsg1-1+deb12u1 │               │ initscripts in rPath Linux 1 sets insecure permissions for   │
│                           │                     │          │              │                        │               │ the /var/lo ......                                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2007-5686                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-56433      │          │              │                        │               │ shadow-utils: Default subordinate ID configuration in        │
│                           │                     │          │              │                        │               │ /etc/login.defs could lead to compromise                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-56433                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ TEMP-0628843-DBAD28 │          │              │                        │               │ [more related to CVE-2005-4890]                              │
│                           │                     │          │              │                        │               │ https://security-tracker.debian.org/tracker/TEMP-0628843-DB- │
│                           │                     │          │              │                        │               │ AD28                                                         │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ mount                     │ CVE-2025-14104      │ MEDIUM   │              │ 2.38.1-5+deb12u3       │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                           │                     │          │              │                        │               │ when processing 256-byte usernames                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-0563       │ LOW      │              │                        │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │              │                        │               │ and chsh when compiled...                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ ncurses-base              │ CVE-2023-50495      │ MEDIUM   │              │ 6.4-4                  │               │ ncurses: segmentation fault via _nc_wrap_entry()             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-50495                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-6141       │ LOW      │              │                        │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├───────────────────────────┼─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ ncurses-bin               │ CVE-2023-50495      │ MEDIUM   │              │                        │               │ ncurses: segmentation fault via _nc_wrap_entry()             │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-50495                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2025-6141       │ LOW      │              │                        │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ openssl                   │ CVE-2025-27587      │          │              │ 3.0.17-1~deb12u3       │               │ OpenSSL 3.0.0 through 3.3.2 on the PowerPC architecture is   │
│                           │                     │          │              │                        │               │ vulnerable ......                                            │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-27587                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ passwd                    │ CVE-2007-5686       │          │              │ 1:4.13+dfsg1-1+deb12u1 │               │ initscripts in rPath Linux 1 sets insecure permissions for   │
│                           │                     │          │              │                        │               │ the /var/lo ......                                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2007-5686                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2024-56433      │          │              │                        │               │ shadow-utils: Default subordinate ID configuration in        │
│                           │                     │          │              │                        │               │ /etc/login.defs could lead to compromise                     │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2024-56433                   │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ TEMP-0628843-DBAD28 │          │              │                        │               │ [more related to CVE-2005-4890]                              │
│                           │                     │          │              │                        │               │ https://security-tracker.debian.org/tracker/TEMP-0628843-DB- │
│                           │                     │          │              │                        │               │ AD28                                                         │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ perl-base                 │ CVE-2011-4116       │          │              │ 5.36.0-7+deb12u3       │               │ perl: File:: Temp insecure temporary file handling           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2011-4116                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2023-31486      │          │              │                        │               │ http-tiny: insecure TLS cert default                         │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-31486                   │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ sysvinit-utils            │ TEMP-0517018-A83CE6 │          │              │ 3.06-4                 │               │ [sysvinit: no-root option in expert installer exposes        │
│                           │                     │          │              │                        │               │ locally exploitable security flaw]                           │
│                           │                     │          │              │                        │               │ https://security-tracker.debian.org/tracker/TEMP-0517018-A8- │
│                           │                     │          │              │                        │               │ 3CE6                                                         │
├───────────────────────────┼─────────────────────┤          │              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ tar                       │ CVE-2005-2541       │          │              │ 1.34+dfsg-1.2+deb12u1  │               │ tar: does not properly warn the user when extracting setuid  │
│                           │                     │          │              │                        │               │ or setgid...                                                 │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2005-2541                    │
│                           ├─────────────────────┤          │              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ TEMP-0290435-0B57B5 │          │              │                        │               │ [tar's rmt command may have undesired side effects]          │
│                           │                     │          │              │                        │               │ https://security-tracker.debian.org/tracker/TEMP-0290435-0B- │
│                           │                     │          │              │                        │               │ 57B5                                                         │
├───────────────────────────┼─────────────────────┼──────────┤              ├────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ util-linux                │ CVE-2025-14104      │ MEDIUM   │              │ 2.38.1-5+deb12u3       │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                           │                     │          │              │                        │               │ when processing 256-byte usernames                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-0563       │ LOW      │              │                        │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │              │                        │               │ and chsh when compiled...                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│ util-linux-extra          │ CVE-2025-14104      │ MEDIUM   │              │                        │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                           │                     │          │              │                        │               │ when processing 256-byte usernames                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                           ├─────────────────────┼──────────┤              │                        ├───────────────┼──────────────────────────────────────────────────────────────┤
│                           │ CVE-2022-0563       │ LOW      │              │                        │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                           │                     │          │              │                        │               │ and chsh when compiled...                                    │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├───────────────────────────┼─────────────────────┼──────────┼──────────────┼────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ zlib1g                    │ CVE-2023-45853      │ CRITICAL │ will_not_fix │ 1:1.2.13.dfsg-1        │               │ zlib: integer overflow and resultant heap-based buffer       │
│                           │                     │          │              │                        │               │ overflow in zipOpenNewFileInZip4_6                           │
│                           │                     │          │              │                        │               │ https://avd.aquasec.com/nvd/cve-2023-45853                   │
└───────────────────────────┴─────────────────────┴──────────┴──────────────┴────────────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
2025-12-20T03:04:24Z    INFO    [vuln] Vulnerability scanning is enabled
2025-12-20T03:04:24Z    INFO    [secret] Secret scanning is enabled
2025-12-20T03:04:24Z    INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-12-20T03:04:24Z    INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2025-12-20T03:04:24Z    INFO    Detected OS     family="debian" version="12.12"
2025-12-20T03:04:24Z    INFO    [debian] Detecting vulnerabilities...   os_version="12" pkg_num=130
2025-12-20T03:04:24Z    INFO    Number of language-specific files       num=1
2025-12-20T03:04:24Z    INFO    [python-pkg] Detecting vulnerabilities...
2025-12-20T03:04:24Z    WARN    Using severities from other vendors for some vulnerabilities. Read https://trivy.dev/docs/v0.68/guide/scanner/vulnerability#severity-selection for details.

Report Summary

┌──────────────────────────────────────────────────────────────────────────────────┬────────────┬─────────────────┬─────────┐
│                                      Target                                      │    Type    │ Vulnerabilities │ Secrets │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ tg_bot_hb-backend (debian 12.12)                                                 │   debian   │       29        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/APScheduler-3.10.4.dist-info/METADATA     │ python-pkg │        0        │    -    │
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
│ usr/local/lib/python3.11/site-packages/annotated_doc-0.0.4.dist-info/METADATA    │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/annotated_types-0.7.0.dist-info/METADATA  │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.11/site-packages/anyio-4.12.0.dist-info/METADATA           │ python-pkg │        0        │    -    │
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
│ usr/local/lib/python3.11/site-packages/fastapi-0.125.0.dist-info/METADATA        │ python-pkg │        0        │    -    │
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
│ usr/local/lib/python3.11/site-packages/pillow-12.0.0.dist-info/METADATA          │ python-pkg │        0        │    -    │
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
│ usr/local/lib/python3.11/site-packages/starlette-0.50.0.dist-info/METADATA       │ python-pkg │        0        │    -    │
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


tg_bot_hb-backend (debian 12.12)

Total: 29 (UNKNOWN: 1, MEDIUM: 22, HIGH: 4, CRITICAL: 2)

┌────────────────────┬────────────────┬──────────┬──────────────┬────────────────────┬───────────────┬────────────────────────────────────────────────────────────┐
│      Library       │ Vulnerability  │ Severity │    Status    │ Installed Version  │ Fixed Version │                           Title                            │
├────────────────────┼────────────────┼──────────┼──────────────┼────────────────────┼───────────────┼────────────────────────────────────────────────────────────┤
│ bsdutils           │ CVE-2025-14104 │ MEDIUM   │ affected     │ 1:2.38.1-5+deb12u3 │               │ util-linux: util-linux: Heap buffer overread in setpwnam() │
│                    │                │          │              │                    │               │ when processing 256-byte usernames                         │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2025-14104                 │
├────────────────────┼────────────────┤          │              ├────────────────────┼───────────────┼────────────────────────────────────────────────────────────┤
│ gpgv               │ CVE-2025-30258 │          │              │ 2.2.40-1.1+deb12u1 │               │ gnupg: verification DoS due to a malicious subkey in the   │
│                    │                │          │              │                    │               │ keyring                                                    │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2025-30258                 │
├────────────────────┼────────────────┤          │              ├────────────────────┼───────────────┼────────────────────────────────────────────────────────────┤
│ libblkid1          │ CVE-2025-14104 │          │              │ 2.38.1-5+deb12u3   │               │ util-linux: util-linux: Heap buffer overread in setpwnam() │
│                    │                │          │              │                    │               │ when processing 256-byte usernames                         │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2025-14104                 │
├────────────────────┼────────────────┼──────────┤              ├────────────────────┼───────────────┼────────────────────────────────────────────────────────────┤
│ libgnutls30        │ CVE-2025-9820  │ UNKNOWN  │              │ 3.7.9-2+deb12u5    │               │ [GNUTLS-SA-2025-11-18]                                     │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2025-9820                  │
├────────────────────┼────────────────┼──────────┤              ├────────────────────┼───────────────┼────────────────────────────────────────────────────────────┤
│ libmount1          │ CVE-2025-14104 │ MEDIUM   │              │ 2.38.1-5+deb12u3   │               │ util-linux: util-linux: Heap buffer overread in setpwnam() │
│                    │                │          │              │                    │               │ when processing 256-byte usernames                         │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2025-14104                 │
├────────────────────┼────────────────┤          │              ├────────────────────┼───────────────┼────────────────────────────────────────────────────────────┤
│ libncursesw6       │ CVE-2023-50495 │          │              │ 6.4-4              │               │ ncurses: segmentation fault via _nc_wrap_entry()           │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2023-50495                 │
├────────────────────┼────────────────┼──────────┤              ├────────────────────┼───────────────┼────────────────────────────────────────────────────────────┤
│ libpam-modules     │ CVE-2025-6020  │ HIGH     │              │ 1.5.2-6+deb12u1    │               │ linux-pam: Linux-pam directory Traversal                   │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2025-6020                  │
│                    ├────────────────┼──────────┼──────────────┤                    ├───────────────┼────────────────────────────────────────────────────────────┤
│                    │ CVE-2024-10041 │ MEDIUM   │ will_not_fix │                    │               │ pam: libpam: Libpam vulnerable to read hashed password     │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2024-10041                 │
│                    ├────────────────┤          ├──────────────┤                    ├───────────────┼────────────────────────────────────────────────────────────┤
│                    │ CVE-2024-22365 │          │ affected     │                    │               │ pam: allowing unprivileged user to block another user      │
│                    │                │          │              │                    │               │ namespace                                                  │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2024-22365                 │
├────────────────────┼────────────────┼──────────┤              │                    ├───────────────┼────────────────────────────────────────────────────────────┤
│ libpam-modules-bin │ CVE-2025-6020  │ HIGH     │              │                    │               │ linux-pam: Linux-pam directory Traversal                   │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2025-6020                  │
│                    ├────────────────┼──────────┼──────────────┤                    ├───────────────┼────────────────────────────────────────────────────────────┤
│                    │ CVE-2024-10041 │ MEDIUM   │ will_not_fix │                    │               │ pam: libpam: Libpam vulnerable to read hashed password     │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2024-10041                 │
│                    ├────────────────┤          ├──────────────┤                    ├───────────────┼────────────────────────────────────────────────────────────┤
│                    │ CVE-2024-22365 │          │ affected     │                    │               │ pam: allowing unprivileged user to block another user      │
│                    │                │          │              │                    │               │ namespace                                                  │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2024-22365                 │
├────────────────────┼────────────────┼──────────┤              │                    ├───────────────┼────────────────────────────────────────────────────────────┤
│ libpam-runtime     │ CVE-2025-6020  │ HIGH     │              │                    │               │ linux-pam: Linux-pam directory Traversal                   │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2025-6020                  │
│                    ├────────────────┼──────────┼──────────────┤                    ├───────────────┼────────────────────────────────────────────────────────────┤
│                    │ CVE-2024-10041 │ MEDIUM   │ will_not_fix │                    │               │ pam: libpam: Libpam vulnerable to read hashed password     │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2024-10041                 │
│                    ├────────────────┤          ├──────────────┤                    ├───────────────┼────────────────────────────────────────────────────────────┤
│                    │ CVE-2024-22365 │          │ affected     │                    │               │ pam: allowing unprivileged user to block another user      │
│                    │                │          │              │                    │               │ namespace                                                  │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2024-22365                 │
├────────────────────┼────────────────┼──────────┤              │                    ├───────────────┼────────────────────────────────────────────────────────────┤
│ libpam0g           │ CVE-2025-6020  │ HIGH     │              │                    │               │ linux-pam: Linux-pam directory Traversal                   │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2025-6020                  │
│                    ├────────────────┼──────────┼──────────────┤                    ├───────────────┼────────────────────────────────────────────────────────────┤
│                    │ CVE-2024-10041 │ MEDIUM   │ will_not_fix │                    │               │ pam: libpam: Libpam vulnerable to read hashed password     │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2024-10041                 │
│                    ├────────────────┤          ├──────────────┤                    ├───────────────┼────────────────────────────────────────────────────────────┤
│                    │ CVE-2024-22365 │          │ affected     │                    │               │ pam: allowing unprivileged user to block another user      │
│                    │                │          │              │                    │               │ namespace                                                  │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2024-22365                 │
├────────────────────┼────────────────┤          │              ├────────────────────┼───────────────┼────────────────────────────────────────────────────────────┤
│ libsmartcols1      │ CVE-2025-14104 │          │              │ 2.38.1-5+deb12u3   │               │ util-linux: util-linux: Heap buffer overread in setpwnam() │
│                    │                │          │              │                    │               │ when processing 256-byte usernames                         │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2025-14104                 │
├────────────────────┼────────────────┼──────────┤              ├────────────────────┼───────────────┼────────────────────────────────────────────────────────────┤
│ libsqlite3-0       │ CVE-2025-7458  │ CRITICAL │              │ 3.40.1-2+deb12u2   │               │ sqlite: SQLite integer overflow                            │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2025-7458                  │
│                    ├────────────────┼──────────┤              │                    ├───────────────┼────────────────────────────────────────────────────────────┤
│                    │ CVE-2025-7709  │ MEDIUM   │              │                    │               │ An integer overflow exists in the FTS5                     │
│                    │                │          │              │                    │               │ https://sqlite.org/fts5.html e ...                         │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2025-7709                  │
├────────────────────┼────────────────┤          │              ├────────────────────┼───────────────┼────────────────────────────────────────────────────────────┤
│ libtinfo6          │ CVE-2023-50495 │          │              │ 6.4-4              │               │ ncurses: segmentation fault via _nc_wrap_entry()           │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2023-50495                 │
├────────────────────┼────────────────┤          │              ├────────────────────┼───────────────┼────────────────────────────────────────────────────────────┤
│ libuuid1           │ CVE-2025-14104 │          │              │ 2.38.1-5+deb12u3   │               │ util-linux: util-linux: Heap buffer overread in setpwnam() │
│                    │                │          │              │                    │               │ when processing 256-byte usernames                         │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2025-14104                 │
├────────────────────┤                │          │              │                    ├───────────────┤                                                            │
│ mount              │                │          │              │                    │               │                                                            │
│                    │                │          │              │                    │               │                                                            │
│                    │                │          │              │                    │               │                                                            │
├────────────────────┼────────────────┤          │              ├────────────────────┼───────────────┼────────────────────────────────────────────────────────────┤
│ ncurses-base       │ CVE-2023-50495 │          │              │ 6.4-4              │               │ ncurses: segmentation fault via _nc_wrap_entry()           │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2023-50495                 │
├────────────────────┤                │          │              │                    ├───────────────┤                                                            │
│ ncurses-bin        │                │          │              │                    │               │                                                            │
│                    │                │          │              │                    │               │                                                            │
├────────────────────┼────────────────┤          │              ├────────────────────┼───────────────┼────────────────────────────────────────────────────────────┤
│ util-linux         │ CVE-2025-14104 │          │              │ 2.38.1-5+deb12u3   │               │ util-linux: util-linux: Heap buffer overread in setpwnam() │
│                    │                │          │              │                    │               │ when processing 256-byte usernames                         │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2025-14104                 │
├────────────────────┤                │          │              │                    ├───────────────┤                                                            │
│ util-linux-extra   │                │          │              │                    │               │                                                            │
│                    │                │          │              │                    │               │                                                            │
│                    │                │          │              │                    │               │                                                            │
├────────────────────┼────────────────┼──────────┼──────────────┼────────────────────┼───────────────┼────────────────────────────────────────────────────────────┤
│ zlib1g             │ CVE-2023-45853 │ CRITICAL │ will_not_fix │ 1:1.2.13.dfsg-1    │               │ zlib: integer overflow and resultant heap-based buffer     │
│                    │                │          │              │                    │               │ overflow in zipOpenNewFileInZip4_6                         │
│                    │                │          │              │                    │               │ https://avd.aquasec.com/nvd/cve-2023-45853