from django.db import models


# Create your models here.
class Student(models.Model):
    COMPUTER_SCIENCE = 'CSE'
    INFORMATION_TECHNOLOGY = 'IT'
    ELECTRONICS = 'ECE'
    DATA_SCIENCE_ARTIFICIAL_INTELLIGENCE = 'DSAI'

    branches = [
        (COMPUTER_SCIENCE, "Computer Science and Engineering"),
        (INFORMATION_TECHNOLOGY, "Information Technology"),
        (ELECTRONICS, "Electronics and Communication Engineering"),
        (DATA_SCIENCE_ARTIFICIAL_INTELLIGENCE, "Data Science and Artificial Intelligence")
    ]

    roll_number = models.PositiveIntegerField(unique=True, null=False)
    first_name = models.CharField(max_length=50, null=False, default='Jon')
    last_name = models.CharField(max_length=50, null=False, default='Doe')
    age = models.PositiveIntegerField()
    branch = models.CharField(max_length=5, choices=branches)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return self.full_name

    def get_branch(self):
        return self.branch

    def __str__(self):
        return f"{self.first_name} {self.last_name}@{self.roll_number}"
