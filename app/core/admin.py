"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        """Make email read-only when editing an existing user."""
        if obj:  # If the user object exists, we are editing
            return ['email', 'last_login']  # Make email read-only
        return super().get_readonly_fields(request, obj)


admin.site.register(models.User, UserAdmin)
