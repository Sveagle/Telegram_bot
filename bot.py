import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет! Твой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}')


@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')


@dp.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('Нормально')


@dp.message(Command('get_photo'))
async def send_photo(message: Message):
    await message.answer_photo(photo='https://pngimg.com/uploads/pokemon/pokemon_PNG23.png',
                               caption='кикичу')


@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # на проде - вырубить
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
