from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

choose_university = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="НАТІ НУБІП 🚜")
        ],
    ],
    resize_keyboard=True, one_time_keyboard=False
)

choose_fackelti = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ІНЖЕНЕРІЇ ТА ЕНЕРГЕТИКИ - БМ, БМск, МА 📗"),
        ],
        [
            KeyboardButton(text="ІНЖЕНЕРІЇ ТА ЕНЕРГЕТИКИ - БЕ, БЕск, МЕ 📘"),

        ],
        [
            KeyboardButton(text="АГРЕТЕХНОЛОГІЙ ТА ЕКОНОМІКИ  📕"),

        ],
        [
            KeyboardButton(text="Дополнительно 🚀"),

        ],


    ],
    resize_keyboard=True, one_time_keyboard=False
)

