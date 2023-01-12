from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm

# Create your views here.


def products(request, category_slug=None):
    """ A view to return products page """
    categories = None
    products = None
    query = None

    if category_slug is None:
        products = Product.objects.all().filter(in_stock=True)
        product_count = products.count()
    else:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories,
                                          in_stock=True)
        product_count = products.count()

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You did not enter any search creteria!")
                return redirect(reverse('products'))

            queries = Q(product_name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
        'search_term': query,
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

    template = 'products/product_detail.html'

    return render(request, template, context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ Edit a product """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.product_name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """Delete a product function"""
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, f"{product.product_name} has been deleted")
    return redirect(reverse('products'))
