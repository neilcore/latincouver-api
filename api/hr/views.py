from django.shortcuts import render
from rest_framework import generics

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import status



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
    DepartmentsSerializers,
    CountryChoiceSerializer

)

# Models
from .models import (
    JobTitle, Employee, Contractor, Volunteer, VolunteerSkill, VolunteeringArea,
    VolunteerApplication, VolunteerHour, ScheduleEmployee, LeaveRequest,
    EmergencyContact, Departments, GenderChoices
)


class HomeView(APIView):
     
   permission_classes = (IsAuthenticated, )
   def get(self, request):
       content = {"message": "welcome to latincouver"}
       return Response(content)
   

class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CountriesChoicesAPI(APIView):

    def get(self, request):
        from django_countries import countries
        countries_choices = dict(countries)
        return Response(countries_choices)
    

# list and create
class JobTitleAPIView(generics.ListCreateAPIView):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer

# retrieve and update
class JobTitleDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer
    lookup_field = "pk"

# destroy
class JobTitleDestropAPI(generics.DestroyAPIView):
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


# list and create
class VolunteerSkillsAPIView(generics.ListCreateAPIView):
    queryset = VolunteerSkill.objects.all()
    serializer_class = VolunteerSkillsSerializer

class VolunteeringAreaAPIView(generics.ListCreateAPIView):
    queryset = VolunteeringArea.objects.all()
    serializer_class = VolunteeringAreaSerializer


# list and create
class VolunteeringApplicationAPIView(generics.ListCreateAPIView):
    queryset = VolunteerApplication.objects.all()
    serializer_class = VolunteeringApplicationSerializer


class VolunteerHourAPIView(generics.ListCreateAPIView):
    queryset = VolunteerHour.objects.all()
    serializer_class = VolunteerHourSerializer


class ScheduleEmployeeAPIView(generics.ListCreateAPIView):
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



class DepartmentDetailsUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializers
    lookup_field = "pk"