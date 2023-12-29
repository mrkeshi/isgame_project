from django.db.models.signals import post_save
from django.dispatch import receiver

from SiteModule.models import SocialMediaLink
from User.models import User

@receiver(post_save, sender=User)
def addProfileSocialToUser(sender, instance, created, **kwargs):

    if created:

        links, created = SocialMediaLink.objects.get_or_create(user=instance)

        print("ProfileSocial created")