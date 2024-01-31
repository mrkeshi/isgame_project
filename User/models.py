import os

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver


class User(AbstractUser):
    active_code = models.CharField(max_length=80)
    about = models.TextField(null=True)
    avatar=models.ImageField(upload_to='Profile',blank=False,null=True)
    def __str__(self):
        if self.first_name != '' and self.last_name != '':
            return self.get_full_name()
        return self.username


# Create your models here.
class incorrect_attempts(models.Model):
    date = models.DateTimeField(auto_created=True, auto_now_add=True)
    ip = models.CharField(max_length=60, blank=False)
    is_login = models.BooleanField(default=False, blank=False)
    is_ness = models.BooleanField(default=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    browser = models.CharField(max_length=30, blank=False, null=True)
    device = models.CharField(max_length=30, blank=False, null=True)


class TokenAuth(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    token = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_created=True, auto_now_add=True)

