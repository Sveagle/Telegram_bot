import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from app.handlers import router

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
        print('bot is running')
    except KeyboardInterrupt:
        print('Exit')
