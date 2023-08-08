from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Status(models.IntegerChoices):
    AC = 1, 'Active'
    AR = 2, 'Archived'

class WorkType(models.IntegerChoices):
    FT = 1, 'Full Time'
    PT = 2, 'Part Time'


class PayMethod(models.IntegerChoices):
    SL = 1, 'Salary'
    HR = 2, 'Hourly'



class JobTitle(models.Model):

    name = models.CharField(max_length=100)
    status = models.IntegerField(choices=Status.choices, default=1)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Job Titles"


class AbstractModelHR(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.ForeignKey(JobTitle, on_delete=models.SET_NULL, blank=True, null=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    work_type = models.IntegerField(choices=WorkType.choices, default=1)
    pay_method = models.IntegerField(choices=PayMethod.choices, default=1)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_manager = models.BooleanField(default=False)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=250, blank=True, null=True)
    contract = models.URLField(blank=True, null=True)

    class Meta:
        abstract = True


class Employee(
    AbstractModelHR
):
    
    class Departments(models.IntegerChoices):
        HR = 1, 'Human Resources'
        FIN = 2, 'Finance'
        MKT = 3, 'Marketing'
        OPS = 4, 'Operations'
        IT = 5, 'IT'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    department = models.IntegerField(choices=Departments.choices)

    allergies = models.CharField(max_length=200, blank=True, null=True)
    medical_condition = models.CharField(max_length=200, blank=True, null=True)
    photo = models.ImageField(upload_to='static/images/employees', blank=True)

    @property
    def name(self):
        if self.user.first_name:
            return f'{self.user.first_name} {self.user.last_name}'
        return f"{self.user.username}"

    def __str__(self):
        return f"{self.name}"


class Contractor(AbstractModelHR):

    class Departments(models.IntegerChoices):
        HR = 1, 'Human Resources'
        FIN = 2, 'Finance'
        MKT = 3, 'Marketing'
        OPS = 4, 'Operations'
        IT = 5, 'Information Technology'
        GT = 6, 'Grants'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contractor')
    department = models.IntegerField(choices=Departments.choices)

    def __str__(self):
        return f"{self.user}"
