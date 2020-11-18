from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Custom Keyboard
def InlineKeyboard(args: list, row_width: int = 5):
    return InlineKeyboardMarkup(row_width=row_width).add(*[InlineKeyboardButton(text=l[0], callback_data=l[1]) for l in args])