from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Product, Category,Comment,Order
from typing import Optional


def index(request, category_id: Optional[int] = None):
    categories = Category.objects.all().order_by('id')
    if category_id:
        products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.all()

    return render(request, 'online_shop/home.html', {'products': products,
                                                     'categories': categories})

def product_detail(request, product_id):

        product = Product.objects.get(id=product_id)
        comments = Comment.objects.filter(product=product_id,is_provide=True).order_by('-id')
        return render(request, 'online_shop/detail.html', {'product': product, 'comments': comments})

def add_comment(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    if request.method == 'POST':
        user = request.POST.get('user')
        email = request.POST.get('email')
        content = request.POST.get('content')
        comment = Comment(user=user,email=email,content=content)
        comment.product = product
        comment.save()
        return redirect('detail', product_id)
    else:
        pass
    return render(request,'online_shop/detail.html')

def add_order(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    if request.method == 'POST':
        user = request.POST.get('user')
        email = request.POST.get('email')
        quantity = request.POST.get('quantity')
        total_price = request.POST.get('total_price')
        order = Order(user=user,email=email, quantity=quantity, total_price=total_price)
        order.product = product
        order.save()
        return redirect('detail', product_id)
    else:
        pass
    return render(request,'online_shop/detail.html')


