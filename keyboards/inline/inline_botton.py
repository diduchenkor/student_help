from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from parsing.second.generate_link import link0, link1, link2

first = link0[0]
second = link1[0]
three = link2[0]


firs = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Силка на розсклад", url=first)
    ]
])

second = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Силка на розсклад", url=second)
    ]
])

thri = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Силка на розсклад", url=three)
    ]
])