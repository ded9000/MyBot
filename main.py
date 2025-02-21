import asyncio

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder 
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from cred import TOKEN

TWO_SPACE_NUMBERS = "введи 2 числа через пробел"

dp = Dispatcher()


class Calc(StatesGroup):
    input_numbers = State()
    check_numbers = State()
    calculate = State()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Привет! Как дела?")


@dp.message(Command("calc"))
async def command_calc_handler(message: Message) -> None:
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="умножение", callback_data="multiply_operation"))
    builder.add(InlineKeyboardButton(text="деление", callback_data="division_operation"))
    builder.add(InlineKeyboardButton(text="сложение", callback_data="addition_operation"))
    builder.add(InlineKeyboardButton(text="вычитание", callback_data="deduct_operation"))
    builder.adjust(2)
    await message.answer("Выбери операцию:", reply_markup=builder.as_markup())


@dp.callback_query(F.data=="multiply_operation")
async def multiply_operation(callback: CallbackQuery, state: FSMContext): 
    await state.set_state(Calc.input_numbers)
    await callback.message.answer(TWO_SPACE_NUMBERS)


@dp.callback_query(F.data=="division_operation")
async def divsion_operation(callback: CallbackQuery, state: FSMContext): 
    await state.set_state(Calc.input_numbers)
    await callback.message.answer(TWO_SPACE_NUMBERS)


@dp.callback_query(F.data=="addition_operation")
async def addition_operation(callback: CallbackQuery, state: FSMContext): 
    await state.set_state(Calc.input_numbers)
    await callback.message.answer(TWO_SPACE_NUMBERS)


@dp.callback_query(F.data=="deduct_operation")
async def deduct_operation(callback: CallbackQuery, state: FSMContext): 
    await state.set_state(Calc.input_numbers)
    await callback.message.answer(TWO_SPACE_NUMBERS)


@dp.message(Calc.input_numbers)
async def check_numbers(message: Message, state: FSMContext):
    await message.reply("вы ввели числа")


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

