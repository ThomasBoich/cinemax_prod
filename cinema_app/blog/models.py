from django.db import models

# Create your models here.
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField("Заголовок", max_length=255,blank=True)
    description = models.CharField("Описание", max_length=255,blank=True)
    content = models.TextField("Текст статьи", blank=True)
    photo = models.ImageField("Картинка", upload_to="images/%Y/%m/%d/")
    time_create = models.DateTimeField("Дата создания", auto_now_add=True)
    time_update = models.DateTimeField("Дата обновления", auto_now=True)
    is_published = models.BooleanField("Опубликовано", default=True,blank=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['time_create']


class Category(models.Model):
    title = models.CharField('Название категории', max_length=140, db_index=True)
    content = models.CharField('Описание категории', max_length=140,blank=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, null=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('category',kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
