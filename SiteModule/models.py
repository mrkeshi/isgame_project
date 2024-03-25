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

    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True,null=True,related_name="social")




class PublicSettings(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    information=models.TextField(default="بدون توضیحات")
    socialLinks=models.OneToOneField(SocialMediaLink,on_delete=models.CASCADE,unique=True,blank=True,null=True)
    url=models.URLField(default="isgame.ir")
    email=models.EmailField(default="admin@gmail.com")
    logoIcon=models.ImageField(upload_to='SiteSetting/Logo',null=True,blank=True)
    logoSite=models.ImageField(upload_to='SiteSetting/Logo',null=True,blank=True)
    post_per_homePage=models.IntegerField(max_length=3,default=10)
    post_per_cat=models.IntegerField(max_length=3,default=10)
    is_Register=models.BooleanField(default=1)
    is_Comment=models.BooleanField(default=1)



class MediaGallery(models.Model):
    title=models.CharField(max_length=100,null=True,blank=True)
    alt=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='gallery',null=False,blank=False)

class Widget(models.Model):
    urladbaner=models.URLField(max_length=200,null=True,blank=True)
    imageurladbaner=models.URLField(max_length=200,null=True,blank=True)
    statusadbaner=models.BooleanField(default=False)