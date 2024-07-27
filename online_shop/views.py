
from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'online_shop/home.html', {'products': products})

def product_detail(request):
    return render(request, 'online_shop/detail.html')

