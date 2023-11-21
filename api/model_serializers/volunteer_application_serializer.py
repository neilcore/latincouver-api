from rest_framework import serializers
from rest_framework.fields import CharField, EmailField


# from hr.models import Departments

class VolunteerApplicationPublicSerializer(serializers.Serializer):
    first_name = CharField(read_only=True)
    last_name = CharField(read_only=True)
    email = EmailField(read_only=True)
