from django.shortcuts import render
from checkout.models import Order


# Create your views here.


def accounts(request):
    """ A view to return profile page """
    return render(request, 'accounts/account.html')


def shipping_details(request):
    """ A view to return profile page """
    return render(request, 'accounts/shipping_details.html')


def order_history(request):
    """ A view to return profile page """
    orders = Order.objects.all()
    template = 'accounts/order_history.html'
    context = {
        'orders': orders
    }
    return render(request, template, context)
