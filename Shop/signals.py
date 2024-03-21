import os

from django.db.models.signals import pre_save
from django.dispatch import receiver

from Shop.models import Product,LinkDownload


@receiver(pre_save,sender=Product)
def delete_oldimage(sender,instance,**kwargs):
    if instance._state.adding and not instance.pk:
        return False
    try:
        old_file1 = sender.objects.get(pk=instance.pk).image

    except sender.DoesNotExist:
        return False
    file = instance.image
    if not old_file1 == file and old_file1:
        if os.path.isfile(old_file1.path):
            os.remove(old_file1.path)
@receiver(pre_save,sender=LinkDownload)
def delete_oldimage(sender,instance,**kwargs):
    if instance._state.adding and not instance.pk:
        return False
    try:
        old_file1 = sender.objects.get(pk=instance.pk).file

    except sender.DoesNotExist:
        return False
    file = instance.file
    if not old_file1 == file and old_file1:
        if os.path.isfile(old_file1.path):
            os.remove(old_file1.path)
