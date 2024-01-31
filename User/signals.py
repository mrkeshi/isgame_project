import os
from django.db.models.signals import pre_save
from django.dispatch import receiver
from User.models import User


@receiver(pre_save,sender=User)
def delete_old_images(sender,instance,**kwargs):

    if instance._state.adding and not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).avatar

    except sender.DoesNotExist:
        return False
    file = instance.avatar
    if not old_file == file and old_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)