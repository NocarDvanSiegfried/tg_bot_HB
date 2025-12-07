from datetime import date, datetime
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.factories.use_case_factory import UseCaseFactory
from src.presentation.telegram.keyboards import get_birthday_management_keyboard

router = Router()


class BirthdayForm(StatesGroup):
    waiting_for_full_name = State()
    waiting_for_company = State()
    waiting_for_position = State()
    waiting_for_birth_date = State()
    waiting_for_comment = State()


@router.callback_query(lambda c: c.data == "panel_birthdays")
async def panel_birthdays_callback(callback: CallbackQuery):
    """Меню управления ДР."""
    await callback.message.edit_text(
        "Управление днями рождения",
        reply_markup=get_birthday_management_keyboard(),
    )
    await callback.answer()


@router.callback_query(lambda c: c.data == "birthday_add")
async def birthday_add_start(callback: CallbackQuery, state: FSMContext):
    """Начать добавление ДР."""
    await state.set_state(BirthdayForm.waiting_for_full_name)
    await callback.message.answer("Введите ФИО:")
    await callback.answer()


@router.message(BirthdayForm.waiting_for_full_name)
async def process_full_name(message: Message, state: FSMContext):
    """Обработать ФИО."""
    await state.update_data(full_name=message.text)
    await state.set_state(BirthdayForm.waiting_for_company)
    await message.answer("Введите компанию:")


@router.message(BirthdayForm.waiting_for_company)
async def process_company(message: Message, state: FSMContext):
    """Обработать компанию."""
    await state.update_data(company=message.text)
    await state.set_state(BirthdayForm.waiting_for_position)
    await message.answer("Введите должность:")


@router.message(BirthdayForm.waiting_for_position)
async def process_position(message: Message, state: FSMContext):
    """Обработать должность."""
    await state.update_data(position=message.text)
    await state.set_state(BirthdayForm.waiting_for_birth_date)
    await message.answer("Введите дату рождения (формат: ДД.ММ.ГГГГ):")


@router.message(BirthdayForm.waiting_for_birth_date)
async def process_birth_date(message: Message, state: FSMContext, session: AsyncSession):
    """Обработать дату рождения."""
    try:
        birth_date = datetime.strptime(message.text, "%d.%m.%Y").date()
    except ValueError:
        await message.answer("Неверный формат даты. Используйте ДД.ММ.ГГГГ")
        return

    await state.update_data(birth_date=birth_date)
    await state.set_state(BirthdayForm.waiting_for_comment)
    await message.answer("Введите комментарий (или отправьте '-' для пропуска):")


@router.message(BirthdayForm.waiting_for_comment)
async def process_comment(message: Message, state: FSMContext, session: AsyncSession):
    """Обработать комментарий и создать ДР."""
    data = await state.get_data()
    comment = message.text if message.text != "-" else None

    factory = UseCaseFactory(session)
    use_cases = factory.create_birthday_use_cases()
    use_case = use_cases["create"]

    try:
        birthday = await use_case.execute(
            full_name=data["full_name"],
            company=data["company"],
            position=data["position"],
            birth_date=data["birth_date"],
            comment=comment,
        )
        await session.commit()
        await message.answer(f"День рождения добавлен! ID: {birthday.id}")
    except Exception as e:
        await session.rollback()
        await message.answer(f"Ошибка: {str(e)}")

    await state.clear()

