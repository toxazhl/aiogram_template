import logging
import re

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.methods import SendMessage
from aiogram.types import Message

from bot import keyboards as kb
from bot.core.db.models import User
from bot.core.db.repository.repo import Repo
from bot.filters.user import NewUserFilter, EmptyPhoneFilter
from bot.misc.states import RegStates


logger = logging.getLogger(__name__)

router = Router()


@router.message((F.text) | (F.contact), RegStates.phone_number)
async def phone_number(
    message: Message, state: FSMContext, repo: Repo, user: User
) -> SendMessage:
    phone = message.contact.phone_number if message.contact else message.text

    phone = re.sub(r"\D", "", phone)

    if re.match(r"^380[0-9]{9}$", phone):
        phone = f"+{phone}"

    if not re.match(r"^\+[1-9][0-9]{7,14}$", phone):
        return message.answer(
            "Номер телефону має бути в форматі +380XXXXXXXXX"
        )

    user.phone_number = phone

    await repo.commit(user)
    await state.clear()

    return message.answer(
        "Ви в головному меню ⚡\n"
        "Оберіть дію:",
        reply_markup=kb.main_menu.menu()
    )


@router.message(NewUserFilter())
async def new_user_handler(
    message: Message, state: FSMContext, repo: Repo
) -> SendMessage:
    await repo.user.add(id=message.from_user.id)
    return await empty_phone_handler(message, state)


@router.message(EmptyPhoneFilter())
async def empty_phone_handler(
    message: Message, state: FSMContext
) -> SendMessage:
    await state.set_state(RegStates.phone_number)
    return message.answer(
        "Для початку роботи введіть ваш номер телефону або відправте його за "
        "допомогою кнопки",
        reply_markup=kb.reg.send_phone()
    )