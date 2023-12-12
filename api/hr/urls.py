from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name ='home'),
    path('api/logout/', views.LogoutView.as_view(), name ='logout'),
    #countries choices API
    path('api/v1/countries/choices/', views.CountriesChoicesAPI.as_view(), name='country_choices'),
    #job-titles
    path('api/v1/hr/job-titles/', views.JobTitleAPIView.as_view(), name="hr-job-titles"),
    path('api/v1/hr/job-titles/<int:pk>/', views.JobTitleDetailUpdateAPIView.as_view(), name="hr-job-title-detail"),
    path('api/v1/hr/job-titles/destroy/<int:pk>/', views.JobTitleDestropAPI.as_view(), name="job-titles-destroy"),

    # Employees
    path('api/v1/hr/employees/', views.EmployeeListCreateAPIView.as_view(), name="hr-employees"),
    path('api/v1/hr/employees/<int:pk>/', views.EmployeeRetrieveUpdateDeleteAPIView.as_view(), name="employee-detail"),

    path('api/v1/hr/employees-schedule/', views.ScheduleEmployeeAPIView.as_view(), name="hr-employees-schedule"),
    path('api/v1/hr/employees-schedule/<int:pk>/', views.ScheduleEmployeeRetrieveUpdateDeleteAPIView.as_view(), name="hr-employees-schedule-retrieve-update-delete"),

    path('api/v1/hr/contractors/', views.ContractorAPIView.as_view(), name="hr-contractors"),
    path('api/v1/hr/contractors/<int:pk>/', views.ContractorRetrieveUpdateDeleteAPIView.as_view(), name="hr-contractors-retrieve-update-delete"),
    # Volunteers
    path('api/v1/hr/volunteer/', views.VolunteerAPIView.as_view(), name="hr-volunteer"),
    path('api/v1/hr/volunteer/<int:pk>/', views.VolunteerRetrieveUpdateDeleteAPIView.as_view(), name="volunteer-retrieve-update-delete"),
    path('api/v1/hr/volunteering-application/', views.VolunteeringApplicationAPIView.as_view(), name="hr-volunteering-application"),
    path('api/v1/hr/volunteering-application/<int:pk>/', views.VolunteeringApplicationRetrieveUpdateDeleteAPIView.as_view(), name="hr-volunteering-application-retrieve-update-delete"),
    path('api/v1/hr/volunteering-area/', views.VolunteeringAreaAPIView.as_view(), name="hr-volunteering-area"),
    path('api/v1/hr/volunteering-area/<int:pk>/', views.VolunteeringAreaRetrieveUpdateDeleteAPIView.as_view(), name="hr-volunteering-area-retrieve-update-delete"),
    path('api/v1/hr/volunteering-skills/', views.VolunteerSkillsAPIView.as_view(), name="hr-volunteering-skills"),
    path('api/v1/hr/volunteering-skills/<int:pk>/', views.VolunteerSkillsRetrieveUpdateDeleteAPIView.as_view(), name="hr-volunteering-skills-retrieve-update-delete"),
    path('api/v1/hr/volunteering-hour/', views.VolunteerHourAPIView.as_view(), name="hr-volunteering-hour"),
    path('api/v1/hr/volunteering-hour/<int:pk>/', views.VolunteerHourRetrieveUpdateDeleteAPIView.as_view(), name="hr-volunteering-hour-retrieve-update-delete"),
    #leave requests
    path('api/v1/hr/leave-request/', views.LeaveRequestAPIView.as_view(), name="hr-leave-requests"),
    path('api/v1/hr/leave-request/<int:pk>/', views.LeaveRequestRetrieveUpdateDeleteAPIView.as_view(), name='hr-leave-requests-retrieve-update-delete'),

    # Leave Request intended for Superusers | ADMINS | Power Users
    path('api/v1/hr/leave-request/admin-access-level/<int:pk>', views.LeaveRequestAdminHandleRetrieveUpdateDeleteAPIView.as_view(), name="hr-leave-requests_admin-access-level-list-retrieve-update-delete"),

    #Vacation Setup
    path('api/v1/hr/vacation-setup/', views.VacationSetupAPIView.as_view(), name="hr-vacation-setup"),
    path('api/v1/hr/vacation-setup/<int:pk>/', views.VacationSetupRetrieveUpdateDeleteAPIView.as_view(), name='hr-vacation-setup--retrieve-update-delete'),
    #Emergency Contact
    path('api/v1/hr/emergency-contact/', views.EmergencyContactAPIView.as_view(), name="hr-emergency-contacts"),
    path('api/v1/hr/emergency-contact/<int:pk>/', views.EmergencyContactRetrieveUpdateDeleteAPIView.as_view(), name='emergency-contact-retrieve-update-delete'),
    #Department
    path('api/v1/hr/departments/', views.DepartmentAPIView.as_view(), name="hr-departments"),
    path('api/v1/hr/departments/<int:pk>/', views.DepartmentDetailsUpdateDestroyAPIView.as_view(), name="hr-department-detail"),

]