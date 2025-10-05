from django.shortcuts import render
from rest_framework import viewsets

from blogs.models import Blog
from blogs.serializers import BlogSerializer


# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()