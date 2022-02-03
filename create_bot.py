from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
TOKEN = "1488242427:AAHuGIRa03YmzUXc4mluh2wFqHsqpVGIyKM"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)