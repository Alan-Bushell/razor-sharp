from .models import Category


def nav_menu(request):
    menu = Category.objects.all()
    return dict(menu=menu)
