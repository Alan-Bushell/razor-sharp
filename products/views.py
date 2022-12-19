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


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
