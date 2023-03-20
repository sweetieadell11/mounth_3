from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from handlers.config import dp
from decouple import config
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from handlers.client import register_handlers_client
from handlers.call_back import register_handlers_callback
from handlers.extra import register_handlers_extra
register_handlers_callback(dp)
register_handlers_client(dp)
register_handlers_extra(dp)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)