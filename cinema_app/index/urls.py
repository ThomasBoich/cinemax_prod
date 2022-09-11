from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('show/<int:film_id>/', showfilm, name='showfilm'),
    path('addfilm/', add_page, name='addfilm'),
    path('<slug:cat_slug>/', ShowCategory, name='showcategory'),
]