from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.db import models

# Create your models here.

# Custom Manager
class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='Los Angeles')

class UserProfile(models.Model):
    user = models.OneToOneField(User) # Link to user model in django
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)
    los_angeles = UserProfileManager()

    def __str__(self):
        return self.user.username

# To create User Profile object
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
