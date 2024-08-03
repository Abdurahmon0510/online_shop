from typing import Optional
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentModelForm, OrderModelForm, ProductModelForm
from .models import Product, Category, Comment
from django.contrib.auth.decorators import login_required


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
        form = CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
           comment = form.save(commit=False)
           comment.product = product
           comment.save()
           return redirect('detail', product_id)

    else:
        form = CommentModelForm()
    return render(request,'online_shop/detail.html', {'product': product, 'form': form})

def add_order(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    form=OrderModelForm()
    if request.method == 'POST':

       form=OrderModelForm(request.POST)
       if form.is_valid():
           order = form.save(commit=False)
           order.product = product
           if product.quantity > order.quantity:
               product.quantity -= order.quantity
               product.save()
               order.save()

               messages.add_message(request, level=messages.SUCCESS, message='Your order is successfully saved!')
               return redirect('detail', product_id)
           else:

             messages.add_message(
             request, level=messages.ERROR, message='Your order  is not available!'
        )

    context = {'product': product, 'form': form}
    return render(request, 'online_shop/detail.html', context)
@login_required
def add_product(request):
    form = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'online_shop/add_product.html', context)
@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    if product:
        product.delete()
        return redirect('index')
@login_required
def edit_product(request, product_id):
     product = get_object_or_404(Product,id=product_id)
     form = ProductModelForm(instance=product)
     if request.method == 'POST':
         form = ProductModelForm(request.POST, request.FILES, instance=product)
         if form.is_valid():
             form.save()
             return redirect('detail', product_id)
     return render(request, 'online_shop/edit_product.html', {'product': product, 'form': form})
