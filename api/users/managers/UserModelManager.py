from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models

class CustomUserQuerySet(models.QuerySet):

    def search(self, queries, user=None):

        first_name = queries.pop("first_name", None)
        last_name = queries.pop("last_name", None)

        new_query = dict(queries)

        if first_name is not None:
            new_query.update({"first_name__icontains": first_name})

        if last_name is not None:
            new_query.update({"last_name__icontains": last_name})


        print(new_query)
        return self.filter(**new_query)
    


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, **extra_fields):


        if not email:
            raise ValueError(_("Email"))

        if not first_name:
            raise ValueError(_("First name is required"))

        if not last_name:
            raise ValueError(_("Last name is required"))
        

        email = self.normalize_email(email)

        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(
            email, first_name, last_name, password,
            **extra_fields
        )
    

    def get_queryset(self, *args, **kwaargs):
        return CustomUserQuerySet(self.model, using=self._db)
