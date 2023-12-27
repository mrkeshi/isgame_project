from django.db import models

# Create your models here
# c
from User.models import User


class SocialMediaLink(models.Model):
    telegram = models.CharField(max_length=100, blank=True, null=True)
    aparat = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    youtube = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    github = models.CharField(blank=True, null=True,max_length=100)

    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True,null=True)
    is_setting = models.CharField(blank=True, null=True,max_length=10,unique=True)

    def __str__(self):
        return self.user.get_full_name() +'social link'
