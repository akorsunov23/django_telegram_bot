from aiogram import types
from tg_bot.models import FirstCategoryBottom, TwoCategoryBottom, ThreeCategoryBottom

# эмодзи для кнопки "назад"
SMAIL_BOTTOM_BACK = '\U00002B07 '
# текст для кнопки "назад"
TEXT_BOTTOM_BACK = 'назад'
# эмодзи для кнопки "выход"
SMAIL_BOTTOM_EXIT = '\U00002B07 '
# текст для кнопки "выход"
TEXT_BOTTOM_EXIT = 'покинуть бота'
# эмодзи для кнопок первой категории
SMAIL_BOTTOM_FIRST = '\U000023FA '
# эмодзи для кнопки второй категории
SMAIL_BOTTOM_TWO = '\U000023FA '
# эмодзи для кнопки третьей категории
SMAIL_BOTTOM_THREE = '\U000023FA '


def first_category_bottom() -> types.InlineKeyboardMarkup():
    """Кнопки из первой категории."""

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    bottoms = FirstCategoryBottom.objects.all()
    list_bottoms = list()
    for bottom in bottoms:
        list_bottoms.append(types.InlineKeyboardButton(
            text=SMAIL_BOTTOM_FIRST + bottom.name,
            callback_data=bottom.pk),

        )
    keyboard.add(*list_bottoms)
    keyboard.add(types.InlineKeyboardButton(text=SMAIL_BOTTOM_EXIT + TEXT_BOTTOM_EXIT, callback_data='exit'))
    return keyboard


def two_category_bottom(id_category: int) -> types.InlineKeyboardMarkup():
    """Кнопки из второй категории."""

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    bottoms = TwoCategoryBottom.objects.filter(parent=id_category)
    list_bottoms = list()
    for bottom in bottoms:
        list_bottoms.append(types.InlineKeyboardButton(
            text=SMAIL_BOTTOM_TWO + bottom.name,
            callback_data=bottom.pk)
        )
    keyboard.add(*list_bottoms)
    keyboard.add(types.InlineKeyboardButton(text=SMAIL_BOTTOM_BACK + TEXT_BOTTOM_BACK, callback_data='back'))
    keyboard.add(types.InlineKeyboardButton(text=SMAIL_BOTTOM_EXIT + TEXT_BOTTOM_EXIT, callback_data='exit'))
    return keyboard


def three_category_bottom(id_category: int) -> types.InlineKeyboardMarkup():
    """Кнопки из третьей категории."""

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    bottoms = ThreeCategoryBottom.objects.filter(parent=id_category)
    list_bottoms = list()
    for bottom in bottoms:
        list_bottoms.append(types.InlineKeyboardButton(
            text=SMAIL_BOTTOM_THREE + bottom.name,
            callback_data=bottom.pk)
        )
    keyboard.add(*list_bottoms)
    keyboard.add(types.InlineKeyboardButton(text=SMAIL_BOTTOM_BACK + TEXT_BOTTOM_BACK, callback_data='back'))
    keyboard.add(types.InlineKeyboardButton(text=SMAIL_BOTTOM_EXIT + TEXT_BOTTOM_EXIT, callback_data='exit'))
    return keyboard
