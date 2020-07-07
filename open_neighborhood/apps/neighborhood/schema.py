import graphene
from graphene_django import DjangoObjectType
from .models import Person

class PersonType(DjangoObjectType):
    class Meta:
        model= Person


class Query(graphene.ObjectType):
    persons=graphene.List(PersonType)


    def resolve_persons(self, info, **kwargs):
        return Person.objects.all()

