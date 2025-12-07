import logging
import os
from datetime import date
from typing import List, Optional, Dict

from fastapi import APIRouter, Depends, HTTPException, Header
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.factories.use_case_factory import UseCaseFactory
from src.domain.exceptions.not_found import BirthdayNotFoundError, ResponsibleNotFoundError
from src.domain.exceptions.validation import ValidationError
from src.infrastructure.database.database_factory import get_database

logger = logging.getLogger(__name__)

router = APIRouter()


# DTOs
class BirthdayCreate(BaseModel):
    full_name: str
    company: str
    position: str
    birth_date: date
    comment: Optional[str] = None


class BirthdayUpdate(BaseModel):
    full_name: Optional[str] = None
    company: Optional[str] = None
    position: Optional[str] = None
    birth_date: Optional[date] = None
    comment: Optional[str] = None


class ResponsibleCreate(BaseModel):
    full_name: str
    company: str
    position: str


class ResponsibleUpdate(BaseModel):
    full_name: Optional[str] = None
    company: Optional[str] = None
    position: Optional[str] = None


class AssignResponsibleRequest(BaseModel):
    responsible_id: int
    date: date


class GenerateGreetingRequest(BaseModel):
    birthday_id: int
    style: str
    length: str
    theme: Optional[str] = None


class CreateCardRequest(BaseModel):
    birthday_id: int
    greeting_text: str
    qr_url: Optional[str] = None


class VerifyInitDataRequest(BaseModel):
    init_data: str


# Dependency для получения сессии БД
async def get_db_session() -> AsyncSession:
    db = get_database()
    async for session in db.get_session():
        yield session


# Dependency для получения фабрики use-cases
async def get_use_case_factory(
    session: AsyncSession = Depends(get_db_session)
) -> UseCaseFactory:
    """Dependency для получения фабрики use-cases."""
    return UseCaseFactory(session)


# Dependency для проверки авторизации через Telegram
async def verify_telegram_auth(
    x_init_data: Optional[str] = Header(None, alias="X-Init-Data")
) -> Dict:
    """Dependency для проверки авторизации через Telegram WebApp."""
    if not x_init_data:
        raise HTTPException(status_code=401, detail="Missing initData")
    
    # Создаем use-case через фабрику (не требует session)
    factory = UseCaseFactory(session=None)  # Auth use-case не требует БД сессии
    use_case = factory.create_auth_use_case()
    
    try:
        user_data = await use_case.execute(x_init_data)
        return user_data
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid initData")


# Auth endpoints
@router.post("/api/auth/verify")
async def verify_init_data(data: VerifyInitDataRequest):
    """Верифицировать initData от Telegram WebApp."""
    # Создаем use-case через фабрику (не требует session)
    factory = UseCaseFactory(session=None)  # Auth use-case не требует БД сессии
    use_case = factory.create_auth_use_case()
    
    try:
        user_data = await use_case.execute(data.init_data)
        return {
            "valid": True,
            "user": user_data,
        }
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid initData")


# Public endpoints
@router.get("/api/calendar/{date_str}")
async def get_calendar(
    date_str: str,
    factory: UseCaseFactory = Depends(get_use_case_factory)
):
    """Получить данные календаря на дату."""
    try:
        check_date = date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format")

    use_case = factory.create_calendar_use_case()
    return await use_case.execute(check_date)


# Panel endpoints
@router.get("/api/panel/check-access")
async def check_panel_access(
    user: Dict = Depends(verify_telegram_auth),
    factory: UseCaseFactory = Depends(get_use_case_factory),
):
    """Проверить доступ пользователя к панели управления."""
    user_id = user.get("id")
    if not user_id:
        raise HTTPException(status_code=401, detail="User ID not found in initData")
    
    use_case = factory.create_panel_access_use_case()
    
    has_access = await use_case.execute(user_id)
    return {"has_access": has_access}


@router.get("/api/panel/birthdays")
async def list_birthdays(factory: UseCaseFactory = Depends(get_use_case_factory)):
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
async def create_birthday(
    data: BirthdayCreate,
    factory: UseCaseFactory = Depends(get_use_case_factory),
    session: AsyncSession = Depends(get_db_session),
):
    """Создать ДР."""
    use_cases = factory.create_birthday_use_cases()
    use_case = use_cases["create"]

    try:
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
    except ValidationError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        logger.error("Unexpected error in create_birthday", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put("/api/panel/birthdays/{birthday_id}")
async def update_birthday(
    birthday_id: int,
    data: BirthdayUpdate,
    factory: UseCaseFactory = Depends(get_use_case_factory),
    session: AsyncSession = Depends(get_db_session),
):
    """Обновить ДР."""
    use_cases = factory.create_birthday_use_cases()
    use_case = use_cases["update"]

    try:
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
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/api/panel/birthdays/{birthday_id}")
async def delete_birthday(
    birthday_id: int,
    factory: UseCaseFactory = Depends(get_use_case_factory),
    session: AsyncSession = Depends(get_db_session),
):
    """Удалить ДР."""
    use_cases = factory.create_birthday_use_cases()
    use_case = use_cases["delete"]

    try:
        await use_case.execute(birthday_id)
        await session.commit()
        return {"status": "deleted"}
    except BirthdayNotFoundError as e:
        await session.rollback()
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        await session.rollback()
        logger.error("Unexpected error in delete_birthday", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/api/panel/responsible")
async def list_responsible(factory: UseCaseFactory = Depends(get_use_case_factory)):
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
async def create_responsible(
    data: ResponsibleCreate,
    factory: UseCaseFactory = Depends(get_use_case_factory),
    session: AsyncSession = Depends(get_db_session),
):
    """Создать ответственного."""
    responsible_use_cases = factory.create_responsible_use_cases()
    use_case = responsible_use_cases["create"]

    try:
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
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/api/panel/responsible/{responsible_id}")
async def update_responsible(
    responsible_id: int,
    data: ResponsibleUpdate,
    factory: UseCaseFactory = Depends(get_use_case_factory),
    session: AsyncSession = Depends(get_db_session),
):
    """Обновить ответственного."""
    responsible_use_cases = factory.create_responsible_use_cases()
    use_case = responsible_use_cases["update"]

    try:
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
    except ResponsibleNotFoundError as e:
        await session.rollback()
        raise HTTPException(status_code=404, detail=str(e))
    except ValidationError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        logger.error("Unexpected error in update_responsible", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/api/panel/responsible/{responsible_id}")
async def delete_responsible(
    responsible_id: int,
    factory: UseCaseFactory = Depends(get_use_case_factory),
    session: AsyncSession = Depends(get_db_session),
):
    """Удалить ответственного."""
    responsible_use_cases = factory.create_responsible_use_cases()
    use_case = responsible_use_cases["delete"]

    try:
        await use_case.execute(responsible_id)
        await session.commit()
        return {"status": "deleted"}
    except ResponsibleNotFoundError as e:
        await session.rollback()
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        await session.rollback()
        logger.error("Unexpected error in delete_responsible", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/api/panel/assign-responsible")
async def assign_responsible(
    data: AssignResponsibleRequest,
    factory: UseCaseFactory = Depends(get_use_case_factory),
    session: AsyncSession = Depends(get_db_session),
):
    """Назначить ответственного на дату."""
    responsible_use_cases = factory.create_responsible_use_cases()
    use_case = responsible_use_cases["assign_to_date"]

    try:
        await use_case.execute(data.responsible_id, data.date)
        await session.commit()
        return {"status": "assigned"}
    except (BirthdayNotFoundError, ResponsibleNotFoundError) as e:
        await session.rollback()
        raise HTTPException(status_code=404, detail=str(e))
    except ValidationError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        logger.error("Unexpected error in assign_responsible", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/api/panel/search")
async def search_people(
    q: str,
    factory: UseCaseFactory = Depends(get_use_case_factory),
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
async def generate_greeting(
    data: GenerateGreetingRequest,
    factory: UseCaseFactory = Depends(get_use_case_factory),
):
    """Сгенерировать поздравление."""
    greeting_use_cases = factory.create_greeting_use_cases()
    use_case = greeting_use_cases["generate"]

    try:
        greeting_text = await use_case.execute(
            birthday_id=data.birthday_id,
            style=data.style,
            length=data.length,
            theme=data.theme,
        )
        return {"greeting": greeting_text}
    except BirthdayNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("Unexpected error in generate_greeting", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/api/panel/create-card")
async def create_card(
    data: CreateCardRequest,
    factory: UseCaseFactory = Depends(get_use_case_factory),
):
    """Создать открытку."""
    greeting_use_cases = factory.create_greeting_use_cases()
    use_case = greeting_use_cases["create_card"]

    try:
        card_bytes = await use_case.execute(
            birthday_id=data.birthday_id,
            greeting_text=data.greeting_text,
            qr_url=data.qr_url,
        )
        from fastapi.responses import Response
        return Response(content=card_bytes, media_type="image/png")
    except BirthdayNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error("Unexpected error in create_card", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")

