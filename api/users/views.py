from django.shortcuts import render
from .serializers import CustomUserSerializer
from rest_framework import generics

from .models import CustomUser

def defaultPage(requests):
    return render(requests, 'users/defaultPage.html')



class UsersAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class GetUserDetailAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = "pk"