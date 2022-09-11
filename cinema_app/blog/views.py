from django.shortcuts import render
from .models import Blog


def blogShow(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
        'title': 'Новости'
    }
    return render(request, 'blog/index.html', context=context)


def postshow(request, post_id):
    post = Blog.objects.filter(pk=post_id)
    context = {
        'post': post,
    }
    return render(request, 'blog/postshow.html', context=context)