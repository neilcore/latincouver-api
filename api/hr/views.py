from django.shortcuts import render
from rest_framework import generics

# Serializers
from .serializers import (
    EmployeeCreateSerializer,
    EmployeeViewSerializer,
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


# Employee
# create
class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeCreateSerializer


# Update

class EmployeeUpdateAPIView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeCreateSerializer

    

# records display
class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeViewSerializer

class EmployeeDetailAPIView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    # serializer_class = EmployeeCreateSerializer
    serializer_class = EmployeeViewSerializer
    lookup_field = "pk"

class EmployeeDeleteAPIView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeCreateSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

# Volunteers

class VolunteerAPIView(generics.ListCreateAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer


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