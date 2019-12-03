import graphene
from graphene_pydantic import PydanticObjectType

from typing import Union
from core.models import CivilizationsModel, get_civs


class Civilization(PydanticObjectType):
    class Meta:
        model = CivilizationsModel


class Query(graphene.ObjectType):
    civilizations = graphene.List(
        Civilization,
        ver=graphene.Argument(type=graphene.String, required=False),
        name=graphene.Argument(type=graphene.String, required=False),
    )

    def resolve_civilizations(
        args,
        info,
        ver: Union[str, None] = None,
        name: Union[str, None] = None,
    ):
        sources = get_civs()
        if ver:
            sources = (x for x in sources if x.__getattribute__('ver') == ver)
        if name:
            sources = (x for x in sources if x.__getattribute__('name') == name)
        return sources


schema = graphene.Schema(query=Query)
