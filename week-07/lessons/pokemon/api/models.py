import os
from dataclasses import dataclass

import mariadb

config = {
    "host": "db",
    "port": 3306,
    "user": "root",
    "password": os.getenv("MARIADB_ROOT_PASSWORD"),
    "database": "pokedex",
}


@dataclass
class PokeType:
    poke_type_id: int
    name: str


@dataclass
class Pokemon:
    dex_number: int
    name: str
    primary_poke_type_id: int
    secondary_poke_type_id: int
    primary_type: PokeType = None
    secondary_type: PokeType = None


def find_poke_type():
    cnx = mariadb.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM poke_type")
    result = cursor.fetchall()

    if len(result) == 0:
        return []

    result = [PokeType(*row) for row in result]

    cursor.close()
    cnx.close()

    return result


def find_all(page=1):
    page = min(max(1, page), 100)

    cnx = mariadb.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM pokemon LIMIT 20 OFFSET %s", (20 * (page - 1),))
    result = cursor.fetchall()

    if len(result) == 0:
        return []

    result = [Pokemon(*row) for row in result]

    cursor.close()
    cnx.close()

    poke_types = find_poke_type()
    poke_type_dict = {poke_type.poke_type_id: poke_type for poke_type in poke_types}

    for pokemon in result:
        pokemon.primary_type = poke_type_dict[pokemon.primary_poke_type_id]
        pokemon.secondary_type = poke_type_dict[pokemon.secondary_poke_type_id]

    return result
