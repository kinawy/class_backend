from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_teacher = models.BooleanField()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name

class Assignment(models.Model):
    name = models.CharField(max_length=50)
    assUrl = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=50)
    gradeLevel = models.IntegerField(max_length=2)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class ClassesAssignments(models.Model):
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)