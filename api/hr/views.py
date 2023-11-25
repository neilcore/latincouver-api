from django.shortcuts import render
from rest_framework import generics

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

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
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer

# retrieve and update
class JobTitleDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer
    lookup_field = "pk"

# destroy
class JobTitleDestropAPI(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer
    lookup_field = "pk"


class ContractorAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer


# list and create
class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Employee.objects.all()
    serializer_class = EmployeeListCreateSerializer



# retrieve | update | delete
class EmployeeRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Employee.objects.all()
    serializer_class = EmployeeListCreateSerializer
    lookup_field = "pk"



# Volunteers
# list and create
class VolunteerAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer


# retrieve | update | delete
class VolunteerRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    lookup_field = "pk"


# list and create
class VolunteerSkillsAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = VolunteerSkill.objects.all()
    serializer_class = VolunteerSkillsSerializer

# retrieve | update | delete
class VolunteerSkillsRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = VolunteerSkill.objects.all()
    serializer_class = VolunteerSkillsSerializer
    lookup_field = "pk"


# list and create
class VolunteeringAreaAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = VolunteeringArea.objects.all()
    serializer_class = VolunteeringAreaSerializer


# retrieve | update | delete
class VolunteeringAreaRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = VolunteeringArea.objects.all()
    serializer_class = VolunteeringAreaSerializer

    lookup_field = "pk"


# list and create
class VolunteeringApplicationAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = VolunteerApplication.objects.all()
    serializer_class = VolunteeringApplicationSerializer


# retireive | update |delete
class VolunteeringApplicationRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = VolunteerApplication.objects.all()
    serializer_class = VolunteeringApplicationSerializer

    lookup_field = "pk"

# list | create
class VolunteerHourAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = VolunteerHour.objects.all()
    serializer_class = VolunteerHourSerializer

# retrieve | update | delete
class VolunteerHourRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = VolunteerHour.objects.all()
    serializer_class = VolunteerHourSerializer

    lookup_field = "pk"

# list | create
class ScheduleEmployeeAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ScheduleEmployee.objects.all()
    serializer_class = ScheduleEmployeeSerializer

# retrieve | update | delete
class ScheduleEmployeeRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ScheduleEmployee.objects.all()
    serializer_class = ScheduleEmployeeSerializer

    lookup_field = "pk"


# list | create
class LeaveRequestAPIView(generics.ListCreateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer


# retireve | update | delete
class LeaveRequestRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    lookup_field = "pk"


# list | create
class EmergencyContactAPIView(generics.ListCreateAPIView):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializers

# retireve | update | delete
class EmergencyContactRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializers
    lookup_field = "pk"



class DepartmentAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Departments.objects.all()
    
    serializer_class = DepartmentsSerializers



class DepartmentDetailsUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializers
    lookup_field = "pk"