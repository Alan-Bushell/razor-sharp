from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category

# Create your views here.


def products(request, category_slug=None):
    """ A view to return products page """
    categories = None
    products = None

    if category_slug is None:
        products = Product.objects.all().filter(in_stock=True)
        product_count = products.count()
    else:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories,
                                          in_stock=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, category_slug, product_slug):
    """ A view to show individual product details """
    try:
        product = Product.objects.get(category__slug=category_slug,
                                      slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
