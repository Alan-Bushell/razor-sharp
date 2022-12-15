from django.shortcuts import render
from .models import Product

# Create your views here.


def products(request):
    """ A view to return products page """
    
    return render(request, 'products/products.html')
