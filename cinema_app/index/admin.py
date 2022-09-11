from django.contrib import admin
from index.models import Film, Category, Photo, Artist, Director, Genre


class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','date','time_create', 'rating', 'time_update', 'is_published', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'content')
    list_editable = ('is_published','rating','date')
    list_filter = ('is_published','category')
    ordering = ('id',)
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['artists']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    ordering = ('id',)
    prepopulated_fields = {'slug': ('title',)}


class AdminPhoto(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    ordering = ('id',)


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'age', 'country')
    list_display_links = ('id', 'name', 'surname')
    search_fields = ('id', 'name', 'age', 'country')
    list_editable = ()
    list_filter = ('name', 'surname')
    ordering = ('id',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    ordering = ('id',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Film, FilmAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Photo, AdminPhoto)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Director)
admin.site.register(Genre, GenreAdmin)