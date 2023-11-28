from pyrogram import Client, filters
from models import users_check, today_check, init_models
from pyrogram.types import Message
from dotenv import load_dotenv
from loguru import logger
import asyncio
import sys
import os

logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO") # Логирование
load_dotenv() # Доступ к переменным окружения
app = Client(
    "my_bot", api_id=os.getenv("API_ID"), api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
) # Создание клиента


@logger.catch
@app.on_message(filters.command("start"))
async def start_messages(client, message: Message):
    """

    """
    await users_check(
        id_tg=message.from_user.id, first_name=message.from_user.first_name, last_name=message.from_user.last_name
    )
    await asyncio.sleep(600) # 10 минут
    await app.send_message(message.chat.id, f'Добрый день!')
    logger.info(f'Успешное отправление: Добрый день!')

    await asyncio.sleep(4800) # 90 минут с начала команды /start
    await app.send_message(message.chat.id, f'Подготовила для вас материал!')
    logger.info(f'Успешное отправление: Подготовила для вас материал!')

    await app.send_photo(
        message.chat.id,
        'https://img.freepik.com/premium-photo/refreshing-nature-background-with-bokeh_948265-2082.jpg?w=1380'
    )
    logger.info(f'Успешное отправление фото пользователю!')

    await asyncio.sleep(1800)  # 120 минут с начала команды /start


@logger.catch
@app.on_message(filters.command("users_today"))
async def users_today(client, message: Message):
    """
    При отправки команды /users_today,
    приходит сообщение в избранное о новых пользователях за сегодня.
    day_users - запрос из БД количество новых пользователей за сегодня
    """
    async with Client("my_account", api_id=os.getenv("API_ID"), api_hash=os.getenv("API_HASH")) as me:
        day_users = await today_check()
        await me.send_message("me", f'Новых пользователей сегодня: {day_users}!')


if __name__ == '__main__':
    # asyncio.run(init_models()) # Добавление модели User в БД
    app.run() # Запуск
