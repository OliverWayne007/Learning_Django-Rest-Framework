from django.shortcuts import render
from rest_framework import viewsets

from comments.models import Comment
from comments.serializers import CommentSerializer


# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
