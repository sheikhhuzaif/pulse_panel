from django.db import models
from account.constants import USER_TYPE_CHOICES
from django.contrib.auth.models import User
from .address import Address
from phonenumber_field.modelfields import PhoneNumberField
from account.managers.userprofile import ProfileManager
import uuid

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    user_type=models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    id=models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    address=models.ForeignKey(Address, on_delete=models.DO_NOTHING, blank=True, null=True)
    parentage=models.CharField(max_length=128)
    parent_number=PhoneNumberField(blank=False)
    objects=ProfileManager()

    @property
    def get_name(self):
        return self.user.get_full_name