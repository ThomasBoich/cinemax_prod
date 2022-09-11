from django import forms
from django.core.exceptions import ValidationError
from .models import *


class AddFilmForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выбрать категорию'

    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'content': forms.TextInput(attrs={'class': 'form-control', }),
            'slug': forms.TextInput(attrs={'class': 'form-control', }),
            'category': forms.Select(attrs={'class': 'form-select', }),
            'photo': forms.FileInput(attrs={'class': 'form-file-label', }),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input', }),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if len(slug) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return slug

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return content


class AddCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['title', 'content', 'slug'] ##'__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'content': forms.TextInput(attrs={'class': 'form-control', }),
            'slug': forms.TextInput(attrs={'class': 'form-control', }),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if len(slug) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return slug

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return content