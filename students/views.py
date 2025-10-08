from rest_framework import viewsets, status
from rest_framework.response import Response

from students.serializers import StudentSerializer
from .models import Student


#

# class ModelViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,mixins.ListModelMixin,GenericViewSet)

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        print("request.GET.get('age'): ", self.request.GET.get("age"))
        print("request.GET.get('branch'): ", self.request.GET.get("branch"))

        age = self.request.query_params.get("age")
        branch = self.request.query_params.get("branch")
        if age:
            queryset = queryset.filter(age=age)
        if branch:
            queryset = queryset.filter(branch=branch)

        for instance in queryset:
            print("first_name: ", instance.first_name)
            print("last_name: ", instance.last_name)
            print("roll_number: ", instance.roll_number)
            print("branch: ", instance.get_branch())
            print("age: ", instance.age)
            print("full_name: ", instance.full_name)
            print()

        print()

        final_response = []

        # Using only() method to fetch only the required some columns from the database at a time.
        # Only the fields mentioned in the only() method are fetched initially.
        # If other fields which are not mentioned in the only() method are referred later, then separate SQL queries
        # are fired to fetch those fields from the database.
        # The only() method does not modify the existing queryset on which it is applied.
        # The only() method creates a new lazy query plan (queryset) to fetch the fields mentioned in the only() method
        # when the queryset is executed (evaluated, serialized, converted to python natives or iterated over).

        # Note that the full_name method decorated with the "@property" decorator in the Student model
        # cannot be treated as a database field and therefore, it cannot be used inside the only() method.

        # The properties defined using the "@property" decorator in the model class can be considered/treated
        # as an attribute of the model instances but not as actual fields of the database.

        queryset_only = queryset.only('first_name', 'last_name', 'roll_number', 'branch')
        for instance in queryset_only:
            response_item = {}
            print("full_name: ", instance.get_full_name())
            response_item["full_name"] = instance.get_full_name()
            print("roll_number: ", instance.roll_number)
            response_item["roll_number"] = instance.roll_number
            print("branch: ", instance.get_branch())
            response_item["branch"] = instance.get_branch()
            final_response.append(response_item)
            print()

        print()

        # Using values_list()
        queryset_valuelist = queryset.values_list()
        for db_obj_value in queryset_valuelist:
            print("db_obj_value: ", db_obj_value)

        print()

        return Response(data={"students": final_response}, status=status.HTTP_200_OK)
