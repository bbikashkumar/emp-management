# from django.db.models.signals import post_save,post_delete
# from django.dispatch import receiver
# from empmapp.models import Employee


# @receiver(pre_save, sender=Employee)
# def emp_created(sender, instance, **kwargs):
#     print(f"Before creating of {instance.Name}")
#     if not instance.email:
#         print(f"Employee {instance.Name} is being created")
        
# @receiver(post_save, sender=Employee)
# def emp_created_for_post(sender, instance, created, **kwargs):
#     print(f"Employee {instance.Name} post_save signal triggered! {created}")
#     if created:
#         print(f"Employee {instance.Name} created!")


#after adding the new employee count the number of emp
# @receiver(post_save, sender=Employee)
# def emp_created_for_post(sender, instance, created, **kwargs):
#     if created:
#         employee_count = Employee.objects.count()
#         print(f"Employee {instance.Name} created! Total employees: {employee_count}")


#@receiver(post_save, sender=Employee)
# def emp_created_for_post(sender, instance, created, **kwargs):
#     if created:
#         department = instance.department  #  department is a ForeignKey in Employee model
#         employee_count = Employee.objects.filter(department=department).count()
#         print(f"Employee {instance.Name} created in department {department}! Total employees in {department}: {employee_count}")


# @receiver(post_delete, sender=Employee)
# def emp_deleted_for_post(sender, instance, **kwargs):
#     department = instance.department  # department is a ForeignKey in  Employee model
#     employee_count = Employee.objects.filter(department=department).count()
#     print(f"Employee {instance.Name} deleted from department {department}! Total employees in {department}: {employee_count}")

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from empmapp.models import Employee

@receiver(post_save, sender=Employee)
def emp_created_for_post(sender, instance, created, **kwargs):
    if created:
        department = instance.department
        employee_count = Employee.objects.filter(department=department).count()
        print(f"Employee {instance.Name} created in department {department}! Total employees in {department}: {employee_count}")

@receiver(post_delete, sender=Employee)
def emp_deleted_for_post(sender, instance, **kwargs):
    department = instance.department
    employee_count = Employee.objects.filter(department=department).count()
    print(f"Employee {instance.Name} deleted from department {department}! Total employees in {department}: {employee_count}")

