1s
1s
1s
2s
11s
16s
0s
0s
1s
0s
4s
Run # Запускаем основные тесты
  
============================= test session starts ==============================
platform linux -- Python 3.11.14, pytest-7.4.3, pluggy-1.6.0 -- /opt/hostedtoolcache/Python/3.11.14/x64/bin/python
cachedir: .pytest_cache
rootdir: /home/runner/work/tg_bot_HB/tg_bot_HB/backend
configfile: pytest.ini
plugins: anyio-3.7.1, asyncio-0.21.1, mock-3.12.0, cov-4.1.0
asyncio: mode=Mode.AUTO
collecting ... collected 171 items / 1 error
==================================== ERRORS ====================================
____ ERROR collecting tests/infrastructure/test_notifications_scheduler.py _____
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/python.py:617: in _importtestmodule
    mod = import_path(self.path, mode=importmode, root=self.config.rootpath)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/pathlib.py:567: in import_path
    importlib.import_module(module_name)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1204: in _gcd_import
    ???
<frozen importlib._bootstrap>:1176: in _find_and_load
    ???
<frozen importlib._bootstrap>:1147: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:690: in _load_unlocked
    ???
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:177: in exec_module
    source_stat, co = _rewrite_test(fn, self.config)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:359: in _rewrite_test
    tree = ast.parse(source, filename=strfn)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/ast.py:50: in parse
    return compile(source, filename, mode, flags,
E     File "/home/runner/work/tg_bot_HB/tg_bot_HB/backend/tests/infrastructure/test_notifications_scheduler.py", line 34
E       importlib.reload(notifications_scheduler)
E   IndentationError: unexpected indent
---------- coverage: platform linux, python 3.11.14-final-0 ----------
Name                                                                       Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------------------------------------
src/__init__.py                                                                0      0   100%
src/application/__init__.py                                                    0      0   100%
src/application/factories/__init__.py                                          0      0   100%
src/application/factories/use_case_factory.py                                 94     45    52%   40-47, 51-53, 57-59, 63-65, 69-71, 75-83, 87-89, 93-95, 99, 108, 116, 126, 130, 137, 141, 145-148
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
src/application/use_cases/auth/verify_telegram_auth.py                        10      6    40%   8-9, 13-17
src/application/use_cases/birthday/__init__.py                                 0      0   100%
src/application/use_cases/birthday/create_birthday.py                          9      3    67%   9, 20-28
src/application/use_cases/birthday/delete_birthday.py                          9      5    44%   6, 10-13
src/application/use_cases/birthday/get_all_birthdays.py                        7      2    71%   9, 13
src/application/use_cases/birthday/get_birthdays_by_date.py                    8      2    75%   9, 13
src/application/use_cases/birthday/update_birthday.py                         12      6    50%   9, 21-33
src/application/use_cases/calendar/__init__.py                                 0      0   100%
src/application/use_cases/calendar/get_calendar_data.py                       14      7    50%   15-17, 24-28
src/application/use_cases/greeting/__init__.py                                 0      0   100%
src/application/use_cases/greeting/create_card.py                             12      6    50%   12-13, 22-26
src/application/use_cases/greeting/generate_greeting.py                       11      6    45%   11-12, 22-26
src/application/use_cases/holiday/__init__.py                                  0      0   100%
src/application/use_cases/holiday/create_holiday.py                            9      3    67%   9, 18-24
src/application/use_cases/holiday/delete_holiday.py                            9      5    44%   6, 10-13
src/application/use_cases/holiday/update_holiday.py                           12      6    50%   9, 19-29
src/application/use_cases/panel/__init__.py                                    0      0   100%
src/application/use_cases/panel/check_panel_access.py                          6      2    67%   6, 10
src/application/use_cases/panel/record_panel_access.py                         6      2    67%   6, 10
src/application/use_cases/responsible/__init__.py                              0      0   100%
src/application/use_cases/responsible/assign_responsible_to_date.py           10      5    50%   8, 12-15
src/application/use_cases/responsible/create_responsible.py                    8      3    62%   7, 16-22
src/application/use_cases/responsible/delete_responsible.py                    9      5    44%   6, 10-13
src/application/use_cases/responsible/get_all_responsible.py                   7      2    71%   9, 13
src/application/use_cases/responsible/update_responsible.py                   11      6    45%   7, 17-27
src/application/use_cases/search/__init__.py                                   0      0   100%
src/application/use_cases/search/search_people.py                             17     10    41%   13-14, 23-33
src/domain/entities/__init__.py                                                0      0   100%
src/domain/entities/birthday.py                                               15      4    73%   16-22
src/domain/entities/professional_holiday.py                                    8      0   100%
src/domain/entities/responsible_person.py                                      7      0   100%
src/domain/exceptions/__init__.py                                              5      0   100%
src/domain/exceptions/api_exceptions.py                                       12      4    67%   14-15, 22, 29
src/domain/exceptions/base.py                                                  2      0   100%
src/domain/exceptions/business.py                                              3      0   100%
src/domain/exceptions/not_found.py                                             7      0   100%
src/domain/exceptions/validation.py                                            5      0   100%
src/infrastructure/__init__.py                                                 0      0   100%
src/infrastructure/config/__init__.py                                          0      0   100%
src/infrastructure/config/openrouter_config.py                                18      8    56%   27-40
src/infrastructure/database/__init__.py                                        0      0   100%
src/infrastructure/database/database.py                                       12      6    50%   8-13, 21-22, 26-27
src/infrastructure/database/database_factory.py                               10      6    40%   12-17
src/infrastructure/database/models.py                                         47      0   100%
src/infrastructure/database/repositories/__init__.py                           0      0   100%
src/infrastructure/database/repositories/birthday_repository_impl.py          61     43    30%   13, 17, 28, 38-48, 51-55, 58-62, 65-72, 75-93, 96-102, 105-116, 119-121
src/infrastructure/database/repositories/holiday_repository_impl.py           48     33    31%   13, 17, 25-33, 36-40, 43-49, 52-68, 71-77, 80-82
src/infrastructure/database/repositories/panel_access_repository_impl.py      15      7    53%   10, 14-16, 20-22
src/infrastructure/database/repositories/responsible_repository_impl.py       65     48    26%   16, 20, 28-36, 39-43, 46-61, 64-80, 83-89, 93-108, 111-122, 125-127
src/infrastructure/external/__init__.py                                        0      0   100%
src/infrastructure/external/openrouter_client_impl.py                         56     47    16%   17-21, 33-100, 112-146
src/infrastructure/external/telegram_auth.py                                  43     32    26%   14-42, 46-55, 61-62, 67-68, 73-77
src/infrastructure/image/__init__.py                                           0      0   100%
src/infrastructure/image/card_generator.py                                    79     67    15%   15-25, 37-121, 125-144, 148-153
src/infrastructure/services/__init__.py                                        0      0   100%
src/infrastructure/services/notification_service_impl.py                      87     69    21%   22-24, 28-32, 36-49, 60-76, 87-106, 117-126, 132-138, 142-148
src/infrastructure/services/notifications_scheduler.py                        30     30     0%   1-65
src/presentation/__init__.py                                                   0      0   100%
src/presentation/telegram/__init__.py                                          0      0   100%
src/presentation/telegram/bot.py                                              26     26     0%   1-47
src/presentation/telegram/handlers/__init__.py                                 2      2     0%   1-10
src/presentation/telegram/handlers/birthday_handlers.py                       64     64     0%   1-103
src/presentation/telegram/handlers/calendar_handler.py                        72     72     0%   1-109
src/presentation/telegram/handlers/greeting_handlers.py                       87     87     0%   1-148
src/presentation/telegram/handlers/panel_handler.py                           17     17     0%   1-33
src/presentation/telegram/handlers/responsible_handlers.py                    45     45     0%   1-74
src/presentation/telegram/handlers/start_handler.py                            8      8     0%   1-13
src/presentation/telegram/keyboards.py                                        19     19     0%   1-106
src/presentation/web/__init__.py                                               0      0   100%
src/presentation/web/app.py                                                   15      2    87%   14, 31
src/presentation/web/routes/__init__.py                                        0      0   100%
src/presentation/web/routes/api.py                                           248    170    31%   71-73, 79, 85-96, 104-114, 121-127, 137-144, 150-153, 173-202, 213-236, 246-259, 265-268, 286-304, 315-344, 354-367, 377-396, 405-409, 427-446, 455-475
--------------------------------------------------------------------------------------------------------
TOTAL                                                                       1548   1053    32%
Coverage HTML written to dir htmlcov
Coverage XML written to file coverage.xml
=========================== short test summary info ============================
ERROR tests/infrastructure/test_notifications_scheduler.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 2 warnings, 1 error in 2.75s =========================
Error: Process completed with exit code 2.
0s
0s
0s
0s
0s
0s
0s
Post job cleanup.
/usr/bin/git version
git version 2.52.0
Temporarily overriding HOME='/home/runner/work/_temp/24456a5c-d27e-4dfb-8b85-4e1fb408c525' before making global git config changes
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
