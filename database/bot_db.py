# SQL - Structured Query Language
# СУБД - Система Управления Базой Данных

import random
import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS anketa "
               "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "id_mentor TEXT, "
               "name VARCHAR (100), "
               "age INTEGER, "
               "direction VARCHAR (50), "
               "group_ment VARCHAR (20)) ")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO anketa VALUES (null, ?, ?, ?, ?, ?)",
                       tuple(data.values()))
        db.commit()


async def sql_command_random():
    result = cursor.execute("SELECT * FROM anketa").fetchall()
    random_user = random.choice(result)
    return random_user


async def sql_command_all():
    return cursor.execute("SELECT * FROM anketa").fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM anketa WHERE id = ?", (id,))
    db.commit()


async def sql_command_all_id():
    return cursor.execute("SELECT id FROM anketa").fetchall()