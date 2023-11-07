from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin): 
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "middle_name", "email")}),
        (_("Permissions"),{"fields": ("is_active", "is_staff", "is_superuser", "is_deleted", "groups", "user_permissions",),},),
        (_("Important dates"), {"fields": ("first_login", "last_login", "date_joined")}),
        (_("Custom info"), {"fields": ("phone", "avatar")}),
    )
