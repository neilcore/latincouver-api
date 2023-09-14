from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeAPIView.as_view(), name="hr-employees"),
    path('contractors/', views.ContractorAPIView.as_view(), name="hr-contractors"),
    path('job-titles/', views.JobTitleAPIView.as_view(), name="hr-job-titles"),
    # Volunteers
    path('volunteering-application/', views.VolunteeringApplicationAPIView.as_view(), name="hr-volunteering-application"),
    path('volunteering-area/', views.VolunteeringAreaAPIView.as_view(), name="hr-volunteering-area"),
    path('volunteering-skills/', views.VolunteerSkillsAPIView.as_view(), name="hr-volunteering-skills"),
    path('volunteering-hour/', views.VolunteerHourAPIView.as_view(), name="hr-volunteering-hour"),
    path('volunteering-schedule/', views.ScheduleEmployeeAPIView.as_view(), name="hr-volunteering-schedule"),
    path('emergency-contact/', views.LeaveRequestAPIView.as_view(), name="hr-emergency-contacts"),

]