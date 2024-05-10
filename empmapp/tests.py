from django.test import RequestFactory, TestCase

# Create your tests here.

from django.test import TestCase, Client
from django.urls import reverse
from .models import Employee, Department
from .views import *
from django.template.response import TemplateResponse 

#Test for URL mapping 
class URLTests(TestCase):
    def test_home_url(self):
        response = self.client.get(reverse('home'))
        # Check for a response (status code 200) 
        self.assertEqual(response.status_code, 200)

    def test_employee_list_url(self):
        redirect = self.client.get(reverse('employee-details'))
        # Check for a redirect (status code 302) 
        self.assertEqual(redirect.status_code, 302)



#Test for department model
class DepartmentModelTests(TestCase):
    def test_department_creation(self):
        # Create a department object
        department = Department.objects.create(
            Name='Test Department',
            supervisor_name='Test Supervisor',
            Description='Test Description'
        )
        # Retrieve the department from the database
        try:
            retrieved_department = Department.objects.get(Name='Test Department')
        except Department.DoesNotExist:
            retrieved_department = None

        # Check if the retrieved department matches the created department
        self.assertIsNotNone(retrieved_department)
        if retrieved_department:
            self.assertEqual(retrieved_department.supervisor_name, 'Test Supervisor')
            self.assertEqual(retrieved_department.Description, 'Test Description')

        # Optionally, you can also check if the department object is created successfully
        department_count = Department.objects.count()
        self.assertEqual(department_count, 1)




#Test for add department view function 
class AddDepartmentViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_request(self):
        # Create a sample department
        department = Department.objects.create(Name='Test Department', supervisor_name='Supervisor', Description='Description')

        # Create a GET request
        request = self.factory.get(reverse('add_department'))

        # Call the view function
        response = add_department(request)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if departments are present in the response context
        if isinstance(response, TemplateResponse):
            self.assertIn('departments', response.context)
            self.assertIn(department, response.context['departments'])

    def test_invalid_post_request(self):
        # Create a POST request with invalid data
        data = {'Name': '', 'supervisor_name': 'New Supervisor', 'Description': 'New Description'}
        request = self.factory.post(reverse('add_department'), data)

        # Call the view function
        response = add_department(request)

        # Check if the response status code is 200 (OK) because of form validation error
        self.assertEqual(response.status_code, 200)

        # Check if the form errors are present in the response context
        if isinstance(response, TemplateResponse):
            self.assertIn('form', response.context)
            self.assertTrue(response.context['form'].errors)

