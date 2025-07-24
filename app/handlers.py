"""Модуль обработки сообщений и команд для Telegram бота.

Этот модуль содержит обработчики для:
- Стартовой команды (/start)
- Текстовых команд (Помощь, Как дела?, Фото)
- Callback-запросов (каталог)
- Возврата в главное меню
- Обработки полученных фото

Использует:
- aiogram для обработки Telegram сообщений
- Собственный модуль app.keyboards для клавиатур
"""

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Обработчик команды /start. Вывод меню и приветствия.

    Args:
        message: Объект сообщения от пользователя.
    """
    await message.reply(
        f'Привет! Это тестовый бот за моим авторством,\n'
        f'Ваше имя: {message.from_user.first_name}',
        reply_markup=kb.main_kb
    )


@router.message(F.text == 'Помощь')
async def get_help(message: Message) -> None:
    """Обработчик кнопки 'Помощь'. Отправляет справочное сообщение.

    Args:
        message: Объект сообщения от пользователя.
    """
    await message.answer(
        'Это команда "Помощь"',
        reply_markup=kb.back_kb
    )


@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message) -> None:
    """Обработчик кнопки 'Как дела?'. Отправляет ответ на вопрос.

    Args:
        message: Объект сообщения от пользователя.
    """
    await message.answer(
        'Нормально',
        reply_markup=kb.back_kb
    )


@router.message(F.text == 'Фото')
async def send_photo(message: Message) -> None:
    """Обработчик кнопки 'Фото'. Отправляет изображение Пикачу.

    Args:
        message: Объект сообщения от пользователя.
    """
    await message.answer_photo(
        photo='https://pngimg.com/uploads/pokemon/pokemon_PNG23.png',
        caption='пикачу',
        reply_markup=kb.back_kb
    )


@router.message(F.photo)
async def get_photo(message: Message) -> None:
    """Обработчик получения фото. Отправляет file_id полученного фото.

    Args:
        message: Объект сообщения с фото от пользователя.
    """
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery) -> None:
    """Обработчик callback запроса для кнопки 'Каталог'.

    Args:
        callback: Объект callback запроса.
    """
    await callback.message.edit_text(
        'Привет!',
        reply_markup=await kb.back_kb
    )


@router.message(F.text == "Назад в меню")
async def back_to_menu(message: Message) -> None:
    """Обработчик кнопки 'Назад в меню'. Возвращает главное меню.

    Args:
        message: Объект сообщения от пользователя.
    """
    await message.answer(
        "Возвращаю в главное меню:",
        reply_markup=kb.main_kb,
    )
