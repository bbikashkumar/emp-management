from django.urls import path
from .import views
from django.urls import path
from .views import chat_with_ai





urlpatterns = [
    path('',views.home,name='home'),
    path('employee_details/',views.employee_list,name='employee-details'),
    path('add/employedetails/',views.employee_list,name='employee_list'),
    path('add_dept/department_details/',views.department_list,name='department_list'),
    path('attendence_details/',views.attendence_details,name='attendence_details'),
    path('add/', views.add_employee, name='add_employee'),
    path('edit_employee/<str:email>/', views.edit_employee, name='edit_employee'),
    path('delete_employee/<str:email>/', views.delete_employee, name='delete_employee'),
    path('confirm_delete_employee/<str:email>/', views.confirm_delete_employee, name='confirm_delete_employee'),
    path('add_dept/',views.add_department,name='add_department'),
    path('loginPage/',views.loginpage,name='loginPage'),
    path('login/', views.login_view, name="loginView"),
    # path('delete_dept/<str:name>/',views.delete_department,name='delete_department'),
    path('register/',views.Registeradmin.as_view()),

    path('about/', views.aboutpage, name="aboutpage"),
    path('contact-us/', views.contactus, name="contactus"),
    
    path('chat/', chat_with_ai, name='chat_with_ai'),
    #path('chatbot/', chatbot, name='chatbot'),


    # path('employedetails/', views.EmployeeListView.as_view(), name='employee_list'),
    # path('employedetails/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    # path('employedetails/new/', views.EmployeeCreateView.as_view(), name='employee_create'),
    # path('employedetails/<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    # path('employedetails/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    

    
]

