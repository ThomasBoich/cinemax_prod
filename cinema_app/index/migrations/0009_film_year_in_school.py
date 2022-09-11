# Generated by Django 4.1 on 2022-09-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0008_film_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="film",
            name="year_in_school",
            field=models.CharField(
                blank=True,
                choices=[
                    ("FRESHMAN", "Freshman"),
                    ("SOPHOMORE", "Sophomore"),
                    ("JUNIOR", "Junior"),
                    ("SENIOR", "Senior"),
                    ("GRADUATE", "Graduate"),
                ],
                max_length=199,
            ),
        ),
    ]