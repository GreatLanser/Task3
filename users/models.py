from django.db import models
from django import forms
import uuid


class UserInformation(models.Model):
    #  Field
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True, verbose_name='User Name',
                                help_text='Enter your user name less 30 symbols.')
    email = models.EmailField(max_length=254, unique=True, verbose_name='E-mail',
                              help_text='Enter your e-mail.')
    status = models.CharField(max_length=30, default='Allowed', verbose_name='Status account',
                              choices=[
                                  ("Allowed", "Allowed"),
                                  ("Blocked", "Blocked"),
                              ]
                              )

    #  metadata
    class Meta:
        ordering = ["id"]

    #  method
    def __str__(self):
        return self.username
