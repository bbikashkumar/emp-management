# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Employee, Department, AttendenceDetails

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['Name', 'supervisor_name', 'Description']

    

class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','password']

#for add operation 
# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ['Name', 'email', 'phone_num', 'department', 'position', 'salary']


#for displaying in the employe list 
# class EmployeeSerializerDisplay(serializers.ModelSerializer):
#     department = DepartmentSerializer()
#     class Meta:
#         model = Employee
#         fields = ['Name', 'email', 'phone_num', 'department', 'position', 'salary']
        

        
class EmployeeSerializerDisplay(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.Name', read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
    
    def create(self, validated_data):
        #print("validated data"  , validated_data)
        department_id = validated_data.pop('department_id', None)
        if department_id:
            validated_data['department_id'] = department_id
        return super().create(validated_data)

    def update(self, instance, validated_data):
        department_id = validated_data.pop('department_id', None)
        if department_id:
            validated_data['department_id'] = department_id
        return super().update(instance, validated_data)
    


        

# class EmployeeSerializerDisplay(serializers.ModelSerializer):
#     department_name = serializers.CharField(source='department.Name', read_only=True)

#     class Meta:
#         model = Employee
#         fields = ['Name', 'email', 'phone_num', 'department','department_name', 'position', 'salary']

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         #print("My data: ",data)
#         data['department_name'] = instance.department.Name
#         return data







class AttendenceDetailsSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializerDisplay()  # Use the EmployeeSerializer for the employee field

    class Meta:
        model = AttendenceDetails
        fields = '__all__'