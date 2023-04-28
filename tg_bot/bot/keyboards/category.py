from aiogram import types
from tg_bot.models import FirstCategoryBottom, TwoCategoryBottom, ThreeCategoryBottom


def first_category_bottom() -> types.InlineKeyboardMarkup():
    """Кнопки из первой категории."""

    keyboard = types.InlineKeyboardMarkup()
    bottoms = FirstCategoryBottom.objects.all()
    for bottom in bottoms:
        keyboard.add(types.InlineKeyboardButton(
            text='\U000023FA ' + bottom.name,
            callback_data=bottom.pk),

        )
    keyboard.add(types.InlineKeyboardButton(text='\U00002B07 покинуть бота', callback_data='exit'))
    return keyboard


def two_category_bottom(id_category: int) -> types.InlineKeyboardMarkup():
    """Кнопки из второй категории."""

    keyboard = types.InlineKeyboardMarkup()
    bottoms = TwoCategoryBottom.objects.filter(parent=id_category)
    for bottom in bottoms:
        keyboard.add(types.InlineKeyboardButton(
            text='\U000023FA ' + bottom.name,
            callback_data=bottom.pk)
        )
    keyboard.add(types.InlineKeyboardButton(text='\U00002B05 назад', callback_data='back'))
    keyboard.add(types.InlineKeyboardButton(text='\U00002B07 покинуть бота', callback_data='exit'))
    return keyboard


def three_category_bottom(id_category: int) -> types.InlineKeyboardMarkup():
    """Кнопки из третьей категории."""

    keyboard = types.InlineKeyboardMarkup()
    bottoms = ThreeCategoryBottom.objects.filter(parent=id_category)
    for bottom in bottoms:
        keyboard.add(types.InlineKeyboardButton(
            text='\U000023FA ' + bottom.name,
            callback_data=bottom.pk)
        )
    keyboard.add(types.InlineKeyboardButton(text='\U00002B05 назад', callback_data='back'))
    keyboard.add(types.InlineKeyboardButton(text='\U00002B07 покинуть бота', callback_data='exit'))
    return keyboard
