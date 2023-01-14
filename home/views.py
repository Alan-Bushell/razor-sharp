from django.shortcuts import render
from blog.models import Post

# Create your views here.


def index(request):
    """ A view to return index page """

    return render(request, 'home/index.html')


def handle_404_error(request, exception):
    """View to return 404 if page not found"""
    template = 'home/templates/home/404.html'
    return render(request, template, {})
