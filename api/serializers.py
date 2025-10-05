from rest_framework import serializers

from blogs.models import Blog
from students.models import Student
from employees.models import Employee
from users.models import User


# Observations:
# ---> Which columns to be displayed/sent in the Response is decided in the Serializer class
# ---> Which rows to be displayed/sent in the Response (row-filtering) is decided in the View class

# class StudentSerializer(serializers.ModelSerializer):
#     student_description = serializers.SerializerMethodField()
#     student_name = serializers.CharField(source="name")
#     student_age = serializers.IntegerField(source="age")
#     student_roll_number = serializers.IntegerField(source="roll_number")
#     student_branch = serializers.CharField(source="branch")
#
#     def get_student_description(self, obj):
#         return (f"I'm {obj.name}, I'm {obj.age} years old. "
#                 f"My roll number is {obj.roll_number} and "
#                 f"I'm from {obj.branch} branch")
#
#     class Meta:
#         model = Student
#         fields = ['student_name', 'student_description', 'student_age', 'student_branch', 'student_roll_number']


# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         # fields = ['employee_id', 'designation', 'employee_name']
#         fields = "__all__"






