from django.db import models

# Create your models here.
class Student(models.Model):
    branch=models.CharField(max_length=6,default="NA")
    section=models.CharField(max_length=1,default="NA")
    semester=models.IntegerField(default=1)
    studentid=models.CharField(max_length=10)
    studentname=models.CharField(max_length=50)

    def __str__(self):
        return self.studentname
