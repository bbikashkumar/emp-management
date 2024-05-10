from multiprocessing import AuthenticationError
from django import forms
from .models import Employee, Department
from django.contrib.auth.forms import AuthenticationForm


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Name', 'email', 'phone_num', 'department', 'position', 'salary']


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['Name', 'supervisor_name', 'Description']  # Adjust fields based on your model


