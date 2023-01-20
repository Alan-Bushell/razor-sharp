"""razor_sharp URL Configuration"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from myapp.views import handle_404_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profiles/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('checkout/', include('checkout.urls')),
    path('cart/', include('cart.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'home.views.handle_404_error'





urlpatterns = [
    path('', include('myapp.urls')),
    path('admin/', admin.site.urls),
    # other url patterns go here...
]

handler404 = custom_404
handler500 = custom_500