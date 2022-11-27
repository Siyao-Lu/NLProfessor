from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=60)
    unique_name = models.CharField(max_length=10)
    major = models.CharField(max_length=10, null=True)
    year = models.CharField(max_length=10, null=True)
    course_choice = models.TextField(null=True)  # a list that stores course numbers, will be serialized by json

class Classes(models.Model):
    name = models.CharField(max_length=30)
    course_num = models.IntegerField(null=True)
    course_description = models.TextField()
    workload = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
