from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurant', 'menu_item', 'quantity',
                    'total_price', 'payment_method', 'status',)
    list_filter = ('status', 'payment_method',)
    search_fields = ('user__username', 'restaurant__name', 'menu_item__name',)

admin.site.register(Order, OrderAdmin)