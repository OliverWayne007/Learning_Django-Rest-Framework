import django_filters
from employees.models import Employee


class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
    employee_name = django_filters.CharFilter(field_name='employee_name', lookup_expr='icontains')

    class Meta:
        model = Employee
        fields = ['designation', 'employee_name']
