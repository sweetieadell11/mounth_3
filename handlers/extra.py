from config import bot
from aiogram import types, Dispatcher
from random import choice

async def echo(message: types.Message):
    if message.text == "python":
        await message.answer("I love it!")
    elif message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text) ** 2)
    elif message.text == "!pin":
        try:
            await bot.pin_chat_message(message.chat.id,
                                       message.reply_to_message.message_id)
        except AttributeError:
            await bot.send_message(message.chat.id, 'Сообщение должно быть ответом!')

    elif message.text == 'game':
        list1 = ['⚽️', '🏀', '🎲', '🎰', '🎯', '🎳']
        emoji = choice(list1)
        await message.answer(emoji)
    else:
        await bot.send_message(message.from_user.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)

