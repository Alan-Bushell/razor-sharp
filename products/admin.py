from django.contrib import admin
from .models import Category, Product, Review
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


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'subject',
                    'review', 'status', 'created_at')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
