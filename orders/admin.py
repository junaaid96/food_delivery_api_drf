from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurant', 'status', 'payment_method',
                    'total_items', 'total_price', 'created_at')
    search_fields = ('user', 'restaurant', 'status', 'payment_method',
                     'total_items', 'total_price', 'created_at', 'updated_at')
    list_filter = ('status', 'payment_method')


admin.site.register(Order, OrderAdmin)
