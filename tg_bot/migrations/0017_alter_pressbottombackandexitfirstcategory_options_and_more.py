# Generated by Django 4.2 on 2023-04-28 12:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tg_bot", "0016_pressbottomtwocategory_pressbottomthreecategory_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pressbottombackandexitfirstcategory",
            options={
                "verbose_name_plural": "Статистика нажатия кнопок первой категории"
            },
        ),
        migrations.AlterModelOptions(
            name="pressbottombackandexitthreecategory",
            options={
                "verbose_name_plural": "Статистика нажатия кнопок третьей категории"
            },
        ),
        migrations.AlterModelOptions(
            name="pressbottombackandexittwocategory",
            options={
                "verbose_name_plural": "Статистика нажатия кнопок второй категории"
            },
        ),
        migrations.AlterModelOptions(
            name="pressbottomfirstcategory",
            options={
                "verbose_name_plural": "Статистика нажатия кнопок первой категории"
            },
        ),
        migrations.AlterModelOptions(
            name="pressbottomthreecategory",
            options={
                "verbose_name_plural": "Статистика нажатия кнопок третьей категории"
            },
        ),
        migrations.AlterModelOptions(
            name="pressbottomtwocategory",
            options={
                "verbose_name_plural": "Статистика нажатия кнопок второй категории"
            },
        ),
    ]
