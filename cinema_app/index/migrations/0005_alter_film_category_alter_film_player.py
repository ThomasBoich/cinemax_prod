# Generated by Django 4.1 on 2022-09-09 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0004_photo_alter_film_category_alter_film_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="film",
            name="category",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="films",
                to="index.category",
                verbose_name="Жанр",
            ),
        ),
        migrations.AlterField(
            model_name="film",
            name="player",
            field=models.TextField(
                blank=True, max_length=1000, verbose_name="Ссылка на плэер"
            ),
        ),
    ]
