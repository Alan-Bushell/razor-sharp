from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.
from .forms import Order


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'There is nothing in your cart')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = checkout/checkout.html
    context = {
        'order_form': order_form
    }

    return render(request, template, context)
