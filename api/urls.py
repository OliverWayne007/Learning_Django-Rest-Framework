from django.urls import path, include

from comments.views import CommentViewSet
from employees.views import EmployeeViewSet
from users.views import UserViewSet
from blogs.views import BlogViewSet
from students.views import StudentViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('employees', EmployeeViewSet, 'employees')
router.register('students', StudentViewSet, 'students')
router.register('users', UserViewSet, 'users')
router.register('blogs', BlogViewSet, 'blogs')
router.register('comments', CommentViewSet, 'comments')

urlpatterns = [
    # path('students/', views.studentsView),
    # path('students/<int:pk>/', views.studentDetailView),
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>', views.EmployeeDetail.as_view())
    path('', include(router.urls))
]
