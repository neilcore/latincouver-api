from rest_framework import serializers
from rest_framework.fields import CharField

class UserPublicSerializer(serializers.Serializer):
    username = CharField(read_only=True)
    first_name = CharField(read_only=True)
    last_name = CharField(read_only=True)