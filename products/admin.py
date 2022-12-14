from django.contrib import admin
from .models import Category, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = (
        'friendly_name',
        'name',
        'slug',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category',
                    'last_modified', 'in_stock')
    prepopulated_fields = {'slug': ('product_name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
