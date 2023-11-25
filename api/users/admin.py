from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("first_name", "last_name", "email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        ("Personal Information", {"fields": ("first_name", "last_name", "email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        ("Personal Information", {
            "classes": ("wide",),
            "fields": (
                "first_name", "last_name", "email", "password1", "password2"
            )}
        ),
        ("Permissions", {
            "classes": ("wide",),
            "fields": (
                "is_staff", "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("first_name", "last_name", "email")
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
