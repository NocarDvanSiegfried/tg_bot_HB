Run # Запускаем основные тесты
  # Запускаем основные тесты
  pytest tests/application tests/domain tests/infrastructure tests/presentation/web \
    -v --tb=short --cov=src --cov-report=term-missing --cov-report=xml --cov-report=html
  # Запускаем presentation/telegram тесты отдельно для изоляции
  pytest tests/presentation/telegram \
    -v --tb=short --cov=src --cov-append --cov-report=term-missing --cov-report=xml --cov-report=html
  shell: /usr/bin/bash -e {0}
  env:
    pythonLocation: /opt/hostedtoolcache/Python/3.11.14/x64
    PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.14/x64/lib/pkgconfig
    Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.14/x64
    Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.14/x64
    Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.14/x64
    LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.14/x64/lib
    PYTHONPATH: /home/runner/work/tg_bot_HB/tg_bot_HB/backend
  
============================= test session starts ==============================
platform linux -- Python 3.11.14, pytest-7.4.3, pluggy-1.6.0 -- /opt/hostedtoolcache/Python/3.11.14/x64/bin/python
cachedir: .pytest_cache
rootdir: /home/runner/work/tg_bot_HB/tg_bot_HB/backend
configfile: pytest.ini
plugins: anyio-3.7.1, asyncio-0.21.1, mock-3.12.0, cov-4.1.0
asyncio: mode=Mode.AUTO
collecting ... collected 197 items
tests/application/test_assign_responsible_use_case.py::TestAssignResponsibleToDateUseCase::test_assign_responsible_success PASSED [  0%]
tests/application/test_assign_responsible_use_case.py::TestAssignResponsibleToDateUseCase::test_assign_responsible_not_found PASSED [  1%]
tests/application/test_check_panel_access_use_case.py::TestCheckPanelAccessUseCase::test_check_panel_access_has_access PASSED [  1%]
tests/application/test_check_panel_access_use_case.py::TestCheckPanelAccessUseCase::test_check_panel_access_no_access PASSED [  2%]
tests/application/test_create_birthday_use_case.py::TestCreateBirthdayUseCase::test_create_birthday_success PASSED [  2%]
tests/application/test_create_birthday_use_case.py::TestCreateBirthdayUseCase::test_create_birthday_without_comment PASSED [  3%]
tests/application/test_create_card_use_case.py::TestCreateCardUseCase::test_create_card_success PASSED [  3%]
tests/application/test_create_card_use_case.py::TestCreateCardUseCase::test_create_card_without_qr PASSED [  4%]
tests/application/test_create_card_use_case.py::TestCreateCardUseCase::test_create_card_birthday_not_found PASSED [  4%]
tests/application/test_create_holiday_use_case.py::TestCreateHolidayUseCase::test_create_holiday_success PASSED [  5%]
tests/application/test_create_holiday_use_case.py::TestCreateHolidayUseCase::test_create_holiday_without_description PASSED [  5%]
tests/application/test_create_responsible_use_case.py::TestCreateResponsibleUseCase::test_create_responsible_success PASSED [  6%]
tests/application/test_delete_birthday_use_case.py::TestDeleteBirthdayUseCase::test_delete_birthday_success PASSED [  6%]
tests/application/test_delete_birthday_use_case.py::TestDeleteBirthdayUseCase::test_delete_birthday_not_found PASSED [  7%]
tests/application/test_delete_holiday_use_case.py::TestDeleteHolidayUseCase::test_delete_holiday_success PASSED [  7%]
tests/application/test_delete_holiday_use_case.py::TestDeleteHolidayUseCase::test_delete_holiday_not_found PASSED [  8%]
tests/application/test_delete_responsible_use_case.py::TestDeleteResponsibleUseCase::test_delete_responsible_success PASSED [  8%]
tests/application/test_delete_responsible_use_case.py::TestDeleteResponsibleUseCase::test_delete_responsible_not_found PASSED [  9%]
tests/application/test_generate_greeting_use_case.py::TestGenerateGreetingUseCase::test_generate_greeting_success PASSED [  9%]
tests/application/test_generate_greeting_use_case.py::TestGenerateGreetingUseCase::test_generate_greeting_with_theme PASSED [ 10%]
tests/application/test_generate_greeting_use_case.py::TestGenerateGreetingUseCase::test_generate_greeting_birthday_not_found PASSED [ 10%]
tests/application/test_get_all_birthdays_use_case.py::TestGetAllBirthdaysUseCase::test_get_all_birthdays_success PASSED [ 11%]
tests/application/test_get_all_birthdays_use_case.py::TestGetAllBirthdaysUseCase::test_get_all_birthdays_empty PASSED [ 11%]
tests/application/test_get_all_responsible_use_case.py::TestGetAllResponsibleUseCase::test_get_all_responsible_success PASSED [ 12%]
tests/application/test_get_all_responsible_use_case.py::TestGetAllResponsibleUseCase::test_get_all_responsible_empty PASSED [ 12%]
tests/application/test_get_birthdays_by_date.py::TestGetBirthdaysByDateUseCase::test_get_birthdays_by_date_success PASSED [ 13%]
tests/application/test_get_birthdays_by_date.py::TestGetBirthdaysByDateUseCase::test_get_birthdays_by_date_empty PASSED [ 13%]
tests/application/test_get_birthdays_by_date.py::TestGetBirthdaysByDateUseCase::test_get_birthdays_by_date_repository_error PASSED [ 14%]
tests/application/test_get_calendar_data_use_case.py::TestGetCalendarDataUseCase::test_get_calendar_data_success PASSED [ 14%]
tests/application/test_get_calendar_data_use_case.py::TestGetCalendarDataUseCase::test_get_calendar_data_empty PASSED [ 15%]
tests/application/test_get_calendar_data_use_case.py::TestGetCalendarDataUseCase::test_get_calendar_data_repository_error PASSED [ 15%]
tests/application/test_record_panel_access_edge_cases.py::TestRecordPanelAccessUseCaseEdgeCases::test_execute_with_large_user_id PASSED [ 16%]
tests/application/test_record_panel_access_edge_cases.py::TestRecordPanelAccessUseCaseEdgeCases::test_execute_repository_error PASSED [ 16%]
tests/application/test_record_panel_access_edge_cases.py::TestRecordPanelAccessUseCaseEdgeCases::test_execute_zero_user_id PASSED [ 17%]
tests/application/test_record_panel_access_use_case.py::TestRecordPanelAccessUseCase::test_record_panel_access_success PASSED [ 17%]
tests/application/test_record_panel_access_use_case.py::TestRecordPanelAccessUseCase::test_record_panel_access_different_user PASSED [ 18%]
tests/application/test_search_people.py::TestSearchPeopleUseCase::test_search_success PASSED [ 18%]
tests/application/test_search_people.py::TestSearchPeopleUseCase::test_search_empty_result PASSED [ 19%]
tests/application/test_search_people.py::TestSearchPeopleUseCase::test_search_only_birthdays PASSED [ 19%]
tests/application/test_search_people.py::TestSearchPeopleUseCase::test_search_only_responsible PASSED [ 20%]
tests/application/test_search_people.py::TestSearchPeopleUseCase::test_search_repository_error PASSED [ 20%]
tests/application/test_update_birthday_use_case.py::TestUpdateBirthdayUseCase::test_update_birthday_success PASSED [ 21%]
tests/application/test_update_birthday_use_case.py::TestUpdateBirthdayUseCase::test_update_birthday_not_found PASSED [ 21%]
tests/application/test_update_holiday_use_case.py::TestUpdateHolidayUseCase::test_update_holiday_success PASSED [ 22%]
tests/application/test_update_holiday_use_case.py::TestUpdateHolidayUseCase::test_update_holiday_partial PASSED [ 22%]
tests/application/test_update_holiday_use_case.py::TestUpdateHolidayUseCase::test_update_holiday_not_found PASSED [ 23%]
tests/application/test_update_responsible_use_case.py::TestUpdateResponsibleUseCase::test_update_responsible_success PASSED [ 23%]
tests/application/test_update_responsible_use_case.py::TestUpdateResponsibleUseCase::test_update_responsible_not_found PASSED [ 24%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_create_birthday_use_cases PASSED [ 24%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_create_calendar_use_case PASSED [ 25%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_create_responsible_use_cases PASSED [ 25%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_create_search_use_case PASSED [ 26%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_create_greeting_use_cases PASSED [ 26%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_create_panel_access_use_case PASSED [ 27%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_create_auth_use_case PASSED [ 27%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_lazy_initialization_repositories PASSED [ 28%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_factory_without_session PASSED [ 28%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_openrouter_client_missing_env PASSED [ 29%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_auth_use_case_missing_token PASSED [ 29%]
tests/application/test_verify_telegram_auth_use_case.py::TestVerifyTelegramAuthUseCase::test_verify_telegram_auth_success PASSED [ 30%]
tests/application/test_verify_telegram_auth_use_case.py::TestVerifyTelegramAuthUseCase::test_verify_telegram_auth_invalid PASSED [ 30%]
tests/application/test_verify_telegram_auth_use_case.py::TestVerifyTelegramAuthUseCase::test_verify_telegram_auth_empty_user_data PASSED [ 31%]
tests/domain/test_birthday_entity.py::TestBirthdayEntity::test_birthday_creation PASSED [ 31%]
tests/domain/test_birthday_entity.py::TestBirthdayEntity::test_birthday_without_comment PASSED [ 32%]
tests/domain/test_birthday_entity.py::TestBirthdayEntity::test_calculate_age_same_year PASSED [ 32%]
tests/domain/test_birthday_entity.py::TestBirthdayEntity::test_calculate_age_next_year PASSED [ 33%]
tests/domain/test_birthday_entity.py::TestBirthdayEntity::test_calculate_age_before_birthday PASSED [ 34%]
tests/domain/test_birthday_entity.py::TestBirthdayEntity::test_calculate_age_after_birthday PASSED [ 34%]
tests/infrastructure/test_base_repository.py::TestBaseRepositoryImpl::test_create PASSED [ 35%]
tests/infrastructure/test_base_repository.py::TestBaseRepositoryImpl::test_get_by_id_found PASSED [ 35%]
tests/infrastructure/test_base_repository.py::TestBaseRepositoryImpl::test_get_by_id_not_found PASSED [ 36%]
tests/infrastructure/test_base_repository.py::TestBaseRepositoryImpl::test_get_all PASSED [ 36%]
tests/infrastructure/test_base_repository.py::TestBaseRepositoryImpl::test_get_all_empty PASSED [ 37%]
tests/infrastructure/test_base_repository.py::TestBaseRepositoryImpl::test_delete_found PASSED [ 37%]
tests/infrastructure/test_base_repository.py::TestBaseRepositoryImpl::test_delete_not_found PASSED [ 38%]
tests/infrastructure/test_base_repository.py::TestBaseRepositoryImpl::test_update_not_implemented PASSED [ 38%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_create_birthday PASSED [ 39%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_get_by_id_found PASSED [ 39%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_get_by_id_not_found PASSED [ 40%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_get_by_date PASSED [ 40%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_delete_birthday PASSED [ 41%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_get_by_date_range PASSED [ 41%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_get_by_date_range_empty PASSED [ 42%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_update_birthday PASSED [ 42%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_update_birthday_no_id PASSED [ 43%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_update_birthday_not_found PASSED [ 43%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_search PASSED [ 44%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_search_empty PASSED [ 44%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_search_by_company PASSED [ 45%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_get_all PASSED [ 45%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_get_all_empty PASSED [ 46%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_to_model_conversion PASSED [ 46%]
tests/infrastructure/test_card_generator.py::TestCardGeneratorImpl::test_generate_card_handles_font_load_error_with_specific_exception PASSED [ 47%]
tests/infrastructure/test_card_generator.py::TestCardGeneratorImpl::test_generate_card_handles_ioerror_with_specific_exception PASSED [ 47%]
tests/infrastructure/test_database.py::TestDatabase::test_database_initialization PASSED [ 48%]
tests/infrastructure/test_database.py::TestDatabase::test_get_session PASSED [ 48%]
tests/infrastructure/test_database.py::TestDatabase::test_create_tables PASSED [ 49%]
tests/infrastructure/test_database.py::TestDatabase::test_multiple_sessions PASSED [ 49%]
tests/infrastructure/test_database_factory.py::TestDatabaseFactory::test_singleton_pattern PASSED [ 50%]
tests/infrastructure/test_database_factory.py::TestDatabaseFactory::test_create_database_with_env PASSED [ 50%]
tests/infrastructure/test_database_factory.py::TestDatabaseFactory::test_missing_database_url PASSED [ 51%]
tests/infrastructure/test_database_factory.py::TestDatabaseFactory::test_database_url_empty_string PASSED [ 51%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_create_holiday PASSED [ 52%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_get_by_id_exists PASSED [ 52%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_get_by_id_not_exists PASSED [ 53%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_get_by_date PASSED [ 53%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_update_holiday PASSED [ 54%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_update_holiday_no_id PASSED [ 54%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_update_holiday_not_found PASSED [ 55%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_delete_holiday PASSED [ 55%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_delete_holiday_not_exists PASSED [ 56%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_get_all PASSED [ 56%]
tests/infrastructure/test_notification_service_impl.py::TestNotificationServiceImpl::test_send_today_notifications_logs_error_on_failure PASSED [ 57%]
tests/infrastructure/test_notification_service_impl.py::TestNotificationServiceImpl::test_send_week_notifications_logs_error_on_failure PASSED [ 57%]
tests/infrastructure/test_notification_service_impl.py::TestNotificationServiceImpl::test_send_month_notifications_logs_error_on_failure PASSED [ 58%]
tests/infrastructure/test_notifications_scheduler.py::TestNotificationsScheduler::test_scheduler_initialization PASSED [ 58%]
tests/infrastructure/test_notifications_scheduler.py::TestNotificationsScheduler::test_scheduler_start PASSED [ 59%]
tests/infrastructure/test_notifications_scheduler.py::TestNotificationsScheduler::test_scheduler_stop PASSED [ 59%]
tests/infrastructure/test_notifications_scheduler.py::TestNotificationsScheduler::test_scheduler_jobs_configuration PASSED [ 60%]
tests/infrastructure/test_notifications_scheduler.py::TestNotificationsScheduler::test_send_today_execution PASSED [ 60%]
tests/infrastructure/test_notifications_scheduler.py::TestNotificationsScheduler::test_send_week_execution PASSED [ 61%]
tests/infrastructure/test_notifications_scheduler.py::TestNotificationsScheduler::test_send_month_execution PASSED [ 61%]
tests/infrastructure/test_notifications_scheduler.py::TestNotificationsScheduler::test_send_today_error_handling PASSED [ 62%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_success PASSED [ 62%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_with_theme PASSED [ 63%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_http_error PASSED [ 63%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_timeout_error PASSED [ 64%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_invalid_response_not_dict PASSED [ 64%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_invalid_response_missing_choices PASSED [ 65%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_invalid_response_empty_choices PASSED [ 65%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_invalid_response_missing_message PASSED [ 66%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_invalid_response_missing_content PASSED [ 67%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_invalid_response_content_not_string PASSED [ 67%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_retry_on_http_error PASSED [ 68%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_build_prompt_without_theme PASSED [ 68%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_build_prompt_with_theme PASSED [ 69%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_build_prompt_unknown_style_and_length PASSED [ 69%]
tests/infrastructure/test_panel_access_repository.py::TestPanelAccessRepositoryImpl::test_has_access_true PASSED [ 70%]
tests/infrastructure/test_panel_access_repository.py::TestPanelAccessRepositoryImpl::test_has_access_false PASSED [ 70%]
tests/infrastructure/test_panel_access_repository.py::TestPanelAccessRepositoryImpl::test_record_access PASSED [ 71%]
tests/infrastructure/test_panel_access_repository_bigint.py::TestPanelAccessRepositoryBigInt::test_record_access_with_large_user_id PASSED [ 71%]
tests/infrastructure/test_panel_access_repository_bigint.py::TestPanelAccessRepositoryBigInt::test_has_access_with_large_user_id PASSED [ 72%]
tests/infrastructure/test_panel_access_repository_edge_cases.py::TestPanelAccessRepositoryEdgeCases::test_record_access_zero_user_id PASSED [ 72%]
tests/infrastructure/test_panel_access_repository_edge_cases.py::TestPanelAccessRepositoryEdgeCases::test_record_access_negative_user_id PASSED [ 73%]
tests/infrastructure/test_panel_access_repository_edge_cases.py::TestPanelAccessRepositoryEdgeCases::test_has_access_multiple_records PASSED [ 73%]
tests/infrastructure/test_panel_access_repository_edge_cases.py::TestPanelAccessRepositoryEdgeCases::test_has_access_database_error PASSED [ 74%]
tests/infrastructure/test_panel_access_repository_edge_cases.py::TestPanelAccessRepositoryEdgeCases::test_record_access_database_error PASSED [ 74%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_create_responsible PASSED [ 75%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_get_by_id_exists PASSED [ 75%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_get_by_id_not_exists PASSED [ 76%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_get_by_date_exists PASSED [ 76%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_get_by_date_not_exists PASSED [ 77%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_assign_to_date PASSED [ 77%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_update_responsible PASSED [ 78%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_update_responsible_no_id PASSED [ 78%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_update_responsible_not_found PASSED [ 79%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_delete_responsible PASSED [ 79%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_delete_responsible_not_exists PASSED [ 80%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_get_all PASSED [ 80%]
tests/infrastructure/test_telegram_auth.py::TestTelegramAuthServiceImpl::test_verify_init_data_success PASSED [ 81%]
tests/infrastructure/test_telegram_auth.py::TestTelegramAuthServiceImpl::test_verify_init_data_invalid_hash PASSED [ 81%]
tests/infrastructure/test_telegram_auth.py::TestTelegramAuthServiceImpl::test_verify_init_data_missing_hash PASSED [ 82%]
tests/infrastructure/test_telegram_auth.py::TestTelegramAuthServiceImpl::test_verify_init_data_invalid_format PASSED [ 82%]
tests/infrastructure/test_telegram_auth.py::TestTelegramAuthServiceImpl::test_parse_init_data_success PASSED [ 83%]
tests/infrastructure/test_telegram_auth.py::TestTelegramAuthServiceImpl::test_parse_init_data_without_user PASSED [ 83%]
tests/infrastructure/test_telegram_auth.py::TestTelegramAuthServiceImpl::test_parse_init_data_invalid_json PASSED [ 84%]
tests/infrastructure/test_telegram_auth.py::TestTelegramAuthServiceImpl::test_parse_init_data_invalid_format PASSED [ 84%]
tests/infrastructure/test_telegram_auth.py::TestDeprecatedFunctions::test_verify_telegram_init_data_function PASSED [ 85%]
tests/infrastructure/test_telegram_auth.py::TestDeprecatedFunctions::test_parse_init_data_function PASSED [ 85%]
tests/infrastructure/test_telegram_auth.py::TestDeprecatedFunctions::test_get_user_id_from_init_data_success PASSED [ 86%]
tests/infrastructure/test_telegram_auth.py::TestDeprecatedFunctions::test_get_user_id_from_init_data_no_user PASSED [ 86%]
tests/infrastructure/test_telegram_auth.py::TestDeprecatedFunctions::test_get_user_id_from_init_data_no_id PASSED [ 87%]
tests/presentation/web/test_api.py::TestAuthEndpoints::test_verify_init_data_success PASSED [ 87%]
tests/presentation/web/test_api.py::TestAuthEndpoints::test_verify_init_data_invalid PASSED [ 88%]
tests/presentation/web/test_api.py::TestCalendarEndpoints::test_get_calendar_success FAILED [ 88%]
tests/presentation/web/test_api.py::TestCalendarEndpoints::test_get_calendar_invalid_date FAILED [ 89%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_check_panel_access_success FAILED [ 89%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_check_panel_access_no_auth PASSED [ 90%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_list_birthdays FAILED [ 90%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_create_birthday_success PASSED [ 91%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_update_birthday_success PASSED [ 91%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_delete_birthday_success PASSED [ 92%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_list_responsible FAILED [ 92%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_create_responsible_success PASSED [ 93%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_update_responsible_success PASSED [ 93%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_delete_responsible_success PASSED [ 94%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_assign_responsible_success PASSED [ 94%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_search_people FAILED [ 95%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_generate_greeting_success FAILED [ 95%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_create_card_success FAILED [ 96%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_generate_greeting_not_found FAILED [ 96%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_create_birthday_validation_error FAILED [ 97%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_delete_birthday_not_found PASSED [ 97%]
tests/presentation/web/test_app.py::TestWebApp::test_app_creation PASSED [ 98%]
tests/presentation/web/test_app.py::TestWebApp::test_root_endpoint PASSED [ 98%]
tests/presentation/web/test_app.py::TestWebApp::test_cors_middleware_configured PASSED [ 99%]
tests/presentation/web/test_app.py::TestWebApp::test_router_included PASSED [100%]
=================================== FAILURES ===================================
_______________ TestCalendarEndpoints.test_get_calendar_success ________________
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1969: in _exec_single_context
    self.dialect.do_execute(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/default.py:922: in do_execute
    cursor.execute(statement, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:146: in execute
    self._adapt_connection._handle_exception(error)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:298: in _handle_exception
    raise error
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:128: in execute
    self.await_(_cursor.execute(operation, parameters))
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:125: in await_only
    return current.driver.switch(awaitable)  # type: ignore[no-any-return]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:185: in greenlet_spawn
    value = await result
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:48: in execute
    await self._execute(self._cursor.execute, sql, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:40: in _execute
    return await self._conn._execute(fn, *args, **kwargs)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:133: in _execute
    return await future
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:106: in run
    result = function()
E   sqlite3.OperationalError: no such table: birthdays
The above exception was the direct cause of the following exception:
tests/presentation/web/test_api.py:153: in test_get_calendar_success
    response = client.get("/api/calendar/2024-01-15")
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:499: in get
    return super().get(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:1041: in get
    return self.request(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:465: in request
    return super().request(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:814: in request
    return self.send(request, auth=auth, follow_redirects=follow_redirects)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:901: in send
    response = self._send_handling_auth(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:929: in _send_handling_auth
    response = self._send_handling_redirects(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:966: in _send_handling_redirects
    response = self._send_single_request(request)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:1002: in _send_single_request
    response = transport.handle_request(request)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:342: in handle_request
    raise exc
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:339: in handle_request
    portal.call(self.app, scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/anyio/from_thread.py:277: in call
    return cast(T_Retval, self.start_task_soon(func, *args).result())
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/concurrent/futures/_base.py:456: in result
    return self.__get_result()
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/concurrent/futures/_base.py:401: in __get_result
    raise self._exception
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/anyio/from_thread.py:217: in _call_func
    retval = await retval
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/applications.py:1106: in __call__
    await super().__call__(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/applications.py:122: in __call__
    await self.middleware_stack(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/errors.py:184: in __call__
    raise exc
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/errors.py:162: in __call__
    await self.app(scope, receive, _send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/cors.py:83: in __call__
    await self.app(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/exceptions.py:79: in __call__
    raise exc
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/exceptions.py:68: in __call__
    await self.app(scope, receive, sender)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py:20: in __call__
    raise e
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py:17: in __call__
    await self.app(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/routing.py:718: in __call__
    await route.handle(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/routing.py:276: in handle
    await self.app(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/routing.py:66: in app
    response = await func(request)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/routing.py:274: in app
    raw_response = await run_endpoint_function(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/routing.py:191: in run_endpoint_function
    return await dependant.call(**values)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/slowapi/extension.py:734: in async_wrapper
    response = await func(*args, **kwargs)  # type: ignore
src/presentation/web/routes/api.py:211: in get_calendar
    return await use_case.execute(check_date)
src/application/use_cases/calendar/get_calendar_data.py:24: in execute
    birthdays = await self.birthday_repository.get_by_date(check_date)
src/infrastructure/database/repositories/birthday_repository_impl.py:43: in get_by_date
    result = await self.session.execute(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/ext/asyncio/session.py:455: in execute
    result = await greenlet_spawn(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:190: in greenlet_spawn
    result = context.throw(*sys.exc_info())
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/session.py:2308: in execute
    return self._execute_internal(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/session.py:2190: in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/context.py:293: in orm_execute_statement
    result = conn.execute(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1416: in execute
    return meth(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/sql/elements.py:516: in _execute_on_connection
    return connection._execute_clauseelement(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1639: in _execute_clauseelement
    ret = self._execute_context(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1848: in _execute_context
    return self._exec_single_context(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1988: in _exec_single_context
    self._handle_dbapi_exception(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:2343: in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1969: in _exec_single_context
    self.dialect.do_execute(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/default.py:922: in do_execute
    cursor.execute(statement, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:146: in execute
    self._adapt_connection._handle_exception(error)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:298: in _handle_exception
    raise error
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:128: in execute
    self.await_(_cursor.execute(operation, parameters))
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:125: in await_only
    return current.driver.switch(awaitable)  # type: ignore[no-any-return]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:185: in greenlet_spawn
    value = await result
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:48: in execute
    await self._execute(self._cursor.execute, sql, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:40: in _execute
    return await self._conn._execute(fn, *args, **kwargs)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:133: in _execute
    return await future
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:106: in run
    result = function()
E   sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: birthdays
E   [SQL: SELECT birthdays.id, birthdays.full_name, birthdays.company, birthdays.position, birthdays.birth_date, birthdays.comment, birthdays.created_at, birthdays.updated_at 
E   FROM birthdays 
E   WHERE birthdays.birth_date = ?]
E   [parameters: ('2024-01-15',)]
E   (Background on this error at: https://sqlalche.me/e/20/e3q8)
_____________ TestCalendarEndpoints.test_get_calendar_invalid_date _____________
tests/presentation/web/test_api.py:163: in test_get_calendar_invalid_date
    assert response.status_code == 400
E   assert 422 == 400
E    +  where 422 = <Response [422 Unprocessable Entity]>.status_code
______________ TestPanelEndpoints.test_check_panel_access_success ______________
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1969: in _exec_single_context
    self.dialect.do_execute(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/default.py:922: in do_execute
    cursor.execute(statement, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:146: in execute
    self._adapt_connection._handle_exception(error)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:298: in _handle_exception
    raise error
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:128: in execute
    self.await_(_cursor.execute(operation, parameters))
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:125: in await_only
    return current.driver.switch(awaitable)  # type: ignore[no-any-return]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:185: in greenlet_spawn
    value = await result
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:48: in execute
    await self._execute(self._cursor.execute, sql, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:40: in _execute
    return await self._conn._execute(fn, *args, **kwargs)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:133: in _execute
    return await future
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:106: in run
    result = function()
E   sqlite3.OperationalError: no such table: panel_access
The above exception was the direct cause of the following exception:
tests/presentation/web/test_api.py:182: in test_check_panel_access_success
    response = client.get(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:499: in get
    return super().get(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:1041: in get
    return self.request(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:465: in request
    return super().request(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:814: in request
    return self.send(request, auth=auth, follow_redirects=follow_redirects)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:901: in send
    response = self._send_handling_auth(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:929: in _send_handling_auth
    response = self._send_handling_redirects(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:966: in _send_handling_redirects
    response = self._send_single_request(request)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:1002: in _send_single_request
    response = transport.handle_request(request)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:342: in handle_request
    raise exc
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:339: in handle_request
    portal.call(self.app, scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/anyio/from_thread.py:277: in call
    return cast(T_Retval, self.start_task_soon(func, *args).result())
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/concurrent/futures/_base.py:456: in result
    return self.__get_result()
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/concurrent/futures/_base.py:401: in __get_result
    raise self._exception
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/anyio/from_thread.py:217: in _call_func
    retval = await retval
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/applications.py:1106: in __call__
    await super().__call__(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/applications.py:122: in __call__
    await self.middleware_stack(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/errors.py:184: in __call__
    raise exc
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/errors.py:162: in __call__
    await self.app(scope, receive, _send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/cors.py:83: in __call__
    await self.app(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/exceptions.py:79: in __call__
    raise exc
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/exceptions.py:68: in __call__
    await self.app(scope, receive, sender)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py:20: in __call__
    raise e
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py:17: in __call__
    await self.app(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/routing.py:718: in __call__
    await route.handle(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/routing.py:276: in handle
    await self.app(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/routing.py:66: in app
    response = await func(request)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/routing.py:274: in app
    raw_response = await run_endpoint_function(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/routing.py:191: in run_endpoint_function
    return await dependant.call(**values)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/slowapi/extension.py:734: in async_wrapper
    response = await func(*args, **kwargs)  # type: ignore
src/presentation/web/routes/api.py:229: in check_panel_access
    has_access = await use_case.execute(user_id)
src/application/use_cases/panel/check_panel_access.py:10: in execute
    return await self.panel_access_repository.has_access(user_id)
src/infrastructure/database/repositories/panel_access_repository_impl.py:15: in has_access
    result = await self.session.execute(stmt)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/ext/asyncio/session.py:455: in execute
    result = await greenlet_spawn(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:190: in greenlet_spawn
    result = context.throw(*sys.exc_info())
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/session.py:2308: in execute
    return self._execute_internal(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/session.py:2190: in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/context.py:293: in orm_execute_statement
    result = conn.execute(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1416: in execute
    return meth(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/sql/elements.py:516: in _execute_on_connection
    return connection._execute_clauseelement(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1639: in _execute_clauseelement
    ret = self._execute_context(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1848: in _execute_context
    return self._exec_single_context(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1988: in _exec_single_context
    self._handle_dbapi_exception(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:2343: in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1969: in _exec_single_context
    self.dialect.do_execute(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/default.py:922: in do_execute
    cursor.execute(statement, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:146: in execute
    self._adapt_connection._handle_exception(error)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:298: in _handle_exception
    raise error
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:128: in execute
    self.await_(_cursor.execute(operation, parameters))
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:125: in await_only
    return current.driver.switch(awaitable)  # type: ignore[no-any-return]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:185: in greenlet_spawn
    value = await result
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:48: in execute
    await self._execute(self._cursor.execute, sql, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:40: in _execute
    return await self._conn._execute(fn, *args, **kwargs)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:133: in _execute
    return await future
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:106: in run
    result = function()
E   sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: panel_access
E   [SQL: SELECT panel_access.id, panel_access.user_id, panel_access.accessed_at 
E   FROM panel_access 
E   WHERE panel_access.user_id = ?
E    LIMIT ? OFFSET ?]
E   [parameters: (123, 1, 0)]
E   (Background on this error at: https://sqlalche.me/e/20/e3q8)
____________________ TestPanelEndpoints.test_list_birthdays ____________________
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1969: in _exec_single_context
    self.dialect.do_execute(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/default.py:922: in do_execute
    cursor.execute(statement, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:146: in execute
    self._adapt_connection._handle_exception(error)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:298: in _handle_exception
    raise error
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:128: in execute
    self.await_(_cursor.execute(operation, parameters))
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:125: in await_only
    return current.driver.switch(awaitable)  # type: ignore[no-any-return]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:185: in greenlet_spawn
    value = await result
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:48: in execute
    await self._execute(self._cursor.execute, sql, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:40: in _execute
    return await self._conn._execute(fn, *args, **kwargs)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:133: in _execute
    return await future
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:106: in run
    result = function()
E   sqlite3.OperationalError: no such table: birthdays
The above exception was the direct cause of the following exception:
tests/presentation/web/test_api.py:214: in test_list_birthdays
    response = client.get("/api/panel/birthdays")
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:499: in get
    return super().get(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:1041: in get
    return self.request(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:465: in request
    return super().request(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:814: in request
    return self.send(request, auth=auth, follow_redirects=follow_redirects)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:901: in send
    response = self._send_handling_auth(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:929: in _send_handling_auth
    response = self._send_handling_redirects(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:966: in _send_handling_redirects
    response = self._send_single_request(request)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:1002: in _send_single_request
    response = transport.handle_request(request)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:342: in handle_request
    raise exc
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:339: in handle_request
    portal.call(self.app, scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/anyio/from_thread.py:277: in call
    return cast(T_Retval, self.start_task_soon(func, *args).result())
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/concurrent/futures/_base.py:456: in result
    return self.__get_result()
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/concurrent/futures/_base.py:401: in __get_result
    raise self._exception
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/anyio/from_thread.py:217: in _call_func
    retval = await retval
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/applications.py:1106: in __call__
    await super().__call__(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/applications.py:122: in __call__
    await self.middleware_stack(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/errors.py:184: in __call__
    raise exc
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/errors.py:162: in __call__
    await self.app(scope, receive, _send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/cors.py:83: in __call__
    await self.app(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/exceptions.py:79: in __call__
    raise exc
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/exceptions.py:68: in __call__
    await self.app(scope, receive, sender)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py:20: in __call__
    raise e
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py:17: in __call__
    await self.app(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/routing.py:718: in __call__
    await route.handle(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/routing.py:276: in handle
    await self.app(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/routing.py:66: in app
    response = await func(request)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/routing.py:274: in app
    raw_response = await run_endpoint_function(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/routing.py:191: in run_endpoint_function
    return await dependant.call(**values)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/slowapi/extension.py:734: in async_wrapper
    response = await func(*args, **kwargs)  # type: ignore
src/presentation/web/routes/api.py:243: in list_birthdays
    birthdays = await use_case.execute()
src/application/use_cases/birthday/get_all_birthdays.py:13: in execute
    return await self.birthday_repository.get_all()
src/infrastructure/database/repositories/base_repository.py:94: in get_all
    result = await self.session.execute(select(self.model_class))
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/ext/asyncio/session.py:455: in execute
    result = await greenlet_spawn(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:190: in greenlet_spawn
    result = context.throw(*sys.exc_info())
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/session.py:2308: in execute
    return self._execute_internal(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/session.py:2190: in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/context.py:293: in orm_execute_statement
    result = conn.execute(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1416: in execute
    return meth(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/sql/elements.py:516: in _execute_on_connection
    return connection._execute_clauseelement(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1639: in _execute_clauseelement
    ret = self._execute_context(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1848: in _execute_context
    return self._exec_single_context(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1988: in _exec_single_context
    self._handle_dbapi_exception(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:2343: in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1969: in _exec_single_context
    self.dialect.do_execute(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/default.py:922: in do_execute
    cursor.execute(statement, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:146: in execute
    self._adapt_connection._handle_exception(error)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:298: in _handle_exception
    raise error
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:128: in execute
    self.await_(_cursor.execute(operation, parameters))
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:125: in await_only
    return current.driver.switch(awaitable)  # type: ignore[no-any-return]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:185: in greenlet_spawn
    value = await result
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:48: in execute
    await self._execute(self._cursor.execute, sql, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:40: in _execute
    return await self._conn._execute(fn, *args, **kwargs)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:133: in _execute
    return await future
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:106: in run
    result = function()
E   sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: birthdays
E   [SQL: SELECT birthdays.id, birthdays.full_name, birthdays.company, birthdays.position, birthdays.birth_date, birthdays.comment, birthdays.created_at, birthdays.updated_at 
E   FROM birthdays]
E   (Background on this error at: https://sqlalche.me/e/20/e3q8)
___________________ TestPanelEndpoints.test_list_responsible ___________________
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1969: in _exec_single_context
    self.dialect.do_execute(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/default.py:922: in do_execute
    cursor.execute(statement, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:146: in execute
    self._adapt_connection._handle_exception(error)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:298: in _handle_exception
    raise error
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:128: in execute
    self.await_(_cursor.execute(operation, parameters))
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:125: in await_only
    return current.driver.switch(awaitable)  # type: ignore[no-any-return]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:185: in greenlet_spawn
    value = await result
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:48: in execute
    await self._execute(self._cursor.execute, sql, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:40: in _execute
    return await self._conn._execute(fn, *args, **kwargs)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:133: in _execute
    return await future
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:106: in run
    result = function()
E   sqlite3.OperationalError: no such table: responsible_persons
The above exception was the direct cause of the following exception:
tests/presentation/web/test_api.py:302: in test_list_responsible
    response = client.get("/api/panel/responsible")
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:499: in get
    return super().get(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:1041: in get
    return self.request(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:465: in request
    return super().request(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:814: in request
    return self.send(request, auth=auth, follow_redirects=follow_redirects)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:901: in send
    response = self._send_handling_auth(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:929: in _send_handling_auth
    response = self._send_handling_redirects(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:966: in _send_handling_redirects
    response = self._send_single_request(request)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:1002: in _send_single_request
    response = transport.handle_request(request)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:342: in handle_request
    raise exc
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:339: in handle_request
    portal.call(self.app, scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/anyio/from_thread.py:277: in call
    return cast(T_Retval, self.start_task_soon(func, *args).result())
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/concurrent/futures/_base.py:456: in result
    return self.__get_result()
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/concurrent/futures/_base.py:401: in __get_result
    raise self._exception
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/anyio/from_thread.py:217: in _call_func
    retval = await retval
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/applications.py:1106: in __call__
    await super().__call__(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/applications.py:122: in __call__
    await self.middleware_stack(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/errors.py:184: in __call__
    raise exc
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/errors.py:162: in __call__
    await self.app(scope, receive, _send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/cors.py:83: in __call__
    await self.app(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/exceptions.py:79: in __call__
    raise exc
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/exceptions.py:68: in __call__
    await self.app(scope, receive, sender)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py:20: in __call__
    raise e
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py:17: in __call__
    await self.app(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/routing.py:718: in __call__
    await route.handle(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/routing.py:276: in handle
    await self.app(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/routing.py:66: in app
    response = await func(request)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/routing.py:274: in app
    raw_response = await run_endpoint_function(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/routing.py:191: in run_endpoint_function
    return await dependant.call(**values)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/slowapi/extension.py:734: in async_wrapper
    response = await func(*args, **kwargs)  # type: ignore
src/presentation/web/routes/api.py:352: in list_responsible
    responsible = await use_case.execute()
src/application/use_cases/responsible/get_all_responsible.py:13: in execute
    return await self.responsible_repository.get_all()
src/infrastructure/database/repositories/base_repository.py:94: in get_all
    result = await self.session.execute(select(self.model_class))
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/ext/asyncio/session.py:455: in execute
    result = await greenlet_spawn(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:190: in greenlet_spawn
    result = context.throw(*sys.exc_info())
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/session.py:2308: in execute
    return self._execute_internal(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/session.py:2190: in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/context.py:293: in orm_execute_statement
    result = conn.execute(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1416: in execute
    return meth(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/sql/elements.py:516: in _execute_on_connection
    return connection._execute_clauseelement(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1639: in _execute_clauseelement
    ret = self._execute_context(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1848: in _execute_context
    return self._exec_single_context(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1988: in _exec_single_context
    self._handle_dbapi_exception(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:2343: in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1969: in _exec_single_context
    self.dialect.do_execute(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/default.py:922: in do_execute
    cursor.execute(statement, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:146: in execute
    self._adapt_connection._handle_exception(error)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:298: in _handle_exception
    raise error
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:128: in execute
    self.await_(_cursor.execute(operation, parameters))
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:125: in await_only
    return current.driver.switch(awaitable)  # type: ignore[no-any-return]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:185: in greenlet_spawn
    value = await result
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:48: in execute
    await self._execute(self._cursor.execute, sql, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:40: in _execute
    return await self._conn._execute(fn, *args, **kwargs)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:133: in _execute
    return await future
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:106: in run
    result = function()
E   sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: responsible_persons
E   [SQL: SELECT responsible_persons.id, responsible_persons.full_name, responsible_persons.company, responsible_persons.position, responsible_persons.created_at, responsible_persons.updated_at 
E   FROM responsible_persons]
E   (Background on this error at: https://sqlalche.me/e/20/e3q8)
__________________ TestAdditionalEndpoints.test_search_people __________________
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1969: in _exec_single_context
    self.dialect.do_execute(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/default.py:922: in do_execute
    cursor.execute(statement, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:146: in execute
    self._adapt_connection._handle_exception(error)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:298: in _handle_exception
    raise error
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:128: in execute
    self.await_(_cursor.execute(operation, parameters))
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:125: in await_only
    return current.driver.switch(awaitable)  # type: ignore[no-any-return]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:185: in greenlet_spawn
    value = await result
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:48: in execute
    await self._execute(self._cursor.execute, sql, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:40: in _execute
    return await self._conn._execute(fn, *args, **kwargs)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:133: in _execute
    return await future
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:106: in run
    result = function()
E   sqlite3.OperationalError: no such table: birthdays
The above exception was the direct cause of the following exception:
tests/presentation/web/test_api_additional.py:170: in test_search_people
    response = client.get("/api/panel/search?q=Иван")
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:499: in get
    return super().get(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:1041: in get
    return self.request(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:465: in request
    return super().request(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:814: in request
    return self.send(request, auth=auth, follow_redirects=follow_redirects)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:901: in send
    response = self._send_handling_auth(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:929: in _send_handling_auth
    response = self._send_handling_redirects(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:966: in _send_handling_redirects
    response = self._send_single_request(request)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/httpx/_client.py:1002: in _send_single_request
    response = transport.handle_request(request)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:342: in handle_request
    raise exc
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/testclient.py:339: in handle_request
    portal.call(self.app, scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/anyio/from_thread.py:277: in call
    return cast(T_Retval, self.start_task_soon(func, *args).result())
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/concurrent/futures/_base.py:456: in result
    return self.__get_result()
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/concurrent/futures/_base.py:401: in __get_result
    raise self._exception
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/anyio/from_thread.py:217: in _call_func
    retval = await retval
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/applications.py:1106: in __call__
    await super().__call__(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/applications.py:122: in __call__
    await self.middleware_stack(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/errors.py:184: in __call__
    raise exc
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/errors.py:162: in __call__
    await self.app(scope, receive, _send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/cors.py:83: in __call__
    await self.app(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/exceptions.py:79: in __call__
    raise exc
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/middleware/exceptions.py:68: in __call__
    await self.app(scope, receive, sender)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py:20: in __call__
    raise e
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py:17: in __call__
    await self.app(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/routing.py:718: in __call__
    await route.handle(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/routing.py:276: in handle
    await self.app(scope, receive, send)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/starlette/routing.py:66: in app
    response = await func(request)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/routing.py:274: in app
    raw_response = await run_endpoint_function(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/fastapi/routing.py:191: in run_endpoint_function
    return await dependant.call(**values)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/slowapi/extension.py:734: in async_wrapper
    response = await func(*args, **kwargs)  # type: ignore
src/presentation/web/routes/api.py:471: in search_people
    results = await use_case.execute(q)
src/application/use_cases/search/search_people.py:26: in execute
    birthdays = await self.birthday_repository.search(query)
src/infrastructure/database/repositories/birthday_repository_impl.py:104: in search
    result = await self.session.execute(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/ext/asyncio/session.py:455: in execute
    result = await greenlet_spawn(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:190: in greenlet_spawn
    result = context.throw(*sys.exc_info())
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/session.py:2308: in execute
    return self._execute_internal(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/session.py:2190: in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/context.py:293: in orm_execute_statement
    result = conn.execute(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1416: in execute
    return meth(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/sql/elements.py:516: in _execute_on_connection
    return connection._execute_clauseelement(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1639: in _execute_clauseelement
    ret = self._execute_context(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1848: in _execute_context
    return self._exec_single_context(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1988: in _exec_single_context
    self._handle_dbapi_exception(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:2343: in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py:1969: in _exec_single_context
    self.dialect.do_execute(
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/default.py:922: in do_execute
    cursor.execute(statement, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:146: in execute
    self._adapt_connection._handle_exception(error)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:298: in _handle_exception
    raise error
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py:128: in execute
    self.await_(_cursor.execute(operation, parameters))
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:125: in await_only
    return current.driver.switch(awaitable)  # type: ignore[no-any-return]
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py:185: in greenlet_spawn
    value = await result
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:48: in execute
    await self._execute(self._cursor.execute, sql, parameters)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py:40: in _execute
    return await self._conn._execute(fn, *args, **kwargs)
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:133: in _execute
    return await future
/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py:106: in run
    result = function()
E   sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: birthdays
E   [SQL: SELECT birthdays.id, birthdays.full_name, birthdays.company, birthdays.position, birthdays.birth_date, birthdays.comment, birthdays.created_at, birthdays.updated_at 
E   FROM birthdays 
E   WHERE lower(birthdays.full_name) LIKE lower(?) OR lower(birthdays.company) LIKE lower(?) OR lower(birthdays.position) LIKE lower(?)]
E   [parameters: ('%Иван%', '%Иван%', '%Иван%')]
E   (Background on this error at: https://sqlalche.me/e/20/e3q8)
____________ TestAdditionalEndpoints.test_generate_greeting_success ____________
tests/presentation/web/test_api_additional.py:193: in test_generate_greeting_success
    assert response.status_code == 200
E   assert 500 == 200
E    +  where 500 = <Response [500 Internal Server Error]>.status_code
------------------------------ Captured log call -------------------------------
ERROR    src.presentation.web.decorators:decorators.py:96 Unexpected error in generate_greeting
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
    cursor.execute(statement, parameters)
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py", line 146, in execute
    self._adapt_connection._handle_exception(error)
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py", line 298, in _handle_exception
    raise error
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py", line 128, in execute
    self.await_(_cursor.execute(operation, parameters))
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 125, in await_only
    return current.driver.switch(awaitable)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 185, in greenlet_spawn
    value = await result
            ^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py", line 48, in execute
    await self._execute(self._cursor.execute, sql, parameters)
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py", line 40, in _execute
    return await self._conn._execute(fn, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py", line 133, in _execute
    return await future
           ^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py", line 106, in run
    result = function()
             ^^^^^^^^^^
sqlite3.OperationalError: no such table: birthdays
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File "/home/runner/work/tg_bot_HB/tg_bot_HB/backend/src/presentation/web/decorators.py", line 61, in wrapper
    return await func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/tg_bot_HB/tg_bot_HB/backend/src/presentation/web/routes/api.py", line 498, in generate_greeting
    greeting_text = await use_case.execute(
                    ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/tg_bot_HB/tg_bot_HB/backend/src/application/use_cases/greeting/generate_greeting.py", line 22, in execute
    birthday = await self.birthday_repository.get_by_id(birthday_id)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/tg_bot_HB/tg_bot_HB/backend/src/infrastructure/database/repositories/base_repository.py", line 81, in get_by_id
    result = await self.session.execute(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/ext/asyncio/session.py", line 455, in execute
    result = await greenlet_spawn(
             ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 190, in greenlet_spawn
    result = context.throw(*sys.exc_info())
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
    return self._execute_internal(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
    result = conn.execute(
             ^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
    return meth(
           ^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
    return connection._execute_clauseelement(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
    ret = self._execute_context(
          ^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2343, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
    cursor.execute(statement, parameters)
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py", line 146, in execute
    self._adapt_connection._handle_exception(error)
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py", line 298, in _handle_exception
    raise error
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py", line 128, in execute
    self.await_(_cursor.execute(operation, parameters))
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 125, in await_only
    return current.driver.switch(awaitable)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 185, in greenlet_spawn
    value = await result
            ^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py", line 48, in execute
    await self._execute(self._cursor.execute, sql, parameters)
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py", line 40, in _execute
    return await self._conn._execute(fn, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py", line 133, in _execute
    return await future
           ^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py", line 106, in run
    result = function()
             ^^^^^^^^^^
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: birthdays
[SQL: SELECT birthdays.id, birthdays.full_name, birthdays.company, birthdays.position, birthdays.birth_date, birthdays.comment, birthdays.created_at, birthdays.updated_at 
FROM birthdays 
WHERE birthdays.id = ?]
[parameters: (1,)]
(Background on this error at: https://sqlalche.me/e/20/e3q8)
_______________ TestAdditionalEndpoints.test_create_card_success _______________
tests/presentation/web/test_api_additional.py:212: in test_create_card_success
    assert response.status_code == 200
E   assert 500 == 200
E    +  where 500 = <Response [500 Internal Server Error]>.status_code
------------------------------ Captured log call -------------------------------
ERROR    src.presentation.web.decorators:decorators.py:96 Unexpected error in create_card
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
    cursor.execute(statement, parameters)
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py", line 146, in execute
    self._adapt_connection._handle_exception(error)
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py", line 298, in _handle_exception
    raise error
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py", line 128, in execute
    self.await_(_cursor.execute(operation, parameters))
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 125, in await_only
    return current.driver.switch(awaitable)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 185, in greenlet_spawn
    value = await result
            ^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py", line 48, in execute
    await self._execute(self._cursor.execute, sql, parameters)
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py", line 40, in _execute
    return await self._conn._execute(fn, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py", line 133, in _execute
    return await future
           ^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py", line 106, in run
    result = function()
             ^^^^^^^^^^
sqlite3.OperationalError: no such table: birthdays
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File "/home/runner/work/tg_bot_HB/tg_bot_HB/backend/src/presentation/web/decorators.py", line 61, in wrapper
    return await func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/tg_bot_HB/tg_bot_HB/backend/src/presentation/web/routes/api.py", line 520, in create_card
    card_bytes = await use_case.execute(
                 ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/tg_bot_HB/tg_bot_HB/backend/src/application/use_cases/greeting/create_card.py", line 22, in execute
    birthday = await self.birthday_repository.get_by_id(birthday_id)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/tg_bot_HB/tg_bot_HB/backend/src/infrastructure/database/repositories/base_repository.py", line 81, in get_by_id
    result = await self.session.execute(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/ext/asyncio/session.py", line 455, in execute
    result = await greenlet_spawn(
             ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 190, in greenlet_spawn
    result = context.throw(*sys.exc_info())
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
    return self._execute_internal(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
    result = conn.execute(
             ^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
    return meth(
           ^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
    return connection._execute_clauseelement(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
    ret = self._execute_context(
          ^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2343, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
    cursor.execute(statement, parameters)
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py", line 146, in execute
    self._adapt_connection._handle_exception(error)
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py", line 298, in _handle_exception
    raise error
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py", line 128, in execute
    self.await_(_cursor.execute(operation, parameters))
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 125, in await_only
    return current.driver.switch(awaitable)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 185, in greenlet_spawn
    value = await result
            ^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py", line 48, in execute
    await self._execute(self._cursor.execute, sql, parameters)
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py", line 40, in _execute
    return await self._conn._execute(fn, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py", line 133, in _execute
    return await future
           ^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py", line 106, in run
    result = function()
             ^^^^^^^^^^
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: birthdays
[SQL: SELECT birthdays.id, birthdays.full_name, birthdays.company, birthdays.position, birthdays.birth_date, birthdays.comment, birthdays.created_at, birthdays.updated_at 
FROM birthdays 
WHERE birthdays.id = ?]
[parameters: (1,)]
(Background on this error at: https://sqlalche.me/e/20/e3q8)
ERROR    sqlalchemy.pool.impl.StaticPool:base.py:1010 Exception during reset or similar
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/pool/base.py", line 988, in _finalize_fairy
    fairy._reset(
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/pool/base.py", line 1438, in _reset
    pool._dialect.do_rollback(self)
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 692, in do_rollback
    dbapi_connection.rollback()
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py", line 263, in rollback
    self.await_(self._connection.rollback())
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 125, in await_only
    return current.driver.switch(awaitable)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 185, in greenlet_spawn
    value = await result
            ^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py", line 170, in rollback
    await self._execute(self._conn.rollback)
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py", line 133, in _execute
    return await future
           ^^^^^^^^^^^^
asyncio.exceptions.CancelledError
___________ TestAdditionalEndpoints.test_generate_greeting_not_found ___________
tests/presentation/web/test_api_additional.py:234: in test_generate_greeting_not_found
    assert response.status_code == 404
E   assert 500 == 404
E    +  where 500 = <Response [500 Internal Server Error]>.status_code
------------------------------ Captured log call -------------------------------
ERROR    src.presentation.web.decorators:decorators.py:96 Unexpected error in generate_greeting
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
    cursor.execute(statement, parameters)
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py", line 146, in execute
    self._adapt_connection._handle_exception(error)
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py", line 298, in _handle_exception
    raise error
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/dialects/sqlite/aiosqlite.py", line 128, in execute
    self.await_(_cursor.execute(operation, parameters))
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 125, in await_only
    return current.driver.switch(awaitable)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 185, in greenlet_spawn
    value = await result
            ^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py", line 48, in execute
    await self._execute(self._cursor.execute, sql, parameters)
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/cursor.py", line 40, in _execute
    return await self._conn._execute(fn, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py", line 133, in _execute
    return await future
           ^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/aiosqlite/core.py", line 106, in run
    result = function()
             ^^^^^^^^^^
sqlite3.OperationalError: no such table: birthdays
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File "/home/runner/work/tg_bot_HB/tg_bot_HB/backend/src/presentation/web/decorators.py", line 61, in wrapper
    return await func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/tg_bot_HB/tg_bot_HB/backend/src/presentation/web/routes/api.py", line 498, in generate_greeting
    greeting_text = await use_case.execute(
                    ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/tg_bot_HB/tg_bot_HB/backend/src/application/use_cases/greeting/generate_greeting.py", line 22, in execute
    birthday = await self.birthday_repository.get_by_id(birthday_id)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/tg_bot_HB/tg_bot_HB/backend/src/infrastructure/database/repositories/base_repository.py", line 81, in get_by_id
    result = await self.session.execute(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/ext/asyncio/session.py", line 455, in execute
    result = await greenlet_spawn(
             ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/util/_concurrency_py3k.py", line 190, in greenlet_spawn
    result = context.throw(*sys.exc_info())
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
    return self._execute_internal(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.14/x64/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
    result = conn.execute(
             ^^^^^^^^^^^^^
Error: Process completed with exit code 1.