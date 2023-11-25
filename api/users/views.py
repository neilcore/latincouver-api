from django.shortcuts import render
from .serializers import CustomUserSerializer
from rest_framework import generics

from .models import CustomUser



# authentication/views.py

# from django.conf import settings
# from django.http import HttpResponseRedirect

def defaultPage(requests):
    return render(requests, 'users/defaultPage.html')



class UsersAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer



# retrieve | update | delete
class UserRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = "pk"



# def email_confirm_redirect(request, key):
#     return HttpResponseRedirect(
#         f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{key}/"
#     )


# def password_reset_confirm_redirect(request, uidb64, token):
#     return HttpResponseRedirect(
#         f"{settings.PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL}{uidb64}/{token}/"
#     )