# myapp/middleware.py

from django.http import HttpResponseForbidden
from django.urls import resolve
from views import *

class DepartmentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Resolve the current view
            resolved_view = resolve(request.path_info)
            # Check if the resolved view is in the restricted views
            if resolved_view.view_name in self.restricted_views():
                user_department = request.user.department
                # Check if the user's department is allowed for the requested view
                if user_department not in self.allowed_departments(resolved_view.view_name):
                    return HttpResponseForbidden("You don't have permission to access this page.")
        response = self.get_response(request)
        return response

    def restricted_views(self):
        return ['department_list']

    # def allowed_departments(self, view_name):
    #     # Define the allowed departments for each restricted view
    #     if view_name == 'department_list':
    #         return ['finance', 'hr']
    #     elif view_name == 'restricted_view_2':
    #         return ['sales', 'hr']
    #     else:
    #         return []  # Return an empty list if view_name is not recognized
