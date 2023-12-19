from django.contrib import admin
from .models import (
    Employee, Contractor, JobTitle, VolunteerHour,
    Volunteer, VolunteerApplication, VolunteeringArea, VolunteerSkill,
    ScheduleEmployee, Departments, LeaveRequest, EmergencyContact, VacationSetup,
    Policies
)

# IMPORT-EXPORT
#===================================================================

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class JobTitleResources(resources.ModelResource):
    class Meta:
        model=JobTitle

class EmployeeResource(resources.ModelResource):
    class Meta:
        model=Employee

class VolunteerResource(resources.ModelResource):
    class Meta:
        model = Volunteer

class VolunteerApplicationResource(resources.ModelResource):
    class Meta:
        model = VolunteerApplication

class VolunteerHourResource(resources.ModelResource):
    class Meta:
        model = VolunteerHour

class ScheduleEMployeeResource(resources.ModelResource):
    class Meta:
        model = ScheduleEmployee


class ContractorResource(resources.ModelResource):
    class Meta:
        model = Contractor

class LeaveRequestResource(resources.ModelResource):
    class Meta:
        model = LeaveRequest


class PoliciesResource(resources.ModelResource):
    class Meta:
        model = Policies

class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Departments



#===================================================================


class CustomJobtitleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [JobTitleResources]
    class Meta:
        model=JobTitle


class CustomEmployeeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [EmployeeResource]
    model = Employee
    list_display = ("employee_name", "work_type", "is_manager", "start_date", "end_date", "status")
    
    def employee_name(self, obj) -> str:
        return f"{obj.user.first_name} {obj.user.last_name}"
    

class CustomVolunteerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classess = [VolunteerResource]
    model = Volunteer
    list_display = ("volunteer_name", "application", "supervisor", "country", "status")
    
    def volunteer_name(self, obj) -> str:
        return f"{obj.user.first_name} {obj.user.last_name}"
    


class CustomVolunterringApplication(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [VolunteerApplicationResource]
    model = VolunteerApplication
    list_display = ("first_name", "last_name", "email", "phone_number", "country_origin", "area_volunteering", "status")


class CustomVolunteerHour(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [VolunteerHourResource]
    model = VolunteerHour
    list_display = (
        "volunteer_username", "time_in", "time_out", "location"
    )

    def volunteer_username(self, obj) -> str:
        return f"{obj.volunteer.user.first_name} {obj.volunteer.user.last_name}"

    readonly_fields = ('hours_worked','updated_by',)
    


class CustomScheduleEmployee(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [ScheduleEMployeeResource]
    model = ScheduleEmployee
    list_display = (
        "schedule_employee", "day_of_week", "start_time", "end_time", "home_office"
    )

    def schedule_employee(self, obj) -> str:
        return f"{obj.employee.user.first_name} {obj.employee.user.last_name}"
    

class CustomContractorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [ContractorResource]
    model = Contractor
    list_display = ("contractor_name", "work_type", "is_manager", "start_date", "end_date", "status")
    
    def contractor_name(self, obj) -> str:
        return f"{obj.user.first_name} {obj.user.last_name}"



class CustomLeaveRequestAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [LeaveRequestResource]
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
            "approved", "approved_by", "updated_by"
        )}),
    )
    readonly_fields = ('approved_by', 'updated_by',)



# for Policies Model
class CustomPoliciesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [PoliciesResource]
    model=Policies
    list_display=("name","policy_type","status","updated_by")
    list_filter=("name","policy_type")
    readonly_fields=("updated_by",)

class CustomDepartmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [DepartmentResource]
    model=Departments
    list_display = ["name",]
    

admin.site.register(JobTitle, CustomJobtitleAdmin)
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
admin.site.register(Departments, CustomDepartmentAdmin)
admin.site.register(Policies, CustomPoliciesAdmin)
