from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserProfile(AbstractUser):
    genders = [('s', "Male"), ("F", "Female")]
    cell = models.CharField (max_length=10)
    gender = models.CharField (choices=genders, max_length=1)
    address = models.TextField();


