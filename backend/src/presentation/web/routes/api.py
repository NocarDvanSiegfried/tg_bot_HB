import logging
from datetime import date

from fastapi import APIRouter, Body, Depends, Header, HTTPException, Path, Query, Request
from pydantic import BaseModel, Field, field_validator
from slowapi import Limiter
from slowapi.util import get_remote_address
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.factories.use_case_factory import UseCaseFactory
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
    if not x_init_data:
        raise HTTPException(status_code=401, detail="Missing initData")

    # Создаем use-case через фабрику (не требует session)
    factory = UseCaseFactory(session=None)  # Auth use-case не требует БД сессии
    use_case = factory.create_auth_use_case()

    try:
        user_data = await use_case.execute(x_init_data)
        return user_data
    except ValueError as e:
        raise HTTPException(status_code=401, detail="Invalid initData") from e


# Dependency для проверки прав доступа к панели управления
async def require_panel_access(
    user: dict = Depends(verify_telegram_auth),
    factory: UseCaseFactory = Depends(get_readonly_use_case_factory),
) -> dict:
    """
    Dependency для проверки прав доступа к панели управления.

    Проверяет:
    1. Авторизацию через Telegram (verify_telegram_auth)
    2. Наличие прав доступа к панели (check_panel_access)

    Raises:
        HTTPException 401: Если пользователь не авторизован или нет user_id
        HTTPException 403: Если у пользователя нет доступа к панели
    """
    user_id = user.get("id")
    if not user_id:
        raise HTTPException(status_code=401, detail="User ID not found in initData")

    # Проверяем доступ к панели
    use_case = factory.create_panel_access_use_case()
    has_access = await use_case.execute(user_id)

    if not has_access:
        raise HTTPException(
            status_code=403, detail="Access denied. You don't have permission to access the panel."
        )

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
    user: dict = Depends(require_panel_access),
    factory: UseCaseFactory = Depends(get_use_case_factory),
):
    """Обновить ДР."""
    use_cases = factory.create_birthday_use_cases()
    use_case = use_cases["update"]

    birthday = await use_case.execute(
        birthday_id=birthday_id,
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


@router.delete("/api/panel/birthdays/{birthday_id}")
@limiter.limit(WRITE_LIMIT)
@handle_api_errors
async def delete_birthday(
    request: Request,
    birthday_id: int = Path(..., gt=0, description="ID дня рождения"),
    session: AsyncSession = Depends(get_db_session),
    user: dict = Depends(require_panel_access),
    factory: UseCaseFactory = Depends(get_use_case_factory),
):
    """Удалить ДР."""
    use_cases = factory.create_birthday_use_cases()
    use_case = use_cases["delete"]

    await use_case.execute(birthday_id)
    await session.commit()
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
    greeting_use_cases = factory.create_greeting_use_cases()
    use_case = greeting_use_cases["generate"]

    greeting_text = await use_case.execute(
        birthday_id=data.birthday_id,
        style=data.style,
        length=data.length,
        theme=data.theme,
    )
    return {"greeting": greeting_text}


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
    greeting_use_cases = factory.create_greeting_use_cases()
    use_case = greeting_use_cases["create_card"]

    card_bytes = await use_case.execute(
        birthday_id=data.birthday_id,
        greeting_text=data.greeting_text,
        qr_url=data.qr_url,
    )
    from fastapi.responses import Response

    return Response(content=card_bytes, media_type="image/png")
