from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null=False)
    student_email = models.EmailField(unique=True)
    personal_email = models.EmailField(blank=True, null=True)
    locker_number = models.IntegerField()
    locker_combination = models.CharField(max_length=20)
    good_student = models.BooleanField(default=True)

    def __str__(self):
        return self.name