Run ruff check src/
src/infrastructure/config/env_validator.py:3:1: I001 [*] Import block is un-sorted or un-formatted
   |
 1 |   """Валидация переменных окружения."""
 2 |   
 3 | / import os
 4 | | import re
 5 | | from urllib.parse import urlparse
 6 | | from typing import Optional, Tuple
 7 | | 
 8 | | 
 9 | | def validate_database_url(database_url: str) -> Tuple[bool, Optional[str], Optional[str]]:
   | |_^ I001
10 |       """
11 |       Валидирует формат DATABASE_URL и извлекает информацию о базе данных.
   |
   = help: Organize imports

src/infrastructure/config/env_validator.py:3:8: F401 [*] `os` imported but unused
  |
1 | """Валидация переменных окружения."""
2 | 
3 | import os
  |        ^^ F401
4 | import re
5 | from urllib.parse import urlparse
  |
  = help: Remove unused import: `os`

src/infrastructure/config/env_validator.py:4:8: F401 [*] `re` imported but unused
  |
3 | import os
4 | import re
  |        ^^ F401
5 | from urllib.parse import urlparse
6 | from typing import Optional, Tuple
  |
  = help: Remove unused import: `re`

src/infrastructure/config/env_validator.py:6:1: UP035 `typing.Tuple` is deprecated, use `tuple` instead
  |
4 | import re
5 | from urllib.parse import urlparse
6 | from typing import Optional, Tuple
  | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ UP035
  |

src/infrastructure/config/env_validator.py:9:49: UP006 [*] Use `tuple` instead of `Tuple` for type annotation
   |
 9 | def validate_database_url(database_url: str) -> Tuple[bool, Optional[str], Optional[str]]:
   |                                                 ^^^^^ UP006
10 |     """
11 |     Валидирует формат DATABASE_URL и извлекает информацию о базе данных.
   |
   = help: Replace with `tuple`

src/infrastructure/config/env_validator.py:9:61: UP007 [*] Use `X | Y` for type annotations
   |
 9 | def validate_database_url(database_url: str) -> Tuple[bool, Optional[str], Optional[str]]:
   |                                                             ^^^^^^^^^^^^^ UP007
10 |     """
11 |     Валидирует формат DATABASE_URL и извлекает информацию о базе данных.
   |
   = help: Convert to `X | Y`

src/infrastructure/config/env_validator.py:9:76: UP007 [*] Use `X | Y` for type annotations
   |
 9 | def validate_database_url(database_url: str) -> Tuple[bool, Optional[str], Optional[str]]:
   |                                                                            ^^^^^^^^^^^^^ UP007
10 |     """
11 |     Валидирует формат DATABASE_URL и извлекает информацию о базе данных.
   |
   = help: Convert to `X | Y`

src/infrastructure/config/env_validator.py:59:54: UP007 [*] Use `X | Y` for type annotations
   |
59 | def get_database_name_from_url(database_url: str) -> Optional[str]:
   |                                                      ^^^^^^^^^^^^^ UP007
60 |     """
61 |     Извлекает имя базы данных из DATABASE_URL.
   |
   = help: Convert to `X | Y`

src/infrastructure/config/env_validator.py:104:44: UP006 [*] Use `tuple` instead of `Tuple` for type annotation
    |
104 | def validate_telegram_token(token: str) -> Tuple[bool, Optional[str]]:
    |                                            ^^^^^ UP006
105 |     """
106 |     Валидирует формат Telegram Bot Token.
    |
    = help: Replace with `tuple`

src/infrastructure/config/env_validator.py:104:56: UP007 [*] Use `X | Y` for type annotations
    |
104 | def validate_telegram_token(token: str) -> Tuple[bool, Optional[str]]:
    |                                                        ^^^^^^^^^^^^^ UP007
105 |     """
106 |     Валидирует формат Telegram Bot Token.
    |
    = help: Convert to `X | Y`

src/infrastructure/database/repositories/birthday_repository_impl.py:83:1: W293 Blank line contains whitespace
   |
81 |         """
82 |         Поиск по ФИО, компании, должности.
83 |         
   | ^^^^^^^^ W293
84 |         Args:
85 |             query: Поисковый запрос (валидируется и санитизируется)
   |
   = help: Remove whitespace from blank line

src/infrastructure/database/repositories/birthday_repository_impl.py:86:1: W293 Blank line contains whitespace
   |
84 |         Args:
85 |             query: Поисковый запрос (валидируется и санитизируется)
86 |             
   | ^^^^^^^^^^^^ W293
87 |         Returns:
88 |             Список найденных дней рождения
   |
   = help: Remove whitespace from blank line

src/infrastructure/database/repositories/birthday_repository_impl.py:89:1: W293 Blank line contains whitespace
   |
87 |         Returns:
88 |             Список найденных дней рождения
89 |             
   | ^^^^^^^^^^^^ W293
90 |         Raises:
91 |             ValidationError: Если запрос невалиден или пуст
   |
   = help: Remove whitespace from blank line

src/infrastructure/database/repositories/birthday_repository_impl.py:100:1: W293 [*] Blank line contains whitespace
    |
 98 |                 "and contain only letters, numbers, spaces, and basic punctuation."
 99 |             )
100 |         
    | ^^^^^^^^ W293
101 |         # Используем параметризованный запрос для безопасности
102 |         # SQLAlchemy автоматически экранирует параметры
    |
    = help: Remove whitespace from blank line

src/infrastructure/database/repositories/responsible_repository_impl.py:100:1: W293 Blank line contains whitespace
    |
 98 |         """
 99 |         Поиск по ФИО, компании, должности.
100 |         
    | ^^^^^^^^ W293
101 |         Args:
102 |             query: Поисковый запрос (валидируется и санитизируется)
    |
    = help: Remove whitespace from blank line

src/infrastructure/database/repositories/responsible_repository_impl.py:103:1: W293 Blank line contains whitespace
    |
101 |         Args:
102 |             query: Поисковый запрос (валидируется и санитизируется)
103 |             
    | ^^^^^^^^^^^^ W293
104 |         Returns:
105 |             Список найденных ответственных лиц
    |
    = help: Remove whitespace from blank line

src/infrastructure/database/repositories/responsible_repository_impl.py:106:1: W293 Blank line contains whitespace
    |
104 |         Returns:
105 |             Список найденных ответственных лиц
106 |             
    | ^^^^^^^^^^^^ W293
107 |         Raises:
108 |             ValidationError: Если запрос невалиден или пуст
    |
    = help: Remove whitespace from blank line

src/infrastructure/database/repositories/responsible_repository_impl.py:117:1: W293 [*] Blank line contains whitespace
    |
115 |                 "and contain only letters, numbers, spaces, and basic punctuation."
116 |             )
117 |         
    | ^^^^^^^^ W293
118 |         # Используем параметризованный запрос для безопасности
119 |         # SQLAlchemy автоматически экранирует параметры
    |
    = help: Remove whitespace from blank line

src/infrastructure/database/repositories/search_validator.py:3:1: I001 [*] Import block is un-sorted or un-formatted
  |
1 |   """Валидация и санитизация входных данных для поиска."""
2 |   
3 | / import re
4 | | from typing import Tuple
5 | | 
6 | | 
7 | | # Максимальная длина поискового запроса
  | |_^ I001
8 |   MAX_SEARCH_QUERY_LENGTH = 200
  |
  = help: Organize imports

src/infrastructure/database/repositories/search_validator.py:4:1: UP035 `typing.Tuple` is deprecated, use `tuple` instead
  |
3 | import re
4 | from typing import Tuple
  | ^^^^^^^^^^^^^^^^^^^^^^^^ UP035
  |

src/infrastructure/database/repositories/search_validator.py:18:55: UP006 [*] Use `tuple` instead of `Tuple` for type annotation
   |
18 | def validate_and_sanitize_search_query(query: str) -> Tuple[str, bool]:
   |                                                       ^^^^^ UP006
19 |     """
20 |     Валидирует и санитизирует поисковый запрос.
   |
   = help: Replace with `tuple`

src/infrastructure/database/repositories/search_validator.py:21:1: W293 Blank line contains whitespace
   |
19 |     """
20 |     Валидирует и санитизирует поисковый запрос.
21 |     
   | ^^^^ W293
22 |     Args:
23 |         query: Исходный поисковый запрос
   |
   = help: Remove whitespace from blank line

src/infrastructure/database/repositories/search_validator.py:24:1: W293 Blank line contains whitespace
   |
22 |     Args:
23 |         query: Исходный поисковый запрос
24 |         
   | ^^^^^^^^ W293
25 |     Returns:
26 |         Tuple[str, bool]: (санитизированный запрос, валидность)
   |
   = help: Remove whitespace from blank line

src/infrastructure/database/repositories/search_validator.py:29:1: W293 Blank line contains whitespace
   |
27 |         - Если запрос валиден, возвращается санитизированная версия
28 |         - Если запрос невалиден, возвращается пустая строка и False
29 |         
   | ^^^^^^^^ W293
30 |     Raises:
31 |         ValueError: Если query не является строкой
   |
   = help: Remove whitespace from blank line

src/infrastructure/database/repositories/search_validator.py:35:1: W293 [*] Blank line contains whitespace
   |
33 |     if not isinstance(query, str):
34 |         raise ValueError("Search query must be a string")
35 |     
   | ^^^^ W293
36 |     # Удаляем лишние пробелы
37 |     query = query.strip()
   |
   = help: Remove whitespace from blank line

src/infrastructure/database/repositories/search_validator.py:38:1: W293 [*] Blank line contains whitespace
   |
36 |     # Удаляем лишние пробелы
37 |     query = query.strip()
38 |     
   | ^^^^ W293
39 |     # Проверяем длину
40 |     if len(query) < MIN_SEARCH_QUERY_LENGTH:
   |
   = help: Remove whitespace from blank line

src/infrastructure/database/repositories/search_validator.py:42:1: W293 [*] Blank line contains whitespace
   |
40 |     if len(query) < MIN_SEARCH_QUERY_LENGTH:
41 |         return "", False
42 |     
   | ^^^^ W293
43 |     if len(query) > MAX_SEARCH_QUERY_LENGTH:
44 |         # Обрезаем до максимальной длины
   |
   = help: Remove whitespace from blank line

src/infrastructure/database/repositories/search_validator.py:46:1: W293 [*] Blank line contains whitespace
   |
44 |         # Обрезаем до максимальной длины
45 |         query = query[:MAX_SEARCH_QUERY_LENGTH]
46 |     
   | ^^^^ W293
47 |     # Удаляем потенциально опасные символы
48 |     sanitized = SAFE_SEARCH_PATTERN.sub("", query)
   |
   = help: Remove whitespace from blank line

src/infrastructure/database/repositories/search_validator.py:49:1: W293 [*] Blank line contains whitespace
   |
47 |     # Удаляем потенциально опасные символы
48 |     sanitized = SAFE_SEARCH_PATTERN.sub("", query)
49 |     
   | ^^^^ W293
50 |     # Проверяем, что после санитизации остался хотя бы один символ
51 |     if not sanitized.strip():
   |
   = help: Remove whitespace from blank line

src/infrastructure/database/repositories/search_validator.py:53:1: W293 [*] Blank line contains whitespace
   |
51 |     if not sanitized.strip():
52 |         return "", False
53 |     
   | ^^^^ W293
54 |     return sanitized.strip(), True
   |
   = help: Remove whitespace from blank line

src/presentation/telegram/keyboards.py:20:1: W293 Blank line contains whitespace
   |
18 |     """
19 |     Проверяет, настроен ли URL для Mini App.
20 |     
   | ^^^^ W293
21 |     Args:
22 |         webapp_url: URL из переменной окружения TELEGRAM_WEBAPP_URL
   |
   = help: Remove whitespace from blank line

src/presentation/telegram/keyboards.py:23:1: W293 Blank line contains whitespace
   |
21 |     Args:
22 |         webapp_url: URL из переменной окружения TELEGRAM_WEBAPP_URL
23 |         
   | ^^^^^^^^ W293
24 |     Returns:
25 |         True, если URL настроен и не является placeholder значением
   |
   = help: Remove whitespace from blank line

src/presentation/telegram/keyboards.py:34:1: W293 [*] Blank line contains whitespace
   |
32 |     webapp_url = os.getenv("TELEGRAM_WEBAPP_URL", "")
33 |     buttons = [[KeyboardButton(text="📅 Календарь")]]
34 |     
   | ^^^^ W293
35 |     # Добавляем кнопку Mini App, если URL настроен
36 |     if is_webapp_url_configured(webapp_url):
   |
   = help: Remove whitespace from blank line

src/presentation/telegram/keyboards.py:45:1: W293 [*] Blank line contains whitespace
   |
43 |             "Установите TELEGRAM_WEBAPP_URL в переменных окружения (должен быть HTTPS URL)."
44 |         )
45 |     
   | ^^^^ W293
46 |     keyboard = ReplyKeyboardMarkup(
47 |         keyboard=buttons,
   |
   = help: Remove whitespace from blank line

src/presentation/telegram/keyboards.py:70:1: W293 [*] Blank line contains whitespace
   |
68 |         [InlineKeyboardButton(text="📅 Календарь", callback_data="panel_calendar")],
69 |     ]
70 |     
   | ^^^^ W293
71 |     # Добавляем кнопку Mini App, если URL настроен
72 |     if is_webapp_url_configured(webapp_url):
   |
   = help: Remove whitespace from blank line

src/presentation/telegram/keyboards.py:79:1: W293 [*] Blank line contains whitespace
   |
77 |             )
78 |         ])
79 |     
   | ^^^^ W293
80 |     keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
81 |     return keyboard
   |
   = help: Remove whitespace from blank line

src/presentation/telegram/middleware/database_middleware.py:4:1: UP035 [*] Import from `collections.abc` instead: `Awaitable`, `Callable`
  |
3 | import logging
4 | from typing import Any, Awaitable, Callable
  | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ UP035
5 | 
6 | from aiogram import BaseMiddleware
  |
  = help: Import from `collections.abc`

src/presentation/telegram/middleware/database_middleware.py:8:36: F401 [*] `sqlalchemy.ext.asyncio.AsyncSession` imported but unused
   |
 6 | from aiogram import BaseMiddleware
 7 | from aiogram.types import TelegramObject
 8 | from sqlalchemy.ext.asyncio import AsyncSession
   |                                    ^^^^^^^^^^^^ F401
 9 | 
10 | from src.infrastructure.database.database_factory import get_database
   |
   = help: Remove unused import: `sqlalchemy.ext.asyncio.AsyncSession`

src/presentation/web/app.py:3:30: F401 [*] `fastapi.Request` imported but unused
  |
1 | import os
2 | 
3 | from fastapi import FastAPI, Request
  |                              ^^^^^^^ F401
4 | from fastapi.middleware.cors import CORSMiddleware
5 | from slowapi import Limiter, _rate_limit_exceeded_handler
  |
  = help: Remove unused import: `fastapi.Request`

src/presentation/web/decorators.py:3:1: I001 [*] Import block is un-sorted or un-formatted
   |
 1 |   """Декораторы для обработки ошибок в API endpoints."""
 2 |   
 3 | / import logging
 4 | | from functools import wraps
 5 | | from typing import Callable, Any
 6 | | 
 7 | | from fastapi import HTTPException
 8 | | from sqlalchemy.ext.asyncio import AsyncSession
 9 | | 
10 | | from src.domain.exceptions.api_exceptions import (
11 | |     OpenRouterAPIError,
12 | |     OpenRouterRateLimitError,
13 | |     OpenRouterTimeoutError,
14 | | )
15 | | from src.domain.exceptions.business import BusinessRuleError
16 | | from src.domain.exceptions.not_found import (
17 | |     BirthdayNotFoundError,
18 | |     ResponsibleNotFoundError,
19 | | )
20 | | from src.domain.exceptions.validation import ValidationError
21 | | 
22 | | logger = logging.getLogger(__name__)
   | |_^ I001
   |
   = help: Organize imports

src/presentation/web/decorators.py:5:1: UP035 [*] Import from `collections.abc` instead: `Callable`
  |
3 | import logging
4 | from functools import wraps
5 | from typing import Callable, Any
  | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ UP035
6 | 
7 | from fastapi import HTTPException
  |
  = help: Import from `collections.abc`

src/presentation/web/decorators.py:28:1: W293 Blank line contains whitespace
   |
26 |     """
27 |     Декоратор для централизованной обработки ошибок в API endpoints.
28 |     
   | ^^^^ W293
29 |     Автоматически обрабатывает:
30 |     - NotFound ошибки (404)
   |
   = help: Remove whitespace from blank line

src/presentation/web/decorators.py:35:1: W293 Blank line contains whitespace
   |
33 |     - API ошибки (502, 503, 504)
34 |     - Неожиданные ошибки (500)
35 |     
   | ^^^^ W293
36 |     Автоматически выполняет rollback сессии при ошибках.
   |
   = help: Remove whitespace from blank line

src/presentation/web/decorators.py:37:1: W293 Blank line contains whitespace
   |
36 |     Автоматически выполняет rollback сессии при ошибках.
37 |     
   | ^^^^ W293
38 |     Примечание: session должен быть передан через Depends(get_db_session) в FastAPI.
39 |     """
   |
   = help: Remove whitespace from blank line

src/presentation/web/decorators.py:45:1: W293 [*] Blank line contains whitespace
   |
43 |         # FastAPI передает зависимости через kwargs с именами параметров функции
44 |         session: AsyncSession | None = None
45 |         
   | ^^^^^^^^ W293
46 |         # Ищем session в kwargs по имени параметра
47 |         if "session" in kwargs:
   |
   = help: Remove whitespace from blank line

src/presentation/web/decorators.py:49:1: W293 [*] Blank line contains whitespace
   |
47 |         if "session" in kwargs:
48 |             session = kwargs.get("session")
49 |         
   | ^^^^^^^^ W293
50 |         # Если не нашли в kwargs, проверяем позиционные аргументы
51 |         # (на случай, если session передана напрямую)
   |
   = help: Remove whitespace from blank line

src/presentation/web/decorators.py:57:1: W293 [*] Blank line contains whitespace
   |
55 |                     session = arg
56 |                     break
57 |         
   | ^^^^^^^^ W293
58 |         try:
59 |             return await func(*args, **kwargs)
   |
   = help: Remove whitespace from blank line

src/presentation/web/decorators.py:106:1: W293 [*] Blank line contains whitespace
    |
104 |                 detail="Internal server error"
105 |             ) from e
106 |     
    | ^^^^ W293
107 |     return wrapper
    |
    = help: Remove whitespace from blank line

src/presentation/web/dependencies.py:13:1: W293 Blank line contains whitespace
   |
11 |     """
12 |     Dependency для получения сессии БД.
13 |     
   | ^^^^ W293
14 |     Сессия автоматически закрывается после завершения запроса.
15 |     """
   |
   = help: Remove whitespace from blank line

src/presentation/web/dependencies.py:24:1: W293 Blank line contains whitespace
   |
22 |     """
23 |     Dependency для получения фабрики use-cases.
24 |     
   | ^^^^ W293
25 |     Args:
26 |         session: Сессия БД, получаемая через dependency injection.
   |
   = help: Remove whitespace from blank line

src/presentation/web/dependencies.py:27:1: W293 Blank line contains whitespace
   |
25 |     Args:
26 |         session: Сессия БД, получаемая через dependency injection.
27 |     
   | ^^^^ W293
28 |     Returns:
29 |         UseCaseFactory с настроенными зависимостями
   |
   = help: Remove whitespace from blank line

src/presentation/web/dependencies.py:37:1: W293 Blank line contains whitespace
   |
35 |     """
36 |     Dependency для получения фабрики use-cases для read-only операций.
37 |     
   | ^^^^ W293
38 |     Используется для endpoints, которые только читают данные и не требуют транзакций.
39 |     Создает новую сессию БД для каждого запроса.
   |
   = help: Remove whitespace from blank line

src/presentation/web/routes/api.py:11:45: F401 [*] `src.domain.exceptions.not_found.BirthdayNotFoundError` imported but unused
   |
10 | from src.application.factories.use_case_factory import UseCaseFactory
11 | from src.domain.exceptions.not_found import BirthdayNotFoundError, ResponsibleNotFoundError
   |                                             ^^^^^^^^^^^^^^^^^^^^^ F401
12 | from src.domain.exceptions.validation import ValidationError
13 | from src.infrastructure.config.rate_limits import (
   |
   = help: Remove unused import

src/presentation/web/routes/api.py:11:68: F401 [*] `src.domain.exceptions.not_found.ResponsibleNotFoundError` imported but unused
   |
10 | from src.application.factories.use_case_factory import UseCaseFactory
11 | from src.domain.exceptions.not_found import BirthdayNotFoundError, ResponsibleNotFoundError
   |                                                                    ^^^^^^^^^^^^^^^^^^^^^^^^ F401
12 | from src.domain.exceptions.validation import ValidationError
13 | from src.infrastructure.config.rate_limits import (
   |
   = help: Remove unused import

src/presentation/web/routes/api.py:12:46: F401 [*] `src.domain.exceptions.validation.ValidationError` imported but unused
   |
10 | from src.application.factories.use_case_factory import UseCaseFactory
11 | from src.domain.exceptions.not_found import BirthdayNotFoundError, ResponsibleNotFoundError
12 | from src.domain.exceptions.validation import ValidationError
   |                                              ^^^^^^^^^^^^^^^ F401
13 | from src.infrastructure.config.rate_limits import (
14 |     ACCESS_CHECK_LIMIT,
   |
   = help: Remove unused import: `src.domain.exceptions.validation.ValidationError`

src/presentation/web/routes/api.py:122:1: E402 Module level import not at top of file
    |
121 |   # Импортируем dependencies из отдельного модуля
122 | / from src.presentation.web.dependencies import (
123 | |     get_db_session,
124 | |     get_readonly_use_case_factory,
125 | |     get_use_case_factory,
126 | | )
    | |_^ E402
    |

src/presentation/web/routes/api.py:153:1: W293 Blank line contains whitespace
    |
151 |     """
152 |     Dependency для проверки прав доступа к панели управления.
153 |     
    | ^^^^ W293
154 |     Проверяет:
155 |     1. Авторизацию через Telegram (verify_telegram_auth)
    |
    = help: Remove whitespace from blank line

src/presentation/web/routes/api.py:157:1: W293 Blank line contains whitespace
    |
155 |     1. Авторизацию через Telegram (verify_telegram_auth)
156 |     2. Наличие прав доступа к панели (check_panel_access)
157 |     
    | ^^^^ W293
158 |     Raises:
159 |         HTTPException 401: Если пользователь не авторизован или нет user_id
    |
    = help: Remove whitespace from blank line

src/presentation/web/routes/api.py:169:1: W293 [*] Blank line contains whitespace
    |
167 |     use_case = factory.create_panel_access_use_case()
168 |     has_access = await use_case.execute(user_id)
169 |     
    | ^^^^ W293
170 |     if not has_access:
171 |         raise HTTPException(
    |
    = help: Remove whitespace from blank line

src/presentation/web/routes/api.py:175:1: W293 [*] Blank line contains whitespace
    |
173 |             detail="Access denied. You don't have permission to access the panel."
174 |         )
175 |     
    | ^^^^ W293
176 |     return user
    |
    = help: Remove whitespace from blank line

Found 60 errors.
[*] 37 fixable with the `--fix` option (20 hidden fixes can be enabled with the `--unsafe-fixes` option).
Error: Process completed with exit code 1.