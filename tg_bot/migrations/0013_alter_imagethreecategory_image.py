# Generated by Django 4.2 on 2023-04-27 22:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tg_bot", "0012_errormessage_welcomemessage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagethreecategory",
            name="image",
            field=models.ImageField(
                upload_to="image_bottom/three_category",
                verbose_name="изображение к сообщению",
            ),
        ),
    ]
