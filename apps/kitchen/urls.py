from django.urls import path

from .views import *


urlpatterns = [
    path('products/', products_list, name = 'products-list'),
]