from aiogram import executor, filters
from bin.main_var import dp, loop
import logging

from bot.functions.default.start_func import start_func


# Process Name (for Linux)
if sys.platform == 'linux':
    import ctypes
    libc = ctypes.cdll.LoadLibrary('libc.so.6')
    libc.prctl(15, 'A', 0, 0, 0)

# Logging
#logging.basicConfig(level=logging.DEBUG, filename='error.log', filemode='w')


# Handlers
'''<<<-----   DEFAULT   ----->>>'''
dp.register_message_handler(start_func, commands='start')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, loop=loop)