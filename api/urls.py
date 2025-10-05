from django.urls import path, include

import blogs.views
import users.views
from comments.views import CommentViewSet
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('employees', views.EmployeeViewSet, 'employees')
router.register('students', views.StudentViewSet, 'students')
router.register('users', users.views.UserViewSet, 'users')
router.register('blogs', blogs.views.BlogViewSet, 'blogs')
router.register('comments', CommentViewSet, 'comments')

urlpatterns = [
    # path('students/', views.studentsView),
    # path('students/<int:pk>/', views.studentDetailView),
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>', views.EmployeeDetail.as_view())
    path('', include(router.urls))
]
