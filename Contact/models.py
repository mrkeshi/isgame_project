from django.db import models


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    description=models.TextField()
    is_Displayed =models.BooleanField(default=0)
    date = models.DateTimeField(auto_created=True, auto_now_add=True)