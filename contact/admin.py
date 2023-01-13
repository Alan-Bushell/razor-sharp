from django.contrib import admin
from .models import Contact

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Add contact filters to admin panel"""
    list_display = ('email', 'subject', 'message', 'reason')
    list_filter = ('email', 'reason')
    search_fields = ('email', 'reason')
