import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.factories.use_case_factory import UseCaseFactory
from src.presentation.telegram.keyboards import get_responsible_management_keyboard

logger = logging.getLogger(__name__)

router = Router()


class ResponsibleForm(StatesGroup):
    waiting_for_full_name = State()
    waiting_for_company = State()
    waiting_for_position = State()


@router.callback_query(lambda c: c.data == "responsible_add")
async def responsible_add_start(callback: CallbackQuery, state: FSMContext):
    """Начать добавление ответственного."""
    await state.set_state(ResponsibleForm.waiting_for_full_name)
    await callback.message.answer("Введите ФИО:")
    await callback.answer()


@router.message(ResponsibleForm.waiting_for_full_name)
async def process_full_name(message: Message, state: FSMContext):
    """Обработать ФИО."""
    await state.update_data(full_name=message.text)
    await state.set_state(ResponsibleForm.waiting_for_company)
    await message.answer("Введите компанию:")


@router.message(ResponsibleForm.waiting_for_company)
async def process_company(message: Message, state: FSMContext):
    """Обработать компанию."""
    await state.update_data(company=message.text)
    await state.set_state(ResponsibleForm.waiting_for_position)
    await message.answer("Введите должность:")


@router.message(ResponsibleForm.waiting_for_position)
async def process_position(message: Message, state: FSMContext, session: AsyncSession):
    """Обработать должность и создать ответственного."""
    data = await state.get_data()

    factory = UseCaseFactory(session)
    responsible_use_cases = factory.create_responsible_use_cases()
    use_case = responsible_use_cases["create"]

    try:
        responsible = await use_case.execute(
            full_name=data["full_name"],
            company=data["company"],
            position=message.text,
        )
        await session.commit()
        logger.info(f"Ответственный создан: ID={responsible.id}, ФИО={responsible.full_name}")
        await message.answer(f"Ответственный добавлен! ID: {responsible.id}")
    except Exception as e:
        await session.rollback()
        logger.error(f"Ошибка при создании ответственного: {type(e).__name__}: {e}")
        await message.answer(f"Ошибка: {str(e)}")

    await state.clear()
