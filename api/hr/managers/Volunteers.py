from django.db import models
from django.db.models import Q


class VolunteerQuerySet(models.QuerySet):

    def search(self, queries, user=None):

        is_active = queries.pop("is_active", None)
        first_name = queries.pop("first_name", None)
        last_name = queries.pop("last_name", None)
        email = queries.pop("user_email", None)
        application_first_name = queries.pop("application_first_name", None)
        application_last_name = queries.pop("application_last_name", None)
        application_email = queries.pop("application_email", None)

        new_query = dict(queries)

        if first_name is not None:
            new_query.update({"user__first_name__icontains": first_name})

        if last_name is not None:
            new_query.update({"user__last_name__icontains": last_name})

        if email is not None:
            new_query.update({"user__email__iexact": email})

        if is_active is not None:
            new_query.update({"user__is_active": is_active})

        if application_first_name is not None:
            new_query.update({
                "application__first_name__icontains":
                application_first_name
            })

        if application_last_name is not None:
            new_query.update({
                "application__last_name__icontains":
                application_last_name
            })

        if application_email is not None:
            new_query.update({
                "application__email__iexact":
                application_email
            })
        
        return self.filter(**new_query)
        
class VolunteerManager(models.Manager):

    def get_queryset(self, *args, **kwaargs):
        return VolunteerQuerySet(self.model, using=self._db)