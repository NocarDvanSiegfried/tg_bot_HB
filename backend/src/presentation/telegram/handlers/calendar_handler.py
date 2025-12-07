from datetime import date, datetime
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.factories.use_case_factory import UseCaseFactory
from src.presentation.telegram.keyboards import get_calendar_navigation_keyboard

router = Router()


@router.message(lambda m: m.text == "📅 Календарь")
async def show_calendar(message: Message):
    """Показать календарь."""
    today = date.today()
    await message.answer(
        f"Календарь на {today.year}-{today.month:02d}",
        reply_markup=get_calendar_navigation_keyboard(today.year, today.month),
    )


@router.callback_query(lambda c: c.data and c.data.startswith("cal_"))
async def calendar_callback(callback: CallbackQuery, session: AsyncSession):
    """Обработка навигации по календарю."""
    data = callback.data
    
    if data == "cal_info":
        await callback.answer("Информация о календаре")
        return

    today = date.today()
    year = today.year
    month = today.month

    if data.startswith("cal_prev_"):
        parts = data.split("_")
        year = int(parts[2])
        month = int(parts[3])
        month -= 1
        if month < 1:
            month = 12
            year -= 1
    elif data.startswith("cal_next_"):
        parts = data.split("_")
        year = int(parts[2])
        month = int(parts[3])
        month += 1
        if month > 12:
            month = 1
            year += 1

    await callback.message.edit_text(
        f"Календарь на {year}-{month:02d}",
        reply_markup=get_calendar_navigation_keyboard(year, month),
    )
    await callback.answer()


@router.callback_query(lambda c: c.data and c.data.startswith("date_"))
async def date_selected_callback(callback: CallbackQuery, session: AsyncSession):
    """Обработка выбора даты в календаре."""
    # Парсим дату из callback_data (формат: date_YYYY-MM-DD)
    date_str = callback.data.replace("date_", "")
    selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()

    # Получаем данные календаря
    factory = UseCaseFactory(session)
    use_case = factory.create_calendar_use_case()
    calendar_data = await use_case.execute(selected_date)

    # Формируем ответ
    text = f"📅 {selected_date.strftime('%d.%m.%Y')}\n\n"

    # Дни рождения
    if calendar_data["birthdays"]:
        text += "🎂 Дни рождения:\n"
        for bd in calendar_data["birthdays"]:
            text += f"• {bd['full_name']}\n"
            text += f"  {bd['company']}, {bd['position']}\n"
            text += f"  Исполняется {bd['age']} лет\n"
            if bd["comment"]:
                text += f"  Комментарий: {bd['comment']}\n"
            text += "\n"
    else:
        text += "🎂 Дни рождения: нет\n\n"

    # Праздники
    if calendar_data["holidays"]:
        text += "🎉 Профессиональные праздники:\n"
        for holiday in calendar_data["holidays"]:
            text += f"• {holiday['name']}\n"
            if holiday["description"]:
                text += f"  {holiday['description']}\n"
            text += "\n"
    else:
        text += "🎉 Профессиональные праздники: нет\n\n"

    # Ответственный
    if calendar_data["responsible"]:
        resp = calendar_data["responsible"]
        text += f"👤 Ответственное лицо:\n"
        text += f"• {resp['full_name']}\n"
        text += f"  {resp['company']}, {resp['position']}\n"
    else:
        text += "👤 Ответственное лицо: не назначено\n"

    await callback.message.answer(text)
    await callback.answer()

