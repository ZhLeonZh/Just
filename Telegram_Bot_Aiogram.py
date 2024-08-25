import asyncio
#import logging

from aiogram import Bot, Dispatcher, types


TOKEN_API = "7167295687:AAFaDaMJRDdMAvkzaJQJNVzyj_pdSEH0OoA" #token of bot

bot = Bot(token=TOKEN_API)
dp = Dispatcher()

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(text=message.text)


async def main():
#    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())