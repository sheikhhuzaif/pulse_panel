from django.contrib import admin
from .models.address import Address
from .models.users import UserProfile
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Address)