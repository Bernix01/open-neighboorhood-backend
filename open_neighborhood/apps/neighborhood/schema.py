import graphene
from graphene_django import DjangoObjectType
from .models import Person, Resident, House, Block, Employee, Role_employee, Role
from dataclasses import dataclass


@dataclass
class PersonType(DjangoObjectType):
    """ A person representation """
    class Meta:
        model = Person


class ResidentType(DjangoObjectType):
    class Meta:
        model = Resident


class HouseType(DjangoObjectType):
    class Meta:
        model = House


class BlockType(DjangoObjectType):
    class Meta:
        model = Block


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee


class Role_employeeType(DjangoObjectType):
    class Meta:
        model = Role_employee


class RoleType(DjangoObjectType):
    class Meta:
        model = Role


class Query(graphene.ObjectType):
    persons = graphene.List(PersonType)
    residents = graphene.List(ResidentType)
    houses = graphene.List(HouseType)
    blocks = graphene.List(BlockType)
    employees = graphene.List(EmployeeType)
    role_employees = graphene.List(Role_employeeType)
    roles = graphene.List(RoleType)

    def resolve_persons(self):
        return Person.objects.all()

    def resolve_residents(self):
        return Resident.objects.all()

    def resolve_houses(self):
        return House.objects.all()

    def resolve_blocks(self):
        return Block.objects.all()

    def resolve_employees(self):
        return Employee.objects.all()

    def resolve_role_employees(self):
        return Role_employee.objects.all()

    def resolve_roles(self):
        return Role.objects.all()
