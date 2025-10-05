from django.db import models

from blogs.models import Blog
from users.models import User


# Create your models here.
class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="comments")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")