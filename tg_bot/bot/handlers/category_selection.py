import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot_django.settings')
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
django.setup()

from django.contrib.auth import settings
from django.db.models import F
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageToDeleteNotFound
from tg_bot.models import \
    FirstCategoryBottom, \
    TwoCategoryBottom, \
    ThreeCategoryBottom, \
    TelegramUser, \
    WelcomeMessage, \
    ImageFirstCategory, \
    ImageTwoCategory, \
    MessageThreeCategory, \
    ImageThreeCategory, \
    PressBottomFirstCategory, \
    PressBottomBackAndExitFirstCategory, \
    PressBottomTwoCategory, \
    PressBottomBackAndExitTwoCategory, \
    PressBottomThreeCategory, \
    PressBottomBackAndExitThreeCategory, \
    FileThreeCategory
from tg_bot.bot.config import dp, bot
from tg_bot.bot.utils.state import RegisterUser, ButtonPress
from tg_bot.bot.utils.filter import filter_queryset
from tg_bot.bot.keyboards.category import \
    first_category_bottom, \
    two_category_bottom, \
    three_category_bottom, \
    SMAIL_BOTTOM_BACK, \
    SMAIL_BOTTOM_EXIT, \
    TEXT_BOTTOM_BACK, \
    TEXT_BOTTOM_EXIT


@dp.message_handler(state=RegisterUser.end_register, text='start_survey')
async def start_survey(message: types.Message, state: FSMContext):
    """Зарегистрированному пользователю даётся выбор из первой категории."""

    await state.update_data(message_start=message)

    data = await state.get_data()
    welcome_message = WelcomeMessage.objects.only('message').get(pk=1)

    await bot.send_message(
        chat_id=message.chat.id,
        text=welcome_message.message.format(name=data['name']),
        reply_markup=first_category_bottom(),
        parse_mode='HTML'
    )

    await state.set_state(ButtonPress.group_one)


@dp.callback_query_handler(state=ButtonPress.group_one)
async def press_one_bottom(callback: types.CallbackQuery, state: FSMContext):
    """Реакция на нажатие кнопки первой категории, и вывод соответствующего результата."""

    await state.update_data(call_one=callback)
    data = await state.get_data()
    user = TelegramUser.objects.get(id_telegram=callback.message.chat.id)

    if callback.data == 'exit':
        if PressBottomBackAndExitFirstCategory.objects.filter(user=user.pk, name_bottom='покинуть бота').exists():
            PressBottomBackAndExitFirstCategory.objects.filter(user=user.pk, name_bottom='покинуть бота').update(
                count=F('count') + 1
            )
        else:
            PressBottomBackAndExitFirstCategory.objects.create(
                user=user,
                name_bottom='покинуть бота',
                count=1
            )
        await callback.message.delete()
        await state.finish()
    else:
        try:
            await callback.message.delete()
        except MessageToDeleteNotFound:
            pass
        finally:
            bottom = FirstCategoryBottom.objects.only('descriptions').get(pk=callback.data)

            if PressBottomFirstCategory.objects.filter(user=user.pk, bottom=bottom.pk).exists():
                PressBottomFirstCategory.objects.filter(user=user.pk, bottom=bottom.pk).update(
                    count=F('count') + 1
                )
            else:
                PressBottomFirstCategory.objects.create(
                    user=user,
                    bottom=bottom,
                    count=1
                )

            if ImageFirstCategory.objects.only('image').filter(parent=callback.data).exists():
                image = ImageFirstCategory.objects.only('image').get(parent=callback.data).image.path
            else:
                image = os.path.join(settings.MEDIA_ROOT, 'image_bottom/no_photo.jpg')
            await bot.send_photo(
                chat_id=callback.message.chat.id,
                photo=types.InputFile(image),
                caption=bottom.descriptions.format(name=data['name']),
                reply_markup=two_category_bottom(id_category=callback.data),
                parse_mode='HTML'
            )

            await state.set_state(ButtonPress.group_two)


@dp.callback_query_handler(state=ButtonPress.group_two)
async def press_two_bottom(callback: types.CallbackQuery, state: FSMContext):
    """Реакция на нажатие кнопки второй категории, и вывод соответствующего результата."""

    await state.update_data(call_two=callback)

    data = await state.get_data()
    user = TelegramUser.objects.get(id_telegram=callback.message.chat.id)

    if callback.data == 'exit':
        if PressBottomBackAndExitTwoCategory.objects.filter(user=user.pk, name_bottom='покинуть бота').exists():
            PressBottomBackAndExitTwoCategory.objects.filter(user=user.pk, name_bottom='покинуть бота').update(
                count=F('count') + 1
            )
        else:
            PressBottomBackAndExitTwoCategory.objects.create(
                user=user,
                name_bottom='покинуть бота',
                count=1
            )
        await callback.message.delete()
        await state.finish()
    elif callback.data == 'back':
        if PressBottomBackAndExitTwoCategory.objects.filter(user=user.pk, name_bottom='назад').exists():
            PressBottomBackAndExitTwoCategory.objects.filter(user=user.pk, name_bottom='назад').update(
                count=F('count') + 1
            )
        else:
            PressBottomBackAndExitTwoCategory.objects.create(
                user=user,
                name_bottom='назад',
                count=1
            )
        await callback.message.delete()
        await start_survey(data['message_start'], state)
    else:
        try:
            await callback.message.delete()
        except MessageToDeleteNotFound:
            pass
        finally:
            bottom = TwoCategoryBottom.objects.only('descriptions').get(pk=callback.data)

            if PressBottomTwoCategory.objects.filter(user=user.pk, bottom=bottom.pk).exists():
                PressBottomTwoCategory.objects.filter(user=user.pk, bottom=bottom.pk).update(
                    count=F('count') + 1
                )
            else:
                PressBottomTwoCategory.objects.create(
                    user=user,
                    bottom=bottom,
                    count=1
                )

            if ImageTwoCategory.objects.only('image').filter(parent=callback.data).exists():
                image = ImageTwoCategory.objects.only('image').get(parent=callback.data).image.path
            else:
                image = os.path.join(settings.MEDIA_ROOT, 'image_bottom/no_photo.jpg')
            await bot.send_photo(
                chat_id=callback.message.chat.id,
                photo=types.InputFile(image),
                caption=bottom.descriptions.format(name=data['name']),
                reply_markup=three_category_bottom(id_category=callback.data),
                parse_mode='HTML'
            )

            await state.set_state(ButtonPress.group_three)


@dp.callback_query_handler(state=ButtonPress.group_three)
async def press_three_bottom(callback: types.CallbackQuery, state: FSMContext):
    """Реакция на нажатие третьей категории кнопок, и вывод соответствующего результата."""

    user = TelegramUser.objects.get(id_telegram=callback.message.chat.id)

    if callback.data == 'exit':
        if PressBottomBackAndExitThreeCategory.objects.filter(user=user.pk, name_bottom='покинуть бота').exists():
            PressBottomBackAndExitThreeCategory.objects.filter(user=user.pk, name_bottom='покинуть бота').update(
                count=F('count') + 1
            )
        else:
            PressBottomBackAndExitThreeCategory.objects.create(
                user=user,
                name_bottom='покинуть бота',
                count=1
            )
        await callback.message.delete()
        await state.finish()
    elif callback.data == 'back':
        if PressBottomBackAndExitThreeCategory.objects.filter(user=user.pk, name_bottom='назад').exists():
            PressBottomBackAndExitThreeCategory.objects.filter(user=user.pk, name_bottom='назад').update(
                count=F('count') + 1
            )
        else:
            PressBottomBackAndExitThreeCategory.objects.create(
                user=user,
                name_bottom='назад',
                count=1
            )
        await callback.message.delete()
        data = await state.get_data()
        await press_one_bottom(data['call_one'], state)
    else:
        await callback.message.delete()
        bottom = ThreeCategoryBottom.objects.get(pk=callback.data)

        if PressBottomThreeCategory.objects.filter(user=user.pk, bottom=bottom.pk).exists():
            PressBottomThreeCategory.objects.filter(user=user.pk, bottom=bottom.pk).update(
                count=F('count') + 1
            )
        else:
            PressBottomThreeCategory.objects.create(
                user=user,
                bottom=bottom,
                count=1
            )

        messages = MessageThreeCategory.objects.filter(parent=callback.data)
        filter_messages = filter_queryset(queryset=messages)

        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text=SMAIL_BOTTOM_BACK + TEXT_BOTTOM_BACK, callback_data='back'))
        keyboard.add(types.InlineKeyboardButton(text=SMAIL_BOTTOM_EXIT + TEXT_BOTTOM_EXIT, callback_data='exit'))
        list_id_message = list()

        for message in filter_messages:
            if ImageThreeCategory.objects.filter(parent=message.pk).exists():
                images = ImageThreeCategory.objects.filter(parent=message.pk)
                media_group = types.MediaGroup()
                for index in range(len(images)):
                    if index == 0:
                        media_group.attach_photo(
                            types.InputFile(images[index].image.path),
                            caption=message.descriptions.format(name=user.name),
                            parse_mode='HTML'
                        )
                    else:
                        media_group.attach_photo(types.InputFile(images[index].image.path))
                mes = await bot.send_media_group(chat_id=callback.message.chat.id, media=media_group)
                for i in mes:
                    list_id_message.append(i['message_id'])

            else:
                image = os.path.join(settings.MEDIA_ROOT, 'image_bottom/no_photo.jpg')
                mes = await bot.send_photo(
                    chat_id=callback.message.chat.id,
                    photo=types.InputFile(image),
                    caption=message.descriptions.format(name=user.name),
                    parse_mode='HTML'
                )
                list_id_message.append(mes['message_id'])
            if FileThreeCategory.objects.filter(parent=message.pk).exists():
                file = FileThreeCategory.objects.get(parent=message.pk)
                mes = await bot.send_document(
                    chat_id=callback.message.chat.id,
                    document=types.InputFile(file.image.path),
                )
                list_id_message.append(mes['message_id'])

        await bot.send_message(
            chat_id=callback.message.chat.id,
            text=F'Уважаемый {user.name}, выберите действие:',
            reply_markup=keyboard,
            parse_mode='HTML'
        )

        await state.update_data(id_mess=list_id_message)
        await state.set_state(ButtonPress.finish)


@dp.callback_query_handler(state=ButtonPress.finish)
async def press_three_bottom(callback: types.CallbackQuery, state: FSMContext):
    """Реакция на нажатие кнопок после отрабатывания третьей категории кнопок, и вывод соответствующего результата."""

    data = await state.get_data()

    if callback.data == 'exit':
        await callback.message.delete()
        for i in data['id_mess']:
            await callback.message.chat.delete_message(i)
        await state.finish()
    elif callback.data == 'back':
        await callback.message.delete()
        for i in data['id_mess']:
            await callback.message.chat.delete_message(i)
        await press_two_bottom(data['call_two'], state)
