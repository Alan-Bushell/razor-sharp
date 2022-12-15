from django.shortcuts import render

# Create your views here.


def profile(request):
    """ A view to return profile page """
    return render(request, 'accounts/account.html')
