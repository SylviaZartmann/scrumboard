from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    salary = models.IntegerField(default='')
    hours = models.IntegerField(default='')

    def __str__(self):
        return self.username