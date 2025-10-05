from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from students.models import Student
from employees.models import Employee
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets


# Create your views here.

# @api_view(['GET', 'POST'])
# def studentsView(request):
#     # Retrieving all the students from the database
#
#     # Student.objects.all() returns a query-set
#     # students = Student.objects.all()
#
#     # Serialization is the process of converting complex Model objects/ Query-Set obtained from the database
#     # into Json (User Understandable) format.
#
#     # Serializing the query-set manually (NOT RECOMMENDED in case of serializing complex data obtained from DB)
#     # students_list = list(students.values())
#
#     # Serializing the query-set using Django-Rest-Framework (HIGHLY RECOMMENDED)
#     # print(students_list)
#
#     if request.method == 'GET':
#         # Get all the data from the Student table
#         queryset = Student.objects.all()
#         serializer = StudentSerializer(queryset, many=True)
#         students_list = serializer.data
#         return Response({"students": students_list}, status=status.HTTP_200_OK)
#
#     if request.method == 'POST':
#         # request.data is the json request body sent by the client, converted to Python dict format.
#         print(request.data)
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             # serializer.validated_data is just the json request body converted to a Python dict and validated.
#             # It is the representation of the input-data before saving it to the database.
#             # This is why, it does not contain the "id" field.
#             print(serializer.validated_data)
#             # serializer.save() returns an instance of the Student model class
#             student = serializer.save()
#             print(student)
#             # Basically, the DjangoORM converts the Python dict to the Model class object and generates SQL query
#             # to save the data into the database when the serializer.save() line is executed.
#             # "serializer.data" is a Python dict representation (also called the output-representation)
#             # of the actual Student row saved in the database.
#             # That is why, "serializer.data" contains the "id" field whereas "serializer.validated_data" doesn't.
#             print(serializer.data)
#             # Note that "serializer.data" is of Python dict format and not Json format.
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def studentDetailView(request, pk):
#     try:
#         student = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = StudentSerializer(student)
#         # There is no need of validation in case of a 'GET' request because, in a 'GET' request, the data
#         # is fetched directly from the DB and the data stored in the DB is already validated.
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = StudentSerializer(student, data=request.data)
#         # Validation is required in case of 'PUT' and 'POST' request because in these cases, the data is
#         # coming from the client's side, which should not be blindly trusted.
#         if serializer.is_valid():
#             print(serializer.validated_data)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         student.delete()
#         return Response(status=status.HTTP_200_OK)


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


"""
# Class-Based Views

# class Employees(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         employee_data = request.data
#         serializer = EmployeeSerializer(data=employee_data)
#         if serializer.is_valid():
#             print(serializer.validated_data)
#             employee = serializer.save()
#             print(employee)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class EmployeeDetail(APIView):
#     def get(self, request, pk):
#         try:
#             employee = Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         try:
#             employee_data = Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         employee_data_update = request.data
#         print("employee_data: ", employee_data)
#         serializer = EmployeeSerializer(employee_data, data=employee_data_update)
#         if serializer.is_valid():
#             print(serializer.validated_data)
#             employee = serializer.save()
#             print("employee: ", employee)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         try:
#             employee = Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

"""


# mixins.CreateModelMixin for POST
# mixins.ListModelMixin for GET ALL
# mixins.RetrieveModelMixin for GET ONE
# mixins.DestroyModelMixin for DELETE
# mixins.UpdateModelMixin for PUT


"""
# Mixins
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


# Mixins
class EmployeeDetail(mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                     generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
        
"""


"""
class Employees(generics.ListAPIView, generics.CreateAPIView):
    queryset = Employee.objects.all()
    # queryset = Employee.objects.filter(designation='Software Developer')
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
"""


"""
class EmployeeViewSet(viewsets.ViewSet):
    
    queryset = Employee.objects.all()

    # For GET all request
    def list(self, request):
        serializer = EmployeeSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # For GET by id request
    def retrieve(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # For POST  request
    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # For PUT request
    def update(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # For DELETE request
    def destroy(self, request, pk=None):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
