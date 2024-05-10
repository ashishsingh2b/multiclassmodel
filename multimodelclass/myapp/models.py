from django.db import models

# Create your models here.

class Commoninfo(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    schoolname = models.CharField(max_length=50)
    indexno = models.IntegerField()


class Student(Commoninfo):
    parentsname= models.CharField(max_length=50)
    percentage =  models.IntegerField()
    presentday = models.IntegerField()

class Teacher(Commoninfo):
    salary = models.IntegerField()
    subjectname = models.CharField(max_length=50)


