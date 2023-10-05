from rest_framework import serializers

from rest_framework.fields import CharField, DecimalField, EmailField, DateTimeField, IntegerField

from .models import (
    Employee, Contractor, JobTitle, Volunteer, VolunteerSkill, VolunteeringArea,
    VolunteerApplication, VolunteerHour, ScheduleEmployee, LeaveRequest, EmergencyContact, Departments
    )

from users.serializers import UserPublicSerializer


class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobTitle
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    class Meta:
        model=Employee
        fields = [
            'user', 'department', 'title', 'bio', 'work_type', 'pay_method',
            'salary', 'is_manager', 'start_date', 'end_date', 'notes',
            'contract', 'gender', 'allergies', 'medical_condition', 'photo'
        ]


class ContractorSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    class Meta:
        model=Contractor
        fields=[
            'user', 'department', 'title', 'bio', 'work_type', 'pay_method',
            'salary', 'is_manager', 'start_date', 'end_date', 'notes',
            'contract'
        ]


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Volunteer
        fields = [
            "user", "gender", "application", "supervisor", "country", "photo"
        ]

class VolunteerSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model=VolunteerSkill
        fields= ['name']



class VolunteeringAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model=VolunteeringArea
        fields = ['name']


class VolunteeringApplicationSerializer(serializers.ModelSerializer):

    skills = serializers.PrimaryKeyRelatedField(queryset=VolunteerSkill.objects.all(), required=False, many=True)
    area_volunteering = serializers.PrimaryKeyRelatedField(queryset=VolunteeringArea.objects.all())

    class Meta:
        model=VolunteerApplication
        fields = [
            "first_name", "last_name", "email", "phone_number",
            "bio", "interests", "skills", "country_origin",
            "language_spoken", "are_volunteering", "status"
        ]


class VolunteerHourSerializer(serializers.ModelSerializer):

    class Meta:
        model = VolunteerHour
        fields = [
            "volunteer", "time_in", "time_out", "date", "location"
        ]



class ScheduleEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScheduleEmployee
        fields = [
            "employee", "start_date", "end_date", "leave_type", "description"
        ]


class LeaveRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeaveRequest
        fields = "__all__"


class EmergencyContactSerializers(serializers.ModelSerializer):

    class Meta:
        model = EmergencyContact
        fields = "__all__"


class DepartmentsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Departments
        fields = "__all__"