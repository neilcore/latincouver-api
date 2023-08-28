from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeAPIView.as_view(), name="hr-employees"),
    path('contractors/', views.ContractorAPIView.as_view(), name="hr-contractors"),
    path('job-titles/', views.JobTitleAPIView.as_view(), name="hr-job-titles"),
    path('volunteering-application/', views.VolunteeringApplicationAPIView.as_view(), name="hr-volunteering-application"),
    path('volunteering-area/', views.VolunteeringAreaAPIView.as_view(), name="hr-volunteering-area"),
    path('volunteering-skills/', views.VolunteerSkillsAPIView.as_view(), name="hr-volunteering-skills"),

]