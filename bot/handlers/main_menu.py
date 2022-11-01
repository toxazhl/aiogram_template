import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.methods import SendMessage
from aiogram.types import Message

from bot import keyboards as kb


logger = logging.getLogger(__name__)

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext) -> SendMessage:
    await state.clear()
    return message.answer(
        "Ви в головному меню ⚡\n"
        "Оберіть дію:",
        reply_markup=kb.main_menu.menu()
    )
