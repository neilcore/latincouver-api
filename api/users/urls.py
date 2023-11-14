from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/users/', views.UsersAPIView.as_view(), name="users"),
    path('api/v1/users/user/<int:pk>/', views.GetUserDetailAPIView.as_view(), name="user-detail"),
]