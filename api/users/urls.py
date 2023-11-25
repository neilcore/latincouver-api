from django.urls import path
from . import views

# from dj_rest_auth.registration.views import RegisterView

# from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


    # path("register/", RegisterView.as_view(), name="rest_register"),
    path('api/v1/users/', views.UsersAPIView.as_view(), name="users"),
]