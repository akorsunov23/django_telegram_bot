# Generated by Django 4.2 on 2023-04-28 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("tg_bot", "0015_pressbottombackandexitfirstcategory"),
    ]

    operations = [
        migrations.CreateModel(
            name="PressBottomTwoCategory",
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
                    "count",
                    models.IntegerField(default=0, verbose_name="количество нажатий"),
                ),
                (
                    "bottom",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tg_bot.twocategorybottom",
                        verbose_name="кнопка",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tg_bot.telegramuser",
                        verbose_name="пользователь",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PressBottomThreeCategory",
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
                    "count",
                    models.IntegerField(default=0, verbose_name="количество нажатий"),
                ),
                (
                    "bottom",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tg_bot.threecategorybottom",
                        verbose_name="кнопка",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tg_bot.telegramuser",
                        verbose_name="пользователь",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PressBottomBackAndExitTwoCategory",
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
                    "name_bottom",
                    models.CharField(max_length=100, verbose_name="кнопка"),
                ),
                (
                    "count",
                    models.IntegerField(default=0, verbose_name="количество нажатий"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tg_bot.telegramuser",
                        verbose_name="пользователь",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PressBottomBackAndExitThreeCategory",
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
                    "name_bottom",
                    models.CharField(max_length=100, verbose_name="кнопка"),
                ),
                (
                    "count",
                    models.IntegerField(default=0, verbose_name="количество нажатий"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tg_bot.telegramuser",
                        verbose_name="пользователь",
                    ),
                ),
            ],
        ),
    ]
