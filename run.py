import asyncio
import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

bot = Bot(token='сюда ваш токен бота')
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет!\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}')
    await message.answer('Из функций пока что:\n1)/help\n2)Отвечаю на вопрос: Как дела?\n3)Отвечаю на отправку фото')


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Это команда /help')


@dp.message(F.text == 'Как дела?')
async def dela(message: Message):
    delishki = ['хорошо', 'прикольно', 'круто', 'всё намази']
    await message.answer(f'У меня {random.choice(delishki)}, у тебя как?')


@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer_photo(photo=message.photo[-1].file_id,
                               caption='Вы мне прислали это фото')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
