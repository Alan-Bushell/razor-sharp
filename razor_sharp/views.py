
from django.shortcuts import render


def handler404(request, exception):
    """ 404 error Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """ 500 error Server Error """
    return render(request, "errors/500.html", status=500)
