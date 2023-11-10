from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/v1/hr/employees/', views.EmployeeAPIView.as_view(), name="hr-employees"),
    path('api/v1/hr/contractors/', views.ContractorAPIView.as_view(), name="hr-contractors"),
    path('api/v1/hr/job-titles/', views.JobTitleAPIView.as_view(), name="hr-job-titles"),
    # Volunteers
    path('api/v1/hr/volunteer/', views.VolunteerAPIView.as_view(), name="hr-volunteer"),
    path('api/v1/hr/volunteering-application/', views.VolunteeringApplicationAPIView.as_view(), name="hr-volunteering-application"),
    path('api/v1/hr/volunteering-area/', views.VolunteeringAreaAPIView.as_view(), name="hr-volunteering-area"),
    path('api/v1/hr/volunteering-skills/', views.VolunteerSkillsAPIView.as_view(), name="hr-volunteering-skills"),
    path('api/v1/hr/volunteering-hour/', views.VolunteerHourAPIView.as_view(), name="hr-volunteering-hour"),
    path('api/v1/hr/volunteering-schedule/', views.ScheduleEmployeeAPIView.as_view(), name="hr-volunteering-schedule"),
    #Emergency Contact
    path('api/v1/hr/emergency-contact/', views.LeaveRequestAPIView.as_view(), name="hr-emergency-contacts"),
    #Department
    path('api/v1/hr/departments/', views.DepartmentAPIView.as_view(), name="hr-departments"),

]