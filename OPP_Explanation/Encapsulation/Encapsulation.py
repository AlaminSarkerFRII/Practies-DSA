from django.db import models

# Using Django

class CommonInformation(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class StudentInfo(CommonInformation):
    student_id = models.CharField(max_length=100, unique=True)
    grade = models.PositiveIntegerField(null=True, blank=True)
    student_description = models.TextField()

    def __str__(self):
        return self.student_id



class TeacherInfo(CommonInformation):
    teacher_id = models.CharField(max_length=100, unique=True)
    subject = models.CharField(max_length=100)
    teacher_description = models.TextField()

    def __str__(self):
        return self.teacher_id


# Now you can create views and Return Response for showing Student and Teacher information