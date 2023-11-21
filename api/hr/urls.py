from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    # token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Employees
    path('api/v1/hr/employees/', views.EmployeeListCreateAPIView.as_view(), name="hr-employees"),
    path('api/v1/hr/employees/<int:pk>/', views.EmployeeRetrieveUpdateDeleteAPIView.as_view(), name="employee-detail"),

    path('api/v1/hr/employees-schedule/', views.ScheduleEmployeeAPIView.as_view(), name="hr-employees-schedule"),

    path('api/v1/hr/contractors/', views.ContractorAPIView.as_view(), name="hr-contractors"),
    path('api/v1/hr/job-titles/', views.JobTitleAPIView.as_view(), name="hr-job-titles"),
    path('api/v1/hr/job-titles/<int:pk>/', views.JobTitleDetailAPIView.as_view(), name="hr-job-title-detail"),
    # Volunteers
    path('api/v1/hr/volunteer/', views.VolunteerAPIView.as_view(), name="hr-volunteer"),
    path('api/v1/hr/volunteer/<int:pk>/', views.VolunteerRetrieveUpdateDeleteAPIView.as_view(), name="volunteer-retrieve-update-delete"),
    path('api/v1/hr/volunteering-application/', views.VolunteeringApplicationAPIView.as_view(), name="hr-volunteering-application"),
    path('api/v1/hr/volunteering-area/', views.VolunteeringAreaAPIView.as_view(), name="hr-volunteering-area"),
    path('api/v1/hr/volunteering-skills/', views.VolunteerSkillsAPIView.as_view(), name="hr-volunteering-skills"),
    path('api/v1/hr/volunteering-hour/', views.VolunteerHourAPIView.as_view(), name="hr-volunteering-hour"),
    #Emergency Contact
    path('api/v1/hr/emergency-contact/', views.LeaveRequestAPIView.as_view(), name="hr-emergency-contacts"),
    #Department
    path('api/v1/hr/departments/', views.DepartmentAPIView.as_view(), name="hr-departments"),
    path('api/v1/hr/departments/<int:pk>/', views.DepartmentDetailsAPIView.as_view(), name="hr-department-detail"),

]