from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class PersonManager(BaseUserManager):

    def create_user(self, email, username, password):
        if not email:
            msg = 'Users must have an email address'
            raise ValueError(msg)

        if not username:
            msg = 'This username is not valid'
            raise ValueError(msg)

        user = self.model(email=self.normalize_email(email), username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, password=password, username=username)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Users(AbstractUser):
    objects = PersonManager()
    is_blocked = models.BooleanField(default=False, verbose_name='Status account')

    def __str__(self):
        return self.username


def change_user(action, user_id):
    user = Users.objects.get(id=user_id)
    if action == 'block':
        user.is_blocked = 1
        user.save()
    elif action == 'unblock':
        user.is_blocked = 0
        user.save()
    elif action == 'delete':
        user.delete()
