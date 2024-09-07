from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'role')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('role',)


admin.site.register(User, UserAdmin)
