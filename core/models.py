from pydantic import BaseModel
import json
import typing
import pathlib


civ_data = {}
unit_data = {}


def get_data(file_name) -> str:
    file = pathlib.Path(__file__).resolve().parent.parent.joinpath(f"data/{file_name}")
    with open(file, "r") as reader:
        return reader.read()


class CivilizationsModel(BaseModel):
    name: str
    version: str

    speciality: str

    uniqueUnit: typing.List[str]
    uniqueTech: typing.List[str]
    uniqueBuilding: typing.Optional[typing.List[str]]

    bonus: typing.List[str]
    teamBonus: str


def get_civ(name):
    return civ_data.get(name)


def get_civs() -> typing.List[CivilizationsModel]:
    return [model for model in civ_data.values()]


class UnitsModel(BaseModel):
    name: str
    type: str


def get_unit(name):
    return unit_data.get(name)


def get_units() -> typing.List[UnitsModel]:
    return [model for model in unit_data.values()]


def setup_data():
    global civ_data, unit_data

    civ_data = {
        x['name']: CivilizationsModel(**x) for x in json.loads(get_data("civilizations.json"))
    }

    unit_data = {
        x['name']: UnitsModel(**x) for x in json.loads(get_data("units.json"))
    }


setup_data()
