from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=50, null=False, unique=True)
    password = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50, null=False, unique=True)

    def __str__(self):
        return f"{self.username}"
