from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User) # Link to user model in django
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)

# To create User Profile object
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
