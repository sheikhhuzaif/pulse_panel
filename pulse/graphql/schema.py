import graphene
from graphqlapi.account.schema import Query as accountquery
from graphqlapi.account.mutations import Mutation as accountmutation
class Query(accountquery):
    pass


class Mutation(accountmutation):
    pass


schema = graphene.Schema(query=Query,mutation=Mutation)