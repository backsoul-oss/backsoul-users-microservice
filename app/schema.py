import graphene
import graphql_jwt

import users.schema


class Mutation(users.schema.Mutation, graphene.ObjectType):
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))


schema = graphene.Schema(query=Query, mutation=Mutation)
