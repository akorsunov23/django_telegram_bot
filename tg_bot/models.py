from django.db import models
from django.utils import timezone


class TelegramUser(models.Model):
    """Модель для добавления зарегистрированных пользователей в телеграм."""

    id_telegram = models.CharField(max_length=100, unique=True, verbose_name='id пользователя в телеграмм')
    username = models.CharField(max_length=100, verbose_name='никнейм')
    name = models.CharField(max_length=100, verbose_name='имя')
    email = models.EmailField(null=False, verbose_name='электронная почта')
    created_at = models.DateTimeField(auto_now_add=timezone.now(), verbose_name='зарегистрирован')

    def __str__(self):
        return f'{self.id_telegram} - {self.username}'

    class Meta:
        verbose_name = '1. Зарегистрированный пользователь'
        verbose_name_plural = '1. Зарегистрированные пользователи'
        ordering = '-created_at',


class AdminTelegramBot(models.Model):
    """Модель для добавления администраторов бота."""

    id_telegram = models.CharField(max_length=100, unique=True, verbose_name='id администратора в телеграмм')
    username = models.CharField(default='не заполнено', max_length=100, null=True, blank=True, verbose_name='никнейм')

    class Meta:
        verbose_name = '5. Администратор бота'
        verbose_name_plural = '5. Администраторы бота'

    def __str__(self):
        return f'Администратор - id: {self.id_telegram}'


class FirstCategoryBottom(models.Model):
    """Модель хранения кнопок первой категории."""

    name = models.CharField(max_length=100, unique=True, verbose_name='название кнопки')
    descriptions = models.TextField(verbose_name='описание кнопки')

    class Meta:
        verbose_name = '2. Первая категория кнопок'
        verbose_name_plural = '2. Первая категория кнопок'

    def __str__(self):
        return self.name


class ImageFirstCategory(models.Model):
    """Модель для хранения изображений кнопок первой категории."""

    parent = models.ForeignKey(FirstCategoryBottom, on_delete=models.CASCADE, verbose_name='родительская кнопка')
    image = models.ImageField(upload_to='image_bottom/first_category', verbose_name='изображение к кнопки')

    class Meta:
        verbose_name = 'Изображение первой категории'
        verbose_name_plural = 'Изображения первой категории'


class PressBottomFirstCategory(models.Model):
    """Модель для хранения статистики нажатия кнопок первой категории."""

    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, verbose_name='пользователь')
    bottom = models.ForeignKey(FirstCategoryBottom, on_delete=models.CASCADE, verbose_name='кнопка')
    count = models.IntegerField(default=0, verbose_name='количество нажатий')

    class Meta:
        verbose_name_plural = 'Статистика нажатия кнопок первой категории'

    def __str__(self):
        return f'Кнопка первой категории id - {self.pk}'


class PressBottomBackAndExitFirstCategory(models.Model):
    """Модель для хранения статистики нажатия кнопок "назад" и "выход" первой категории."""

    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, verbose_name='пользователь')
    name_bottom = models.CharField(max_length=100, verbose_name='кнопка')
    count = models.IntegerField(default=0, verbose_name='количество нажатий')

    class Meta:
        verbose_name_plural = 'Статистика нажатия кнопок первой категории'

    def __str__(self):
        return f'Кнопка первой категории id - {self.pk}'


class TwoCategoryBottom(models.Model):
    """Модель хранения кнопок второй категории."""

    parent = models.ForeignKey(FirstCategoryBottom, on_delete=models.CASCADE, verbose_name='родительская кнопка')
    name = models.CharField(max_length=100, unique=True, verbose_name='название кнопки')
    descriptions = models.TextField(verbose_name='описание кнопки')

    class Meta:
        verbose_name = '3. Вторая категория кнопок'
        verbose_name_plural = '3. Вторая категория кнопок'

    def __str__(self):
        return self.name


class ImageTwoCategory(models.Model):
    """Модель для хранения изображений кнопок первой категории."""

    parent = models.ForeignKey(TwoCategoryBottom, on_delete=models.CASCADE, verbose_name='родительская кнопка')
    image = models.ImageField(upload_to='image_bottom/two_category', verbose_name='изображение к кнопки')

    class Meta:
        verbose_name = 'Изображение второй категории'
        verbose_name_plural = 'Изображения второй категории'


class PressBottomTwoCategory(models.Model):
    """Модель для хранения статистики нажатия кнопок второй категории."""

    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, verbose_name='пользователь')
    bottom = models.ForeignKey(TwoCategoryBottom, on_delete=models.CASCADE, verbose_name='кнопка')
    count = models.IntegerField(default=0, verbose_name='количество нажатий')

    class Meta:
        verbose_name_plural = 'Статистика нажатия кнопок второй категории'

    def __str__(self):
        return f'Кнопка второй категории id - {self.pk}'


class PressBottomBackAndExitTwoCategory(models.Model):
    """Модель для хранения статистики нажатия кнопок "назад" и "выход" второй категории."""

    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, verbose_name='пользователь')
    name_bottom = models.CharField(max_length=100, verbose_name='кнопка')
    count = models.IntegerField(default=0, verbose_name='количество нажатий')

    class Meta:
        verbose_name_plural = 'Статистика нажатия кнопок второй категории'

    def __str__(self):
        return f'Кнопка второй категории id - {self.pk}'


class ThreeCategoryBottom(models.Model):
    """Модель хранения кнопок третьей категории."""

    parent = models.ForeignKey(TwoCategoryBottom, on_delete=models.CASCADE, verbose_name='родительская кнопка')
    name = models.CharField(max_length=100, unique=True, verbose_name='название кнопки')

    class Meta:
        verbose_name = '4. Третья категория кнопок'
        verbose_name_plural = '4. Третья категория кнопок'

    def __str__(self):
        return self.name


class PressBottomThreeCategory(models.Model):
    """Модель для хранения статистики нажатия кнопок третьей категории."""

    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, verbose_name='пользователь')
    bottom = models.ForeignKey(ThreeCategoryBottom, on_delete=models.CASCADE, verbose_name='кнопка')
    count = models.IntegerField(default=0, verbose_name='количество нажатий')

    class Meta:
        verbose_name_plural = 'Статистика нажатия кнопок третьей категории'

    def __str__(self):
        return f'Кнопка третьей категории id - {self.pk}'


class PressBottomBackAndExitThreeCategory(models.Model):
    """Модель для хранения статистики нажатия кнопок "назад" и "выход" третьей категории."""

    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, verbose_name='пользователь')
    name_bottom = models.CharField(max_length=100, verbose_name='кнопка')
    count = models.IntegerField(default=0, verbose_name='количество нажатий')

    class Meta:
        verbose_name_plural = 'Статистика нажатия кнопок третьей категории'

    def __str__(self):
        return f'Кнопка третьей категории id - {self.pk}'


class MessageThreeCategory(models.Model):
    """Модель хранения сообщений, отправляемые после нажатие кнопки третьей группы."""

    parent = models.ForeignKey(ThreeCategoryBottom, on_delete=models.CASCADE, verbose_name='родительская кнопка')
    descriptions = models.TextField(verbose_name='описание')
    ship_from = models.DateField(null=True, blank=True, verbose_name='отправка с')
    ship_to = models.DateField(null=True, blank=True, verbose_name='отправка до')
    lifetime = models.BooleanField(default=False, blank=True, null=True, verbose_name='пожизненно')
    season = models.BooleanField(default=False, blank=True, null=True, verbose_name='сезон')

    class Meta:
        verbose_name = 'Сообщение к 3 категории кнопок'
        verbose_name_plural = 'Сообщения к 3 категории кнопок'

    def __str__(self):
        return self.parent.name


class ImageThreeCategory(models.Model):
    """Модель хранения изображений описания кнопок третьей категории."""

    parent = models.ForeignKey(MessageThreeCategory, on_delete=models.CASCADE, verbose_name='сообщение')
    image = models.ImageField(upload_to='image_bottom/three_category', verbose_name='изображение к сообщению')

    class Meta:
        verbose_name = 'Изображение к 3 категории кнопок'
        verbose_name_plural = 'Изображения к 3 категории кнопок'


class FileThreeCategory(models.Model):
    """Модель хранения изображений описания кнопок третьей категории."""

    parent = models.ForeignKey(MessageThreeCategory, on_delete=models.CASCADE, verbose_name='сообщение')
    image = models.FileField(upload_to='file/three_category', verbose_name='документы к сообщению')

    class Meta:
        verbose_name = 'Документ к 3 категории кнопок'
        verbose_name_plural = 'Документы к 3 категории кнопок'


class WelcomeMessage(models.Model):
    """Модель хранения приветственного сообщения после регистрации пользователя в боте."""
    message = models.TextField(verbose_name='сообщение')

    class Meta:
        verbose_name = '6. Приветственное сообщение'
        verbose_name_plural = '6. Приветственное сообщение'


class ErrorMessage(models.Model):
    """Модель хранения сообщения об ошибке после рандомного ввода текста пользователем в боте."""
    message = models.TextField(verbose_name='сообщение')

    class Meta:
        verbose_name = '7. Сообщение об ошибке ввода'
        verbose_name_plural = '7. Сообщение об ошибке ввода'
