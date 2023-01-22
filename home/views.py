from django.shortcuts import render
from blog.models import Post

# Create your views here.


def index(request):
    """ A view to return index page """

    return render(request, 'home/index.html')


def privacy(request):
    """ A view to return the privacy policy page """

    return render(request, 'home/privacy.html')
