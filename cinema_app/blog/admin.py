from django.contrib import admin
from blog.models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'time_update', 'is_published', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    ordering = ('id',)
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    ordering = ('id',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category,CategoryAdmin)
