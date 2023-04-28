import logging
import tg_bot.bot.handlers

from django.core.management.base import BaseCommand
from aiogram.utils import executor
from tg_bot.bot.config import dp


class Command(BaseCommand):
    """Кастомная команда Джанго, для запуска телеграм бота."""

    help = 'Starting a telegram bot'

    def handle(self, *args, **kwargs):
        logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] [%(levelname)s] [%(message)s]')
        executor.start_polling(dp, skip_updates=True)
