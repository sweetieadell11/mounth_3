from handlers.config import dp, bot
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
from aiogram import Dispatcher

async def start_command(message: types.Message):
    await message.answer("Hello world!")


async def help_command(message: types.Message):
    await message.answer("Сам разбирайся!")


async def mem_command(message: types.Message):
    photos = (
        'media/img.png',
        'media/img_1.png',
    )
    photo = open(random.choice(photos), 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "By whom invented Python?"
    answer = [
        "Harry Potter",
        "Putin",
        "Guido Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=30,
        reply_markup=markup
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(mem_command, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
