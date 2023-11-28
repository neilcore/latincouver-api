from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


class EmployeeQuerySet(models.QuerySet):

    def search(self, queries, user=None):

        is_active = queries.pop("is_active", None)
        first_name = queries.pop("first_name", None)
        last_name = queries.pop("last_name", None)
        email = queries.pop("user_email", None)
        title = queries.pop("title", None)
        departments = queries.pop("department", None)

        new_query = dict(queries)

        if departments is not None:
            try:
                int(departments[0])
            except:
                departments = [name.lower() for name in departments]
                new_query.update({"department__name__in": departments})
            else:
                new_query.update({"department__id__in": departments})


        if title is not None:
            try:
                int(title)
            except:
                new_query.update({"title__name__iexact": title.lower()})
            else:
                new_query.update({"title__id__exact": title})

        if first_name is not None:
            #new_query.update({"user__first_name__iexact": first_name})
            new_query.update({"user__first_name__icontains": first_name})

        if last_name is not None:
            #new_query.update({"user__last_name__iexact": last_name})
            new_query.update({"user__last_name__icontains": last_name})

        if email is not None:
            new_query.update({"user__email__iexact": email})

        if is_active is not None:
            new_query.update({"user__is_active": is_active})


        return self.filter(**new_query)
        



class EmployeeManager(models.Manager):

    def get_queryset(self, *args, **kwaargs):
        return EmployeeQuerySet(self.model, using=self._db)