from rest_framework import serializers
from rest_framework.fields import CharField


# from hr.models import Departments

class DepartmentsPublicSerializer(serializers.Serializer):
    name = CharField(read_only=True)