from rest_framework import serializers

from blogs.models import Blog
from comments.serializers import CommentSerializer


class BlogSerializer(serializers.ModelSerializer):
    blog_title = serializers.CharField(source='title')
    blog_content = serializers.CharField(source='content')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'blog_title', 'blog_content', 'creator', 'comments']
