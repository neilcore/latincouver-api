from django.shortcuts import render
from rest_framework import generics

# Serializers
from .serializers import (
    EmployeeSerializer,
    JobTitleSerializer,
    ContractorSerializer,
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
    JobTitle, Employee, Contractor, VolunteerSkill, VolunteeringArea,
    VolunteerApplication, VolunteerHour, ScheduleEmployee, LeaveRequest,
    EmergencyContact, Departments
)


class JobTitleAPIView(generics.ListCreateAPIView):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer


class ContractorAPIView(generics.ListCreateAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer


class EmployeeAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Volunteers

class VolunteerSkillsAPIView(generics.ListCreateAPIView):
    queryset = VolunteerSkill.objects.all()
    serializer_class = VolunteerSkillsSerializer

class VolunteeringAreaAPIView(generics.ListCreateAPIView):
    queryset = VolunteeringArea.objects.all()
    serializer_class = VolunteeringAreaSerializer


class VolunteeringApplicationAPIView(generics.ListCreateAPIView):
    queryset = VolunteerApplication.objects.all()
    serializer_class = VolunteeringApplicationSerializer


class VolunteerHourAPIView(generics.CreateAPIView):
    queryset = VolunteerHour.objects.all()
    serilizer_class = VolunteerHourSerializer


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