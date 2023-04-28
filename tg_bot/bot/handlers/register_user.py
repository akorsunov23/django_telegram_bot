import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot_django.settings')
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
django.setup()

import re
from aiogram import types
from aiogram.dispatcher import FSMContext
from tg_bot.models import TelegramUser, AdminTelegramBot
from tg_bot.bot.config import dp, bot
from tg_bot.bot.utils.state import RegisterUser
from tg_bot.bot.handlers.category_selection import *


@dp.message_handler(state=RegisterUser.start_register)
async def start_register(message: types.Message, state: FSMContext):
    """Начало регистрации."""

    await message.answer('Здравствуйте, Введите своё имя:', parse_mode='HTML')
    await state.set_state(RegisterUser.name)


@dp.message_handler(state=RegisterUser.name)
async def get_email(message: types.Message, state: FSMContext):
    """Хандлер, срабатывающий после ввода имени. Проверяет имя на валидность и запрашивает email."""

    if message.text.isalpha():
        await state.update_data(name=message.text)
        await message.answer('Введите свою электронную почту:', parse_mode='HTML')
        await state.set_state(RegisterUser.email)
    else:
        await message.answer('Имя может содержать только буквы!', parse_mode='HTML')


@dp.message_handler(state=RegisterUser.email)
async def end_register(message: types.Message, state: FSMContext):
    """Хандлер, проверяющий почту на валидность и сохраняющий данные в БД."""

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(regex, message.text):
        name = await state.get_data()
        TelegramUser.objects.create(
            id_telegram=message.chat.id,
            username=message.chat.username or 'None',
            name=name['name'],
            email=message.text
        )

        admins = list(AdminTelegramBot.objects.all().only('id_telegram').values())
        for admin in admins:
            await bot.send_message(
                int(admin['id_telegram']),
                text=f'Новый зарегистрированный пользователь:\n'
                     f'Имя - {name["name"]}\n'
                     f'id - {message.chat.id}\n'
                     f'username - {message.chat.username or "None"}\n'
                     f'email - {message.text}\n',
                parse_mode='HTML'
            )
        await state.set_state(RegisterUser.end_register)
        await start_survey(message, state)
    else:
        await message.answer('Введите корректные данные.', parse_mode='HTML')
