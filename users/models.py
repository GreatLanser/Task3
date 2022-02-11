from django.db import models
from django.contrib.auth.models import AbstractUser

# from .managers import CustomUserManager


class User(AbstractUser):
    status = models.CharField(max_length=30, default='Allowed', verbose_name='Status account',
                              choices=[
                                  ("Allowed", "Allowed"),
                                  ("Blocked", "Blocked"),
                              ]
                              )

    def __str__(self):
        return self.username
