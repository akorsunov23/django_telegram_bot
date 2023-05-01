import nested_admin
from django.contrib import admin
from .models import \
    TelegramUser, \
    AdminTelegramBot, \
    FirstCategoryBottom, \
    TwoCategoryBottom, \
    ThreeCategoryBottom, \
    MessageThreeCategory, \
    ImageFirstCategory, \
    ImageTwoCategory, \
    ImageThreeCategory, \
    WelcomeMessage, \
    ErrorMessage, \
    PressBottomFirstCategory, \
    PressBottomBackAndExitFirstCategory, \
    PressBottomTwoCategory, \
    PressBottomBackAndExitTwoCategory, \
    PressBottomThreeCategory, \
    PressBottomBackAndExitThreeCategory, \
    FileThreeCategory


HELP_TEXT = 'Для форматирования текста доступны следующие HTML тэги: ' \
            '&ltb&gtтекст&lt/b&gt - жирный, ' \
            '&lti&gtтекст&lt/i&gt - курсив, ' \
            '&ltu&gtтекст&lt/u&gt - подчёркнутый, ' \
            '&lts&gtтекст&lt/s&gt - зачеркнутый, ' \
            '&ltspan class="tg-spoiler"&gtтекст&lt/span&gt - скрытый, ' \
            '&lta href="ссылка"&gtтекст&lt/a&gt - гиперссылка, ' \
            'для эмодзи необходимо использовать их представление в HTML коде. ' \
            '{name} - используется для добавления имени пользователя. ' \
            '{message} - используется для добавления текста присланного сообщения.'


class ImageFirstInline(admin.TabularInline):
    model = ImageFirstCategory
    max_num = 1
    extra = 0


class ImageTwoInline(admin.TabularInline):
    model = ImageTwoCategory
    max_num = 1
    extra = 0


class ImageTreeInLine(nested_admin.NestedStackedInline):
    model = ImageThreeCategory
    extra = 0
    max_num = 3


class FileTreeInLine(nested_admin.NestedStackedInline):
    model = FileThreeCategory
    extra = 0
    max_num = 1


class MessageInline(nested_admin.NestedStackedInline):
    model = MessageThreeCategory
    extra = 0
    inlines = [ImageTreeInLine, FileTreeInLine, ]


class StatisticFirstBottom(admin.TabularInline):
    model = PressBottomFirstCategory
    extra = 0
    max_num = 0
    fields = 'bottom', 'count',
    readonly_fields = 'bottom', 'count',


class StatisticFirstBottomBackExit(admin.TabularInline):
    model = PressBottomBackAndExitFirstCategory
    extra = 0
    max_num = 0
    fields = 'name_bottom', 'count',
    readonly_fields = 'name_bottom', 'count',


class StatisticTwoBottom(admin.TabularInline):
    model = PressBottomTwoCategory
    extra = 0
    max_num = 0
    fields = 'bottom', 'count',
    readonly_fields = 'bottom', 'count',


class StatisticBottomBackAndExitTwo(admin.TabularInline):
    model = PressBottomBackAndExitTwoCategory
    extra = 0
    max_num = 0
    fields = 'name_bottom', 'count',
    readonly_fields = 'name_bottom', 'count',


class StatisticBottomThreeCategory(admin.TabularInline):
    model = PressBottomThreeCategory
    extra = 0
    max_num = 0
    fields = 'bottom', 'count',
    readonly_fields = 'bottom', 'count',


class StatisticBottomBackAndExitThreeCategory(admin.TabularInline):
    model = PressBottomBackAndExitThreeCategory
    extra = 0
    max_num = 0
    fields = 'name_bottom', 'count',
    readonly_fields = 'name_bottom', 'count',


@admin.register(TelegramUser)
class TgUsersAdmin(admin.ModelAdmin):
    """Регистрация модели зарегистрированных пользователей в телеграм."""
    inlines = (
        StatisticFirstBottom,
        StatisticFirstBottomBackExit,
        StatisticTwoBottom,
        StatisticBottomBackAndExitTwo,
        StatisticBottomThreeCategory,
        StatisticBottomBackAndExitThreeCategory
    )
    list_display = 'id', 'id_telegram', 'username', 'name', 'email', 'created_at',
    readonly_fields = 'id_telegram', 'username', 'name', 'email', 'created_at',

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(AdminTelegramBot)
class AdminBotAdmin(admin.ModelAdmin):
    """Регистрация модели администраторов в телеграм."""

    list_display = 'id', 'id_telegram', 'username',


@admin.register(FirstCategoryBottom)
class FirstBottomAdmin(admin.ModelAdmin):
    """Регистрация модели кнопок первой категории."""

    inlines = ImageFirstInline,
    list_display = 'id', 'name', 'descriptions',

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields['descriptions'].help_text = HELP_TEXT
        return form


@admin.register(TwoCategoryBottom)
class TwoBottomAdmin(admin.ModelAdmin):
    """Регистрация модели кнопок второй категории."""

    inlines = ImageTwoInline,
    list_display = 'id', 'parent', 'name', 'descriptions',

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields['descriptions'].help_text = HELP_TEXT
        return form


@admin.register(ThreeCategoryBottom)
class ThreeBottomAdmin(nested_admin.NestedModelAdmin):
    """Регистрация модели кнопок третьей категории."""

    inlines = MessageInline,
    list_display = 'id', 'parent', 'name',

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields['name'].help_text = HELP_TEXT
        return form


@admin.register(WelcomeMessage)
class WelcomeMessageAdmin(admin.ModelAdmin):
    """Регистрация модели приветственного сообщения пользователю."""

    list_display = 'message',

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields['message'].help_text = HELP_TEXT
        return form

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(ErrorMessage)
class ErrorMessageAdmin(admin.ModelAdmin):
    """Регистрация модели сообщение о рандомном вводе текста от пользователя."""

    list_display = 'message',

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields['message'].help_text = HELP_TEXT
        return form

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False
