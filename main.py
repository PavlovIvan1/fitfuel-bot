import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
import logging
import os

API_TOKEN = os.environ.get['API_TOKEN']

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Открыть приложение", 
										web_app=WebAppInfo(url='https://fitfuel-nine.vercel.app')
                )
            ]
        ]
    )

    
    await message.answer("✅ Добро пожаловать в FitFuel!", reply_markup=keyboard,)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
