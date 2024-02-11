import os

from django.db.models.signals import post_save, pre_save,post_delete
from django.dispatch import receiver

from SiteModule.models import SocialMediaLink, MediaGallery
from User.models import User
from  .models import PublicSettings
@receiver(post_save, sender=User)
def addProfileSocialToUser(sender, instance, created, **kwargs):

    if created:
        links, created = SocialMediaLink.objects.get_or_create(user=instance)
        print("ProfileSocial created")


@receiver(pre_save,sender=PublicSettings)
def delete_old_images(sender,instance,**kwargs):
    if instance._state.adding and not instance.pk:
        return False
    try:
        old_file1 = sender.objects.get(pk=instance.pk).logoIcon
        old_file2 = sender.objects.get(pk=instance.pk).logoSite
    except sender.DoesNotExist:
        return False
    file = instance.logoIcon
    if not old_file1 == file and old_file1:
        if os.path.isfile(old_file1.path):
            os.remove(old_file1.path)
    file2 = instance.logoSite
    if not old_file2 == file2 and old_file2:
        if os.path.isfile(old_file2.path):
            os.remove(old_file2.path)

@receiver(post_delete, sender=MediaGallery)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)