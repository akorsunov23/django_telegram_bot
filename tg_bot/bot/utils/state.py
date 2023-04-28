import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot_django.settings')
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
django.setup()

from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterUser(StatesGroup):
    """Класс состояний при регистрации пользователя."""
    start_register = State()
    name = State()
    email = State()
    end_register = State()


class ButtonPress(StatesGroup):
    """Класс состояний по нажатиям кнопок."""
    group_one = State()
    group_two = State()
    group_three = State()
    finish = State()
