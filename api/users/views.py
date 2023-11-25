from django.shortcuts import render
from .serializers import CustomUserSerializer
from rest_framework import generics

from .models import CustomUser



# authentication/views.py

# from django.conf import settings
# from django.http import HttpResponseRedirect



class UsersAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer