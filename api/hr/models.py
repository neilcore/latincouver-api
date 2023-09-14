from django.db import models
from django.conf import settings

# country field
from django_countries.fields import CountryField
# Geopy
from geopy.geocoders import Nominatim

# Slugify
from django.utils.text import slugify

from datetime import datetime

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
    is_manager = models.BooleanField(default=False, verbose_name="Manager")
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=250, blank=True, null=True)
    contract = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

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
    

    def save(self, *args, **kwargs):

        self.slug = slugify(f"{self.user.first_name} {self.user.last_name}")

        super().save(*args, **kwargs)



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
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.user.first_name} {self.user.last_name}")
        super().save(*args, **kwargs)
    

# Volunteers

class VolunteerSkill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'
    

class VolunteeringArea(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'
    

class VolunteerApplication(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )

    class LanguageSpoken(models.IntegerChoices):
        ENGLISH = 1, 'English'
        SPANISH = 2, 'Spanish'
        PORTUGUESE = 3, 'Portuguese'
        OTHER = 4, 'Other'

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True, null=True)
    interests = models.CharField(max_length=100, blank=True, null=True)
    skills = models.ManyToManyField(VolunteerSkill, blank=True)
    country_origin = CountryField(blank=True, null=True)
    language_spoken = models.IntegerField(choices=LanguageSpoken.choices, blank=True, default=1)
    area_volunteering = models.ForeignKey(VolunteeringArea, on_delete=models.CASCADE, default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.first_name + " " + self.last_name}'
    


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    application = models.ForeignKey(VolunteerApplication, on_delete=models.SET_NULL, null=True, blank=True)
    supervisor = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    country = CountryField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    photo = models.ImageField(upload_to='static/images/volunteers', blank=True)

    def save(self, *args, **kwargs):
        geolocator = Nominatim(user_agent='hr-app')
        location = geolocator.geocode(str(self.country))
        print(f'location: {location}')
        if location:
            self.latitude = location.latitude
            self.longitude = location.longitude
        super(Volunteer, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"



# TIMESHEETS

class VolunteerHour(models.Model):
    class LocationChoices(models.IntegerChoices):
        RM = 1, 'Remote'
        OF = 2, 'Office'
        EV = 3, 'At Event'

    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)    
    date = models.DateField(default=datetime.now)
    time_in = models.TimeField(default=datetime.now().strftime('%H:%M:%S'))
    time_out = models.TimeField(default=datetime.now().strftime('%H:%M:%S'))
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    location = models.IntegerField(choices=LocationChoices.choices, default='2')    

    def save(self, *args, **kwargs):

        # Calculate the number of hours worked based on the time_in and time_out fields
        time_worked = datetime.combine(datetime.now().date(), self.time_out) - datetime.combine(datetime.now().date(), self.time_in)

        self.hours_worked = round(time_worked.seconds / 3600, 2)
        
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.volunteer.user.last_name} {self.volunteer.user.first_name}"
    




# Schedules
class ScheduleEmployee(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]

    TYPE_CHOICES = [
        ('home', 'Home'),
        ('office', 'Office'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.CharField(max_length=3, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    home_office = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.get_day_of_week_display()} - {self.employee}"




#  Leave Requests

class LeaveRequest(models.Model):

    LEAVE_TYPES = [
        ('S', 'Sick Leave'),
        ('V', 'Vacation'),
        ('H', 'Work from Home'),
        ('O', 'Day-Off'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employee_leave_request_fk")
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=2, choices=LEAVE_TYPES)
    description = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee.user.first_name} {self.employee.user.last_name} - {self.start_date} to {self.end_date} ({self.leave_type})"





class EmergencyContact(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_Name="employee_emergency_contact_fk")
    name = models.CharField(max_length=150)
    relationship = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.employee} _ {self.name}"