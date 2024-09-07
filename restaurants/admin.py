from django.contrib import admin
from .models import Restaurant, Menu, MenuItem


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant_type', 'location', 'phone', 'owner')
    search_fields = ('name', 'location', 'phone', 'owner')
    list_filter = ('restaurant_type',)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_category', 'restaurant')
    search_fields = ('name', 'menu_category', 'restaurant')
    list_filter = ('menu_category',)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'menu')
    search_fields = ('name', 'price', 'menu')
    list_filter = ('menu',)


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
