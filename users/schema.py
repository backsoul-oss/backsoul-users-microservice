
import graphene
from graphene_django import DjangoObjectType
import graphql_jwt
from .models import UserProfile as User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class UserMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, username, password, email):
        user = User.objects.create_user(username, email, password)
        return UserMutation(user=user)


class TokenAuthMutation(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)


class Mutation(graphene.ObjectType):
    create_user = UserMutation.Field()
    token_auth = TokenAuthMutation.Field()
