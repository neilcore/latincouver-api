from django.shortcuts import render
from rest_framework import generics

# Serializers
from .serializers import (
    EmployeeListCreateSerializer,
    JobTitleSerializer,
    ContractorSerializer,
    VolunteerSerializer,
    VolunteeringApplicationSerializer,
    VolunteerSkillsSerializer,
    VolunteeringAreaSerializer,
    VolunteerHourSerializer,
    ScheduleEmployeeSerializer,
    LeaveRequestSerializer,
    EmergencyContactSerializers,
    DepartmentsSerializers

)

# Models
from .models import (
    JobTitle, Employee, Contractor, Volunteer, VolunteerSkill, VolunteeringArea,
    VolunteerApplication, VolunteerHour, ScheduleEmployee, LeaveRequest,
    EmergencyContact, Departments
)


class JobTitleAPIView(generics.ListCreateAPIView):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer

class JobTitleDetailAPIView(generics.RetrieveAPIView):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer
    lookup_field = "pk"


class ContractorAPIView(generics.ListCreateAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer


# list and create
class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeListCreateSerializer



# retrieve | update | delete
class EmployeeRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeListCreateSerializer
    lookup_field = "pk"



# Volunteers
# list and create
class VolunteerAPIView(generics.ListCreateAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer


# retrieve | update | delete
class VolunteerRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    lookup_field = "pk"


class VolunteerSkillsAPIView(generics.ListCreateAPIView):
    queryset = VolunteerSkill.objects.all()
    serializer_class = VolunteerSkillsSerializer

class VolunteeringAreaAPIView(generics.ListCreateAPIView):
    queryset = VolunteeringArea.objects.all()
    serializer_class = VolunteeringAreaSerializer


class VolunteeringApplicationAPIView(generics.ListCreateAPIView):
    queryset = VolunteerApplication.objects.all()
    serializer_class = VolunteeringApplicationSerializer


class VolunteerHourAPIView(generics.ListCreateAPIView):
    queryset = VolunteerHour.objects.all()
    serializer_class = VolunteerHourSerializer


class ScheduleEmployeeAPIView(generics.CreateAPIView):
    queryset = ScheduleEmployee.objects.all()
    serializer_class = ScheduleEmployeeSerializer

class LeaveRequestAPIView(generics.CreateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer


class EmergencyContactAPIView(generics.CreateAPIView):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializers



class DepartmentAPIView(generics.ListCreateAPIView):
    queryset = Departments.objects.all()
    
    serializer_class = DepartmentsSerializers



class DepartmentDetailsAPIView(generics.RetrieveAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializers
    lookup_field = "pk"