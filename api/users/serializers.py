from rest_framework import serializers
from rest_framework.fields import CharField

from .models import CustomUser

class UserPublicSerializer(serializers.Serializer):
    # username = CharField(read_only=True)
    first_name = CharField(read_only=True)
    last_name = CharField(read_only=True)



class CustomUserSerializer(serializers.ModelSerializer):
    is_active = serializers.StringRelatedField(many=False)
    class Meta:
        model=CustomUser
        fields = ['id', 'is_active', 'date_joined', 'first_name', 'last_name', 'email']