from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    POSITIONS=[('LC','Lab chief'),
    ('TL','Team leader'),
    ('PM' , 'Permanent member'),
    ('AM' , 'Associate member')]

    profil_pic= models.ImageField("Profile", upload_to='users', height_field=None, width_field=None, max_length=None , blank=True)

    position = models.CharField(max_length=50, choices=POSITIONS,blank=True)
    domaine = models.CharField("Domaine of expertise", max_length=50)

    labo = models.ForeignKey("library.Laboratory" , on_delete=models.SET_NULL , null = True)
    team = models.ForeignKey("library.Team" , on_delete=models.SET_NULL,null = True)
  
    bio = models.TextField("Bio :", blank=True , help_text = "Say something about yourself")

    def __str__(self):
        return self.user.get_full_name()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()