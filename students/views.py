from rest_framework import viewsets

from students.serializers import StudentSerializer
from .models import Student


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()

        print("request.GET.get('age'): ", self.request.GET.get("age"))
        print("request.GET.get('branch'): ", self.request.GET.get("branch"))

        age = self.request.query_params.get("age")
        branch = self.request.query_params.get("branch")
        if age:
            queryset = queryset.filter(age=age)
        if branch:
            queryset = queryset.filter(branch=branch)
        return queryset
