from django.shortcuts import render
from .serializers import CustomUserSerializer
from rest_framework import generics

from .models import CustomUser



class UsersAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        queries = {}

        if self.request.GET.get("is_active"):
            queries['is_active'] = True if self.request.GET.get("is_active").lower() == "true" else False

        if self.request.GET.get("first_name"):
            queries['first_name'] = self.request.GET.get("first_name")

        if self.request.GET.get("last_name"):
            queries['last_name'] = self.request.GET.get("last_name")

        if self.request.GET.get("user_email"):
            queries['email'] = self.request.GET.get("user_email")

        if queries:
            return qs.search(queries)
        return qs