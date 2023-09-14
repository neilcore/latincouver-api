from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "first_name", "last_name", "is_staff", "is_active",)
    list_filter = ("username", "is_staff", "is_active",)
    fieldsets = (
        ("Personal Information", {"fields": ("username", "first_name", "last_name", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        ("Personal Information", {
            "classes": ("wide",),
            "fields": (
                "username", "first_name", "last_name", "password1", "password2"
            )}
        ),
        ("Permissions", {
            "classes": ("wide",),
            "fields": (
                "is_staff", "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("username", "last_name")
    ordering = ("username",)


admin.site.register(CustomUser, CustomUserAdmin)
