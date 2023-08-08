from rest_framework import serializers

from rest_framework.fields import CharField, DecimalField

from .models import Employee, Contractor

from users.serializers import UserPublicSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    class Meta:
        model=Employee
        fields = [
            'user', 'department', 'title', 'bio', 'work_type', 'pay_method',
            'salary', 'is_manager', 'start_date', 'end_date', 'notes',
            'contract', 'allergies', 'medical_condition', 'photo'
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