from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category,Comment


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'online_shop/home.html', {'products': products,
                                                     'categories': categories})

def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        comments = Comment.objects.filter(product=product_id)
        return render(request, 'online_shop/detail.html', {'product': product, 'comments': comments})
    except:
        return HttpResponse('Product not found',status=404)


