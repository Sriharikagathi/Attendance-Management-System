from django.db import models
# Create your models here.
class CIVIL(models.Model):
    date=models.DateField()
    semester=models.IntegerField()
    section=models.CharField(max_length=1)
    facultyid=models.IntegerField()
    Timeslot=models.CharField(max_length=50)
    subjectid=models.CharField(max_length=10,blank=True,null=True)
    subjectname=models.CharField(max_length=10,default="NA",blank=True,null=True)
    studentid=models.CharField(max_length=10)
    status=models.BooleanField()

class MECH(models.Model):
    date=models.DateField()
    semester=models.IntegerField()
    section=models.CharField(max_length=1)
    facultyid=models.IntegerField()
    Timeslot=models.CharField(max_length=50)
    subjectid=models.CharField(max_length=10,blank=True,null=True)
    subjectname=models.CharField(max_length=10,default="NA",blank=True,null=True)
    studentid=models.CharField(max_length=10)
    status=models.BooleanField()

class EEE(models.Model):
    date=models.DateField()
    semester=models.IntegerField()
    section=models.CharField(max_length=1)
    facultyid=models.IntegerField()
    Timeslot=models.CharField(max_length=50)
    subjectid=models.CharField(max_length=10,blank=True,null=True)
    subjectname=models.CharField(max_length=10,default="NA",blank=True,null=True)
    studentid=models.CharField(max_length=10)
    status=models.BooleanField()

class ECE(models.Model):
    date=models.DateField()
    semester=models.IntegerField()
    section=models.CharField(max_length=1)
    facultyid=models.IntegerField()
    Timeslot=models.CharField(max_length=50)
    subjectid=models.CharField(max_length=10,blank=True,null=True)
    subjectname=models.CharField(max_length=10,default="NA",blank=True,null=True)
    studentid=models.CharField(max_length=10)
    status=models.BooleanField()

class CSE(models.Model):
    date=models.DateField()
    semester=models.IntegerField()
    section=models.CharField(max_length=1)
    facultyid=models.IntegerField()
    Timeslot=models.CharField(max_length=50)
    subjectid=models.CharField(max_length=10,blank=True,null=True)
    subjectname=models.CharField(max_length=10,default="NA",blank=True,null=True)
    studentid=models.CharField(max_length=10)
    status=models.BooleanField()

class CSBS(models.Model):
    date=models.DateField()
    semester=models.IntegerField()
    section=models.CharField(max_length=1)
    facultyid=models.IntegerField()
    Timeslot=models.CharField(max_length=50)
    subjectid=models.CharField(max_length=10,blank=True,null=True)
    subjectname=models.CharField(max_length=10,default="NA",blank=True,null=True)
    studentid=models.CharField(max_length=10)
    status=models.BooleanField()

class CSM(models.Model):
    date=models.CharField(max_length=30)
    semester=models.IntegerField()
    section=models.CharField(max_length=1)
    facultyid=models.IntegerField()
    Timeslot=models.CharField(max_length=50)
    subjectid=models.CharField(max_length=10,blank=True,null=True)
    subjectname=models.CharField(max_length=10,default="NA",blank=True,null=True)
    studentid=models.CharField(max_length=10)
    status=models.BooleanField()

class CSD(models.Model):
    date=models.DateField()
    semester=models.IntegerField()
    section=models.CharField(max_length=1)
    facultyid=models.IntegerField()
    Timeslot=models.CharField(max_length=50)
    subjectid=models.CharField(max_length=10,blank=True,null=True)
    subjectname=models.CharField(max_length=10,default="NA",blank=True,null=True)
    studentid=models.CharField(max_length=10)
    status=models.BooleanField()

class FACULTY(models.Model):
    facultyid=models.IntegerField()
    subjectid=models.CharField(max_length=10)
    section=models.CharField(max_length=1)
    semester=models.IntegerField()
    numberclass=models.IntegerField(default="1")
    branch=models.CharField(max_length=10,default="NA")


class STUDENTDETAILS(models.Model):
    studentid=models.CharField(max_length=10)
    reportdate=models.DateField()
    councellingno=models.IntegerField()
    section=models.CharField(max_length=1)
    startdate=models.DateField()
    branch=models.CharField(max_length=6)