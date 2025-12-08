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
======================== 2 warnings, 8 errors in 3.63s =========================
Error: Process completed with exit code 2.