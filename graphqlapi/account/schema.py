from .types import *
from django.contrib.auth.models import Group


class Query(graphene.ObjectType):
    students=graphene.List(UserProfileType, group=graphene.types.String(required=False))
    groups=graphene.List(GroupType)

    def resolve_groups(self,info):
        return Group.objects.all()


    def resolve_students(self, info, **kwargs):
        group=kwargs.get('group',0)
        if group:
            if group=='NA':
                groups=list(Group.objects.all().values('name'))
                all_students=list(UserProfile.objects.filter(user_type=STUDENT))
                group_students=[]
                for g in groups:
                    group_students=group_students+list(UserProfile.objects.filter(user_type=STUDENT,user__groups__name=g.get('name')))
                return list(set(all_students)-set(group_students))
            else:    
                return UserProfile.objects.filter(user_type=STUDENT, user__groups__name=group)
        else:
            return UserProfile.objects.filter(user_type=STUDENT)


