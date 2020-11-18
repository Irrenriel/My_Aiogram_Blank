from aiogram.types import ReplyKeyboardMarkup


# Custom Keyboard
def ReplyKeyboard(*args: str, row_width: int = 3):
    return ReplyKeyboardMarkup(resize_keyboard=True, selective=True, row_width=row_width).add(*args)