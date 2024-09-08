from django.contrib import admin
from .models import Restaurant, Menu, MenuItem

# customizing and registering the Restaurant, Menu, and MenuItem models to show in admin panel


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant_type', 'location', 'phone', 'owner')
    search_fields = ('name', 'location', 'phone', 'owner')
    list_filter = ('restaurant_type',)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant')
    search_fields = ('name', 'restaurant')
    list_filter = ('restaurant',)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available_stock', 'order_count', 'menu')
    search_fields = ('name', 'price', 'menu')
    list_filter = ('menu',)


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
