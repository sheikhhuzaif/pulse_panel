from django.contrib.auth.models import User
from django.db import models
from account.constants import *
from datetime import date
class ProfileManager(models.Manager):
    def create_student(self, password,firstname,lastname, parentage,personal_number,parent_number,address):
        user=User.objects.get_or_create(username=personal_number)
        user.password=date.today()+"junk"
        user.first_name=firstname
        user.last_name=lastname
        user.is_active=False
        user.save()
        profile=UserProfile.objects.get_or_create(user=user)[0]
        profile.user_type=STUDENT
        if address:
            profile.address=address
        if parentage:
            profile.parentage=parentage
        if parent_number:
            profile.parent_number=parent_number
        profile.save()
        return profile
    

    def create_faculty(self, password,firstname,lastname,personal_number, user_type=None):
        user=User.objects.get_or_create(username=personal_number)
        user.password=date.today()+"junk"
        user.first_name=firstname
        user.last_name=lastname
        user.save()
        profile=UserProfile.objects.get_or_create(user=user)
        profile.user_type=user_type
        if personal_number:
            profile.personal_number=personal_number
        profile.save()
        return profile