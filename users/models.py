from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    backend_name = models.CharField(max_length=50, default='USERS')
