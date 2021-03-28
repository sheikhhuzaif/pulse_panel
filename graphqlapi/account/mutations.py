import graphene
from account.models import *
from django.contrib.auth.models import User, Group

class add_user_group(graphene.Mutation):
    user=graphene.String()
    group=graphene.String()

    class Arguments:
        user=graphene.String()
        group=graphene.String()

    def mutate(self,info,user,group):
        class_group=Group.objects.get(name=group)
        new_user=User.objects.get(username=user)
        new_user.groups.add(class_group)
        new_user.save()

        return add_user_group(user=new_user,group=class_group)


class Mutation(graphene.ObjectType):
    add_user_group = add_user_group.Field()