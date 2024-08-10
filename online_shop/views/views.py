from typing import Optional
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from online_shop.forms import CommentModelForm, OrderModelForm, ProductModelForm
from online_shop.models import Product, Category, Comment
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def index(request, category_slug: Optional[str] = None):
    products = Product.objects.all()
    categories = Category.objects.all().order_by('id')
    search = request.GET.get('q')
    filter_type = request.GET.get('filter')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        if filter_type == 'expensive':
            products = Product.objects.filter(category=category).order_by('-price')
        elif filter_type == 'cheap':
            products = Product.objects.filter(category=category).order_by('price')
        elif filter_type == 'rating':
            products = Product.objects.filter(Q(category=category) & Q(rating__gte=3)).order_by('-rating')
        else:
            products = Product.objects.filter(category=category)
    else:
        if filter_type == 'expensive':
            products = Product.objects.all().order_by('-price')
        elif filter_type == 'cheap':
            products = Product.objects.all().order_by('price')
        elif filter_type == 'rating':
            products = Product.objects.filter(Q(rating__gte=3)).order_by('-rating')
        else:
            products = Product.objects.all()

    if search:
        products = products.filter(Q(name__icontains=search) | Q(comments__content__icontains=search))

    return render(request, 'online_shop/home.html', {'products': products, 'categories': categories})


def product_detail(request, product_slug):
    categories = Category.objects.all().order_by('id')
    product = get_object_or_404(Product, slug=product_slug)
    min_price = product.price * 0.2
    max_price = product.price * 1.8

    related_products = Product.objects.filter(category=product.category, price__range=(min_price, max_price)).exclude(
        slug=product_slug)
    comments = Comment.objects.filter(product=product, is_provide=True).order_by('-id')
    search = request.GET.get('q')

    if search:
        comments = comments.filter(Q(content__icontains=search) | Q(user__username__icontains=search))

    context = {
        'product': product,
        'comments': comments,
        'categories': categories,
        'related_products': related_products
    }
    return render(request, 'online_shop/detail.html', context)


def add_comment(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('detail', product_slug=product_slug)
    else:
        form = CommentModelForm()

    return render(request, 'online_shop/detail.html', {'product': product, 'form': form})


def add_order(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    form = OrderModelForm()

    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            if product.quantity >= order.quantity:
                product.quantity -= order.quantity
                product.save()
                order.save()

                messages.success(request, 'Your order is successfully saved!')
                return redirect('detail', product_slug=product_slug)
            else:
                messages.error(request, 'Your order is not available!')

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
def delete_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    product.delete()
    return redirect('index')


@login_required
def edit_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    form = ProductModelForm(instance=product)

    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('detail', product_slug=product_slug)

    return render(request, 'online_shop/edit_product.html', {'product': product, 'form': form})
