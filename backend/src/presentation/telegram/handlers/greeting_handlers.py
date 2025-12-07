from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.factories.use_case_factory import UseCaseFactory
from src.presentation.telegram.keyboards import get_greeting_options_keyboard

router = Router()


class GreetingForm(StatesGroup):
    waiting_for_birthday_id = State()
    waiting_for_text = State()
    waiting_for_style = State()
    waiting_for_length = State()
    waiting_for_theme = State()
    waiting_for_qr_url = State()


@router.callback_query(lambda c: c.data == "panel_greetings")
async def panel_greetings_callback(callback: CallbackQuery):
    """Меню генерации поздравлений."""
    await callback.message.edit_text(
        "Генерация поздравлений и открыток",
        reply_markup=get_greeting_options_keyboard(),
    )
    await callback.answer()


@router.callback_query(lambda c: c.data == "greeting_manual")
async def greeting_manual_start(callback: CallbackQuery, state: FSMContext):
    """Начать ручной ввод текста."""
    await state.set_state(GreetingForm.waiting_for_birthday_id)
    await callback.message.answer("Введите ID сотрудника (из поиска или календаря):")
    await callback.answer()


@router.callback_query(lambda c: c.data == "greeting_generate")
async def greeting_generate_start(callback: CallbackQuery, state: FSMContext):
    """Начать генерацию через DeepSeek."""
    await state.set_state(GreetingForm.waiting_for_birthday_id)
    await callback.message.answer("Введите ID сотрудника:")
    await callback.answer()


@router.message(GreetingForm.waiting_for_birthday_id)
async def process_birthday_id(message: Message, state: FSMContext):
    """Обработать ID сотрудника."""
    try:
        birthday_id = int(message.text)
        await state.update_data(birthday_id=birthday_id)
        
        # Определяем, какой путь выбран
        current_state = await state.get_state()
        if current_state == GreetingForm.waiting_for_birthday_id:
            # Проверяем, какой callback был вызван
            # Для упрощения, если это генерация, переходим к выбору стиля
            await state.set_state(GreetingForm.waiting_for_style)
            await message.answer("Выберите стиль (formal/friendly/humorous/warm):")
    except ValueError:
        await message.answer("Неверный формат ID. Введите число.")


@router.message(GreetingForm.waiting_for_style)
async def process_style(message: Message, state: FSMContext):
    """Обработать стиль."""
    await state.update_data(style=message.text)
    await state.set_state(GreetingForm.waiting_for_length)
    await message.answer("Выберите длину (short/medium/long):")


@router.message(GreetingForm.waiting_for_length)
async def process_length(message: Message, state: FSMContext):
    """Обработать длину."""
    await state.update_data(length=message.text)
    await state.set_state(GreetingForm.waiting_for_theme)
    await message.answer("Введите тему (или '-' для пропуска):")


@router.message(GreetingForm.waiting_for_theme)
async def process_theme(message: Message, state: FSMContext, session: AsyncSession):
    """Обработать тему и сгенерировать поздравление."""
    data = await state.get_data()
    theme = message.text if message.text != "-" else None

    factory = UseCaseFactory(session)
    greeting_use_cases = factory.create_greeting_use_cases()
    use_case = greeting_use_cases["generate"]

    try:
        greeting_text = await use_case.execute(
            birthday_id=data["birthday_id"],
            style=data["style"],
            length=data["length"],
            theme=theme,
        )
        await message.answer(f"Сгенерированное поздравление:\n\n{greeting_text}")
    except Exception as e:
        await message.answer(f"Ошибка: {str(e)}")

    await state.clear()


@router.callback_query(lambda c: c.data == "greeting_card")
async def greeting_card_start(callback: CallbackQuery, state: FSMContext):
    """Начать создание открытки."""
    await state.set_state(GreetingForm.waiting_for_birthday_id)
    await callback.message.answer("Введите ID сотрудника:")
    await callback.answer()


@router.message(GreetingForm.waiting_for_text)
async def process_text(message: Message, state: FSMContext):
    """Обработать текст для открытки."""
    await state.update_data(greeting_text=message.text)
    await state.set_state(GreetingForm.waiting_for_qr_url)
    await message.answer("Введите URL для QR-кода (или '-' для пропуска):")


@router.message(GreetingForm.waiting_for_qr_url)
async def process_qr_url(message: Message, state: FSMContext, session: AsyncSession):
    """Обработать QR URL и создать открытку."""
    data = await state.get_data()
    qr_url = message.text if message.text != "-" else None

    factory = UseCaseFactory(session)
    greeting_use_cases = factory.create_greeting_use_cases()
    use_case = greeting_use_cases["create_card"]

    try:
        card_bytes = await use_case.execute(
            birthday_id=data["birthday_id"],
            greeting_text=data["greeting_text"],
            qr_url=qr_url,
        )
        
        from aiogram.types import BufferedInputFile
        await message.answer_photo(
            BufferedInputFile(card_bytes, filename="card.png"),
            caption="Открытка создана!",
        )
    except Exception as e:
        await message.answer(f"Ошибка: {str(e)}")

    await state.clear()

