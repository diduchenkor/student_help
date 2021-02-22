import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.knopki import choose_university, choose_fackelti

from aiogram.types import InputFile

from keyboards.inline.new_menu import big_dick, send_bot
from photos import *
from keyboards.inline.inline_botton import firs, thri, second
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        print(err)
    await message.answer(
        "\n".join(
            [
                f"Привіт, {message.from_user.full_name}! 😎",
                f"Підтвердити навчяльний заклад \n"
                f"👇"
            ]
        ), reply_markup=choose_university
    )


@dp.message_handler(text="НАТІ НУБІП 🚜")
async def choose_fekelti(message: types.Message):
    await message.answer((f"Щоб переглянути розклад \n"
                         f"Виберіть факультет"), reply_markup=choose_fackelti)


@dp.message_handler(text="ІНЖЕНЕРІЇ ТА ЕНЕРГЕТИКИ - БМ, БМск, МА 📗")
async def grupa_one(message: types.Message):
    photo = InputFile(path_or_bytesio="photos/1.png")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption=("<b>ІНЖЕНЕРІЇ ТА ЕНЕРГЕТИКИ - БМ, БМск, МА 📗</b>"), reply_markup=firs)


@dp.message_handler(text="ІНЖЕНЕРІЇ ТА ЕНЕРГЕТИКИ - БЕ, БЕск, МЕ 📘")
async def grupa_two(message: types.Message):
    photo = InputFile(path_or_bytesio="photos/2.png")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption=("<b>ІНЖЕНЕРІЇ ТА ЕНЕРГЕТИКИ - БМ, БМск, МА 📗</b>"), reply_markup=second)



@dp.message_handler(text="АГРЕТЕХНОЛОГІЙ ТА ЕКОНОМІКИ  📕")
async def grupa_thri(message: types.Message):
    photo = InputFile(path_or_bytesio="photos/3.png")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption=("<b>ІНЖЕНЕРІЇ ТА ЕНЕРГЕТИКИ - БМ, БМск, МА 📗</b>"), reply_markup=thri)


@dp.message_handler(text="Дополнительно 🚀")
async def new_whole(message: types.Message):
    await message.answer("Дополнительни функції", reply_markup=big_dick)


@dp.callback_query_handler(text_contains="big1")
async def statistic_user(call: types.CallbackQuery):
    count = db.count_users()[0]
    await call.message.answer(f"Привет чувак, да чувак!'\n"
                              f"В цьому боті всі пользователі чувакі!👨‍🎓\n"
                              f"Чому чувак?👨‍🎓\n"
                              f"Еслі ти норм чувак то ти понімаеш чого 😎 \n\n"
                              f"Ботом пользуються: \n"
                              f"<b>{count}</b> - Чуваків")


@dp.callback_query_handler(text_contains="big2")
async def send_friends(call: types.CallbackQuery):
    await call.message.answer("Щоб допомогти другу, жми 👇🏻", reply_markup=send_bot)


@dp.callback_query_handler(text_contains="big3")
async def myself(call: types.CallbackQuery):
    await call.message.answer(f"Набогато краще и удобніше\n"
                              f"Получять розклад в боті\n"
                              f"Цей бот економить ваше время\n"
                              f"\n\n\n"
                              f"Python programming language\n"
                              f"Aiogram construction library\n"
                              f"Creator @mentorsx"
                              )