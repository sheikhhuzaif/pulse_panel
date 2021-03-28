import graphene
from graphene_django import DjangoObjectType
from account.models.users import UserProfile
from account.constants import *
from django.contrib.auth.models import User, Group

class UserType(DjangoObjectType):
    class Meta:
        model= User

class GroupType(DjangoObjectType):
    class Meta:
        model=Group

class UserProfileType(DjangoObjectType):
    class Meta:
        model=UserProfile