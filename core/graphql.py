import graphene
import string
from graphene_pydantic import PydanticObjectType

from typing import Union
from core.models import CivilizationsModel, get_civs


class Civilization(PydanticObjectType):
    class Meta:
        model = CivilizationsModel


class Query(graphene.ObjectType):
    civilizations = graphene.List(
        Civilization,
        version=graphene.Argument(type=graphene.String, required=False),
        name=graphene.Argument(type=graphene.String, required=False),
        specialityContains=graphene.Argument(type=graphene.String, required=False),
    )

    def resolve_civilizations(
        args,
        info,
        version: Union[str, None] = None,
        name: Union[str, None] = None,
        specialityContains: Union[str, None] = None,
    ):
        civs = get_civs()
        if version:
            civs = (x for x in civs if x.__getattribute__('ver') == version)
        if name:
            civs = (x for x in civs if x.__getattribute__('name') == name)
        if specialityContains:
            civs = (x for x in civs if specialityContains.lower() in (x.__getattribute__('speciality')).lower())
        return civs


schema = graphene.Schema(query=Query)
