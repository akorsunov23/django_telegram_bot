# Generated by Django 4.2 on 2023-04-26 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("tg_bot", "0003_firstcategorybottom"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="firstcategorybottom",
            options={
                "verbose_name": "Первая категория кнопок",
                "verbose_name_plural": "Первая категория кнопок",
            },
        ),
        migrations.AddField(
            model_name="firstcategorybottom",
            name="descriptions",
            field=models.TextField(default="ok", verbose_name="описание кнопки"),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="TwoCategoryBottom",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="название кнопки"
                    ),
                ),
                ("descriptions", models.TextField(verbose_name="описание кнопки")),
                (
                    "image",
                    models.ImageField(
                        upload_to="image_bottom/", verbose_name="изображение к кнопки"
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="tg_bot.firstcategorybottom",
                        verbose_name="родительская кнопка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вторая категория кнопок",
                "verbose_name_plural": "Вторая категория кнопок",
            },
        ),
        migrations.CreateModel(
            name="ThreeCategoryBottom",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="название кнопки"
                    ),
                ),
                ("descriptions", models.TextField(verbose_name="описание кнопки")),
                (
                    "image",
                    models.ImageField(
                        upload_to="image_bottom/", verbose_name="изображение к кнопки"
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="tg_bot.twocategorybottom",
                        verbose_name="родительская кнопка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вторая категория кнопок",
                "verbose_name_plural": "Вторая категория кнопок",
            },
        ),
    ]
