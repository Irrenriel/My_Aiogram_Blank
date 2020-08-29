from aiogram.types import Message


async def start_func(mes: Message):
    await mes.answer('Hello world')