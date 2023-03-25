import datetime

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database.bot_db import sql_command_all_id
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger
from config import bot, ADMINS



async def hpd(bot: Bot):
    await bot.send_message(ADMINS[0], 'happy birthday')



async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone='Asia/Bishkek')
    scheduler.add_job(
        hpd,
        trigger=DateTrigger(
            run_date=datetime.datetime(year=2023, month=12, day=19, hour=00, minute=00)
        ),
        kwargs={"bot": bot},
    )

    scheduler.start()