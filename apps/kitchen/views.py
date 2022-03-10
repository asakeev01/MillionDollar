from django.shortcuts import render

from .models import *

def products_list(request):
    all_products = Product.objects.all()
    return render(request, 'index.html', locals())

