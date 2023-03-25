from config import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types, Dispatcher


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton("NEXT", callback_data="button_2")
    markup.add(button_2)

    question = "Сколько яблок на березе??"
    answer = [
        "12",
        "3",
        "БЕССКОНЕЧНОСТЬ",
        "0",
        "-10",
        "999",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=30,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_3 = InlineKeyboardButton("NEXT", callback_data="button_3")
    markup.add(button_3)
    question = "Вам нравится программирование?"
    answer = [
        "Нет",
        "Да",
        "Не определилась!"
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=30,
        reply_markup=markup
    )


async def quiz_4(call: types.CallbackQuery):
    question = "Какой язык программирования вам нравится?"
    answer = [
        "python",
        "Java",
        "Java-Script",
        "Swift",
        "Kotlin",
        "PHP",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Стыдно не знать",
        open_period=30,
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text = 'button_1')
    dp.register_callback_query_handler(quiz_3, text = 'button_2')
    dp.register_callback_query_handler(quiz_4, text = 'button_3')

