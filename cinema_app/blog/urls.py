from django.urls import path
from .views import *

urlpatterns = [
    path('', blogShow, name='blog'),
    path('<int:post_id>/', postshow, name='postshow'),
]