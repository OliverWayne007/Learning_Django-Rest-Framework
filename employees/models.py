from django.db import models


# The "python manage.py makemigrations" command is used to create and modify the table schema in the database
# These changes in the schema are reflected in the DB when we execute "python manage.py migrate"

# Create your models here.
class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    employee_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    employee_email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.employee_name}@{self.employee_id}"
