from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import AddFilmForm
from .models import *


class Index(ListView):
    model = Film
    template_name = 'index/index.html'
    context_object_name = 'films'

    def get_context_data(self, **kwargs):
        kwargs = super(Index, self).get_context_data(**kwargs)
        photo = Photo.objects.all()
        kwargs.update({
            'photo': photo,
            'title': 'CINEMAX'
        })
        return kwargs


def showfilm(request, film_id):
    film = Film.objects.get(pk=film_id)
    meta_keywords = Film
    meta_description = Film
    context = {
        'film': film,
        'meta_keywords': meta_keywords,
        'meta_description': meta_description
    }
    return render(request, 'index/showfilm.html', context=context)


def add_page(request):
    if request.method == 'POST':
        form = AddFilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddFilmForm()
    return render(request, 'index/addpage.html', {'form': form, })


def ShowCategory(request, cat_slug):
    films = Film.objects.filter(slug=cat_slug)
    context = {'films': films, }
    return render(request, 'index/category.html', context=context)
