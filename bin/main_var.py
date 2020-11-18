from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
import asyncio

from bin.config import BOT_TOKEN, DB_NAME, PARSE_MODE
from bin.settings_class import SQLite_db, Scheduler_ex, Middleware

# Loop
loop = asyncio.get_event_loop()

# Scheduler
scheduler = Scheduler_ex(loop)

# MemoryStorage
storage = MemoryStorage()

# Bot
bot = Bot(token=BOT_TOKEN, loop=loop, parse_mode=PARSE_MODE)

# Dispatcher
dp = Dispatcher(bot, storage=storage, loop=loop)

# Database
if DB_NAME:
    db = SQLite_db(db=f'bin\{DB_NAME}.db')
    dp.middleware.setup(Middleware(db))
