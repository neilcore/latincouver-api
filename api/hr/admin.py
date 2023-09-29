from django.contrib import admin
from .models import (
    Employee, Contractor, JobTitle, VolunteerHour,
    Volunteer, VolunteerApplication, VolunteeringArea, VolunteerSkill,
    ScheduleEmployee, Departments
)


class CustomEmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ("employee_username", "employee_name", "is_manager", "start_date", "end_date")

    def employee_username(self, obj) -> str:
        return f"{obj.user.username}"
    
    def employee_name(self, obj) -> str:
        return f"{obj.user.first_name} {obj.user.last_name}"
    


class CustomVolunterringApplication(admin.ModelAdmin):
    model = VolunteerApplication
    list_display = ("first_name", "last_name", "email", "phone_number", "country_origin", "area_volunteering", "status")


class CustomVolunteerHour(admin.ModelAdmin):
    model = VolunteerHour
    list_display = (
        "volunteer_username", "time_in", "time_out", "location"
    )

    def volunteer_username(self, obj) -> str:
        return f"{obj.volunteer.user.first_name} {obj.volunteer.user.last_name}"
    


class CustomScheduleEmployee(admin.ModelAdmin):
    model = ScheduleEmployee
    list_display = (
        "schedule_employee", "day_of_week", "start_time", "end_time", "home_office"
    )

    def schedule_employee(self, obj) -> str:
        return f"{obj.employee.user.first_name} {obj.employee.user.last_name}"
    


admin.site.register(JobTitle)
admin.site.register(Employee, CustomEmployeeAdmin)
admin.site.register(Contractor)
admin.site.register(Volunteer)
admin.site.register(VolunteerApplication, CustomVolunterringApplication)
admin.site.register(VolunteeringArea)
admin.site.register(VolunteerSkill)
admin.site.register(VolunteerHour, CustomVolunteerHour)
admin.site.register(ScheduleEmployee, CustomScheduleEmployee)
admin.site.register(Departments)
