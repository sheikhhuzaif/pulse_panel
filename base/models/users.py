from django.db import models
from base.constants import USER_TYPE_CHOICES
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    user_type=models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    id=models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    @property
    def get_name(self):
        return self.user.get_full_name