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
tests/presentation/web/test_api.py::TestCalendarEndpoints::test_get_calendar_success PASSED [ 88%]
tests/presentation/web/test_api.py::TestCalendarEndpoints::test_get_calendar_invalid_date PASSED [ 89%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_check_panel_access_success PASSED [ 89%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_check_panel_access_no_auth PASSED [ 90%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_list_birthdays PASSED [ 90%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_create_birthday_success PASSED [ 91%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_update_birthday_success PASSED [ 91%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_delete_birthday_success PASSED [ 92%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_list_responsible PASSED [ 92%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_create_responsible_success PASSED [ 93%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_update_responsible_success PASSED [ 93%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_delete_responsible_success PASSED [ 94%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_assign_responsible_success PASSED [ 94%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_search_people PASSED [ 95%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_generate_greeting_success PASSED [ 95%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_create_card_success PASSED [ 96%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_generate_greeting_not_found PASSED [ 96%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_create_birthday_validation_error FAILED [ 97%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_delete_birthday_not_found PASSED [ 97%]
tests/presentation/web/test_app.py::TestWebApp::test_app_creation PASSED [ 98%]
tests/presentation/web/test_app.py::TestWebApp::test_root_endpoint PASSED [ 98%]
tests/presentation/web/test_app.py::TestWebApp::test_cors_middleware_configured PASSED [ 99%]
tests/presentation/web/test_app.py::TestWebApp::test_router_included PASSED [100%]
=================================== FAILURES ===================================
________ TestAdditionalEndpoints.test_create_birthday_validation_error _________
tests/presentation/web/test_api_additional.py:262: in test_create_birthday_validation_error
    assert response.status_code == 400
E   assert 422 == 400
E    +  where 422 = <Response [422 Unprocessable Entity]>.status_code
---------- coverage: platform linux, python 3.11.14-final-0 ----------
Name                                                                       Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------------------------------------
src/__init__.py                                                                0      0   100%
src/application/__init__.py                                                    0      0   100%
src/application/factories/__init__.py                                          0      0   100%
src/application/factories/use_case_factory.py                                 94      1    99%   141
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
src/application/use_cases/auth/verify_telegram_auth.py                        10      0   100%
src/application/use_cases/birthday/__init__.py                                 0      0   100%
src/application/use_cases/birthday/create_birthday.py                          9      0   100%
src/application/use_cases/birthday/delete_birthday.py                          9      0   100%
src/application/use_cases/birthday/get_all_birthdays.py                        7      0   100%
src/application/use_cases/birthday/get_birthdays_by_date.py                    8      0   100%
src/application/use_cases/birthday/update_birthday.py                         12      0   100%
src/application/use_cases/calendar/__init__.py                                 0      0   100%
src/application/use_cases/calendar/get_calendar_data.py                       14      0   100%
src/application/use_cases/greeting/__init__.py                                 0      0   100%
src/application/use_cases/greeting/create_card.py                             12      0   100%
src/application/use_cases/greeting/generate_greeting.py                       11      0   100%
src/application/use_cases/holiday/__init__.py                                  0      0   100%
src/application/use_cases/holiday/create_holiday.py                            9      0   100%
src/application/use_cases/holiday/delete_holiday.py                            9      0   100%
src/application/use_cases/holiday/update_holiday.py                           12      0   100%
src/application/use_cases/panel/__init__.py                                    0      0   100%
src/application/use_cases/panel/check_panel_access.py                          6      0   100%
src/application/use_cases/panel/record_panel_access.py                         6      0   100%
src/application/use_cases/responsible/__init__.py                              0      0   100%
src/application/use_cases/responsible/assign_responsible_to_date.py           10      0   100%
src/application/use_cases/responsible/create_responsible.py                    8      0   100%
src/application/use_cases/responsible/delete_responsible.py                    9      0   100%
src/application/use_cases/responsible/get_all_responsible.py                   7      0   100%
src/application/use_cases/responsible/update_responsible.py                   11      0   100%
src/application/use_cases/search/__init__.py                                   0      0   100%
src/application/use_cases/search/search_people.py                             17      0   100%
src/domain/entities/__init__.py                                                0      0   100%
src/domain/entities/birthday.py                                               15      0   100%
src/domain/entities/professional_holiday.py                                    8      0   100%
src/domain/entities/responsible_person.py                                      7      0   100%
src/domain/exceptions/__init__.py                                              5      0   100%
src/domain/exceptions/api_exceptions.py                                       15      1    93%   29
src/domain/exceptions/base.py                                                  2      0   100%
src/domain/exceptions/business.py                                              3      0   100%
src/domain/exceptions/not_found.py                                             7      0   100%
src/domain/exceptions/validation.py                                            5      0   100%
src/infrastructure/__init__.py                                                 0      0   100%
src/infrastructure/config/__init__.py                                          0      0   100%
src/infrastructure/config/constants.py                                         2      0   100%
src/infrastructure/config/env_validator.py                                    57     57     0%   3-174
src/infrastructure/config/openrouter_config.py                                18      0   100%
src/infrastructure/config/rate_limits.py                                       5      0   100%
src/infrastructure/database/__init__.py                                        0      0   100%
src/infrastructure/database/database.py                                       12      0   100%
src/infrastructure/database/database_factory.py                               10      0   100%
src/infrastructure/database/models.py                                         47      0   100%
src/infrastructure/database/repositories/__init__.py                           0      0   100%
src/infrastructure/database/repositories/base_repository.py                   38      2    95%   115, 122
src/infrastructure/database/repositories/birthday_repository_impl.py          47      1    98%   96
src/infrastructure/database/repositories/holiday_repository_impl.py           31      0   100%
src/infrastructure/database/repositories/panel_access_repository_impl.py      15      0   100%
src/infrastructure/database/repositories/responsible_repository_impl.py       53      8    85%   89, 113-133
src/infrastructure/database/repositories/search_validator.py                  16      4    75%   32, 39, 43, 50
src/infrastructure/external/__init__.py                                        0      0   100%
src/infrastructure/external/openrouter_client_impl.py                         56      2    96%   98-100
src/infrastructure/external/telegram_auth.py                                  43      2    95%   41-42
src/infrastructure/image/__init__.py                                           0      0   100%
src/infrastructure/image/card_generator.py                                    79     18    77%   42-44, 102-103, 113-116, 137-139, 148-153
src/infrastructure/services/__init__.py                                        0      0   100%
src/infrastructure/services/notification_service_impl.py                      87      5    94%   40, 67, 92, 97, 124
src/infrastructure/services/notifications_scheduler.py                        33      0   100%
src/presentation/__init__.py                                                   0      0   100%
src/presentation/telegram/__init__.py                                          0      0   100%
src/presentation/telegram/bot.py                                              26     26     0%   1-47
src/presentation/telegram/handlers/__init__.py                                 2      2     0%   1-10
src/presentation/telegram/handlers/birthday_handlers.py                       62     62     0%   1-103
src/presentation/telegram/handlers/calendar_handler.py                        72     72     0%   1-109
src/presentation/telegram/handlers/greeting_handlers.py                       87     87     0%   1-148
src/presentation/telegram/handlers/panel_handler.py                           17     17     0%   1-33
src/presentation/telegram/handlers/responsible_handlers.py                    43     43     0%   1-74
src/presentation/telegram/handlers/start_handler.py                            8      8     0%   1-13
src/presentation/telegram/keyboards.py                                        34     34     0%   1-146
src/presentation/telegram/middleware/__init__.py                               2      2     0%   3-5
src/presentation/telegram/middleware/database_middleware.py                   32     32     0%   3-79
src/presentation/web/__init__.py                                               0      0   100%
src/presentation/web/app.py                                                   37     15    59%   30-44, 49-56
src/presentation/web/decorators.py                                            59     32    46%   56-58, 67-97
src/presentation/web/dependencies.py                                          17     10    41%   16-18, 31, 41-48
src/presentation/web/routes/__init__.py                                        0      0   100%
src/presentation/web/routes/api.py                                           224     23    90%   46, 62, 76, 90, 116, 133-140, 159-172, 207-208, 225
--------------------------------------------------------------------------------------------------------
TOTAL                                                                       1748    566    68%
Coverage HTML written to dir htmlcov
Coverage XML written to file coverage.xml
=========================== short test summary info ============================
FAILED tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_create_birthday_validation_error - assert 422 == 400
 +  where 422 = <Response [422 Unprocessable Entity]>.status_code
================== 1 failed, 196 passed, 3 warnings in 16.76s ==================
Error: Process completed with exit code 1.