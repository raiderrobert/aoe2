import graphene
from graphene_pydantic import PydanticObjectType

from typing import Union
from core.models import CivilizationsModel, get_civs, UnitsModel, get_units, get_unit


class Civilization(PydanticObjectType):

    uniqueUnit = graphene.List(lambda: Unit)

    class Meta:
        model = CivilizationsModel

    def resolve_uniqueUnit(self, info):
        return [get_unit(f) for f in self.uniqueUnit]


class Unit(PydanticObjectType):
    class Meta:
        model = UnitsModel


class Query(graphene.ObjectType):
    civilizations = graphene.List(
        Civilization,
        version=graphene.Argument(type=graphene.String, required=False),
        name=graphene.Argument(type=graphene.String, required=False),
        speciality_contains=graphene.Argument(type=graphene.String, required=False),
    )
    units = graphene.List(Unit,)

    def resolve_civilizations(
        self,
        info,
        version: Union[str, None] = None,
        name: Union[str, None] = None,
        speciality_contains: Union[str, None] = None,
        *args,
        **kwargs
    ):
        civs = get_civs()
        if version:
            civs = (x for x in civs if x.__getattribute__("ver") == version)
        if name:
            civs = (x for x in civs if x.__getattribute__("name") == name)
        if speciality_contains:
            civs = (
                x for x in civs if speciality_contains.lower() in x.speciality.lower()
            )
        return civs

    def resolve_units(self, info, *args, **kwargs):
        return get_units()


schema = graphene.Schema(query=Query)
