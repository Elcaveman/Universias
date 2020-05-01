from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:#user doesn't exist
        Profile.objects.create(user=instance)

@receiver(post_save , sender = User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:#user exists
        instance.profile.save()