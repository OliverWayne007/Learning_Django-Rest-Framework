from django.urls import path
from students.views import get_branch_students

urlpatterns = [
    path('', get_branch_students)
]
