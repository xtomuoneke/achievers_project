from django.db import models
from django.contrib.auth.models import User

# Put the models here

class Profile(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('admin', 'Admin'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Links to the default User model
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    bio = models.TextField(blank=True)  # Additional field for user details

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Create your models here.
