from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет! Твой ID: {message.from_user.id}\n'
                        f'Имя: {message.from_user.first_name}',
                        reply_markup=kb.main)


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')


@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('Нормально')


@router.message(Command('get_photo'))
async def send_photo(message: Message):
    await message.answer_photo(
        photo='https://pngimg.com/uploads/pokemon/pokemon_PNG23.png',
        caption='кикичу')


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    # await callback.answer('Вы выбрали каталог', show_alert=True)
    await callback.message.edit_text('Привет!',
                                     reply_markup=await kb.inline_cars())
