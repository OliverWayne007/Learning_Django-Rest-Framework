from rest_framework import serializers

from blogs.serializers import BlogSerializer
from comments.serializers import CommentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    blogs = BlogSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'password', 'blogs', 'comments']
