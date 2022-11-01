from aiogram.utils.keyboard import ReplyKeyboardBuilder


def menu():
    builder = ReplyKeyboardBuilder()

    builder.button(text="1 дія")
    builder.button(text="2 дія")
    builder.button(text="3 дія")
    builder.button(text="4 дія")

    builder.adjust(2)

    return builder.as_markup(resize_keyboard=True)
