from pydantic import BaseModel
import json
import typing
import pathlib


class CivilizationsModel(BaseModel):
    name: str
    ver: str
    ct: str
    uu: str
    ut: str

    tb: str
    tt: str
    bs: typing.List[str]


def get_data(file_name) -> str:
    file = pathlib.Path(__file__).resolve().parent.parent.joinpath(f"data/{file_name}")
    with open(file, "r") as reader:
        return reader.read()


def get_civilization_data() -> str:
    return get_data('civilizations.json')


def get_unit_data() -> str:
    return get_data('units.json')


def get_civs() -> typing.List[CivilizationsModel]:
    return [CivilizationsModel(**x) for x in json.loads(get_civilization_data())]