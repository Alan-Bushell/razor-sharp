from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('shipping_details/', views.shipping_details, name='shipping_details'),
]
