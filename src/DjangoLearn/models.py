from django.db import models
from django.contrib.auth.models import User

class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=[('teacher', 'Teacher'), ('student', 'Student')])
    def __str__(self):
        return self.user.username

class CourseModel(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name        