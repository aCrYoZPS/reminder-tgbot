from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("/help")
b2 = KeyboardButton("/readrem")
b3 = KeyboardButton("/newreminder")
b4 = KeyboardButton("/cancel")

kb_welcome = ReplyKeyboardMarkup(resize_keyboard=True)

kb_welcome.row(b1, b2).row(b3, b4)
