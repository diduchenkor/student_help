from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


big_dick = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Количество пользователей бота 💪", callback_data='big1')
    ],
    [
        InlineKeyboardButton(text="Скинуть бот другу 🗣 🦖 ", callback_data='big2')
    ],
    [
        InlineKeyboardButton(text="О боте ! 🔥 ", callback_data='big3')
    ]
])

send_bot = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Отправить друг", switch_inline_query=f"\n"
                                                                             f"https://t.me/NATI_help_bot\n"
                                                                             f"Хватить напрягаться з роскладом 😊")
    ]
])