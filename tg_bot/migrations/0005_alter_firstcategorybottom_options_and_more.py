# Generated by Django 4.2 on 2023-04-27 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("tg_bot", "0004_alter_firstcategorybottom_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="firstcategorybottom",
            options={
                "verbose_name": "1. Первая категория кнопок",
                "verbose_name_plural": "1. Первая категория кнопок",
            },
        ),
        migrations.AlterModelOptions(
            name="threecategorybottom",
            options={
                "verbose_name": "3. Третья категория кнопок",
                "verbose_name_plural": "3. Третья категория кнопок",
            },
        ),
        migrations.AlterModelOptions(
            name="twocategorybottom",
            options={
                "verbose_name": "2. Вторая категория кнопок",
                "verbose_name_plural": "2. Вторая категория кнопок",
            },
        ),
        migrations.RemoveField(
            model_name="firstcategorybottom",
            name="descriptions",
        ),
        migrations.CreateModel(
            name="FinalMessage",
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
                ("descriptions", models.TextField(verbose_name="описание кнопки")),
                (
                    "image",
                    models.ImageField(
                        upload_to="massage_image/",
                        verbose_name="изображение к сообщению",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="tg_bot.threecategorybottom",
                        verbose_name="родительская кнопка",
                    ),
                ),
            ],
            options={
                "verbose_name": "4. Сообщение к 3 категории кнопок",
                "verbose_name_plural": "4. Сообщения к 3 категории кнопок",
            },
        ),
    ]
