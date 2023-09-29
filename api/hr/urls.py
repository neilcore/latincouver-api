from django.urls import path
from . import views

urlpatterns = [
    path('api/hr/employees/', views.EmployeeAPIView.as_view(), name="hr-employees"),
    path('api/hr/contractors/', views.ContractorAPIView.as_view(), name="hr-contractors"),
    path('api/hr/job-titles/', views.JobTitleAPIView.as_view(), name="hr-job-titles"),
    # Volunteers
    path('api/hr/volunteering-application/', views.VolunteeringApplicationAPIView.as_view(), name="hr-volunteering-application"),
    path('api/hr/volunteering-area/', views.VolunteeringAreaAPIView.as_view(), name="hr-volunteering-area"),
    path('api/hr/volunteering-skills/', views.VolunteerSkillsAPIView.as_view(), name="hr-volunteering-skills"),
    path('api/hr/volunteering-hour/', views.VolunteerHourAPIView.as_view(), name="hr-volunteering-hour"),
    path('api/hr/volunteering-schedule/', views.ScheduleEmployeeAPIView.as_view(), name="hr-volunteering-schedule"),
    path('api/hr/emergency-contact/', views.LeaveRequestAPIView.as_view(), name="hr-emergency-contacts"),
    #Department
    path('api/hr/departments/', views.DepartmentAPIView.as_view(), name="hr-departments"),

]