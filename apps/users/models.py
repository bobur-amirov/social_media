from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=13, null=True)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.URLField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.username} {self.pk}"