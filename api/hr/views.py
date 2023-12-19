from django.shortcuts import render
from rest_framework import generics

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from django.db import transaction



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
    LeaveRequestAdminPowerSerializer,
    EmergencyContactSerializers,
    DepartmentsSerializers,
    VacationSetupSerializer,
    PoliciesSerializers

)

# Models
from .models import (
    JobTitle, Employee, Contractor, Volunteer, VolunteerSkill, VolunteeringArea,
    VolunteerApplication, VolunteerHour, ScheduleEmployee, LeaveRequest,
    EmergencyContact, Departments, VacationSetup, Policies
)


@transaction.non_atomic_requests
class HomeView(APIView):
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


# Countries choices
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



# list and create
class ContractorAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer


    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        queries = {}

        if self.request.GET.get("is_active"):
            queries['is_active'] = True if self.request.GET.get("is_active").lower() == "true" else False

        if self.request.GET.get("first_name"):
            queries['first_name'] = self.request.GET.get("first_name")

        if self.request.GET.get("last_name"):
            queries['last_name'] = self.request.GET.get("last_name")

        if self.request.GET.get("user_email"):
            queries['user_email'] = self.request.GET.get("user_email")

        if self.request.GET.get("title"):
            queries['title'] = self.request.GET.get("title")


        if self.request.GET.get("work_type"):
            queries['work_type'] = self.request.GET.get("work_type")


        if self.request.GET.get("phone_number"):
            queries['phone_number'] = self.request.GET.get("phone_number").lower()

        if self.request.GET.get("pay_method"):
            queries['pay_method'] = self.request.GET.get("pay_method")

        if self.request.GET.get("salary"):
            queries['salary'] = self.request.GET.get("salary")

        if self.request.GET.get("is_manager"):
            queries['is_manager'] = True if self.request.GET.get("is_manager").lower() == "true" else False

        if self.request.GET.get("gender"):
            queries['gender'] = 1 if self.request.GET.get("gender") == "1" or self.request.GET.get("gender").lower() == "male" else 2 if self.request.GET.get("gender") == "2" or self.request.GET.get("gender").lower() == "female" else 3

        if self.request.GET.get("department"):
            lendict = len(self.request.GET.get("department"))
            if lendict > 1:
                queries['department'] = self.request.GET.get("department").split(",")
            else:
                queries['department'] = self.request.GET.get("department").split()

        if queries:
            return qs.search(queries)
        return qs
    

# retrieve | update | delete
class ContractorRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer
    lookup_field = "pk"

    def get_object(self):
        obj = self.get_queryset().select_for_update().get(pk=self.kwargs[self.lookup_field])

        if obj is None:
            self.not_found()
        return obj


# list and create
class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Employee.objects.all()
    serializer_class = EmployeeListCreateSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        queries = {}

        if self.request.GET.get("is_active"):
            queries['is_active'] = True if self.request.GET.get("is_active").lower() == "true" else False

        if self.request.GET.get("first_name"):
            queries['first_name'] = self.request.GET.get("first_name")

        if self.request.GET.get("last_name"):
            queries['last_name'] = self.request.GET.get("last_name")

        if self.request.GET.get("user_email"):
            queries['user_email'] = self.request.GET.get("user_email")

        if self.request.GET.get("phone_number"):
            queries['phone_number'] = self.request.GET.get("phone_number").lower()

        if self.request.GET.get("title"):
            queries['title'] = self.request.GET.get("title")

        if self.request.GET.get("allergies"):
            queries['allergies'] = self.request.GET.get("allergies")

        if self.request.GET.get("medical_condition"):
            queries['medical_condition'] = self.request.GET.get("medical_condition")


        if self.request.GET.get("title"):
            queries['title'] = self.request.GET.get("title")

        if self.request.GET.get("work_type"):
            queries['work_type'] = self.request.GET.get("work_type")

        if self.request.GET.get("pay_method"):
            queries['pay_method'] = self.request.GET.get("pay_method")

        if self.request.GET.get("salary"):
            queries['salary'] = self.request.GET.get("salary")

        if self.request.GET.get("is_manager"):
            queries['is_manager'] = True if self.request.GET.get("is_manager").lower() == "true" else False

        if self.request.GET.get("gender"):
            queries['gender'] = 1 if self.request.GET.get("gender") == "1" or self.request.GET.get("gender").lower() == "male" else 2 if self.request.GET.get("gender") == "2" or self.request.GET.get("gender").lower() == "female" else 3

        if self.request.GET.get("department"):
            lendict = len(self.request.GET.get("department"))
            if lendict > 1:
                queries['department'] = self.request.GET.get("department").split(",")
            else:
                queries['department'] = self.request.GET.get("department").split()
        
        if queries:
            return qs.search(queries)
        return qs



# retrieve | update | delete
class EmployeeRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Employee.objects.all()
    serializer_class = EmployeeListCreateSerializer
    lookup_field = "pk"

    def get_object(self):
        obj = self.get_queryset().select_for_update().get(pk=self.kwargs[self.lookup_field])

        if obj is None:
            self.not_found()
        return obj


# Volunteers
# list and create
class VolunteerAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer


    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        queries = {}

        if self.request.GET.get("is_active"):
            queries['is_active'] = True if self.request.GET.get("is_active").lower() == "true" else False

        if self.request.GET.get("first_name"):
            queries['first_name'] = self.request.GET.get("first_name")

        if self.request.GET.get("last_name"):
            queries['last_name'] = self.request.GET.get("last_name")

        if self.request.GET.get("user_email"):
            queries['user_email'] = self.request.GET.get("user_email")


        if self.request.GET.get("country"):
            queries['country'] = self.request.GET.get("country").upper()


        if self.request.GET.get("application_first_name"):
            queries['application_first_name'] = self.request.GET.get("application_first_name")

        if self.request.GET.get("application_last_name"):
            queries['application_last_name'] = self.request.GET.get("application_last_name")

        if self.request.GET.get("application_email"):
            queries['application_email'] = self.request.GET.get("application_email")

        if self.request.GET.get("gender"):
            queries['gender'] = 1 if self.request.GET.get("gender") == "1" or self.request.GET.get("gender").lower() == "male" else 2 if self.request.GET.get("gender") == "2" or self.request.GET.get("gender").lower() == "female" else 3

        if queries:
            return qs.search(queries)
        return qs


#retrieve | update | delete
class VolunteerRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    lookup_field = "pk"

    def get_object(self):
        obj = self.get_queryset().select_for_update().get(pk=self.kwargs[self.lookup_field])

        if obj is None:
            self.not_found()
        return obj



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

    def get_object(self):
        obj = self.get_queryset().select_for_update().get(pk=self.kwargs[self.lookup_field])
        if obj is None:
            self.not_found()
        return obj


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

    def get_object(self):
        obj = self.get_queryset().select_for_update().get(pk=self.kwargs[self.lookup_field])

        if obj is None:
            self.not_found()
        return obj


# list and create
class VolunteeringApplicationAPIView(generics.ListCreateAPIView):
    # remove authentication for this
    queryset = VolunteerApplication.objects.all()
    serializer_class = VolunteeringApplicationSerializer


    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        queries = {}


        if self.request.GET.get("first_name"):
            queries['first_name'] = self.request.GET.get("first_name")

        if self.request.GET.get("last_name"):
            queries['last_name'] = self.request.GET.get("last_name")

        if self.request.GET.get("email"):
            queries['email'] = self.request.GET.get("email")


        if self.request.GET.get("phone_number"):
            queries['phone_number'] = self.request.GET.get("phone_number").lower()

        if self.request.GET.get("interests"):
            queries['interests'] = self.request.GET.get("interests")

        if self.request.GET.get("skills"):
            lendict = len(self.request.GET.get("skills"))
            if lendict > 1:
                queries['skills'] = self.request.GET.get("skills").split(",")
            else:
                queries['skills'] = self.request.GET.get("skills").split()

        if self.request.GET.get("country_origin"):
            queries['country_origin'] = self.request.GET.get("country_origin")

        if self.request.GET.get("language_spoken"):
            if self.request.GET.get("language_spoken") == "1" or self.request.GET.get("language_spoken").lower() == "english":
                queries['language_spoken'] = 1
            elif self.request.GET.get("language_spoken") == "2" or self.request.GET.get("language_spoken").lower() == "spanish":
                queries['language_spoken'] = 2
            elif self.request.GET.get("language_spoken") == "3" or self.request.GET.get("language_spoken").lower() == "portuguese":
                queries['language_spoken'] = 3
            else:
                queries['language_spoken'] = 4


        if self.request.GET.get("area_volunteering"):
            queries['area_volunteering'] = self.request.GET.get("area_volunteering")

        if self.request.GET.get("status"):
            queries['status'] = self.request.GET.get("status").title()

        if queries:
            return qs.search(queries)
        return qs



# retrieve | update |delete
class VolunteeringApplicationRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = VolunteerApplication.objects.all()
    serializer_class = VolunteeringApplicationSerializer
    lookup_field = "pk"

    def get_object(self):
        obj = self.get_queryset().select_for_update().get(pk=self.kwargs[self.lookup_field])

        if obj is None:
            self.not_found()
        return obj

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
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer


# retrieve | update | delete
class LeaveRequestRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):

        if self.request.user.is_authenticated:
            updated_by = self.request.user
            serializer.save(updated_by=updated_by)
        serializer.save()


# Leave Request for User amins | power users | superuser
# retrieve | update | delete
class LeaveRequestAdminHandleRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestAdminPowerSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        aprroved = serializer.validated_data.get("approved")
        updated = dict()
        if self.request.user.is_authenticated:
            if approved:
                updated.update({"approved_by": self.request.user})
            serializer.save(**updated)

        serializer.save()


# list | create
class EmergencyContactAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializers


# retrieve | update | delete
class EmergencyContactRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializers
    lookup_field = "pk"


# list | create
class DepartmentAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Departments.objects.all()
    
    serializer_class = DepartmentsSerializers


# retrieve | update | delete
class DepartmentDetailsUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializers
    lookup_field = "pk"



# list | create
class VacationSetupAPIView(generics.ListCreateAPIView):
    permission_classes = IsAuthenticatedOrReadOnly
    queryset = VacationSetup.objects.all()
    serializer_class = VacationSetupSerializer


# retrieve | update | delete
class VacationSetupRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = VacationSetup.objects.all()
    serializer_class = VacationSetupSerializer
    lookup_field = "pk"


#Policies

# list | create
class PoliciesAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Policies.objects.all()
    serializer_class = PoliciesSerializers

# retrieve | update | delete
class PoliciesRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Policies.objects.all()
    serializer_class = PoliciesSerializers

    def perform_update(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(updated_by=self.request.user)
        serializer.save()
