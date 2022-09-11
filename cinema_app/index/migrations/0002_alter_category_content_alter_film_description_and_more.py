# Generated by Django 4.1 on 2022-08-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='content',
            field=models.CharField(blank=True, max_length=140, verbose_name='Описание категории'),
        ),
        migrations.AlterField(
            model_name='film',
            name='description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='film',
            name='is_published',
            field=models.BooleanField(blank=True, default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='film',
            name='photo',
            field=models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='film',
            name='player',
            field=models.TextField(blank=True, max_length=255, verbose_name='Ссылка на плэер'),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Заголовок'),
        ),
    ]