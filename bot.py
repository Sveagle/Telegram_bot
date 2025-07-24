"""Основной модуль для запуска Telegram бота.

Модуль содержит:
- Конфигурацию бота
- Инициализацию диспетчера
- Запуск поллинга
- Обработку ошибок
"""

import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from app.handlers import router

# Инициализация бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()


async def main() -> None:
    """Основная асинхронная функция для запуска бота.

    Выполняет:
    - Подключение роутера с обработчиками
    - Запуск процесса поллинга
    """
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
        print('Бот запущен и работает')
    except KeyboardInterrupt:
        print('Бот остановлен пользователем')
