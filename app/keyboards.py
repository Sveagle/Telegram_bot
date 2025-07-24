"""Модуль keyboards - содержит клавиатуры для Telegram бота.

Предоставляет предопределенные клавиатуры:
- Главное меню (main_kb)
- Клавиатура возврата (back_kb)
"""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Каталог")],
        [KeyboardButton(text="Корзина"), KeyboardButton(text="Контакты")],
        [KeyboardButton(text="Помощь"), KeyboardButton(text="Фото")],
        [KeyboardButton(text="Как дела?")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие...",
)

back_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Назад в меню")],
    ],
    resize_keyboard=True,
)
