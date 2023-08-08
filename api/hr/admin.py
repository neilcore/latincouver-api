from django.contrib import admin
from .models import Employee, Contractor, JobTitle

admin.site.register(JobTitle)
admin.site.register(Employee)
admin.site.register(Contractor)
