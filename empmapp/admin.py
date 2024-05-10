#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from empmapp.models import Department,Employee,AttendenceDetails
from import_export.admin import ImportExportModelAdmin,ExportActionMixin
from empmapp.admin_resources import EmployeeResource,DepartmentResource,AttendenceResource

# Register your models here.

class EmployeAdmin(ImportExportModelAdmin,ExportActionMixin):
    resource_classes = [EmployeeResource]
   
class DepartmentAdmin(ImportExportModelAdmin,ExportActionMixin):
    resource_classes = [DepartmentResource]

class AttendenceAdmin(ImportExportModelAdmin,ExportActionMixin):
    resource_classes = [AttendenceResource]


admin.site.register(Employee,EmployeAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(AttendenceDetails,AttendenceAdmin)
