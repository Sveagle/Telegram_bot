from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class TestMiddleware(BaseMiddleware):

    async def __call__(self,
                       handler: Callable[
                           [TelegramObject, Dict[str, any]],
                           Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        print('Дейтсвия до обработчика')
        result = await handler(event, data)
        print('Действия после обработчика')
        return result
