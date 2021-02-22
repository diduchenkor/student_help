from asyncio import sleep
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from data.config import ADMINS

from parsing.first.pars import parser
from parsing.second.generate_link import nova
from loader import dp, bot, db


class Mailing(StatesGroup):
    Text = State()
    Confirm = State()


@dp.message_handler(user_id=ADMINS, commands=['update'])
async def update_task(message: types.Message):
    markup = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [InlineKeyboardButton(text='Загрузити нові силкі', callback_data="run")]
        ]
    )
    await message.answer("Для парса ссилок з сайта нажмите кнопку", reply_markup=markup)


@dp.callback_query_handler(user_id=ADMINS, text_contains="run")
async def udate_run(call: types.CallbackQuery):
    parser()
    markup = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [InlineKeyboardButton(text='ОНОВИТИ СИЛКІ', callback_data="piu")]
        ]
    )
    await call.message.answer("Силкі з web NATI завантажені успішно!\n"
                              "Для того щоб обовити їх на кнопках", reply_markup=markup)


@dp.callback_query_handler(user_id=ADMINS, text_contains="piu")
async def update_silki(call: types.CallbackQuery):
    nova()
    await call.message.answer("Все хорошо, провірьте силкі !")


# MAIL


@dp.message_handler(user_id=ADMINS, commands=['tell'])
async def mailing(message: types.Message):
    await message.answer("Напиши текст розсилки")
    await Mailing.Text.set()


@dp.message_handler(user_id=ADMINS, state=Mailing.Text)
async def mailing_puk(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Підтвердити", callback_data='pizda'),
            ],
        ],
        resize_keyboard=True
    )

    await message.answer(("Проверте текст перед отправкой\n"
                          "TEXT: \n\n\""
                          "{text}").format(text=text), reply_markup=markup)

    await Mailing.Confirm.set()


@dp.callback_query_handler(user_id=ADMINS, state=Mailing.Confirm)
async def confirm_mail(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get("text")

    users = db.tell_all()
    for i in users:
        try:
            await bot.send_message(chat_id=i[users.id], text=text)
            await sleep(0.5)
        except Exception:
            pass
    await state.reset_state()
    await call.message.answer(("Сообщеніе успішно розослане.\n"
                          "{text}").format(text=text))
