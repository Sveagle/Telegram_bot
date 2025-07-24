from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

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

# cars = ['Tesla', 'Mercedes', 'BMW']


# async def inline_cars():
#     keyboard = InlineKeyboardBuilder()
#     for car in cars:
#         keyboard.add(InlineKeyboardButton(text=car,
#                                           callback_data=f'car_{car}'))
#     return keyboard.adjust(2).as_markup()
