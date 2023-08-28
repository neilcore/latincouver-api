from django.shortcuts import render
from rest_framework import generics

# Serializers
from .serializers import (
    EmployeeSerializer,
    JobTitleSerializer,
    ContractorSerializer,
    VolunteeringApplicationSerializer,
    VolunteerSkillsSerializer,
    VolunteeringAreaSerializer
)


class JobTitleAPIView(generics.ListCreateAPIView):
    serializer_class = JobTitleSerializer


class ContractorAPIView(generics.ListCreateAPIView):
    serializer_class = ContractorSerializer


class EmployeeAPIView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer

# Volunteers

class VolunteerSkillsAPIView(generics.ListCreateAPIView):
    serializer_class = VolunteerSkillsSerializer

class VolunteeringAreaAPIView(generics.ListCreateAPIView):
    serializer_class = VolunteeringAreaSerializer


class VolunteeringApplicationAPIView(generics.ListCreateAPIView):
    serializer_class = VolunteeringApplicationSerializer