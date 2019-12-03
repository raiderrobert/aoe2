import numpy as np

def make_mana(row):
    return {
        "fire": parse_mana(row["Red (Fire)"]),
        "earth": parse_mana(row["Green (Earth)"]),
        "water": parse_mana(row["Blue (Water)"]),
        "wind": parse_mana(row["Clear (Wind)"]), 
    }


def parse_mana(mana):
    p = {"base": None, "addon": False}
    if mana.isalpha():  # checks if string is just X or Y or w/e
        p['base'] = -1
        p['addon'] = mana
    elif mana in ("0", 0):
        p['base'] = 0
    elif mana in (None, '', np.nan):
        return p
    else:
        base, addon =  mana.split('+')
        p['base'], p['addon'] = int(base), addon
    return p