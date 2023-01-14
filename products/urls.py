from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('<slug:category_slug>', views.products, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',
         views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('submit_review/<int:product_id>',
         views.submit_review, name='submit_review'),
    path('edit/<int:product_id>', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>',
         views.delete_product, name='delete_product'),
]
