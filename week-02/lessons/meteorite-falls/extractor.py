import csv
from meteorite_landing import MeteoriteLanding


# name,id,nametype,recclass,mass (g),fall,year,reclat,reclong,GeoLocation
def map_row_to_meteorite_landing(row):
    row = {key: value.strip() for key, value in row.items()}
    return MeteoriteLanding(
        name=row["name"],
        id=row["id"],
        name_type=row["nametype"],
        rec_class=row["recclass"],
        mass=row["mass (g)"],
        fall=row["fall"],
        year=row["year"],
        latitude=row["reclat"],
        longitude=row["reclong"],
    )


def extract(file_path):
    with open(file_path) as f:
        reader = csv.DictReader(f)
        meteorite_landings = [map_row_to_meteorite_landing(row) for row in reader]

    return meteorite_landings
