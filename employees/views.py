from django.shortcuts import render
from rest_framework import viewsets

from employees.filters import EmployeeFilter
from employees.serializers import EmployeeSerializer
from employees.models import Employee


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_class = EmployeeFilter
