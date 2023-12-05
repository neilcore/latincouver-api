from rest_framework import serializers

from rest_framework.fields import CharField, DecimalField, EmailField, DateTimeField, IntegerField

from .models import (
    Employee, Contractor, JobTitle, Volunteer, VolunteerSkill, VolunteeringArea,
    VolunteerApplication, VolunteerHour, ScheduleEmployee, LeaveRequest, EmergencyContact, Departments, VacationSetup
    )

from users.serializers import UserPublicSerializer

from model_serializers.department_serializer import DepartmentsPublicSerializer
from model_serializers.volunteer_application_serializer import VolunteerApplicationPublicSerializer

from django_countries.fields import CountryField



class CountryChoiceSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=2)
    name = serializers.CharField(max_length=128)

    def to_representation(self, instance):
        return {
            'code': instance.code,
            'name': instance.name
        }


class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobTitle
        fields = "__all__"



class EmployeeListCreateSerializer(serializers.ModelSerializer):

    user_info = UserPublicSerializer(source="user", read_only=True)
    active_status = serializers.StringRelatedField(source="user.is_active", read_only=True)
    department_names = serializers.StringRelatedField(source="department", many=True, read_only=True)
    role = serializers.StringRelatedField(source="title", many=False, read_only=True)

    class Meta:
        model=Employee
        fields = [
            'pk', 'user', 'user_info', 'active_status', 'department', 'department_names', 'title', 'role', 'bio', 'work_type', 'pay_method',
            'salary', 'is_manager', 'start_date', 'end_date', 'notes', 'phone_number',
            'contract', 'gender', 'allergies', 'medical_condition', 'photo'
        ]


class ContractorSerializer(serializers.ModelSerializer):
    user_info = UserPublicSerializer(source="user", read_only=True)
    active_status = serializers.StringRelatedField(source="user.is_active", read_only=True)
    department_names = serializers.StringRelatedField(source="department", many=True, read_only=True)
    role = serializers.StringRelatedField(source="title", many=False, read_only=True)
    class Meta:
        model=Contractor
        fields=[
            'pk', 'user', 'user_info', 'department', 'department_names', 'title', 'role', 'bio', 'work_type', 'pay_method',
            'salary', 'is_manager', 'start_date', 'end_date', 'notes', 'active_status', 'phone_number',
            'contract'
        ]


class VolunteerSerializer(serializers.ModelSerializer):
    user_info = UserPublicSerializer(source="user", read_only=True)
    supervisor_name = serializers.StringRelatedField(source="supervisor", many=False)
    application_name = VolunteerApplicationPublicSerializer(source="application", read_only=True)
    latitude = DecimalField(read_only=True,max_digits=9, decimal_places=6,)
    longitude = DecimalField(read_only=True,max_digits=9, decimal_places=6,)

    class Meta:
        model=Volunteer
        fields = [
            "pk", "user", "user_info", "gender", "application", "application_name", "supervisor", "supervisor_name", "country", "photo", "latitude", "longitude"
        ]



# Volunteer Create and Update
class VolunteerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Volunteer
        fields = [
            "pk", "user", "gender", "application", "supervisor", "country", "photo", "latitude", "longitude"
        ]



        

class VolunteerSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model=VolunteerSkill
        fields= '__all__'



class VolunteeringAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model=VolunteeringArea
        fields = '__all__'


class VolunteeringApplicationSerializer(serializers.ModelSerializer):

    skills_name = serializers.StringRelatedField(many=True, source="skills", read_only=True)
    area_voluntering_name = serializers.StringRelatedField(source="area_volunteering")
    class Meta:
        model=VolunteerApplication
        fields = [
            "pk", "first_name", "last_name", "email", "phone_number",
            "bio", "interests", "skills", "skills_name", "country_origin",
            "language_spoken", "area_volunteering", "area_voluntering_name", "reason", "status"
        ]


class VolunteerHourSerializer(serializers.ModelSerializer):
    volunteer_name = serializers.StringRelatedField(many=False, source="volunteer")
    hours_worked = DecimalField(read_only=True, max_digits=5, decimal_places=2)
    class Meta:
        model = VolunteerHour
        fields = [
            "pk", "volunteer", "volunteer_name", "time_in", "time_out", "hours_worked", "date", "location"
        ]



class ScheduleEmployeeSerializer(serializers.ModelSerializer):
    employee_name = serializers.StringRelatedField(many=False, source="employee")
    class Meta:
        model = ScheduleEmployee
        fields = [
            "pk", "employee", "employee_name", "start_time", "end_time", "home_office", "day_of_week"
        ]


class LeaveRequestSerializer(serializers.ModelSerializer):
    employee_name = serializers.StringRelatedField(source="employee", many=False)
    class Meta:
        model = LeaveRequest
        fields = ['pk', 'employee', 'employee_name', 'start_date', 'end_date', 'leave_type', 'description']


class VacationSetupSerializer(serializers.ModelSerializer):
    employee_name = serializers.StringRelatedField(source="employee", many=False)
    class Meta:
        model = VacationSetup
        fields = ['pk', 'employee', 'employee_name', 'year', 'weeks_of_vacation', 'percentage_salary', 'plan']


class EmergencyContactSerializers(serializers.ModelSerializer):
    employee_name = serializers.StringRelatedField(source="employee", many=False)
    class Meta:
        model = EmergencyContact
        fields = ['pk', 'employee', 'employee_name', 'name', 'relationship', 'phone']


class DepartmentsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Departments
        fields = "__all__"