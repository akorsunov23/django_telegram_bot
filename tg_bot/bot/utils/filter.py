import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot_django.settings')
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
django.setup()

from django.db.models import QuerySet
from datetime import date
from tg_bot.models import MessageThreeCategory


def filter_queryset(queryset: QuerySet) -> list:
    """
    Фильтрация входного queryset на заданные параметры в админ-панели.

    Если установлено параметр "пожизненно" сообщение отправляется всегда.
    Если установлено параметр "сезон" сообщение отправляется в установленные даты, ежегодно.
    Если флаги не установлены и дата меньше нынешней, сообщение удаляется из БД.
    """

    result = list()
    date_now = date.today()

    for query in queryset:
        if query.lifetime:
            result.append(query)
        elif query.season and (query.ship_from and query.ship_to):
            ship_from = query.ship_from.replace(year=date.today().year)
            ship_to = query.ship_to.replace(year=date.today().year)
            if ship_from < date_now < ship_to:
                result.append(query)
        else:
            if query.ship_to > date_now:
                result.append(query)
            else:
                MessageThreeCategory.objects.get(pk=query.pk).delete()

    return result
