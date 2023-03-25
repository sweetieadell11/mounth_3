from config import dp, ADMINS, bot
from aiogram.utils import executor
from handlers import call_back, client, admin, extra, FSMAdminMentor, notification
import logging
from database.bot_db import sql_create

async def on_startup(_):
    await bot.send_message(chat_id=ADMINS[0],
                           text="Bot started!")
    sql_create()

FSMAdminMentor.register_handlers_fsm_anketa(dp)
client.register_handlers_client(dp)
call_back.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
notification.register_handler_notification(dp)

extra.register_handlers_extra(dp)

#надо чтоб меньше нагружалось больше загружалось


if  __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,  skip_updates=True, on_startup=on_startup)