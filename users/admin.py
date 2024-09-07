from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'phone', 'role', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'phone')
    list_filter = ('role', 'is_staff', 'is_superuser')

    fieldsets = BaseUserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('phone', 'address', 'role')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('phone', 'address', 'role')}),
    )


admin.site.register(User, UserAdmin)
