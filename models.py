from sqlalchemy import Column, DateTime, Integer, String, func, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from dotenv import load_dotenv
from sqlalchemy import extract, func
from datetime import datetime
from loguru import logger
import os

load_dotenv() # Переменные окружения
Base = declarative_base()


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    id_tg = Column(Integer, nullable=False)
    first_name = Column(String(80))
    last_name = Column(String(80))
    date_created = Column(DateTime, server_default=func.now())

    def __str__(self):
        return f'User: {self.id_tg}, {self.full_name}'


# Соединение с postgres+asyncpg
DSN_ASYNC = f'postgresql+asyncpg://{os.getenv("DATABASE_USER")}:{os.getenv("DATABASE_PASSWORD")}' \
      f'@{os.getenv("DATABASE_HOST")}:{os.getenv("DATABASE_PORT")}/{os.getenv("DATABASE_NAME")}'

engine = create_async_engine(DSN_ASYNC, echo=True)
session_factory = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


@logger.catch
async def init_models():
    """
    Удаление и создание моделей в БД
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@logger.catch
async def users_check(id_tg: int, first_name: str, last_name: str):
    """
    Функция добавления пользователей в БД
    :param id_tg - ID telegram пользователя
    :param first_name - first_name users in telegram
    :param last_name - last_name users in telegram
    """
    async with session_factory() as session:
        user_verification = await session.execute(select(User).where(User.id_tg == id_tg))
        if user_verification.scalar():
            pass
        else:
            new_user = User(id_tg=id_tg, first_name=first_name, last_name=last_name)
            session.add(new_user)
            await session.commit()


@logger.catch
async def today_check():
    """
    Функция возвращает количесвто пользователей добавленных сегодня
    """
    async with session_factory() as session:

        new_date = await session.execute(
            select(User.id).where(extract('day', User.date_created) == datetime.today().day)
        )
        return len(new_date.scalars().all())


# asyncio.run(today_check())