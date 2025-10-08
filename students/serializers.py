from rest_framework import serializers

from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    student_first_name = serializers.CharField(source="first_name")
    student_last_name = serializers.CharField(source="last_name")
    student_age = serializers.IntegerField(source="age")
    student_roll_number = serializers.IntegerField(source="roll_number")
    student_branch = serializers.CharField(source="branch")

    # student_full_name maps to student.full_name, which is defined as a property in the Student model
    # It is defined as Read-Only because the full_name property is not stored in the database
    student_full_name = serializers.CharField(source="full_name", read_only=True)

    # SerializerMethodField (Read-only field which is not stored in the database)
    student_description = serializers.SerializerMethodField()

    def get_student_description(self, obj):
        return (f"I'm {obj.first_name} {obj.last_name}, I'm {obj.age} years old. "
                f"My roll number is {obj.roll_number} and "
                f"I'm from {obj.branch} branch")

    class Meta:
        model = Student
        fields = ['student_first_name', 'student_last_name', 'student_full_name',
                  'student_description', 'student_age', 'student_branch', 'student_roll_number']
