from django.db import models
from django.contrib.auth.models import User

# class User(AbstractUser):
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=100)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    is_teacher = models.BooleanField()

    def __str__(self):
        return self.user.name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name
