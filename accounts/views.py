from django.shortcuts import render

# Create your views here.


def accounts(request):
    """ A view to return profile page """
    return render(request, 'accounts/account.html')

def shipping_details(request):
    """ A view to return profile page """
    return render(request, 'accounts/shipping_details.html')
