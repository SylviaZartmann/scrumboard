from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    salary = models.IntegerField(default=0, blank=True)
    hours = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.username