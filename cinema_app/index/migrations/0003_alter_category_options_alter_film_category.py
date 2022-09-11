# Generated by Django 4.1 on 2022-09-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0002_alter_category_content_alter_film_description_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["title"],
                "verbose_name": "Жанр",
                "verbose_name_plural": "Жанры",
            },
        ),
        migrations.AlterField(
            model_name="film",
            name="category",
            field=models.ManyToManyField(
                null=True, to="index.category", verbose_name="Жанр"
            ),
        ),
    ]
