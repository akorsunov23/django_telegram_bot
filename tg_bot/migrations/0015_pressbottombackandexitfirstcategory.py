# Generated by Django 4.2 on 2023-04-28 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("tg_bot", "0014_pressbottomfirstcategory"),
    ]

    operations = [
        migrations.CreateModel(
            name="PressBottomBackAndExitFirstCategory",
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
