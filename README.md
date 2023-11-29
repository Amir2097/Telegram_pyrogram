# Взаимодействие с telegam API при помощи Pyrogram

**Воронка взаимодействия бота с пользователем**

`models.py/init_models()` - первоначальное удаление и создание моделей БД
`models.py/users_check()` - проверка пользователя, если нету то добавление в БД
`models.py/today_check()` - извлекает из БД количество добавленных пользователей сегодня
`main.py/start_messages()` - основная логика взаимодействия бота с пользователем
`main.py/users_today()` - при команде */users_today* отправляет в избранное 
количество зарегистрированных пользователей за сегодня

## Использованные технологии:

1. Python 3.11
2. Pyrogram
3. БД:
   - SQLalchemy
   - Asyncpg
   - PostgreSQL
4. Хранение переменных окружения:
   - Python-dotenv
5. Loguru

> Создаем и активируем виртуальное окружение:
1. Linux:
   - `python3 -m venv venv`
   - `source venv/bin/activate`
2. Windows:
   - `python3 -m venv venv`
   - `venv\Scripts\activate.bat`

> Установите библиотеки:
- `pip install -r requirements.txt`

*Переменные окружения:*
1. Библиотека *python-dotenv*. Создайте файл `.env` и внесите ваши данные 
2. Переменные:
    - `DATABASE_NAME` - имя вашей БД
    - `DATABASE_PORT` - порт подключения к БД
    - `DATABASE_USER` - пользователь БД
    - `DATABASE_PASSWORD` - пароль от БД
    - `DATABASE_HOST` - хост подключения к БД
    - `API_ID` - api_id от вашего тг API
    - `API_HASH` - api_hash от вашего тг API
    - `BOT_TOKEN` - токен от бота, может запросить у BotFather

## Для запуска скрипта:

- Требуется провести первоначальную настройку pyrogram
    - Получить ключ Telegram API https://core.telegram.org/api/obtaining_api_id
    - api_id и api_hash следует записать в файл `.env`
    - зайти в Telegram и в чате обратиться к BotFather для создание нового бота
    - пройти инструкцию и получить токен от бота
    - записать токен как `BOT_TOKEN` в файл `.env`

- Запуск скрипта 
   - `python main.py`

