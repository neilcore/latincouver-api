from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, password, **extra_fields):

        if not username:
            raise ValueError(_("Username is required"))

        if not first_name:
            raise ValueError(_("First name is required"))

        if not last_name:
            raise ValueError(_("Last name is required"))

        user = self.model(username=username, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, username, first_name, last_name, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(
            username, first_name, last_name, password,
            **extra_fields
        )
