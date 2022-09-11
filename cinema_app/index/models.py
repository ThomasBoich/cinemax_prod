from django.db import models
from django.urls import reverse


class Film(models.Model):

    PG0 = '0+'
    PG12 = '12+'
    PG18 = '18+'

    RATING = [
        (PG0, '0+'),
        (PG12, '12+'),
        (PG18, '18+'),
    ]

    title = models.CharField("Заголовок", max_length=255,blank=True)
    description = models.CharField("Описание", max_length=255,blank=True)
    meta_description = models.CharField("meta_descriptions", max_length=299, blank=True)
    meta_keyword = models.CharField("meta_keywords", max_length=299, blank=True)
    player = models.TextField("Ссылка на плэер", max_length=1000, blank=True)
    date = models.IntegerField("Дата выхода", blank=True)
    content = models.TextField("Текст статьи", blank=True)
    photo = models.ImageField("Картинка", upload_to="images/%Y/%m/%d/", blank=True)
    time_create = models.DateTimeField("Дата создания", auto_now_add=True)
    time_update = models.DateTimeField("Дата обновления", auto_now=True)
    is_published = models.BooleanField("Опубликовано", default=True, blank=True)
    category = models.ForeignKey('Category', null=True, verbose_name="Категория", related_name="films", blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')
    artists = models.ManyToManyField("Artist", null=True, blank=True, related_name="films")
    country = models.CharField("Страна", null=True, blank=True, max_length=200)
    rating = models.CharField("Рейтинг", null=True, blank=True, max_length=200, choices=RATING, default=PG0)
    director = models.ForeignKey("Director", null=True, on_delete=models.CASCADE, related_name="films", blank=True)
    genre = models.ManyToManyField("Genre", null=True, related_name="films", blank=True)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['time_create']


class Genre(models.Model):
    title = models.CharField('Название жанра', max_length=140, db_index=True)
    content = models.CharField('Описание жанра', max_length=140, blank=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, null=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('category', kwargs={'genre_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['title']


class Category(models.Model):
    title = models.CharField('Название категории', max_length=140, db_index=True)
    content = models.CharField('Описание категории', max_length=140,blank=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, null=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Role(models.Model):
    role = models.CharField('Роль', max_length=140, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
        ordering = ['role']


class Photo(models.Model):
    photo = models.ImageField("Фото", upload_to="images/%Y/%m/%d/")
    title = models.CharField("Заголовок", max_length=255,blank=True)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Реклама'
        verbose_name_plural = 'Реклама'
        ordering = ['title']


class Artist(models.Model):
    name = models.CharField("Имя", max_length=200, blank=True)
    surname = models.CharField("Фамилия", max_length=200, blank=True)
    age = models.CharField("Возраст", max_length=200, blank=True)
    photo = models.ImageField("Фотография", upload_to="images/artists/%Y/%m/%d")
    country = models.CharField("Страна", max_length=199, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta():
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"
        ordering = ['name']


class Director(models.Model):
    name = models.CharField("Имя", max_length=299)
    surname = models.CharField("Фамилия", max_length=299)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta():
        verbose_name = "Режиссер"
        verbose_name_plural = "Режиссеры"
        ordering = ['name']
