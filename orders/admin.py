from django.contrib import admin
from .models import Order

# OrderAdmin class to customize the admin interface for Order model
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurant', 'menu_item', 'quantity',
                    'total_price', 'payment_method', 'status',)
    list_filter = ('status', 'payment_method',)
    search_fields = ('user__username', 'restaurant__name', 'menu_item__name',)

# Registering the Order model and OrderAdmin class to show in admin panel
admin.site.register(Order, OrderAdmin)
