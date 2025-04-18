import asyncio
from aiogram import Bot, Dispatcher
from handlers.start.handlers import router
from database.models import create_tables  # Создание таблиц

async def main():
    create_tables()  # Создание таблиц в базе данных синхронно
    bot = Bot(token='7403482612:AAE7N6pDqf4ECfHhxfmXhYX5uGFm3lml5xA')  # Замените на свой токен
    dp = Dispatcher()
    dp.include_router(router)  # Добавление маршрутов
    await dp.start_polling(bot)  # Запуск бота

if __name__ == '__main__':
    try:
        asyncio.run(main())  # Запуск асинхронного main
    except KeyboardInterrupt:
        print('Бот выключен')  # Обработка завершения работы бота
