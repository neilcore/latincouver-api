from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


class VolunteerApplicationQuerySet(models.QuerySet):

    def search(self, queries, user=None):

        area_volunteering = queries.pop("area_volunteering", None)
        status = queries.pop("status", None)
        first_name = queries.pop("first_name", None)
        last_name = queries.pop("last_name", None)
        skills = queries.pop("skills", None)
        interests = queries.pop("interests", None)

        new_query = dict(queries)


        if skills is not None:
            try:
                int(skills[0])
            except:
                skills = [name.lower() for name in skills]
                new_query.update({"skills__name__in": skills})
            else:
                new_query.update({"skills__id__in": skills})


        if area_volunteering is not None:
            try:
                int(area_volunteering)
            except:
                new_query.update({"area_volunteering__name__iexact": area_volunteering})
            else:
                new_query.update({"area_volunteering__id__exact": area_volunteering})

        if status is not None:
            new_query.update({"status__iexact": status})

        if first_name is not None:
            new_query.update({"first_name__iexact": first_name})

        if last_name is not None:
            new_query.update({"last_name__iexact": last_name})

        if interests is not None:
            new_query.update({"interests__icontains": interests})

        return self.filter(**new_query)
        



class VolunteerApplicationManager(models.Manager):

    def get_queryset(self, *args, **kwaargs):
        return VolunteerApplicationQuerySet(self.model, using=self._db)