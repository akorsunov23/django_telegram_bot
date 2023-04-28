import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot_django.settings')
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
django.setup()

import asyncio
from aiogram import types, filters
from aiogram.dispatcher import FSMContext
from tg_bot.bot.config import dp
from tg_bot.bot.utils.state import RegisterUser
from tg_bot.bot.utils.state import ButtonPress
from tg_bot.models import ErrorMessage
from tg_bot.bot.handlers.register_user import *
from tg_bot.bot.handlers.category_selection import *


@dp.message_handler(filters.Command('start'))
async def command_start(message: types.Message, state: FSMContext):
    """Реакция на команду /start/, и распределение по хандлерам в зависимости от регистрации пользователя."""

    user_id = message.chat.id
    if TelegramUser.objects.filter(id_telegram=user_id).exists():
        user = TelegramUser.objects.get(id_telegram=user_id)
        await state.update_data(name=user.name)
        await state.set_state(RegisterUser.end_register)
        await start_survey(message, state)
    else:
        await state.set_state(RegisterUser.start_register)
        await start_register(message, state)


@dp.message_handler(filters.Text, state=ButtonPress)
async def handle_text_message(message: types.Message):
    """Ловит введенные рандомные сообщения от пользователя."""

    user = TelegramUser.objects.get(id_telegram=message.chat.id)
    message_answer = ErrorMessage.objects.get(pk=1)

    answer = await message.answer(
        text=message_answer.message.format(name=user.name, message=message.text),
        parse_mode='HTML'
    )
    await message.delete()
    await asyncio.sleep(4)
    await answer.delete()
