from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.

admin.site.register(Cart)
admin.site.register(CartItem)

# While I have not added anything of note to the cart admin
# I could display users who had items in cart.
# A thought I considered was emailing customers who had items
# in their cart to remind or encourage checkout.
# Could offer small discount for time sensitive purchase.
# Will revisit.
