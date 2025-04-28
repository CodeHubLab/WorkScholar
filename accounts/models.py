from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES = (
        ('student_working', 'Working Student'),
        ('supervisor', 'Work Supervisor'),
        ('director', 'Working Student Director'),
        ('admin', 'Administrator'),
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    id_number = models.CharField(max_length=20, unique=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.get_user_type_display()}"
