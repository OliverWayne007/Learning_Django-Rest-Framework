from django.db import models
from users.models import User


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255, null=False)
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='blogs')

    def __str__(self):
        return f"{self.title}@{self.creator}"
