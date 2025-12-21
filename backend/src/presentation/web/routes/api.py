import json
import logging
from datetime import date

from fastapi import APIRouter, Body, Depends, Header, HTTPException, Path, Query, Request, Response
from pydantic import BaseModel, Field, field_validator
from slowapi import Limiter
from slowapi.util import get_remote_address
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.factories.use_case_factory import UseCaseFactory
from src.domain.exceptions.not_found import BirthdayNotFoundError
from src.infrastructure.config.rate_limits import (
    ACCESS_CHECK_LIMIT,
    HEAVY_OPERATION_LIMIT,
    PUBLIC_ENDPOINT_LIMIT,
    READ_LIMIT,
    WRITE_LIMIT,
)
from src.presentation.web.decorators import handle_api_errors
from src.presentation.web.dependencies import (
    get_db_session,
    get_readonly_use_case_factory,
    get_use_case_factory,
)

logger = logging.getLogger(__name__)

router = APIRouter()

# Инициализация rate limiter для роутера
limiter = Limiter(key_func=get_remote_address)


# DTOs
class BirthdayCreate(BaseModel):
    full_name: str = Field(..., min_length=1, max_length=200, description="Полное имя")
    company: str = Field(..., min_length=1, max_length=200, description="Компания")
    position: str = Field(..., min_length=1, max_length=200, description="Должность")
    birth_date: date = Field(..., description="Дата рождения")
    comment: str | None = Field(None, max_length=1000, description="Комментарий")

    @field_validator("full_name", "company", "position")
    @classmethod
    def validate_not_empty(cls, v: str) -> str:
        """Проверка, что строка не пустая после удаления пробелов."""
        if not v or not v.strip():
            raise ValueError("Field cannot be empty")
        return v.strip()


class BirthdayUpdate(BaseModel):
    full_name: str | None = Field(None, min_length=1, max_length=200, description="Полное имя")
    company: str | None = Field(None, min_length=1, max_length=200, description="Компания")
    position: str | None = Field(None, min_length=1, max_length=200, description="Должность")
    birth_date: date | None = Field(None, description="Дата рождения")
    comment: str | None = Field(None, max_length=1000, description="Комментарий")

    @field_validator("full_name", "company", "position")
    @classmethod
    def validate_not_empty_if_provided(cls, v: str | None) -> str | None:
        """Проверка, что строка не пустая, если предоставлена."""
        if v is not None and (not v or not v.strip()):
            raise ValueError("Field cannot be empty if provided")
        return v.strip() if v else None


class ResponsibleCreate(BaseModel):
    full_name: str = Field(..., min_length=1, max_length=200, description="Полное имя")
    company: str = Field(..., min_length=1, max_length=200, description="Компания")
    position: str = Field(..., min_length=1, max_length=200, description="Должность")

    @field_validator("full_name", "company", "position")
    @classmethod
    def validate_not_empty(cls, v: str) -> str:
        """Проверка, что строка не пустая после удаления пробелов."""
        if not v or not v.strip():
            raise ValueError("Field cannot be empty")
        return v.strip()


class ResponsibleUpdate(BaseModel):
    full_name: str | None = Field(None, min_length=1, max_length=200, description="Полное имя")
    company: str | None = Field(None, min_length=1, max_length=200, description="Компания")
    position: str | None = Field(None, min_length=1, max_length=200, description="Должность")

    @field_validator("full_name", "company", "position")
    @classmethod
    def validate_not_empty_if_provided(cls, v: str | None) -> str | None:
        """Проверка, что строка не пустая, если предоставлена."""
        if v is not None and (not v or not v.strip()):
            raise ValueError("Field cannot be empty if provided")
        return v.strip() if v else None


class AssignResponsibleRequest(BaseModel):
    responsible_id: int
    date: date


class GenerateGreetingRequest(BaseModel):
    birthday_id: int
    style: str
    length: str
    theme: str | None = None


class CreateCardRequest(BaseModel):
    birthday_id: int = Field(..., gt=0, description="ID дня рождения")
    greeting_text: str = Field(..., min_length=1, max_length=2000, description="Текст поздравления")
    qr_url: str | None = Field(None, max_length=500, description="URL для QR-кода")

    @field_validator("greeting_text")
    @classmethod
    def validate_greeting_text(cls, v: str) -> str:
        """Проверка, что текст поздравления не пустой."""
        if not v or not v.strip():
            raise ValueError("Greeting text cannot be empty")
        return v.strip()


class VerifyInitDataRequest(BaseModel):
    init_data: str = Field(
        ..., min_length=1, max_length=5000, description="Telegram WebApp initData"
    )


# Dependency для проверки авторизации через Telegram
async def verify_telegram_auth(x_init_data: str | None = Header(None, alias="X-Init-Data")) -> dict:
    """Dependency для проверки авторизации через Telegram WebApp."""
    # ЛОГИРОВАНИЕ В САМОМ НАЧАЛЕ ДО ВСЕХ ПРОВЕРОК
    logger.info(f"[AUTH] ===== verify_telegram_auth CALLED =====")
    logger.info(f"[AUTH] X-Init-Data present: {x_init_data is not None}")
    logger.info(f"[AUTH] X-Init-Data length: {len(x_init_data) if x_init_data else 0}")
    
    if not x_init_data:
        logger.warning("[AUTH] Missing X-Init-Data header")
        raise HTTPException(status_code=401, detail="Missing initData")

    # Создаем use-case через фабрику (не требует session)
    factory = UseCaseFactory(session=None)  # Auth use-case не требует БД сессии
    use_case = factory.create_auth_use_case()

    try:
        user_data = await use_case.execute(x_init_data)
        logger.info(f"[AUTH] User authenticated: user_id={user_data.get('id')}")
        
        # Извлекаем start_param из initData для определения режима
        # start_param передается в initData как параметр start_param
        import urllib.parse
        parsed_data = urllib.parse.parse_qs(x_init_data)
        start_param = parsed_data.get("start_param", [None])[0]
        if start_param:
            user_data["start_param"] = start_param
            logger.info(f"[AUTH] Start param detected: {start_param}")
        
        return user_data
    except ValueError as e:
        logger.warning(f"[AUTH] Invalid initData: {e}")
        raise HTTPException(status_code=401, detail="Invalid initData") from e


# Вспомогательная функция для проверки доступа к панели с переданной сессией
async def _check_panel_access(session: AsyncSession, user_id: int) -> bool:
    """
    Проверить доступ пользователя к панели управления с использованием переданной сессии.
    
    Args:
        session: Сессия БД для использования
        user_id: ID пользователя для проверки
        
    Returns:
        True, если у пользователя есть доступ, False в противном случае
    """
    factory = UseCaseFactory(session=session)
    use_case = factory.create_panel_access_use_case()
    return await use_case.execute(user_id)


# Вспомогательная функция для аутентификации и проверки доступа к панели
async def _authenticate_and_check_access(
    session: AsyncSession,
    request: Request,
) -> dict:
    """
    Аутентификация пользователя через Telegram и проверка доступа к панели управления.
    
    Выполняет:
    1. Проверку X-Init-Data header
    2. Верификацию пользователя через auth use case
    3. Проверку доступа к панели
    4. Обработку ошибок авторизации
    
    Args:
        session: Сессия БД для использования при проверке доступа
        request: FastAPI Request объект для получения headers
        
    Returns:
        dict: Данные пользователя (содержит 'id' и другие поля)
        
    Raises:
        HTTPException 401: Если пользователь не авторизован или нет user_id
        HTTPException 403: Если у пользователя нет доступа к панели
    """
    logger.info(f"[AUTH_HELPER] ===== Starting authentication and access check =====")
    
    # Проверяем авторизацию через Telegram
    logger.info(f"[AUTH_HELPER] [STEP 1] Checking X-Init-Data header")
    x_init_data = request.headers.get("X-Init-Data")
    if not x_init_data:
        logger.warning("[AUTH_HELPER] [STEP 1] Missing X-Init-Data header")
        raise HTTPException(status_code=401, detail="Missing initData")
    
    logger.info(f"[AUTH_HELPER] [STEP 1] X-Init-Data header present: {x_init_data[:20]}...")
    
    # Верифицируем пользователя
    logger.info(f"[AUTH_HELPER] [STEP 2] Verifying user via auth use case")
    auth_factory = UseCaseFactory(session=None)  # Auth не требует БД сессии
    auth_use_case = auth_factory.create_auth_use_case()
    try:
        logger.info(f"[AUTH_HELPER] [STEP 2] Executing auth use case")
        user = await auth_use_case.execute(x_init_data)
        logger.info(f"[AUTH_HELPER] [STEP 2] Authentication successful, user: {user}")
    except ValueError as e:
        logger.warning(f"[AUTH_HELPER] [STEP 2] Invalid initData: {e}")
        raise HTTPException(status_code=401, detail="Invalid initData") from e
    
    user_id = user.get("id")
    if not user_id:
        logger.warning("[AUTH_HELPER] [STEP 2] User ID not found in initData")
        raise HTTPException(status_code=401, detail="User ID not found in initData")
    
    logger.info(f"[AUTH_HELPER] [STEP 2] Authentication completed, user_id={user_id}")
    
    # Проверяем доступ к панели используя переданную сессию
    logger.info(f"[AUTH_HELPER] [STEP 3] Checking panel access for user_id={user_id}")
    has_access = await _check_panel_access(session, user_id)
    if not has_access:
        logger.warning(f"[AUTH_HELPER] [STEP 3] Access denied for user_id={user_id}")
        raise HTTPException(
            status_code=403, detail="Access denied. You don't have permission to access the panel."
        )
    
    logger.info(f"[AUTH_HELPER] [STEP 3] Panel access granted for user_id={user_id}")
    logger.info(f"[AUTH_HELPER] ===== Authentication and access check completed successfully =====")
    
    return user


# Dependency для проверки прав доступа к панели управления
async def require_panel_access(
    user: dict = Depends(verify_telegram_auth),
    factory: UseCaseFactory = Depends(get_readonly_use_case_factory),
) -> dict:
    """
    Dependency для проверки прав доступа к панели управления.

    Проверяет:
    1. Авторизацию через Telegram (verify_telegram_auth)
    2. Режим panel в start_param (Mini App должен быть открыт через /panel)
    3. Наличие прав доступа к панели (check_panel_access)

    Raises:
        HTTPException 401: Если пользователь не авторизован или нет user_id
        HTTPException 403: Если Mini App открыт не в режиме panel или нет доступа к панели
    """
    # ЛОГИРОВАНИЕ В САМОМ НАЧАЛЕ ДО ВСЕХ ПРОВЕРОК
    logger.info(f"[AUTH] ===== require_panel_access CALLED =====")
    logger.info(f"[AUTH] User data received: user_id={user.get('id')}, start_param={user.get('start_param')}")
    
    user_id = user.get("id")
    if not user_id:
        logger.warning("[AUTH] User ID not found in initData")
        raise HTTPException(status_code=401, detail="User ID not found in initData")

    # Проверяем, что Mini App открыт в режиме panel
    start_param = user.get("start_param")
    if start_param != "panel":
        logger.warning(
            f"[AUTH] Panel mode required but start_param={start_param}. "
            f"Mini App must be opened via /panel command."
        )
        raise HTTPException(
            status_code=403,
            detail="Panel mode required. Please open Mini App using /panel command."
        )

    # Проверяем доступ к панели
    use_case = factory.create_panel_access_use_case()
    has_access = await use_case.execute(user_id)

    if not has_access:
        logger.warning(f"[AUTH] Access denied for user_id={user_id}")
        raise HTTPException(
            status_code=403, detail="Access denied. You don't have permission to access the panel."
        )

    logger.info(f"[AUTH] Panel access granted for user_id={user_id} (panel mode)")
    return user


# Auth endpoints
@router.post("/api/auth/verify")
async def verify_init_data(data: VerifyInitDataRequest):
    """Верифицировать initData от Telegram WebApp."""
    # Логирование входящего запроса (без чувствительных данных)
    init_data_length = len(data.init_data)
    init_data_preview = (
        data.init_data[:50] + "..." if len(data.init_data) > 50 else data.init_data
    )
    logger.info(
        f"POST /api/auth/verify: Received init_data request (length={init_data_length}, "
        f"preview={init_data_preview})"
    )

    # Создаем use-case через фабрику (не требует session)
    # Auth use-case не требует БД сессии, поэтому передаем None
    try:
        factory = UseCaseFactory(session=None)
        logger.debug("Created UseCaseFactory for auth verification")
    except Exception as e:
        logger.error(f"Failed to create UseCaseFactory: {e}", exc_info=True)
        raise HTTPException(
            status_code=500, detail="Internal server error: failed to initialize auth service"
        ) from e

    try:
        use_case = factory.create_auth_use_case()
        logger.debug("Created VerifyTelegramAuthUseCase")
    except ValueError as e:
        logger.error(f"Failed to create auth use case: {e}", exc_info=True)
        raise HTTPException(
            status_code=500, detail="Internal server error: failed to create auth use case"
        ) from e

    # Валидация формата init_data перед обработкой
    if not data.init_data or not data.init_data.strip():
        logger.warning("Empty or whitespace-only init_data received")
        raise HTTPException(status_code=400, detail="Invalid initData format: empty or whitespace")

    if "=" not in data.init_data:
        logger.warning(f"Invalid init_data format: missing '=' separator (preview: {init_data_preview})")
        raise HTTPException(
            status_code=400, detail="Invalid initData format: expected query string format"
        )

    try:
        logger.debug("Starting init_data verification")
        user_data = await use_case.execute(data.init_data)
        logger.info(f"Successfully verified init_data, user_id: {user_data.get('id', 'unknown')}")
        return {
            "valid": True,
            "user": user_data,
        }
    except ValueError as e:
        error_msg = str(e)
        logger.warning(
            f"InitData verification failed: {error_msg} (init_data_length={init_data_length}, "
            f"preview={init_data_preview})"
        )
        # Определяем тип ошибки для более детального сообщения
        if "Invalid initData" in error_msg or "signature" in error_msg.lower():
            detail = "Invalid initData signature: verification failed"
        elif "format" in error_msg.lower() or "parse" in error_msg.lower():
            detail = "Invalid initData format: unable to parse"
        else:
            detail = f"Invalid initData: {error_msg}"
        raise HTTPException(status_code=401, detail=detail) from e
    except Exception as e:
        logger.error(
            f"Unexpected error during init_data verification: {type(e).__name__}: {e}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=500, detail="Internal server error during verification"
        ) from e


# Public endpoints
@router.get("/api/calendar/{date_str}")
@limiter.limit(PUBLIC_ENDPOINT_LIMIT)
async def get_calendar(
    request: Request,
    date_str: str = Path(
        ..., pattern="^\\d{4}-\\d{2}-\\d{2}$", description="Дата в формате YYYY-MM-DD"
    ),
    factory: UseCaseFactory = Depends(get_readonly_use_case_factory),
):
    """Получить данные календаря на дату."""
    try:
        check_date = date.fromisoformat(date_str)
    except ValueError as e:
        raise HTTPException(status_code=400, detail="Invalid date format") from e

    use_case = factory.create_calendar_use_case()
    return await use_case.execute(check_date)


@router.get("/api/calendar/month/{year}/{month}")
@limiter.limit(PUBLIC_ENDPOINT_LIMIT)
@handle_api_errors
async def get_calendar_month(
    request: Request,
    year: int = Path(..., ge=1900, le=2100, description="Год"),
    month: int = Path(..., ge=1, le=12, description="Месяц (1-12)"),
    factory: UseCaseFactory = Depends(get_readonly_use_case_factory),
):
    """Получить дни рождения за указанный месяц."""
    logger.info(f"[API] Loading birthdays for month {year}-{month:02d}")

    birthday_repo = factory.birthday_repo
    # Получаем все дни рождения в указанном месяце (любой год)
    birthdays = await birthday_repo.get_by_month(month)

    logger.info(f"[API] Found {len(birthdays)} birthdays in month {month}")

    # Группируем дни рождения по датам с годом из запроса для правильного отображения
    birthdays_by_date: dict[str, list[dict]] = {}
    for b in birthdays:
        # Используем день и месяц из birth_date, но год из запроса
        date_key = f"{year}-{b.birth_date.month:02d}-{b.birth_date.day:02d}"
        if date_key not in birthdays_by_date:
            birthdays_by_date[date_key] = []
        birthdays_by_date[date_key].append({
            "id": b.id,
            "full_name": b.full_name,
            "company": b.company,
            "position": b.position,
        })

    logger.info(f"[API] Grouped birthdays into {len(birthdays_by_date)} dates: {list(birthdays_by_date.keys())}")

    return {
        "year": year,
        "month": month,
        "birthdays_by_date": birthdays_by_date,
    }


# Panel endpoints
@router.get("/api/panel/check-access")
@limiter.limit(ACCESS_CHECK_LIMIT)
async def check_panel_access(
    request: Request,
    user: dict = Depends(verify_telegram_auth),
    factory: UseCaseFactory = Depends(get_readonly_use_case_factory),
):
    """Проверить доступ пользователя к панели управления."""
    user_id = user.get("id")
    if not user_id:
        raise HTTPException(status_code=401, detail="User ID not found in initData")

    use_case = factory.create_panel_access_use_case()

    has_access = await use_case.execute(user_id)
    return {"has_access": has_access}


@router.get("/api/panel/birthdays")
@limiter.limit(READ_LIMIT)
async def list_birthdays(
    request: Request,
    user: dict = Depends(require_panel_access),
    factory: UseCaseFactory = Depends(get_readonly_use_case_factory),
):
    """Список всех ДР."""
    use_cases = factory.create_birthday_use_cases()
    use_case = use_cases["get_all"]
    birthdays = await use_case.execute()
    return [
        {
            "id": b.id,
            "full_name": b.full_name,
            "company": b.company,
            "position": b.position,
            "birth_date": b.birth_date.isoformat(),
            "comment": b.comment,
        }
        for b in birthdays
    ]


@router.post("/api/panel/birthdays")
@limiter.limit(WRITE_LIMIT)
@handle_api_errors
async def create_birthday(
    request: Request,
    data: BirthdayCreate,
    session: AsyncSession = Depends(get_db_session),
    user: dict = Depends(require_panel_access),
    factory: UseCaseFactory = Depends(get_use_case_factory),
):
    """Создать ДР."""
    use_cases = factory.create_birthday_use_cases()
    use_case = use_cases["create"]

    birthday = await use_case.execute(
        full_name=data.full_name,
        company=data.company,
        position=data.position,
        birth_date=data.birth_date,
        comment=data.comment,
    )
    await session.commit()
    return {
        "id": birthday.id,
        "full_name": birthday.full_name,
        "company": birthday.company,
        "position": birthday.position,
        "birth_date": birthday.birth_date.isoformat(),
        "comment": birthday.comment,
    }


@router.put("/api/panel/birthdays/{birthday_id}")
@limiter.limit(WRITE_LIMIT)
@handle_api_errors
async def update_birthday(
    request: Request,
    birthday_id: int = Path(..., gt=0, description="ID дня рождения"),
    data: BirthdayUpdate = Body(..., description="Данные для обновления дня рождения"),
    session: AsyncSession = Depends(get_db_session),
):
    """Обновить ДР."""
    # Логирование в самом начале endpoint'а ДО декоратора и всех проверок
    logger.info(f"[API] ===== PUT /api/panel/birthdays/{birthday_id} - ENTRY POINT =====")
    logger.info(f"[API] Request method: {request.method}")
    logger.info(f"[API] Request path: {request.url.path}")
    logger.info(f"[API] Request headers: {dict(request.headers)}")
    logger.info(f"[API] Session ID: {id(session)}")
    
    # Логирование после получения данных из Pydantic
    logger.info(f"[API] [STEP 1] Pydantic validation passed")
    logger.info(f"[API] [STEP 1] Received data: birthday_id={birthday_id}, full_name={data.full_name}, company={data.company}, position={data.position}, birth_date={data.birth_date}, comment={data.comment}")
    
    # Аутентификация и проверка доступа к панели
    logger.info(f"[API] [STEP 2] Starting authentication and access check")
    user = await _authenticate_and_check_access(session, request)
    user_id = user.get("id")
    logger.info(f"[API] [STEP 2] Authentication and access check completed, user_id={user_id}")
    
    # Создаём factory с переданной сессией для операций
    logger.info(f"[API] [STEP 3] Creating UseCaseFactory with session")
    factory = UseCaseFactory(session=session)
    logger.info(f"[API] [STEP 3] UseCaseFactory created")
    
    # Выполняем операцию обновления
    logger.info(f"[API] [STEP 4] Creating birthday use cases")
    use_cases = factory.create_birthday_use_cases()
    use_case = use_cases["update"]
    logger.info(f"[API] [STEP 4] Update use case created")

    try:
        logger.info(f"[API] [STEP 4] Executing update use case for birthday_id={birthday_id}")
        logger.info(f"[API] [STEP 4] Update data: full_name={data.full_name}, company={data.company}, position={data.position}, birth_date={data.birth_date}, comment={data.comment}")
        birthday = await use_case.execute(
            birthday_id=birthday_id,
            full_name=data.full_name,
            company=data.company,
            position=data.position,
            birth_date=data.birth_date,
            comment=data.comment,
        )
        logger.info(f"[API] [STEP 4] Use case executed successfully, birthday: id={birthday.id}, full_name={birthday.full_name}")
        
        logger.info(f"[API] [STEP 5] Starting commit for birthday_id={birthday_id}")
        await session.commit()
        logger.info(f"[API] [STEP 5] Commit completed successfully for birthday_id={birthday_id}")
        logger.info(f"[API] [STEP 5] Transaction committed, changes should be persisted in database")
        
        logger.info(f"[API] ===== PUT /api/panel/birthdays/{birthday_id} - SUCCESS =====")
    except ValueError as e:
        logger.warning(f"[API] [STEP 4/5] Validation error updating birthday {birthday_id}: {e}")
        logger.info(f"[API] [STEP 5] Starting rollback due to ValueError")
        await session.rollback()
        logger.info(f"[API] [STEP 5] Rollback completed")
        raise
    except Exception as e:
        logger.error(f"[API] [STEP 4/5] Error updating birthday {birthday_id}: {type(e).__name__}: {e}", exc_info=True)
        logger.info(f"[API] [STEP 5] Starting rollback due to Exception")
        await session.rollback()
        logger.info(f"[API] [STEP 5] Rollback completed")
        raise
    
    logger.info(f"[API] [STEP 6] Preparing response for birthday_id={birthday_id}")
    return {
        "id": birthday.id,
        "full_name": birthday.full_name,
        "company": birthday.company,
        "position": birthday.position,
        "birth_date": birthday.birth_date.isoformat(),
        "comment": birthday.comment,
    }


@router.delete("/api/panel/birthdays/{birthday_id}")
@limiter.limit(WRITE_LIMIT)
@handle_api_errors
async def delete_birthday(
    request: Request,
    birthday_id: int = Path(..., gt=0, description="ID дня рождения"),
    session: AsyncSession = Depends(get_db_session),
):
    """Удалить ДР."""
    # Логирование в самом начале endpoint'а ДО декоратора и всех проверок
    logger.info(f"[API] ===== DELETE /api/panel/birthdays/{birthday_id} - ENTRY POINT =====")
    logger.info(f"[API] Request method: {request.method}")
    logger.info(f"[API] Request path: {request.url.path}")
    logger.info(f"[API] Request headers: {dict(request.headers)}")
    logger.info(f"[API] Session ID: {id(session)}")
    
    # Логирование после получения данных из Path
    logger.info(f"[API] [STEP 1] Path validation passed")
    logger.info(f"[API] [STEP 1] Received birthday_id: {birthday_id}")
    
    # Аутентификация и проверка доступа к панели
    logger.info(f"[API] [STEP 2] Starting authentication and access check")
    user = await _authenticate_and_check_access(session, request)
    user_id = user.get("id")
    logger.info(f"[API] [STEP 2] Authentication and access check completed, user_id={user_id}")
    
    # Создаём factory с переданной сессией для операций
    logger.info(f"[API] [STEP 3] Creating UseCaseFactory with session")
    factory = UseCaseFactory(session=session)
    logger.info(f"[API] [STEP 3] UseCaseFactory created")
    
    # Выполняем операцию удаления
    logger.info(f"[API] [STEP 4] Creating birthday use cases")
    use_cases = factory.create_birthday_use_cases()
    use_case = use_cases["delete"]
    logger.info(f"[API] [STEP 4] Delete use case created")

    try:
        logger.info(f"[API] [STEP 4] Executing delete use case for birthday_id={birthday_id}")
        await use_case.execute(birthday_id)
        logger.info(f"[API] [STEP 4] Use case executed successfully for birthday_id={birthday_id}")
        
        logger.info(f"[API] [STEP 5] Starting commit for birthday_id={birthday_id}")
        await session.commit()
        logger.info(f"[API] [STEP 5] Commit completed successfully for birthday_id={birthday_id}")
        logger.info(f"[API] [STEP 5] Transaction committed, deletion should be persisted in database")
        
        logger.info(f"[API] ===== DELETE /api/panel/birthdays/{birthday_id} - SUCCESS =====")
    except ValueError as e:
        logger.warning(f"[API] [STEP 4/5] Validation error deleting birthday {birthday_id}: {e}")
        logger.info(f"[API] [STEP 5] Starting rollback due to ValueError")
        await session.rollback()
        logger.info(f"[API] [STEP 5] Rollback completed")
        raise
    except Exception as e:
        logger.error(f"[API] [STEP 4/5] Error deleting birthday {birthday_id}: {type(e).__name__}: {e}", exc_info=True)
        logger.info(f"[API] [STEP 5] Starting rollback due to Exception")
        await session.rollback()
        logger.info(f"[API] [STEP 5] Rollback completed")
        raise
    
    logger.info(f"[API] [STEP 6] Preparing response for birthday_id={birthday_id}")
    return {"status": "deleted"}


@router.get("/api/panel/responsible")
@limiter.limit(READ_LIMIT)
async def list_responsible(
    request: Request,
    user: dict = Depends(require_panel_access),
    factory: UseCaseFactory = Depends(get_readonly_use_case_factory),
):
    """Список всех ответственных."""
    responsible_use_cases = factory.create_responsible_use_cases()
    use_case = responsible_use_cases["get_all"]
    responsible = await use_case.execute()
    return [
        {
            "id": r.id,
            "full_name": r.full_name,
            "company": r.company,
            "position": r.position,
        }
        for r in responsible
    ]


@router.post("/api/panel/responsible")
@limiter.limit(WRITE_LIMIT)
@handle_api_errors
async def create_responsible(
    request: Request,
    data: ResponsibleCreate,
    session: AsyncSession = Depends(get_db_session),
    user: dict = Depends(require_panel_access),
    factory: UseCaseFactory = Depends(get_use_case_factory),
):
    """Создать ответственного."""
    responsible_use_cases = factory.create_responsible_use_cases()
    use_case = responsible_use_cases["create"]

    responsible = await use_case.execute(
        full_name=data.full_name,
        company=data.company,
        position=data.position,
    )
    await session.commit()
    return {
        "id": responsible.id,
        "full_name": responsible.full_name,
        "company": responsible.company,
        "position": responsible.position,
    }


@router.put("/api/panel/responsible/{responsible_id}")
@limiter.limit(WRITE_LIMIT)
@handle_api_errors
async def update_responsible(
    request: Request,
    responsible_id: int = Path(..., gt=0, description="ID ответственного лица"),
    data: ResponsibleUpdate = Body(..., description="Данные для обновления ответственного лица"),
    session: AsyncSession = Depends(get_db_session),
    user: dict = Depends(require_panel_access),
    factory: UseCaseFactory = Depends(get_use_case_factory),
):
    """Обновить ответственного."""
    responsible_use_cases = factory.create_responsible_use_cases()
    use_case = responsible_use_cases["update"]

    responsible = await use_case.execute(
        responsible_id=responsible_id,
        full_name=data.full_name,
        company=data.company,
        position=data.position,
    )
    await session.commit()
    return {
        "id": responsible.id,
        "full_name": responsible.full_name,
        "company": responsible.company,
        "position": responsible.position,
    }


@router.delete("/api/panel/responsible/{responsible_id}")
@limiter.limit(WRITE_LIMIT)
@handle_api_errors
async def delete_responsible(
    request: Request,
    responsible_id: int = Path(..., gt=0, description="ID ответственного лица"),
    session: AsyncSession = Depends(get_db_session),
    user: dict = Depends(require_panel_access),
    factory: UseCaseFactory = Depends(get_use_case_factory),
):
    """Удалить ответственного."""
    responsible_use_cases = factory.create_responsible_use_cases()
    use_case = responsible_use_cases["delete"]

    await use_case.execute(responsible_id)
    await session.commit()
    return {"status": "deleted"}


@router.post("/api/panel/assign-responsible")
@limiter.limit(WRITE_LIMIT)
@handle_api_errors
async def assign_responsible(
    request: Request,
    data: AssignResponsibleRequest,
    session: AsyncSession = Depends(get_db_session),
    user: dict = Depends(require_panel_access),
    factory: UseCaseFactory = Depends(get_use_case_factory),
):
    """Назначить ответственного на дату."""
    responsible_use_cases = factory.create_responsible_use_cases()
    use_case = responsible_use_cases["assign_to_date"]

    await use_case.execute(data.responsible_id, data.date)
    await session.commit()
    return {"status": "assigned"}


@router.get("/api/panel/search")
@limiter.limit(READ_LIMIT)
async def search_people(
    request: Request,
    q: str = Query(..., min_length=1, max_length=200, description="Поисковый запрос"),
    user: dict = Depends(require_panel_access),
    factory: UseCaseFactory = Depends(get_readonly_use_case_factory),
):
    """Поиск людей."""
    use_case = factory.create_search_use_case()

    results = await use_case.execute(q)

    return [
        {
            "type": "birthday" if hasattr(r, "birth_date") else "responsible",
            "id": r.id,
            "full_name": r.full_name,
            "company": r.company,
            "position": r.position,
        }
        for r in results
    ]


@router.post("/api/panel/generate-greeting")
@limiter.limit(HEAVY_OPERATION_LIMIT)
@handle_api_errors
async def generate_greeting(
    request: Request,
    data: GenerateGreetingRequest,
    user: dict = Depends(require_panel_access),
    factory: UseCaseFactory = Depends(get_readonly_use_case_factory),
):
    """Сгенерировать поздравление."""
    logger.info(
        f"[API] Generate greeting request: birthday_id={data.birthday_id}, "
        f"style={data.style}, length={data.length}, theme={data.theme}, "
        f"user_id={user.get('id', 'unknown')}"
    )
    
    greeting_use_cases = factory.create_greeting_use_cases()
    use_case = greeting_use_cases["generate"]

    try:
        greeting_text = await use_case.execute(
            birthday_id=data.birthday_id,
            style=data.style,
            length=data.length,
            theme=data.theme,
        )
        logger.info(
            f"[API] Greeting generated successfully for birthday_id={data.birthday_id}, "
            f"length={len(greeting_text)} characters"
        )
        return {"greeting": greeting_text}
    except BirthdayNotFoundError as e:
        logger.warning(
            f"[API] Birthday not found: birthday_id={data.birthday_id}, error={e}"
        )
        raise
    except Exception as e:
        logger.error(
            f"[API] Error generating greeting for birthday_id={data.birthday_id}: {type(e).__name__}: {e}",
            exc_info=True,
        )
        raise


@router.post("/api/panel/create-card")
@limiter.limit(HEAVY_OPERATION_LIMIT)
@handle_api_errors
async def create_card(
    request: Request,
    data: CreateCardRequest,
    user: dict = Depends(require_panel_access),
    factory: UseCaseFactory = Depends(get_readonly_use_case_factory),
):
    """Создать открытку."""
    logger.info(
        f"[API] Create card request: birthday_id={data.birthday_id}, "
        f"greeting_length={len(data.greeting_text)}, has_qr={bool(data.qr_url)}, "
        f"user_id={user.get('id', 'unknown')}"
    )
    
    greeting_use_cases = factory.create_greeting_use_cases()
    use_case = greeting_use_cases["create_card"]

    try:
        card_bytes = await use_case.execute(
            birthday_id=data.birthday_id,
            greeting_text=data.greeting_text,
            qr_url=data.qr_url,
        )
        logger.info(
            f"[API] Card created successfully for birthday_id={data.birthday_id}, "
            f"size={len(card_bytes)} bytes"
        )
        from fastapi.responses import Response
        return Response(content=card_bytes, media_type="image/png")
    except BirthdayNotFoundError as e:
        logger.warning(
            f"[API] Birthday not found for card creation: birthday_id={data.birthday_id}, error={e}"
        )
        raise
    except Exception as e:
        logger.error(
            f"[API] Error creating card for birthday_id={data.birthday_id}: {type(e).__name__}: {e}",
            exc_info=True,
        )
        raise


# Diagnostic endpoints
@router.get("/api/panel/diagnostic/birthday/{birthday_id}")
@limiter.limit(READ_LIMIT)
@handle_api_errors
async def check_birthday_exists(
    request: Request,
    birthday_id: int = Path(..., gt=0, description="ID дня рождения"),
    user: dict = Depends(require_panel_access),
    factory: UseCaseFactory = Depends(get_readonly_use_case_factory),
):
    """Проверить существование дня рождения по ID."""
    logger.info(f"[API] Checking birthday existence: birthday_id={birthday_id}")
    
    birthday_repo = factory.birthday_repository
    birthday = await birthday_repo.get_by_id(birthday_id)
    
    if birthday:
        logger.info(
            f"[API] Birthday found: id={birthday.id}, name={birthday.full_name}, "
            f"company={birthday.company}, position={birthday.position}"
        )
        return {
            "exists": True,
            "id": birthday.id,
            "full_name": birthday.full_name,
            "company": birthday.company,
            "position": birthday.position,
            "birth_date": birthday.birth_date.isoformat(),
        }
    else:
        logger.warning(f"[API] Birthday not found: birthday_id={birthday_id}")
        return {
            "exists": False,
            "id": birthday_id,
            "message": f"Birthday with id {birthday_id} not found",
        }


@router.get("/api/panel/diagnostic/openrouter-config")
@limiter.limit(READ_LIMIT)
@handle_api_errors
async def check_openrouter_config(
    request: Request,
    user: dict = Depends(require_panel_access),
    factory: UseCaseFactory = Depends(get_readonly_use_case_factory),
):
    """Проверить конфигурацию OpenRouter (без sensitive данных)."""
    logger.info("[API] Checking OpenRouter configuration")
    
    try:
        openrouter_client = factory.openrouter_client
        config = openrouter_client.config
        
        # Маскируем API ключ для безопасности
        api_key_masked = (
            f"{config.api_key[:8]}...{config.api_key[-4:]}" if len(config.api_key) > 12
            else "***"
        )
        
        logger.info(
            f"[API] OpenRouter config check: base_url={config.base_url}, "
            f"model={config.model}, timeout={config.timeout}s, "
            f"max_retries={config.max_retries}, api_key_present={'yes' if config.api_key else 'no'}"
        )
        
        return {
            "configured": True,
            "base_url": config.base_url,
            "model": config.model,
            "timeout": config.timeout,
            "max_retries": config.max_retries,
            "temperature": config.temperature,
            "max_tokens": config.max_tokens,
            "api_key_masked": api_key_masked,
            "api_key_length": len(config.api_key) if config.api_key else 0,
        }
    except ValueError as e:
        logger.error(f"[API] OpenRouter configuration error: {e}")
        return {
            "configured": False,
            "error": str(e),
        }
    except Exception as e:
        logger.error(f"[API] Unexpected error checking OpenRouter config: {type(e).__name__}: {e}", exc_info=True)
        return {
            "configured": False,
            "error": f"Unexpected error: {type(e).__name__}",
        }


# Тестовые endpoints для проверки PUT/DELETE
@router.put("/api/test/put")
@router.delete("/api/test/delete")
async def test_put_delete(request: Request):
    """Тестовый endpoint для проверки PUT/DELETE."""
    logger.info(f"[TEST] ===== {request.method} /api/test/{request.method.lower()} - ENTRY POINT =====")
    logger.info(f"[TEST] Request method: {request.method}")
    logger.info(f"[TEST] Request path: {request.url.path}")
    logger.info(f"[TEST] Request headers: {dict(request.headers)}")
    logger.info(f"[TEST] Query params: {dict(request.query_params)}")
    
    # Пытаемся прочитать тело запроса, если есть
    try:
        body = await request.body()
        if body:
            logger.info(f"[TEST] Request body length: {len(body)} bytes")
            try:
                body_json = json.loads(body)
                logger.info(f"[TEST] Request body (JSON): {body_json}")
            except Exception as e:
                logger.info(f"[TEST] Request body (raw): {body[:200]}... (JSON parse error: {e})")
        else:
            logger.info(f"[TEST] Request body: empty")
    except Exception as e:
        logger.warning(f"[TEST] Error reading request body: {e}")
    
    logger.info(f"[TEST] ===== {request.method} /api/test/{request.method.lower()} - SUCCESS =====")
    return {
        "status": "ok",
        "method": request.method,
        "path": request.url.path,
        "message": "Request reached server successfully",
        "headers_received": list(request.headers.keys())
    }

# Простые тестовые endpoints без зависимостей
@router.put("/api/test/put-simple")
async def test_put_simple(request: Request):
    """Тестовый endpoint для проверки PUT запросов без зависимостей."""
    logger.info(f"[TEST] ===== PUT /api/test/put-simple - Request received =====")
    logger.info(f"[TEST] Request method: {request.method}")
    logger.info(f"[TEST] Request path: {request.url.path}")
    logger.info(f"[TEST] Request headers: {dict(request.headers)}")
    return {"status": "ok", "method": "PUT", "message": "Request reached server"}

@router.delete("/api/test/delete-simple")
async def test_delete_simple(request: Request):
    """Тестовый endpoint для проверки DELETE запросов без зависимостей."""
    logger.info(f"[TEST] ===== DELETE /api/test/delete-simple - Request received =====")
    logger.info(f"[TEST] Request method: {request.method}")
    logger.info(f"[TEST] Request path: {request.url.path}")
    logger.info(f"[TEST] Request headers: {dict(request.headers)}")
    return {"status": "ok", "method": "DELETE", "message": "Request reached server"}

# Диагностический endpoint для проверки CORS
@router.get("/api/debug/cors")
async def debug_cors(request: Request):
    """Диагностический endpoint для проверки CORS."""
    from src.infrastructure.config.cors import get_allowed_origins
    
    # Используем централизованную функцию для определения allowed_origins
    allowed_origins = get_allowed_origins()
    
    return {
        "origin": request.headers.get("origin"),
        "method": request.method,
        "headers": dict(request.headers),
        "cors_allowed_origins": allowed_origins,
    }
