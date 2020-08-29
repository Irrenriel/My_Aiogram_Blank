from aiogram import executor
from bin.main_var import dp, loop
import logging

from bot.functions.default.start_func import start_func


# Logging
#logging.basicConfig(level=logging.DEBUG, filename='error.log', filemode='w')


# Handlers

'''<<<-----   DEFAULT   ----->>>'''
dp.register_message_handler(start_func, commands='start')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, loop=loop)