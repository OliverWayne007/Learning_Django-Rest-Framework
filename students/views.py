from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student

# Create your views here.
def getAllStudents(request):

    students = [
        {
            'roll_number': 1,
            'name': "Ankit Singh",
            'age': 24,
            'branch': "DSAI"
        },
        {
            'roll_number': 2,
            'name': "Harsh Bardhan",
            'age': 22,
            'branch': "ECE"
        },
        {
            'roll_number': 3,
            'name': "Ashley Mao",
            'age': 23,
            'branch': 'IT'
        },
        {
            'roll_number': 4,
            'name': "Arpit Singh",
            'age': 24,
            'branch': "CSE"
        }
    ]

    return JsonResponse({'students': students})
