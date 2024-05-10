from import_export import resources, fields, widgets
from empmapp.models import Employee,Department,AttendenceDetails



#for calculating totall salary with bonus and deducting the tax 
class TotalSalary(fields.Field):
    def get_value(self, obj):
        bonuses_total = 500  #take this value for calculation of totalsalary
        deductions_total = 150
        total_salary = obj.salary + bonuses_total - deductions_total
        return total_salary

class EmployeeResource(resources.ModelResource):
    department = fields.Field(column_name='department', attribute='department__Name')
    total_salary = TotalSalary(column_name='total_salary')
    class Meta:
        model = Employee
        exclude = ('department', 'salary', )

    

#for calculating avg salary       
class AverageSalary(fields.Field):
    def get_value(self, obj):
        employees = Employee.objects.filter(department=obj)
        
        if employees.exists():
            total_salary = sum(employee.salary for employee in employees)
            average_salary = total_salary / employees.count()
            return average_salary
        else:
            return 0
        
    
class DepartmentResource(resources.ModelResource):

    averageSalary = AverageSalary(column_name="average_salary")
    class Meta:
        model = Department
        fields = ('Name', 'supervisor_name', 'Description', 'logo')




#Without include exclude 
class AttendenceResource(resources.ModelResource):

    class Meta:
        model = AttendenceDetails


