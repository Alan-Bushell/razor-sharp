from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('edit_profile/<user_id>', views.edit_profile, name='edit_profile'),
    path('edit_shipping/<user_id>', views.edit_shipping, name='edit_shipping'),
    path('edit_image/<user_id>', views.edit_image, name='edit_image'),
    path('shipping_details/', views.shipping_details, name='shipping_details'),
    path('order_history/', views.order_history, name='order_history'),
]
