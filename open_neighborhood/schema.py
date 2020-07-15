""" The GraphQL Schema """
import graphene
import graphql_jwt
from open_neighborhood.apps.neighborhood import schema


class Query(schema.Query, graphene.ObjectType):
    """ The schema queries """


class Mutation(graphene.ObjectType): # pylint: disable=too-few-public-methods 
    """ The schema mutations """
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
