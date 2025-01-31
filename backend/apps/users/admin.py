from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = [
        "full_name",
        "email",
        "username",
        "last_login",
        "date_joined",
    ]

    fieldsets = (
        ("Basic Credentials", {"fields": ("username", "email", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            "Basic Credentials",
            {"fields": ("username", "email", "password1", "password2")},
        ),
        ("Personal Information", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )


admin.site.register(User, CustomUserAdmin)
