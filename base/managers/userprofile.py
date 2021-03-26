from django.contrib.auth.models import User
from django.db import models
from models.users import UserProfile

class ProfileManager(models.Manager):
    def create_userProfile(self, user,user_type=None):
        profile=UserProfile.objects.get_or_create(user=user)[0]
        if user_type!='Student':
            profile.user.is_active=True
        else:
            profile.user.is_active=False
        profile.user_type=user_type
        profile.save()
        return profile