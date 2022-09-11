# Generated by Django 4.1 on 2022-09-09 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0010_remove_film_year_in_school_alter_film_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="film",
            name="rating",
            field=models.CharField(
                blank=True,
                choices=[("0+", "0+"), ("12+", "12+"), ("18+", "18+")],
                default="0+",
                max_length=200,
                null=True,
                verbose_name="Рейтинг",
            ),
        ),
    ]