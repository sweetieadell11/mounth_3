from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)