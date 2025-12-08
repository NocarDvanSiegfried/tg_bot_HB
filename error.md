Run pytest tests/ --cov=src --cov-report=xml --cov-report=term --cov-report=html -v --import-mode=importlib
  
============================= test session starts ==============================
platform linux -- Python 3.11.14, pytest-7.4.3, pluggy-1.6.0 -- /opt/hostedtoolcache/Python/3.11.14/x64/bin/python
cachedir: .pytest_cache
rootdir: /home/runner/work/tg_bot_HB/tg_bot_HB/backend
configfile: pytest.ini
plugins: anyio-3.7.1, asyncio-0.21.1, mock-3.12.0, cov-4.1.0
asyncio: mode=Mode.AUTO
collecting ... collected 229 items
tests/application/test_assign_responsible_use_case.py::TestAssignResponsibleToDateUseCase::test_assign_responsible_success PASSED [  0%]
tests/application/test_assign_responsible_use_case.py::TestAssignResponsibleToDateUseCase::test_assign_responsible_not_found PASSED [  0%]
tests/application/test_check_panel_access_use_case.py::TestCheckPanelAccessUseCase::test_check_panel_access_has_access PASSED [  1%]
tests/application/test_check_panel_access_use_case.py::TestCheckPanelAccessUseCase::test_check_panel_access_no_access PASSED [  1%]
tests/application/test_create_birthday_use_case.py::TestCreateBirthdayUseCase::test_create_birthday_success PASSED [  2%]
tests/application/test_create_birthday_use_case.py::TestCreateBirthdayUseCase::test_create_birthday_without_comment PASSED [  2%]
tests/application/test_create_card_use_case.py::TestCreateCardUseCase::test_create_card_success PASSED [  3%]
tests/application/test_create_card_use_case.py::TestCreateCardUseCase::test_create_card_without_qr PASSED [  3%]
tests/application/test_create_card_use_case.py::TestCreateCardUseCase::test_create_card_birthday_not_found PASSED [  3%]
tests/application/test_create_holiday_use_case.py::TestCreateHolidayUseCase::test_create_holiday_success PASSED [  4%]
tests/application/test_create_holiday_use_case.py::TestCreateHolidayUseCase::test_create_holiday_without_description PASSED [  4%]
tests/application/test_create_responsible_use_case.py::TestCreateResponsibleUseCase::test_create_responsible_success PASSED [  5%]
tests/application/test_delete_birthday_use_case.py::TestDeleteBirthdayUseCase::test_delete_birthday_success PASSED [  5%]
tests/application/test_delete_birthday_use_case.py::TestDeleteBirthdayUseCase::test_delete_birthday_not_found PASSED [  6%]
tests/application/test_delete_holiday_use_case.py::TestDeleteHolidayUseCase::test_delete_holiday_success PASSED [  6%]
tests/application/test_delete_holiday_use_case.py::TestDeleteHolidayUseCase::test_delete_holiday_not_found PASSED [  6%]
tests/application/test_delete_responsible_use_case.py::TestDeleteResponsibleUseCase::test_delete_responsible_success PASSED [  7%]
tests/application/test_delete_responsible_use_case.py::TestDeleteResponsibleUseCase::test_delete_responsible_not_found PASSED [  7%]
tests/application/test_generate_greeting_use_case.py::TestGenerateGreetingUseCase::test_generate_greeting_success PASSED [  8%]
tests/application/test_generate_greeting_use_case.py::TestGenerateGreetingUseCase::test_generate_greeting_with_theme PASSED [  8%]
tests/application/test_generate_greeting_use_case.py::TestGenerateGreetingUseCase::test_generate_greeting_birthday_not_found PASSED [  9%]
tests/application/test_get_all_birthdays_use_case.py::TestGetAllBirthdaysUseCase::test_get_all_birthdays_success PASSED [  9%]
tests/application/test_get_all_birthdays_use_case.py::TestGetAllBirthdaysUseCase::test_get_all_birthdays_empty PASSED [ 10%]
tests/application/test_get_all_responsible_use_case.py::TestGetAllResponsibleUseCase::test_get_all_responsible_success PASSED [ 10%]
tests/application/test_get_all_responsible_use_case.py::TestGetAllResponsibleUseCase::test_get_all_responsible_empty PASSED [ 10%]
tests/application/test_get_birthdays_by_date.py::TestGetBirthdaysByDateUseCase::test_get_birthdays_by_date_success PASSED [ 11%]
tests/application/test_get_birthdays_by_date.py::TestGetBirthdaysByDateUseCase::test_get_birthdays_by_date_empty PASSED [ 11%]
tests/application/test_get_birthdays_by_date.py::TestGetBirthdaysByDateUseCase::test_get_birthdays_by_date_repository_error PASSED [ 12%]
tests/application/test_get_calendar_data_use_case.py::TestGetCalendarDataUseCase::test_get_calendar_data_success PASSED [ 12%]
tests/application/test_get_calendar_data_use_case.py::TestGetCalendarDataUseCase::test_get_calendar_data_empty PASSED [ 13%]
tests/application/test_get_calendar_data_use_case.py::TestGetCalendarDataUseCase::test_get_calendar_data_repository_error PASSED [ 13%]
tests/application/test_record_panel_access_use_case.py::TestRecordPanelAccessUseCase::test_record_panel_access_success PASSED [ 13%]
tests/application/test_record_panel_access_use_case.py::TestRecordPanelAccessUseCase::test_record_panel_access_different_user PASSED [ 14%]
tests/application/test_search_people.py::TestSearchPeopleUseCase::test_search_success PASSED [ 14%]
tests/application/test_search_people.py::TestSearchPeopleUseCase::test_search_empty_result PASSED [ 15%]
tests/application/test_search_people.py::TestSearchPeopleUseCase::test_search_only_birthdays PASSED [ 15%]
tests/application/test_search_people.py::TestSearchPeopleUseCase::test_search_only_responsible PASSED [ 16%]
tests/application/test_search_people.py::TestSearchPeopleUseCase::test_search_repository_error PASSED [ 16%]
tests/application/test_update_birthday_use_case.py::TestUpdateBirthdayUseCase::test_update_birthday_success PASSED [ 17%]
tests/application/test_update_birthday_use_case.py::TestUpdateBirthdayUseCase::test_update_birthday_not_found PASSED [ 17%]
tests/application/test_update_holiday_use_case.py::TestUpdateHolidayUseCase::test_update_holiday_success PASSED [ 17%]
tests/application/test_update_holiday_use_case.py::TestUpdateHolidayUseCase::test_update_holiday_partial PASSED [ 18%]
tests/application/test_update_holiday_use_case.py::TestUpdateHolidayUseCase::test_update_holiday_not_found PASSED [ 18%]
tests/application/test_update_responsible_use_case.py::TestUpdateResponsibleUseCase::test_update_responsible_success PASSED [ 19%]
tests/application/test_update_responsible_use_case.py::TestUpdateResponsibleUseCase::test_update_responsible_not_found PASSED [ 19%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_create_birthday_use_cases PASSED [ 20%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_create_calendar_use_case PASSED [ 20%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_create_responsible_use_cases PASSED [ 20%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_create_search_use_case PASSED [ 21%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_create_greeting_use_cases PASSED [ 21%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_create_panel_access_use_case PASSED [ 22%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_create_auth_use_case PASSED [ 22%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_lazy_initialization_repositories PASSED [ 23%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_factory_without_session PASSED [ 23%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_openrouter_client_missing_env PASSED [ 24%]
tests/application/test_use_case_factory.py::TestUseCaseFactory::test_auth_use_case_missing_token PASSED [ 24%]
tests/application/test_verify_telegram_auth_use_case.py::TestVerifyTelegramAuthUseCase::test_verify_telegram_auth_success PASSED [ 24%]
tests/application/test_verify_telegram_auth_use_case.py::TestVerifyTelegramAuthUseCase::test_verify_telegram_auth_invalid PASSED [ 25%]
tests/application/test_verify_telegram_auth_use_case.py::TestVerifyTelegramAuthUseCase::test_verify_telegram_auth_empty_user_data PASSED [ 25%]
tests/domain/test_birthday_entity.py::TestBirthdayEntity::test_birthday_creation PASSED [ 26%]
tests/domain/test_birthday_entity.py::TestBirthdayEntity::test_birthday_without_comment PASSED [ 26%]
tests/domain/test_birthday_entity.py::TestBirthdayEntity::test_calculate_age_same_year PASSED [ 27%]
tests/domain/test_birthday_entity.py::TestBirthdayEntity::test_calculate_age_next_year PASSED [ 27%]
tests/domain/test_birthday_entity.py::TestBirthdayEntity::test_calculate_age_before_birthday PASSED [ 27%]
tests/domain/test_birthday_entity.py::TestBirthdayEntity::test_calculate_age_after_birthday PASSED [ 28%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_create_birthday PASSED [ 28%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_get_by_id_found PASSED [ 29%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_get_by_id_not_found PASSED [ 29%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_get_by_date PASSED [ 30%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_delete_birthday PASSED [ 30%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_get_by_date_range PASSED [ 31%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_get_by_date_range_empty PASSED [ 31%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_update_birthday PASSED [ 31%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_update_birthday_no_id PASSED [ 32%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_update_birthday_not_found PASSED [ 32%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_search PASSED [ 33%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_search_empty PASSED [ 33%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_search_by_company PASSED [ 34%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_get_all PASSED [ 34%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_get_all_empty PASSED [ 34%]
tests/infrastructure/test_birthday_repository.py::TestBirthdayRepositoryImpl::test_to_model_conversion PASSED [ 35%]
tests/infrastructure/test_card_generator.py::TestCardGeneratorImpl::test_generate_card_handles_font_load_error_with_specific_exception PASSED [ 35%]
tests/infrastructure/test_card_generator.py::TestCardGeneratorImpl::test_generate_card_handles_ioerror_with_specific_exception PASSED [ 36%]
tests/infrastructure/test_database.py::TestDatabase::test_database_initialization PASSED [ 36%]
tests/infrastructure/test_database.py::TestDatabase::test_get_session PASSED [ 37%]
tests/infrastructure/test_database.py::TestDatabase::test_create_tables PASSED [ 37%]
tests/infrastructure/test_database.py::TestDatabase::test_multiple_sessions PASSED [ 37%]
tests/infrastructure/test_database_factory.py::TestDatabaseFactory::test_singleton_pattern PASSED [ 38%]
tests/infrastructure/test_database_factory.py::TestDatabaseFactory::test_create_database_with_env PASSED [ 38%]
tests/infrastructure/test_database_factory.py::TestDatabaseFactory::test_missing_database_url PASSED [ 39%]
tests/infrastructure/test_database_factory.py::TestDatabaseFactory::test_database_url_empty_string PASSED [ 39%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_create_holiday PASSED [ 40%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_get_by_id_exists PASSED [ 40%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_get_by_id_not_exists PASSED [ 41%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_get_by_date PASSED [ 41%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_update_holiday PASSED [ 41%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_update_holiday_no_id PASSED [ 42%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_update_holiday_not_found PASSED [ 42%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_delete_holiday PASSED [ 43%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_delete_holiday_not_exists PASSED [ 43%]
tests/infrastructure/test_holiday_repository.py::TestHolidayRepositoryImpl::test_get_all PASSED [ 44%]
tests/infrastructure/test_notification_service_impl.py::TestNotificationServiceImpl::test_send_today_notifications_logs_error_on_failure PASSED [ 44%]
tests/infrastructure/test_notification_service_impl.py::TestNotificationServiceImpl::test_send_week_notifications_logs_error_on_failure PASSED [ 44%]
tests/infrastructure/test_notification_service_impl.py::TestNotificationServiceImpl::test_send_month_notifications_logs_error_on_failure PASSED [ 45%]
tests/infrastructure/test_notifications_scheduler.py::TestNotificationsScheduler::test_scheduler_initialization PASSED [ 45%]
tests/infrastructure/test_notifications_scheduler.py::TestNotificationsScheduler::test_scheduler_start PASSED [ 46%]
tests/infrastructure/test_notifications_scheduler.py::TestNotificationsScheduler::test_scheduler_stop PASSED [ 46%]
tests/infrastructure/test_notifications_scheduler.py::TestNotificationsScheduler::test_scheduler_jobs_configuration PASSED [ 47%]
tests/infrastructure/test_notifications_scheduler.py::TestNotificationsScheduler::test_send_today_execution PASSED [ 47%]
tests/infrastructure/test_notifications_scheduler.py::TestNotificationsScheduler::test_send_week_execution PASSED [ 48%]
tests/infrastructure/test_notifications_scheduler.py::TestNotificationsScheduler::test_send_month_execution PASSED [ 48%]
tests/infrastructure/test_notifications_scheduler.py::TestNotificationsScheduler::test_send_today_error_handling PASSED [ 48%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_success PASSED [ 49%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_with_theme PASSED [ 49%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_http_error PASSED [ 50%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_timeout_error PASSED [ 50%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_invalid_response_not_dict PASSED [ 51%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_invalid_response_missing_choices PASSED [ 51%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_invalid_response_empty_choices PASSED [ 51%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_invalid_response_missing_message PASSED [ 52%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_invalid_response_missing_content PASSED [ 52%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_invalid_response_content_not_string PASSED [ 53%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_generate_greeting_retry_on_http_error PASSED [ 53%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_build_prompt_without_theme PASSED [ 54%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_build_prompt_with_theme PASSED [ 54%]
tests/infrastructure/test_openrouter_client.py::TestOpenRouterClientImpl::test_build_prompt_unknown_style_and_length PASSED [ 55%]
tests/infrastructure/test_panel_access_repository.py::TestPanelAccessRepositoryImpl::test_has_access_true PASSED [ 55%]
tests/infrastructure/test_panel_access_repository.py::TestPanelAccessRepositoryImpl::test_has_access_false PASSED [ 55%]
tests/infrastructure/test_panel_access_repository.py::TestPanelAccessRepositoryImpl::test_record_access PASSED [ 56%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_create_responsible PASSED [ 56%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_get_by_id_exists PASSED [ 57%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_get_by_id_not_exists PASSED [ 57%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_get_by_date_exists PASSED [ 58%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_get_by_date_not_exists PASSED [ 58%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_assign_to_date PASSED [ 58%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_update_responsible PASSED [ 59%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_update_responsible_no_id PASSED [ 59%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_update_responsible_not_found PASSED [ 60%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_delete_responsible PASSED [ 60%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_delete_responsible_not_exists PASSED [ 61%]
tests/infrastructure/test_responsible_repository.py::TestResponsibleRepositoryImpl::test_get_all PASSED [ 61%]
tests/infrastructure/test_telegram_auth.py::TestTelegramAuthServiceImpl::test_verify_init_data_success PASSED [ 62%]
tests/infrastructure/test_telegram_auth.py::TestTelegramAuthServiceImpl::test_verify_init_data_invalid_hash PASSED [ 62%]
tests/infrastructure/test_telegram_auth.py::TestTelegramAuthServiceImpl::test_verify_init_data_missing_hash PASSED [ 62%]
tests/infrastructure/test_telegram_auth.py::TestTelegramAuthServiceImpl::test_verify_init_data_invalid_format PASSED [ 63%]
tests/infrastructure/test_telegram_auth.py::TestTelegramAuthServiceImpl::test_parse_init_data_success PASSED [ 63%]
tests/infrastructure/test_telegram_auth.py::TestTelegramAuthServiceImpl::test_parse_init_data_without_user PASSED [ 64%]
tests/infrastructure/test_telegram_auth.py::TestTelegramAuthServiceImpl::test_parse_init_data_invalid_json PASSED [ 64%]
tests/infrastructure/test_telegram_auth.py::TestTelegramAuthServiceImpl::test_parse_init_data_invalid_format PASSED [ 65%]
tests/infrastructure/test_telegram_auth.py::TestDeprecatedFunctions::test_verify_telegram_init_data_function PASSED [ 65%]
tests/infrastructure/test_telegram_auth.py::TestDeprecatedFunctions::test_parse_init_data_function PASSED [ 65%]
tests/infrastructure/test_telegram_auth.py::TestDeprecatedFunctions::test_get_user_id_from_init_data_success PASSED [ 66%]
tests/infrastructure/test_telegram_auth.py::TestDeprecatedFunctions::test_get_user_id_from_init_data_no_user PASSED [ 66%]
tests/infrastructure/test_telegram_auth.py::TestDeprecatedFunctions::test_get_user_id_from_init_data_no_id PASSED [ 67%]
tests/presentation/telegram/test_bot.py::TestTelegramBot::test_main_with_valid_env PASSED [ 67%]
tests/presentation/telegram/test_bot.py::TestTelegramBot::test_main_missing_bot_token PASSED [ 68%]
tests/presentation/telegram/test_bot.py::TestTelegramBot::test_main_missing_database_url PASSED [ 68%]
tests/presentation/telegram/test_bot.py::TestTelegramBot::test_main_registers_all_routers PASSED [ 68%]
tests/presentation/telegram/test_keyboards.py::TestKeyboards::test_get_main_menu_keyboard PASSED [ 69%]
tests/presentation/telegram/test_keyboards.py::TestKeyboards::test_get_panel_menu_keyboard PASSED [ 69%]
tests/presentation/telegram/test_keyboards.py::TestKeyboards::test_get_calendar_navigation_keyboard PASSED [ 70%]
tests/presentation/telegram/test_keyboards.py::TestKeyboards::test_get_birthday_management_keyboard PASSED [ 70%]
tests/presentation/telegram/test_keyboards.py::TestKeyboards::test_get_responsible_management_keyboard PASSED [ 71%]
tests/presentation/telegram/test_keyboards.py::TestKeyboards::test_get_greeting_options_keyboard PASSED [ 71%]
tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_panel_birthdays_callback FAILED [ 72%]
tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_birthday_add_start FAILED [ 72%]
tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_process_full_name FAILED [ 72%]
tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_process_company FAILED [ 73%]
tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_process_position FAILED [ 73%]
tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_process_birth_date_valid FAILED [ 74%]
tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_process_birth_date_invalid FAILED [ 74%]
tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_process_comment_success FAILED [ 75%]
tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_process_comment_with_dash FAILED [ 75%]
tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_process_comment_error FAILED [ 75%]
tests/presentation/telegram/handlers/test_calendar_handler.py::TestCalendarHandler::test_show_calendar FAILED [ 76%]
tests/presentation/telegram/handlers/test_calendar_handler.py::TestCalendarHandler::test_calendar_callback_info FAILED [ 76%]
tests/presentation/telegram/handlers/test_calendar_handler.py::TestCalendarHandler::test_calendar_callback_prev FAILED [ 77%]
tests/presentation/telegram/handlers/test_calendar_handler.py::TestCalendarHandler::test_calendar_callback_next FAILED [ 77%]
tests/presentation/telegram/handlers/test_calendar_handler.py::TestCalendarHandler::test_date_selected_callback_with_data FAILED [ 78%]
tests/presentation/telegram/handlers/test_calendar_handler.py::TestCalendarHandler::test_date_selected_callback_empty FAILED [ 78%]
tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_panel_greetings_callback FAILED [ 79%]
tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_greeting_manual_start FAILED [ 79%]
tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_greeting_generate_start FAILED [ 79%]
tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_greeting_card_start FAILED [ 80%]
tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_birthday_id_valid FAILED [ 80%]
tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_birthday_id_invalid FAILED [ 81%]
tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_style FAILED [ 81%]
tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_length FAILED [ 82%]
tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_theme_success FAILED [ 82%]
tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_theme_with_dash FAILED [ 82%]
tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_theme_error FAILED [ 83%]
tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_text FAILED [ 83%]
tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_qr_url_success FAILED [ 84%]
tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_qr_url_with_dash FAILED [ 84%]
tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_qr_url_error FAILED [ 85%]
tests/presentation/telegram/handlers/test_panel_handler.py::TestPanelHandler::test_cmd_panel FAILED [ 85%]
tests/presentation/telegram/handlers/test_panel_handler.py::TestPanelHandler::test_panel_main_callback FAILED [ 86%]
tests/presentation/telegram/handlers/test_responsible_handlers.py::TestResponsibleHandlers::test_panel_responsible_callback FAILED [ 86%]
tests/presentation/telegram/handlers/test_responsible_handlers.py::TestResponsibleHandlers::test_responsible_add_start FAILED [ 86%]
tests/presentation/telegram/handlers/test_responsible_handlers.py::TestResponsibleHandlers::test_process_full_name FAILED [ 87%]
tests/presentation/telegram/handlers/test_responsible_handlers.py::TestResponsibleHandlers::test_process_company FAILED [ 87%]
tests/presentation/telegram/handlers/test_responsible_handlers.py::TestResponsibleHandlers::test_process_position_success FAILED [ 88%]
tests/presentation/telegram/handlers/test_responsible_handlers.py::TestResponsibleHandlers::test_process_position_error FAILED [ 88%]
tests/presentation/telegram/handlers/test_start_handler.py::TestStartHandler::test_cmd_start FAILED [ 89%]
tests/presentation/web/test_api.py::TestAuthEndpoints::test_verify_init_data_success PASSED [ 89%]
tests/presentation/web/test_api.py::TestAuthEndpoints::test_verify_init_data_invalid PASSED [ 89%]
tests/presentation/web/test_api.py::TestCalendarEndpoints::test_get_calendar_success PASSED [ 90%]
tests/presentation/web/test_api.py::TestCalendarEndpoints::test_get_calendar_invalid_date PASSED [ 90%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_check_panel_access_success PASSED [ 91%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_check_panel_access_no_auth PASSED [ 91%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_list_birthdays PASSED [ 92%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_create_birthday_success PASSED [ 92%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_update_birthday_success PASSED [ 93%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_delete_birthday_success PASSED [ 93%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_list_responsible PASSED [ 93%]
tests/presentation/web/test_api.py::TestPanelEndpoints::test_create_responsible_success PASSED [ 94%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_update_responsible_success PASSED [ 94%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_delete_responsible_success PASSED [ 95%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_assign_responsible_success PASSED [ 95%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_search_people PASSED [ 96%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_generate_greeting_success PASSED [ 96%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_create_card_success PASSED [ 96%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_generate_greeting_not_found PASSED [ 97%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_create_birthday_validation_error PASSED [ 97%]
tests/presentation/web/test_api_additional.py::TestAdditionalEndpoints::test_delete_birthday_not_found PASSED [ 98%]
tests/presentation/web/test_app.py::TestWebApp::test_app_creation PASSED [ 98%]
tests/presentation/web/test_app.py::TestWebApp::test_root_endpoint PASSED [ 99%]
tests/presentation/web/test_app.py::TestWebApp::test_cors_middleware_configured PASSED [ 99%]
tests/presentation/web/test_app.py::TestWebApp::test_router_included PASSED [100%]
=================================== FAILURES ===================================
______________ TestBirthdayHandlers.test_panel_birthdays_callback ______________
tests/presentation/telegram/handlers/test_birthday_handlers.py:70: in test_panel_birthdays_callback
    await panel_birthdays_callback(mock_callback)
E   TypeError: object MagicMock can't be used in 'await' expression
_________________ TestBirthdayHandlers.test_birthday_add_start _________________
tests/presentation/telegram/handlers/test_birthday_handlers.py:83: in test_birthday_add_start
    await birthday_add_start(mock_callback, mock_state)
E   TypeError: object MagicMock can't be used in 'await' expression
_________________ TestBirthdayHandlers.test_process_full_name __________________
tests/presentation/telegram/handlers/test_birthday_handlers.py:94: in test_process_full_name
    await process_full_name(mock_message, mock_state)
E   TypeError: object MagicMock can't be used in 'await' expression
__________________ TestBirthdayHandlers.test_process_company ___________________
tests/presentation/telegram/handlers/test_birthday_handlers.py:105: in test_process_company
    await process_company(mock_message, mock_state)
E   TypeError: object MagicMock can't be used in 'await' expression
__________________ TestBirthdayHandlers.test_process_position __________________
tests/presentation/telegram/handlers/test_birthday_handlers.py:116: in test_process_position
    await process_position(mock_message, mock_state)
E   TypeError: object MagicMock can't be used in 'await' expression
______________ TestBirthdayHandlers.test_process_birth_date_valid ______________
tests/presentation/telegram/handlers/test_birthday_handlers.py:129: in test_process_birth_date_valid
    await process_birth_date(mock_message, mock_state, mock_session)
E   TypeError: object MagicMock can't be used in 'await' expression
_____________ TestBirthdayHandlers.test_process_birth_date_invalid _____________
tests/presentation/telegram/handlers/test_birthday_handlers.py:142: in test_process_birth_date_invalid
    await process_birth_date(mock_message, mock_state, mock_session)
E   TypeError: object MagicMock can't be used in 'await' expression
______________ TestBirthdayHandlers.test_process_comment_success _______________
tests/presentation/telegram/handlers/test_birthday_handlers.py:172: in test_process_comment_success
    await process_comment(mock_message, mock_state, mock_session)
E   TypeError: object MagicMock can't be used in 'await' expression
_____________ TestBirthdayHandlers.test_process_comment_with_dash ______________
tests/presentation/telegram/handlers/test_birthday_handlers.py:205: in test_process_comment_with_dash
    await process_comment(mock_message, mock_state, mock_session)
E   TypeError: object MagicMock can't be used in 'await' expression
_______________ TestBirthdayHandlers.test_process_comment_error ________________
tests/presentation/telegram/handlers/test_birthday_handlers.py:229: in test_process_comment_error
    await process_comment(mock_message, mock_state, mock_session)
E   TypeError: object MagicMock can't be used in 'await' expression
____________________ TestCalendarHandler.test_show_calendar ____________________
tests/presentation/telegram/handlers/test_calendar_handler.py:48: in test_show_calendar
    await show_calendar(mock_message)
E   TypeError: object MagicMock can't be used in 'await' expression
_______________ TestCalendarHandler.test_calendar_callback_info ________________
tests/presentation/telegram/handlers/test_calendar_handler.py:62: in test_calendar_callback_info
    await calendar_callback(mock_callback, None)
E   TypeError: object MagicMock can't be used in 'await' expression
_______________ TestCalendarHandler.test_calendar_callback_prev ________________
tests/presentation/telegram/handlers/test_calendar_handler.py:74: in test_calendar_callback_prev
    await calendar_callback(mock_callback, None)
E   TypeError: object MagicMock can't be used in 'await' expression
_______________ TestCalendarHandler.test_calendar_callback_next ________________
tests/presentation/telegram/handlers/test_calendar_handler.py:88: in test_calendar_callback_next
    await calendar_callback(mock_callback, None)
E   TypeError: object MagicMock can't be used in 'await' expression
__________ TestCalendarHandler.test_date_selected_callback_with_data ___________
tests/presentation/telegram/handlers/test_calendar_handler.py:128: in test_date_selected_callback_with_data
    await date_selected_callback(mock_callback, mock_session)
E   TypeError: object MagicMock can't be used in 'await' expression
____________ TestCalendarHandler.test_date_selected_callback_empty _____________
tests/presentation/telegram/handlers/test_calendar_handler.py:159: in test_date_selected_callback_empty
    await date_selected_callback(mock_callback, mock_session)
E   TypeError: object MagicMock can't be used in 'await' expression
______________ TestGreetingHandlers.test_panel_greetings_callback ______________
tests/presentation/telegram/handlers/test_greeting_handlers.py:72: in test_panel_greetings_callback
    await panel_greetings_callback(mock_callback)
E   TypeError: object MagicMock can't be used in 'await' expression
_______________ TestGreetingHandlers.test_greeting_manual_start ________________
tests/presentation/telegram/handlers/test_greeting_handlers.py:85: in test_greeting_manual_start
    await greeting_manual_start(mock_callback, mock_state)
E   TypeError: object MagicMock can't be used in 'await' expression
______________ TestGreetingHandlers.test_greeting_generate_start _______________
tests/presentation/telegram/handlers/test_greeting_handlers.py:97: in test_greeting_generate_start
    await greeting_generate_start(mock_callback, mock_state)
E   TypeError: object MagicMock can't be used in 'await' expression
________________ TestGreetingHandlers.test_greeting_card_start _________________
tests/presentation/telegram/handlers/test_greeting_handlers.py:109: in test_greeting_card_start
    await greeting_card_start(mock_callback, mock_state)
E   TypeError: object MagicMock can't be used in 'await' expression
_____________ TestGreetingHandlers.test_process_birthday_id_valid ______________
tests/presentation/telegram/handlers/test_greeting_handlers.py:123: in test_process_birthday_id_valid
    await process_birthday_id(mock_message, mock_state)
E   TypeError: object MagicMock can't be used in 'await' expression
____________ TestGreetingHandlers.test_process_birthday_id_invalid _____________
tests/presentation/telegram/handlers/test_greeting_handlers.py:137: in test_process_birthday_id_invalid
    await process_birthday_id(mock_message, mock_state)
E   TypeError: object MagicMock can't be used in 'await' expression
___________________ TestGreetingHandlers.test_process_style ____________________
tests/presentation/telegram/handlers/test_greeting_handlers.py:150: in test_process_style
    await process_style(mock_message, mock_state)
E   TypeError: object MagicMock can't be used in 'await' expression
___________________ TestGreetingHandlers.test_process_length ___________________
tests/presentation/telegram/handlers/test_greeting_handlers.py:165: in test_process_length
    await process_length(mock_message, mock_state)
E   TypeError: object MagicMock can't be used in 'await' expression
_______________ TestGreetingHandlers.test_process_theme_success ________________
tests/presentation/telegram/handlers/test_greeting_handlers.py:190: in test_process_theme_success
    await process_theme(mock_message, mock_state, mock_session)
E   TypeError: object MagicMock can't be used in 'await' expression
______________ TestGreetingHandlers.test_process_theme_with_dash _______________
tests/presentation/telegram/handlers/test_greeting_handlers.py:214: in test_process_theme_with_dash
    await process_theme(mock_message, mock_state, mock_session)
E   TypeError: object MagicMock can't be used in 'await' expression
________________ TestGreetingHandlers.test_process_theme_error _________________
tests/presentation/telegram/handlers/test_greeting_handlers.py:236: in test_process_theme_error
    await process_theme(mock_message, mock_state, mock_session)
E   TypeError: object MagicMock can't be used in 'await' expression
____________________ TestGreetingHandlers.test_process_text ____________________
tests/presentation/telegram/handlers/test_greeting_handlers.py:251: in test_process_text
    await process_text(mock_message, mock_state)
E   TypeError: object MagicMock can't be used in 'await' expression
_______________ TestGreetingHandlers.test_process_qr_url_success _______________
tests/presentation/telegram/handlers/test_greeting_handlers.py:274: in test_process_qr_url_success
    await process_qr_url(mock_message, mock_state, mock_session)
E   TypeError: object MagicMock can't be used in 'await' expression
______________ TestGreetingHandlers.test_process_qr_url_with_dash ______________
tests/presentation/telegram/handlers/test_greeting_handlers.py:298: in test_process_qr_url_with_dash
    await process_qr_url(mock_message, mock_state, mock_session)
E   TypeError: object MagicMock can't be used in 'await' expression
________________ TestGreetingHandlers.test_process_qr_url_error ________________
tests/presentation/telegram/handlers/test_greeting_handlers.py:320: in test_process_qr_url_error
    await process_qr_url(mock_message, mock_state, mock_session)
E   TypeError: object MagicMock can't be used in 'await' expression
_______________________ TestPanelHandler.test_cmd_panel ________________________
tests/presentation/telegram/handlers/test_panel_handler.py:44: in test_cmd_panel
    await cmd_panel(mock_message, mock_session)
E   TypeError: object MagicMock can't be used in 'await' expression
__________________ TestPanelHandler.test_panel_main_callback ___________________
tests/presentation/telegram/handlers/test_panel_handler.py:58: in test_panel_main_callback
    await panel_main_callback(mock_callback)
E   TypeError: object MagicMock can't be used in 'await' expression
___________ TestResponsibleHandlers.test_panel_responsible_callback ____________
tests/presentation/telegram/handlers/test_responsible_handlers.py:62: in test_panel_responsible_callback
    await panel_responsible_callback(mock_callback)
E   TypeError: object MagicMock can't be used in 'await' expression
______________ TestResponsibleHandlers.test_responsible_add_start ______________
tests/presentation/telegram/handlers/test_responsible_handlers.py:75: in test_responsible_add_start
    await responsible_add_start(mock_callback, mock_state)
E   TypeError: object MagicMock can't be used in 'await' expression
________________ TestResponsibleHandlers.test_process_full_name ________________
tests/presentation/telegram/handlers/test_responsible_handlers.py:87: in test_process_full_name
    await process_full_name(mock_message, mock_state)
E   TypeError: object MagicMock can't be used in 'await' expression
_________________ TestResponsibleHandlers.test_process_company _________________
tests/presentation/telegram/handlers/test_responsible_handlers.py:98: in test_process_company
    await process_company(mock_message, mock_state)
E   TypeError: object MagicMock can't be used in 'await' expression
____________ TestResponsibleHandlers.test_process_position_success _____________
tests/presentation/telegram/handlers/test_responsible_handlers.py:126: in test_process_position_success
    await process_position(mock_message, mock_state, mock_session)
E   TypeError: object MagicMock can't be used in 'await' expression
_____________ TestResponsibleHandlers.test_process_position_error ______________
tests/presentation/telegram/handlers/test_responsible_handlers.py:150: in test_process_position_error
    await process_position(mock_message, mock_state, mock_session)
E   TypeError: object MagicMock can't be used in 'await' expression
_______________________ TestStartHandler.test_cmd_start ________________________
tests/presentation/telegram/handlers/test_start_handler.py:24: in test_cmd_start
    await cmd_start(mock_message)
E   TypeError: object MagicMock can't be used in 'await' expression
---------- coverage: platform linux, python 3.11.14-final-0 ----------
Name                                                                       Stmts   Miss  Cover
----------------------------------------------------------------------------------------------
src/__init__.py                                                                0      0   100%
src/application/__init__.py                                                    0      0   100%
src/application/factories/__init__.py                                          0      0   100%
src/application/factories/use_case_factory.py                                 94      1    99%
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
src/domain/exceptions/api_exceptions.py                                       12      0   100%
src/domain/exceptions/base.py                                                  2      0   100%
src/domain/exceptions/business.py                                              3      0   100%
src/domain/exceptions/not_found.py                                             7      0   100%
src/domain/exceptions/validation.py                                            5      0   100%
src/infrastructure/__init__.py                                                 0      0   100%
src/infrastructure/config/__init__.py                                          0      0   100%
src/infrastructure/config/openrouter_config.py                                18      0   100%
src/infrastructure/database/__init__.py                                        0      0   100%
src/infrastructure/database/database.py                                       12      0   100%
src/infrastructure/database/database_factory.py                               10      0   100%
src/infrastructure/database/models.py                                         47      0   100%
src/infrastructure/database/repositories/__init__.py                           0      0   100%
src/infrastructure/database/repositories/birthday_repository_impl.py          61      0   100%
src/infrastructure/database/repositories/holiday_repository_impl.py           48      0   100%
src/infrastructure/database/repositories/panel_access_repository_impl.py      15      0   100%
src/infrastructure/database/repositories/responsible_repository_impl.py       65      5    92%
src/infrastructure/external/__init__.py                                        0      0   100%
src/infrastructure/external/openrouter_client_impl.py                         56      2    96%
src/infrastructure/external/telegram_auth.py                                  43      2    95%
src/infrastructure/image/__init__.py                                           0      0   100%
src/infrastructure/image/card_generator.py                                    79     18    77%
src/infrastructure/services/__init__.py                                        0      0   100%
src/infrastructure/services/notification_service_impl.py                      87      5    94%
src/infrastructure/services/notifications_scheduler.py                        30      0   100%
src/presentation/__init__.py                                                   0      0   100%
src/presentation/telegram/__init__.py                                          0      0   100%
src/presentation/telegram/bot.py                                              26      0   100%
src/presentation/telegram/handlers/__init__.py                                 2      0   100%
src/presentation/telegram/handlers/birthday_handlers.py                       64     35    45%
src/presentation/telegram/handlers/calendar_handler.py                        72     59    18%
src/presentation/telegram/handlers/greeting_handlers.py                       87     52    40%
src/presentation/telegram/handlers/panel_handler.py                           17      6    65%
src/presentation/telegram/handlers/responsible_handlers.py                    45     23    49%
src/presentation/telegram/handlers/start_handler.py                            8      1    88%
src/presentation/telegram/keyboards.py                                        19      0   100%
src/presentation/web/__init__.py                                               0      0   100%
src/presentation/web/app.py                                                   15      1    93%
src/presentation/web/routes/__init__.py                                        0      0   100%
src/presentation/web/routes/api.py                                           248     78    69%
----------------------------------------------------------------------------------------------
TOTAL                                                                       1548    288    81%
Coverage HTML written to dir htmlcov
Coverage XML written to file coverage.xml
=========================== short test summary info ============================
FAILED tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_panel_birthdays_callback - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_birthday_add_start - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_process_full_name - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_process_company - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_process_position - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_process_birth_date_valid - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_process_birth_date_invalid - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_process_comment_success - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_process_comment_with_dash - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_birthday_handlers.py::TestBirthdayHandlers::test_process_comment_error - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_calendar_handler.py::TestCalendarHandler::test_show_calendar - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_calendar_handler.py::TestCalendarHandler::test_calendar_callback_info - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_calendar_handler.py::TestCalendarHandler::test_calendar_callback_prev - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_calendar_handler.py::TestCalendarHandler::test_calendar_callback_next - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_calendar_handler.py::TestCalendarHandler::test_date_selected_callback_with_data - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_calendar_handler.py::TestCalendarHandler::test_date_selected_callback_empty - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_panel_greetings_callback - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_greeting_manual_start - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_greeting_generate_start - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_greeting_card_start - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_birthday_id_valid - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_birthday_id_invalid - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_style - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_length - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_theme_success - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_theme_with_dash - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_theme_error - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_text - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_qr_url_success - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_qr_url_with_dash - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_greeting_handlers.py::TestGreetingHandlers::test_process_qr_url_error - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_panel_handler.py::TestPanelHandler::test_cmd_panel - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_panel_handler.py::TestPanelHandler::test_panel_main_callback - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_responsible_handlers.py::TestResponsibleHandlers::test_panel_responsible_callback - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_responsible_handlers.py::TestResponsibleHandlers::test_responsible_add_start - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_responsible_handlers.py::TestResponsibleHandlers::test_process_full_name - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_responsible_handlers.py::TestResponsibleHandlers::test_process_company - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_responsible_handlers.py::TestResponsibleHandlers::test_process_position_success - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_responsible_handlers.py::TestResponsibleHandlers::test_process_position_error - TypeError: object MagicMock can't be used in 'await' expression
FAILED tests/presentation/telegram/handlers/test_start_handler.py::TestStartHandler::test_cmd_start - TypeError: object MagicMock can't be used in 'await' expression
================ 40 failed, 189 passed, 186 warnings in 11.17s =================
Error: Process completed with exit code 1.