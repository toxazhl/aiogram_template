from aiogram.utils.keyboard import ReplyKeyboardBuilder


def send_phone():
    builder = ReplyKeyboardBuilder()
    builder.button(text="☎️ Відправити контакт", request_contact=True)
    return builder.as_markup(resize_keyboard=True)
