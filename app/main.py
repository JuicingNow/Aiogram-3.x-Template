from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.config import TG_TOKEN
from app.handlers import register_all_handlers
from app.database import start_db

def on_startup():
    print("Bot started!")

async def start_bot():
    bot = Bot(
        token=TG_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    await bot.delete_webhook(drop_pending_updates=True)
    register_all_handlers(dp)
    start_db()
    dp.startup.register(on_startup)
    await dp.start_polling(bot)