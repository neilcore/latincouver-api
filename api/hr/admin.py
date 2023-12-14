from django.contrib import admin
from .models import (
    Employee, Contractor, JobTitle, VolunteerHour,
    Volunteer, VolunteerApplication, VolunteeringArea, VolunteerSkill,
    ScheduleEmployee, Departments, LeaveRequest, EmergencyContact, VacationSetup,
    Policies
)


class CustomEmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ("employee_name", "work_type", "is_manager", "start_date", "end_date", "status")
    
    def employee_name(self, obj) -> str:
        return f"{obj.user.first_name} {obj.user.last_name}"
    

class CustomVolunteerAdmin(admin.ModelAdmin):
    model = Volunteer
    list_display = ("volunteer_name", "application", "supervisor", "country", "status")
    
    def volunteer_name(self, obj) -> str:
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
    

class CustomContractorAdmin(admin.ModelAdmin):
    model = Contractor
    list_display = ("contractor_name", "work_type", "is_manager", "start_date", "end_date", "status")
    
    def contractor_name(self, obj) -> str:
        return f"{obj.user.first_name} {obj.user.last_name}"



class CustomLeaveRequestAdmin(admin.ModelAdmin):
    model = LeaveRequest
    list_display = ("employee_name", "leave_type", "start_date", "end_date", "approved", "approved_by")
    
    def employee_name(self, obj) -> str:
        return f"{obj.employee.user.first_name} {obj.employee.user.last_name}"
    
    list_filter = ("leave_type", "approved",)

    fieldsets = (
        ('Fill Leave Request Form', {"fields": (
            "employee", "leave_type", "description",
        )}),
        ('Duration', {"fields": (
            "start_date", "end_date"
        )}),
        ('Status', {"fields": (
            "approved", "approved_by"
        )}),
    )
    readonly_fields = ('approved_by',)



class CustomPoliciesAdmin(admin.ModelAdmin):
    model = Policies
    list_display = ("name", "policy_type", "status")
    
    list_filter = ("name", "policy_type",)
    

admin.site.register(JobTitle)
admin.site.register(Employee, CustomEmployeeAdmin)
admin.site.register(LeaveRequest, CustomLeaveRequestAdmin)
admin.site.register(VacationSetup)
admin.site.register(EmergencyContact)
admin.site.register(Contractor, CustomContractorAdmin)
admin.site.register(Volunteer, CustomVolunteerAdmin)
admin.site.register(VolunteerApplication, CustomVolunterringApplication)
admin.site.register(VolunteeringArea)
admin.site.register(VolunteerSkill)
admin.site.register(VolunteerHour, CustomVolunteerHour)
admin.site.register(ScheduleEmployee, CustomScheduleEmployee)
admin.site.register(Departments)
admin.site.register(Policies, CustomPoliciesAdmin)
