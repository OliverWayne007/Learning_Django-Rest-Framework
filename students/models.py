from django.db import models


# Create your models here.
class Student(models.Model):

    COMPUTER_SCIENCE = 'CSE'
    INFORMATION_TECHNOLOGY = 'IT'
    ELECTRONICS = 'ECE'
    DATA_SCIENCE_ARTIFICIAL_INTELLIGENCE = 'DSAI'

    branches = [
        (COMPUTER_SCIENCE , "Computer Science and Engineering"),
        (INFORMATION_TECHNOLOGY , "Information Technology"),
        (ELECTRONICS , "Electronics and Communication Engineering"),
        (DATA_SCIENCE_ARTIFICIAL_INTELLIGENCE, "Data Science and Artificial Intelligence")
    ]

    roll_number = models.PositiveIntegerField(unique=True, null=False)
    name = models.CharField(max_length=100, null=False)
    age = models.PositiveIntegerField()
    branch = models.CharField(max_length=5, choices=branches)

    def __str__(self):
        return f"{self.name}@{self.roll_number}"
