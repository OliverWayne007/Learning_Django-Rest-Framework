from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from students.serializers import StudentSerializer
from .models import Student


# The ModelViewSet class inherits all the following mixins:

# class ModelViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,mixins.ListModelMixin,GenericViewSet)

# Therefore, ModelViewSet class has all the following default methods coming from the different mixins:
# list --> to get all
# retrieve ---> to get one based on the pk (id)
# update ---> to update one based on the pk (id)
# destroy ---> to delete one based on the pk (id)

# We can override these methods based on our requirements


# Key Concept: queryset cache isolation:
# Every unique queryset maintains its own cache.
# Calling .filter(), .only(), .exclude(), etc., always returns a new queryset.
# Caches are not shared between them.
# Once a queryset has been evaluated, reusing it will use its cache.
# But chaining new query modifiers creates new unevaluated querysets.


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def list(self, request, *args, **kwargs):
        students = self.get_queryset()

        for student in students:
            print("first_name: ", student.first_name)
            print("last_name: ", student.last_name)
            print("roll_number: ", student.roll_number)
            print("branch: ", student.get_branch())
            print("age: ", student.age)
            print("full_name: ", student.full_name)
            print()

        print()

        final_response = []

        # Using only() method to fetch only the required some columns from the database at a time.
        # Only the fields mentioned in the only() method are loaded initially.
        # If other deferred fields which are not mentioned in the only() method are accessed later, then separate
        # SQL queries are fired to fetch those fields from the database.
        # The only() method does not modify the existing queryset on which it is applied.
        # The only() method creates a new lazy query plan (queryset) to fetch the fields mentioned in the only() method
        # when the queryset is executed (evaluated, serialized, converted to python natives or iterated over).

        # Note that the full_name method decorated with the "@property" decorator in the Student model
        # cannot be treated as a database field and therefore, it cannot be used inside the only() method.

        # The properties defined using the "@property" decorator in the model class can be considered/treated
        # as an attribute of the model instances but not as actual fields of the database.

        for student in students:
            response_item = {}
            response_item["full_name"] = student.get_full_name()
            response_item["roll_number"] = student.roll_number
            response_item["branch"] = student.get_branch()
            response_item["age"] = student.age
            final_response.append(response_item)

        # The value_list() function `

        # Using values_list()
        students_value_list = students.values_list()
        for db_obj_value in students_value_list:
            print("db_obj_value: ", db_obj_value)

        print()

        return Response(data={"students": final_response}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_branch_students(request, branch):
    print("path parameter: <str:branch> : ", branch)

    print("request.GET.get('age'): ", request.GET.get("age"))
    age = request.query_params.get("age")

    students = Student.objects.only('first_name', 'last_name', 'branch', 'roll_number').filter(branch=branch)

    if age:
        students = students.filter(age=age)

    final_response = []

    for student in students:
        response_item = {
            "full_name": student.full_name,
            "branch": student.get_branch(),
            "roll_number": student.roll_number
        }
        final_response.append(response_item)

    return Response(data={"students": final_response}, status=status.HTTP_200_OK)

